from PyQt5 import uic, QtWidgets
from PyQt5.QtGui import QPixmap
from pytube import YouTube
import ui
import requests
import datetime

app = QtWidgets.QApplication([])
MainWindow = QtWidgets.QMainWindow()
ui = ui.Ui_MainWindow()
ui.setupUi(MainWindow)

""" varaveis """


# funcoes
def baixar():
    print('Baixando...')

    try:
        VIDEO_URL = ui.url.toPlainText()
        yt = YouTube(VIDEO_URL)
        print(yt)

        # get thumb
        response = requests.get(yt.thumbnail_url)
        with open('thumb.jpg', 'wb') as thumb:
            thumb.write(response.content)

        # set thumb
        pix = QPixmap('thumb.jpg')
        ui.thumb.setPixmap(pix)

        # set titulo
        ui.titulo.setText(str(yt.title))

        # get set duracao
        video_duracao = (str(datetime.timedelta(seconds=yt.length)))
        ui.duracao.setText(video_duracao)

        yt.streams.get_highest_resolution().download()

    except Exception as e:
        print(f'errooooooo {e}')


""" triggers """
ui.baixar.clicked.connect(baixar)


""" default states """


""" run app """
MainWindow.show()
app.exec()
