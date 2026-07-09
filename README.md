# LinkEasy 
Projeto pessoal feito em python aonde se pode baixar músicas do yotube direto em seu pc , sem anúncios e seguro , apenas é necessário baixar as bibliotecas e arquivos externos para executar em sua máquina

Este projeto foi feito com intuito de permitir a instalação de músicas do youtube apenas colando link, focado mais como portfólio e aprendizado , neste projeto aprendi como trata requisições https e como a segurança de determinados  softwares podem ser exploradas.

## Ferramentas     <img src="image.png" alt="Descrição da imagem" width="30">



|Front-End   |   |Back-End   |   |   |
|---|---|---|---|---|
|HTML   |   |FLASK   |   |   |
|CSS   |   |PYTHON   |   |   |
|FLASK   |   |   |   |   |


# Como Utiliza-lo ?
Por enquanto esse projeto está em suas primeiras versões, podemos dizer que ele está atualmente em sua "versão beta" ainda preciso refinar esse software e permitir opções de dowloads diferentes, mas para utilizar esse software, certifique-se que em  sua máquina esteja instalado uma IDE de texto (como o  Vscode por exemplo) para dar um "run" nesse arquivo.

### Versão do Python
Em seu pc é necessário baixar o interpretador Python para ele interpretar os códigos do arquivo, você pode instalá-lo por aqui : https://www.python.org/downloads/

<img src="image-1.png" alt="Descrição da imagem" width="30" align="center"> <strong>Atenção</strong><br>

A versão do Interpretador Python instalada em meu pc
é a versão 3.13.13, verifique a sua versão pois dependendo da versão instalada , talvez você terá que usar alguns comandos diferentes.

# Flask
Após instalar o interpretador Python agora é necessário baixar as bibliotecas para que os códigos possam funcionar, sendo assim precisamos utilizar o terminal de seu editor de texto ou utilize o powershel , o primeiro comando que deve ser feito em seu computador é este : <strong><code><i>pip install Flask</i></code></strong><br>
Em suma o flask é um framework do python em que é possível criar aplicações web com python é uma ótima opção para criar chat-bots ou criar outras soluções com python.

# Bibliotecas 
Após certificar que em sua máquina esteja instalada o Flask agora é hora de instalar as bibliotecas que farão com que seja possível os downloads de músicas e vídeos em sua máquina , entre eles estão : <strong><code><i>yt_dlp</i></code></strong> , esta biblioteca é a responsável por gerenciar todo o sistema de instalação de arquivos de músicas em seu dispositivo via links que ela for submetida. Para efetuar esta instalação , vá ao terminal do seu editor de texto e digite : <strong><code><i>C:\python313\python.exe -m pip install yt-dlp</i></code></strong>
  <br><img src="image-1.png" alt="Descrição da imagem" width="30" align="center"> Importante: a versão do python em meu pc é a python313 atente para qual é a sua pois se for diferente ela deve ser informada depois do <strong><code><i>C:\ --versaodopythoninstalada--\ </strong></code></i>

  Agora temos dois arquivos principais que devem ser utilizados pois é por meio deles que você consegue baixar um vídeo do youtube ou uma música a partir do link informado são eles : <strong><code><i>ffmpeg-dowloader</strong></code></i> e o <strong><code><i>ffprobe.exe</strong></code></i>