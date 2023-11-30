import sys

from PySide6.QtWidgets import (QApplication, QMainWindow, QFileDialog)

from PHPDiseno import *
from lexer import *
from parser_1 import *


class Main(QMainWindow):

    def __init__(self):

        QMainWindow.__init__(self)

        self.home = Ui_MainWindow()
        self.home.setupUi(self)

        self.home.analisisLexicoButton.clicked.connect(self.ev_lexico)
        self.home.analisisSintacticoButton.clicked.connect(self.ev_sintactico)

        self.home.cargarArchivoButton.clicked.connect(self.ev_archivo)
        self.home.limpiarButton.clicked.connect(self.ev_limpiar)

    def ev_lexico(self):
        '''
        Manejo de analisis de expresion lexemas
        '''

        self.home.analisisLexicoTextEdit.setPlainText('')

        datos = self.home.cargaDeArchivoTextEdit.toPlainText().strip()

        resultado_lexico = analisis_lexico(datos)

        cadena = ''
        for lex in resultado_lexico:
            cadena += lex + "\n"
        self.home.analisisLexicoTextEdit.setPlainText(cadena)

    def ev_sintactico(self):
        '''
        Manejo de analisis sintactico
        '''

        self.home.analisisSintacticoTextEdit.setPlainText('')

        datos = self.home.cargaDeArchivoTextEdit.toPlainText().strip()

        resultado_sintactico = analisis_sintactico(datos)
        cadena = ''

        for item in resultado_sintactico:
            cadena += item + "\n"

        self.home.analisisSintacticoTextEdit.setPlainText(cadena)

    def ev_archivo(self):
        '''
        Manejo de subir archivo
        '''
        dlg = QFileDialog()

        if dlg.exec():
            filenames = dlg.selectedFiles()
            f = open(filenames[0], 'r')

            with f:
                data = f.read().strip()
                if data:
                    self.home.cargaDeArchivoTextEdit.setPlainText(data + "\n")

    def ev_limpiar(self):
        '''
        Manejo de limpieza de campos
        '''
        self.home.cargaDeArchivoTextEdit.setPlainText('')
        self.home.analisisLexicoTextEdit.setPlainText('')
        self.home.analisisSintacticoTextEdit.setPlainText('')


def iniciar():

    app = QApplication(sys.argv)

    ventana = Main()

    ventana.show()

    sys.exit(app.exec())


if __name__ == '__main__':
    iniciar()