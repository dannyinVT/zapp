from PyQt5.QtWidgets import *
from SClib import SoundcloudAPI, Track
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

# Setting color scheme for app, style set for dark color palette
app = QApplication([])
app.setStyle("Fusion")
dark_palette = QPalette()

dark_palette.setColor(QPalette.Window, QColor(53, 53, 53))
dark_palette.setColor(QPalette.WindowText, Qt.white)
dark_palette.setColor(QPalette.Base, QColor(25, 25, 25))
dark_palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
dark_palette.setColor(QPalette.ToolTipBase, Qt.white)
dark_palette.setColor(QPalette.ToolTipText, Qt.white)
dark_palette.setColor(QPalette.Text, Qt.white)
dark_palette.setColor(QPalette.Button, QColor(53, 53, 53))
dark_palette.setColor(QPalette.ButtonText, Qt.white)
dark_palette.setColor(QPalette.BrightText, Qt.red)
dark_palette.setColor(QPalette.Link, QColor(42, 130, 218))
dark_palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
dark_palette.setColor(QPalette.HighlightedText, Qt.black)
qApp.setPalette(dark_palette)


# Creating class for main GUI instance

class Window(QMainWindow):

    # Setting default window size

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Zapp - simplistic SoundCloud downloader")
        self.setGeometry(800, 500, 500, 300)
        self.MainUi()
        self.show()

    # Window objects
    def MainUi(self):

        # Label for describing purpose of program
        info_label = QLabel("SoundCloud downloader front end developed by Danny Davis using sclib, cheers.", self)
        info_label.setGeometry(50, 0, 400, 100)


        # Input URL into text edit box
        line_edit = QLineEdit("Enter URL & hit return", self)
        line_edit.setGeometry(140, 100, 250, 35)
        line_edit.returnPressed.connect(lambda: start_download())

        # Download progress bar
        # downloadprogress = QProgressBar(self)
        # downloadprogress.setGeometry(140, 150, 250, 20)

        # Start button for initiating download
        button = QPushButton("Start Download", self)
        button.setGeometry(200, 200, 120, 40)
        button.clicked.connect(lambda: start_download())

        # from SClib, by Ian Murphy
        def start_download():
            api = SoundcloudAPI()  # never pass a Soundcloud client ID that did not come from this library

            # in related to progress bar values
            self.completed = 0
            while self.completed < 100:
                self.complted += 0.0002
                self.progress.setVal(self.completed)

            url = line_edit.text()
            track = api.resolve(str(url))

            assert type(track) is Track

            filename = f'./{track.artist} - {track.title}.mp3'

            with open(filename, 'wb+') as fp:
                # Will currently write to project directory
                track.write_mp3_to(fp)


App = QApplication(sys.argv)

window = Window()

app.exec()
