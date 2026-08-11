import os

from flask import render_template, request, jsonify, send_file

# se precisar de adicionar mais bibliotecas, adicione aqui nessas linhas
from logica import baixar_musica,processar_dowload_video
from flask import Blueprint,request, jsonify, send_file, render_template

bp = Blueprint('bp', __name__)

@bp.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@bp.route('/baixar', methods=['POST'])
def baixar():
   
    url = request.form.get('url')
    if not url:
        return jsonify({'error': 'URL do vídeo não fornecida'}), 400

    try:
        # chama a função de baixar música e recebe o nome do arquivo mp3  passando a url
        detalhes = baixar_musica(url)
        caminho_arquivo = detalhes['caminho']

        return send_file(caminho_arquivo, as_attachment=True,download_name=os.path.basename(caminho_arquivo),mimetype='audio/mpeg'
        )
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# implementação futura é colocar a rota para baixar vídeos mas por enquanto quero só fazer um para baixar músicas, então deixei o código comentado para não dar erro, mas futuramente quero implementar isso também
@bp.route('/baixar_video', methods=['GET'])
def baixar_video_form():
    return render_template('baixar_video.html')
@bp.route('/baixarvideo', methods=['POST'])
def baixar_video():
    url = request.form.get('url')
    if not url:
        return jsonify({'error': 'URL do vídeo não fornecida'}), 400

    try:
        # chama a função de baixar vídeo e recebe o nome do arquivo mp4 passando a url
        nome_arquivo_video = processar_dowload_video(url)
        return send_file(nome_arquivo_video, as_attachment=True, download_name=os.path.basename(nome_arquivo_video), mimetype='video/mp4'
         )
    except Exception as e:
        return jsonify({'error': str(e)}), 500