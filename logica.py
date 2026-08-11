import os 
import yt_dlp as youtube_dl 
from yt_dlp.utils import DownloadError

FFMPEG_PATH = r'C:\Users\Davi\Downloads\ffmpeg-master-latest-win64-gpl-shared\ffmpeg-master-latest-win64-gpl-shared\bin'

def baixar_musica(url):
    # a pasta 'downloads' será criada se não existir
    if not os.path.exists('downloads'):
        os.makedirs('downloads')

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': 'downloads/%(title)s.%(ext)s',
        'writethumbnail': True,  # baixa a thumbnail/capa
        'postprocessors': [
            {
                'key': 'FFmpegExtractAudio', # extrair apenas o audio
                'preferredcodec': 'mp3',      # preferencia o formato mp3
                'preferredquality': '192',    # qualidade do audio
            },
            {
                'key': 'FFmpegMetadata',  # grava metadados (artista, titulo, album)
                'add_metadata': True,
            },
            {
                'key': 'EmbedThumbnail',  # insere a capa dentro do arquivo MP3
                'already_have_thumbnail': False,
            }
        ],
        'nocheckcertificate': True,       # ignorar erros de certificado SSL
        'quiet': True,                    # suprimir mensagens de log
        'ffmpeg_location': FFMPEG_PATH 
    }
    
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            nome_arquivo = ydl.prepare_filename(info_dict)
            nome_arquivo_mp3 = os.path.splitext(nome_arquivo)[0] + '.mp3'
            
            detalhes = {
                'caminho': nome_arquivo_mp3,
                'titulo': info_dict.get('title', 'Desconhecido'),
                'duracao': info_dict.get('duration', 0),
                'artista': info_dict.get('artist') or info_dict.get('uploader', 'Desconhecido'),
                'album': info_dict.get('album', 'Desconhecido'),
                'data_lancamento': info_dict.get('release_date') or info_dict.get('upload_date', 'Desconhecido')
            }
            return detalhes
            
            print(f"Detalhes: {detalhes}")





    except DownloadError:
        raise Exception("Erro ao baixar a música. Verifique a URL e tente novamente.")


def processar_dowload_video(url):
    # a pasta 'downloads' será criada se não existir
    if not os.path.exists('downloads'):
        os.makedirs('downloads')

    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': 'downloads/%(title)s.%(ext)s',
        'postprocessors': [
            {
                'key': 'FFmpegMetadata',  # grava metadados no vídeo
                'add_metadata': True,
            }
        ],
        'nocheckcertificate': True,       # ignorar erros de certificado SSL
        'quiet': True,                    # suprimir mensagens de log
        'ffmpeg_location': FFMPEG_PATH 
    }
    
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            nome_arquivo = ydl.prepare_filename(info_dict)
            return nome_arquivo

        detalhes = {
            'caminho': nome_arquivo,
            'titulo': info_dict.get('title', 'Desconhecido'),
            'canal': info_dict.get('uploader', 'Desconhecido'),
            'duracao': info_dict.get('duration', 0),
            'capa': info_dict.get('thumbnail', 'Desconhecido'),
            'data_lancamento': info_dict.get('release_date') or info_dict.get('upload_date', 'Desconhecido'),
            'resolucao': f"{info_dict.get('width', 'Desconhecido')}x{info_dict.get('height', 'Desconhecido')}"
        }
        return detalhes
        print(f"Detalhes: {detalhes}")
        
    except DownloadError:
        raise Exception("Erro ao baixar o vídeo. Verifique a URL e tente novamente.")