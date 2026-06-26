import os 
import yt_dlp as youtube_dl 
from yt_dlp.utils import DownloadError

def baixar_musica(url):
    # a pasta 'downloads' será criada se não existir
    if not os.path.exists('downloads'):
        os.makedirs('downloads')

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': 'downloads/%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio', # extrair apenas o audio
            'preferredcodec': 'mp3',      # preferencia o formato mp3
            'preferredquality': '192',    # qualidade do audio
        }],
        'nocheckcertificate': True,       # ignorar erros de certificado SSL
        'quiet': True,                    # suprimir mensagens de log
        # O caminho exato do ffmpeg mapeado para o Python:
        'ffmpeg_location': 'C:\\Users\\Davi\\Downloads\\ffmpeg-master-latest-win64-gpl-shared\\ffmpeg-master-latest-win64-gpl-shared\\bin' 
    }
    
    try:

      with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=True)
        nome_arquivo = ydl.prepare_filename(info_dict)
        nome_arquivo_mp3 = os.path.splitext(nome_arquivo)[0] + '.mp3'
        return nome_arquivo_mp3

    except DownloadError:
        raise Exception("Erro ao baixar a música. Verifique a URL e tente novamente.")
def processar_dowload_video(url):
    # a pasta 'downloads' será criada se não existir
    if not os.path.exists('downloads'):
        os.makedirs('downloads')

    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': 'downloads/%(title)s.%(ext)s',
        'nocheckcertificate': True,       # ignorar erros de certificado SSL
        'quiet': True,                    # suprimir mensagens de log
        # O caminho exato do ffmpeg mapeado para o Python:
        'ffmpeg_location': 'C:\\Users\\Davi\\Downloads\\ffmpeg-master-latest-win64-gpl-shared\\ffmpeg-master-latest-win64-gpl-shared\\bin' 
    }
    
    try:
      with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=True)
        nome_arquivo = ydl.prepare_filename(info_dict)
        return nome_arquivo

    except DownloadError:
        raise Exception("Erro ao baixar o vídeo. Verifique a URL e tente novamente.")