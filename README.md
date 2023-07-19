# Split Video Downloader

Este é um aplicativo Python para baixar vídeos do YouTube e dividi-los em segmentos menores.

## Requisitos

Antes de executar o aplicativo, certifique-se de ter os seguintes requisitos instalados:

- Python 3.x: [https://www.python.org/downloads/](https://www.python.org/downloads/)
- pip (gerenciador de pacotes Python): [https://pip.pypa.io/en/stable/installing/]([https://pip.pypa.io/en/stable/installing/](https://pip.pypa.io/en/stable/installation/))

## Configuração

Siga as etapas abaixo para configurar o aplicativo:

1. Clone este repositório para o seu ambiente local:

- git clone https://github.com/vnniciusg/split_videos_from_youtube

2. Crie um ambiente virtual para o projeto (recomendado):
- python -m venv env

3. Ative o ambiente virtual:
- No Windows:
  ```
  env\Scripts\activate
  ```
- No macOS/Linux:
  ```
  source env/bin/activate
  ```
4. Instale as dependências do projeto usando o arquivo requirements.txt:
- pip install -r requirements.txt

5. Correção de bug do Pytube:

Existe um bug conhecido no Pytube que pode causar o erro `RegexMatchError: get_transform_object could not find match for ...`. Para corrigir esse problema, siga as instruções neste link: [Stack Overflow - Pytube Exceptions RegexMatchError](https://stackoverflow.com/questions/76704097/pytube-exceptions-regexmatcherror-get-transform-object-could-not-find-match-fo).

## Uso

1. Execute o aplicativo:   
- src/python main.py

3. O aplicativo abrirá uma janela GUI (Interface Gráfica do Usuário) onde você poderá inserir a URL do vídeo do YouTube que deseja baixar e dividir, e selecionar o local de salvamento.

4. Clique no botão "Procurar" para selecionar o local de salvamento. Em seguida, clique no botão "Processar" para iniciar o download e a divisão do vídeo.

5. Uma barra de progresso será exibida, mostrando o progresso do processo. Após a conclusão, uma mensagem informando que a divisão dos vídeos foi concluída com sucesso será exibida.
