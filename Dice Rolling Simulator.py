from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
import random

Font = QFont()
Font.setWordSpacing(2)
Font.setLetterSpacing(QFont.AbsoluteSpacing, 1)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.window_configuration()
        self.user_interface()
        self.main_interface_timer.start()

    def window_configuration(self):

        self.setFixedHeight(600)
        self.setFixedWidth(600)
        self.setWindowTitle("Dice Rolling Simulator")

    def user_interface(self):

        self.app_icon = QLabel(self)
        self.app_icon.setPixmap(QPixmap("icon.png"))
        self.app_icon.move(200, 120)

        self.main_interface_timer = QTimer(self)
        self.main_interface_timer.setInterval(5000)
        self.main_interface_timer.timeout.connect(self.start_simulation)

        self.timer_label = QLabel(self)
        self.timer_label.setText("Application Starts in 5s")
        self.timer_label.move(200, 430)
        self.timer_label.setFont(Font)
        self.timer_label.setStyleSheet("font-size: 18px; font-weight: light;")

    def start_simulation(self):

        self.main_interface_timer.stop()
        self.app_icon.close()
        self.timer_label.close()

        self.simulation_dice = QLabel(self)
        self.simulation_dice.setPixmap(QPixmap("dice_1.png"))
        self.simulation_dice.move(250, 130)
        self.simulation_dice.show()

        self.roll_button = QPushButton("Roll Dice",self)
        self.roll_button.move(245, 350)
        self.roll_button.resize(130, 40)
        self.roll_button.setStyleSheet("border: 0px medium; border-radius: 3px; background-color: black; color: white; font-size: 18px; font-weight: light;")
        self.roll_button.clicked.connect(self.roll_dice)
        self.roll_button.show()

    def roll_dice(self):

        dice_1 = "dice_1.png"
        dice_2 = "dice_2.png"
        dice_3 = "dice_3.png"
        dice_4 = "dice_4.png"
        dice_5 = "dice_5.png"
        dice_6 = "dice_6.png"


        random_dice = random.choice([dice_1, dice_2, dice_3, dice_4, dice_5, dice_6])
        self.simulation_dice.setPixmap(QPixmap(random_dice))
        

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

main()
