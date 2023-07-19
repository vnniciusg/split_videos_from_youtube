import os
import cv2
import random


def split_video(video_file, output_directory):
    if not os.path.isfile(video_file):
        print("Arquivo de vídeo não encontrado.")
        return

    cap = cv2.VideoCapture(video_file)

    if not cap.isOpened():
        print("Falha ao abrir o arquivo de vídeo.")
        return

    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))

    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    frames = []
    output_videos = []

    current_frame = 0

    while cap.isOpened():
        ret, frame = cap.read()

        if ret:
            frames.append(frame)
            current_frame += 1
            random_seconds = random.randint(30, 60)
            frame_interval = random_seconds * fps

            if len(frames) == frame_interval or current_frame == frame_count:
                video_filename = os.path.basename(video_file)
                output_filename = "%s_%02d.mp4" % (
                    os.path.splitext(video_filename)[0],
                    len(output_videos),
                )
                output_path = os.path.join(output_directory, output_filename)

                out = cv2.VideoWriter(
                    output_path, cv2.VideoWriter_fourcc(*"mp4v"), fps, (width, height)
                )

                for f in frames:
                    out.write(f)

                out.release()
                output_videos.append(output_filename)
                frames = []

        if ret is False:
            break

    cap.release()

    print("Vídeos divididos:")
    for video in output_videos:
        print(video)
