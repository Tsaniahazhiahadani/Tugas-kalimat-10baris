import sys
from PyQt5.QtWidgets import *

def window():
    #__inisialisasi pyqt5
    app = QApplication(sys.argv)
    window = QWidget()


    #__menyiapkan label, menempelkan label ke window
    #__settext, dan posisi
    first = 1
    while first<=10:
        textlb = QLabel(window)
        textlb.setText("Ini adalah kalimat ke - " + str(first))
        #posisi teks , jarak teks atas dan bawah
        textlb.move(200, first*20)
        first += 1

    #__menentukan ukuran window, + title dan menampilkan
    window.setGeometry(400,100,500,300)
    window.setWindowTitle("PyQt5 10 baris")
    window.setStyleSheet("background-color: grey")
    window.show()
    sys.exit(app.exec_())
	
if __name__ == '__main__':
    window()
