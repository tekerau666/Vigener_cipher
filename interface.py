import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from parentinterface import Ui_MainWindow
import functions


class MainWindow(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.on_encode_button_clicked)
        self.pushButton_2.clicked.connect(self.on_freq_analysis_button_clicked)

    def on_encode_button_clicked(self):
        try:
            if self.lineEdit.text() and len(self.lineEdit.text()) == 6 and self.plainTextEdit.toPlainText():
                self.plainTextEdit_2.setPlainText(functions.encode(self.plainTextEdit.toPlainText(), self.lineEdit.text()))
            elif not self.plainTextEdit.toPlainText():
                QMessageBox.warning(self, "Нет открытого текста!", "Необходимо сначала ввести открытый текст")
            else:
                QMessageBox.warning(self, "Неправильный ключ!", "Ключ должен быть длиной в 6 символов.")
        except:
            QMessageBox.warning(self, "Неподдерживаемый символ!", "В открытом тексте введен неподдерживаемый символ.")

    def on_freq_analysis_button_clicked(self):
        if self.plainTextEdit_2.toPlainText():
            functions.show_plots(self.plainTextEdit_2.toPlainText(), functions.ref_freq)
        else:
            QMessageBox.warning(self, "Нет зашифрованного текста!", "Необходимо сначала зашифровать открытый текст.")


app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
