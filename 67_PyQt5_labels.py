import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ABCXYZ")
        self.setGeometry(750, 360, 500, 500)
        self.setWindowIcon(QIcon("Iron_1_Rank.png"))

        label = QLabel("Hello", self)
        label.setFont(QFont("Arial", 40))
        label.setGeometry(0, 0, 500, 100)
        label.setStyleSheet("color: blue;"
                            "background-color: #fcba03;"
                            "font-weight: bold;"
                            "font-style: italic;"
                            "text-decoration: underline;")
        #label.setAlignment(Qt.AlignTop) #vertically top
        #label.setAlignment(Qt.AlignBottom) #vertically bot
        #label.setAlignment(Qt.AlignVCenter) #vertically center

        #label.setAlignment(Qt.AlignRight) #horizontally right
        #label.setAlignment(Qt.AlignHCenter) #horizontally center
        #label.setAlignment(Qt.AlignLeft) #horizontally left

        #label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter) # center & center
        label.setAlignment(Qt.AlignCenter)
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()