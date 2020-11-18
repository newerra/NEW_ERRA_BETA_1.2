import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow
from BD import bel, ugl, kaloris, name, zir

class Food(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('еда.ui', self)
        for i in name:
            self.produkt.addItem(i)



class Sport(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('спорт.ui', self)
        pol = ['Мужской','Женский']
        for i in pol:
            self.floor_pol.addItem(i)



class Menu(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('меню.ui', self)
        self.sport.clicked.connect(self.menusport)
        self.food.clicked.connect(self.menufood)

    def menusport(self):
        print(101)
        self.window_of_seeing_all = Sport()
        self.window_of_seeing_all.show()

    def menufood(self):
        print(202)
        self.window_of_seeing_all = Food()
        self.window_of_seeing_all.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Menu()
    ex.show()
    sys.exit(app.exec_())
