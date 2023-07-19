import os
import re
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from pytube import YouTube
from threading import Thread

from services.download_video import download_video
from services.split_video import split_video


def update_progress_bar(progress_bar, value):
    progress_bar["value"] = value


def split_video_after_download(url, save_path, progress_bar):
    download_video(url, save_path)
    update_progress_bar(progress_bar, 50)

    filename = f"{YouTube(url).title}.mp4"
    filename = re.sub(r"\|", "", filename)
    video_filename = os.path.join(save_path, filename)

    output_path = os.path.join(save_path, "cortes")
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    split_video(video_filename, output_path)
    update_progress_bar(progress_bar, 100)

    messagebox.showinfo("Processo Completo", "Divisão dos videos feita com sucesso.")


def get_user_input():
    def browse_save_path():
        save_path = filedialog.askdirectory()
        save_path_entry.delete(0, tk.END)
        save_path_entry.insert(0, save_path)

    def process_video():
        url = url_entry.get()
        save_path = save_path_entry.get()

        if url and save_path:
            if not os.path.exists(save_path):
                os.makedirs(save_path)

            progress_bar = ttk.Progressbar(
                root, orient="horizontal", length=300, mode="determinate"
            )
            progress_bar.grid(row=7, columnspan=3, padx=10, pady=10)

            ok_label = tk.Label(root, text="", fg="green")
            ok_label.grid(row=8, column=2)

            thread = Thread(
                target=split_video_after_download, args=(url, save_path, progress_bar)
            )
            thread.start()

    root = tk.Tk()
    root.geometry("500x150")
    root.resizable(False, False)
    root.title("Split Video Downloader")

    root.configure(bg="#F0F0F0")

    label_url = tk.Label(root, text="URL do vídeo:")
    label_url.grid(row=4, column=0, padx=10, pady=10)
    label_url.configure(bg="#F0F0F0")

    url_entry = tk.Entry(root)
    url_entry.configure(width=40)
    url_entry.grid(row=4, column=1)

    label_save_path = tk.Label(root, text="Local de salvamento:")
    label_save_path.grid(row=5, column=0, padx=10)
    label_save_path.configure(bg="#F0F0F0")

    save_path_entry = tk.Entry(root)
    save_path_entry.configure(width=40)
    save_path_entry.grid(row=5, column=1)

    browse_button = tk.Button(root, text="Procurar", command=browse_save_path)
    browse_button.grid(row=5, column=2, padx=10)
    browse_button.configure(width=10)

    process_button = tk.Button(root, text="Processar", command=process_video)
    process_button.grid(row=8, column=1, pady=10)
    process_button.configure(width=15)

    root.mainloop()


get_user_input()
