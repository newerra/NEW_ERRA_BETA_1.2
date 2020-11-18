import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow
from BD import bel, ugl, kal, name, zir
from PyQt5.QtCore import Qt
from PIL import Image


class Food(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('food1.ui', self)
        for i in name:
            self.produkt.addItem(i)
        self.produkt.activated.connect(self.pass_Net_Adap)
        self.grammovka.textChanged[str].connect(self.onChanged)
        self.vicheslit.clicked.connect(self.vich)
        self.sbros.clicked.connect(self.swbros)
    def vich(self):
        self.f = name.index(self.produkt.currentText())
        self.b = int(bel[self.f])
        self.z = int(zir[self.f])
        self.k = int(kal[self.f])
        self.u = int(ugl[self.f])
        self.bw = (self.b / 100) * self.mnoz
        self.zw = (self.z / 100) * self.mnoz
        self.kw = (self.k / 100) * self.mnoz
        self.uw = (self.u / 100) * self.mnoz
        self.belki.display(self.bw)
        self.kalorii.display(self.kw)
        self.uglevodi.display(self.uw)
        self.zhiri.display(self.zw)

    def pass_Net_Adap(self):
        self.f = name.index(self.produkt.currentText())
        self.b = int(bel[self.f])
        self.z = int(zir[self.f])
        self.k = int(kal[self.f])
        self.u = int(ugl[self.f])
        self.belki.display(self.b)
        self.kalorii.display(self.k)
        self.uglevodi.display(self.u)
        self.zhiri.display(self.z)

    def onChanged(self, text):
        if text == '':
            text = 100
        self.mnoz = int(text)
        print(self.mnoz)

    def swbros(self):
        self.mnoz = 0
        self.b = 0
        self.z = 0
        self.k = 0
        self.u = 0
        self.f = name.index(self.produkt.currentText())
        self.belki.display(self.b)
        self.kalorii.display(self.k)
        self.uglevodi.display(self.u)
        self.zhiri.display(self.z)
        self.grammovka.setText('0')

class Sport(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('sport1.ui', self)
        pol = ['Мужской', 'Женский']
        self.polt = True
        self.caloris = 0
        for i in pol:
            self.floor_pol.addItem(i)
        self.pushButton.clicked.connect(self.getValue)
        self.pushButton_2.clicked.connect(self.Sbrosvalue)
    def getValue(self):
        self.valueves = self.ves.value()
        self.valuerost = self.rost.value()
        self.valueAge = self.Age.value()
        pol = self.floor_pol.currentText()
        print(self.valueAge, self.valueves, self.valuerost)
        if pol == "м":
            self.polt = True
        else:
            self.polt = False
        if pol:
            self.caloris = 66.5 + 13.75 * self.valueves + 5.003 * self.valuerost - 6.775 * self.valueAge
        else:
            self.caloris = 655.1 + 9.563 * self.valueves + 1.85 * self.valuerost - 4.676 * self.valueAge
        self.caloris = int(self.caloris)
        round(self.caloris)
        self.caloris = str(self.caloris)
        self.Kolvo_kaloriy.setText(self.caloris)
    def Sbrosvalue(self):
        self.Kolvo_kaloriy.setText('0')
        self.ves.setValue(0)
        self.rost.setValue(0)
        self.Age.setValue(0)



class Menu(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('menu1.ui', self)
        self.sport.clicked.connect(self.menusport)
        self.food.clicked.connect(self.menufood)
        self.menuhelp.addAction('Option #1', self.actionClicked)
    def menusport(self):
        print(101)
        self.window_of_seeing_all = Sport()
        self.window_of_seeing_all.show()

    def actionClicked(self):
        action = self.sender()


    def menufood(self):
        print(202)
        self.window_of_seeing_all = Food()
        self.window_of_seeing_all.show()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_F1:
            print('INFO_ERROR')
        if event.key() == Qt.Key_Q:
            image = Image.open('BUBA.jpg')
            image.show()
            print('Буба')
    def frobnicate(self):
        print('INFO_ERROR')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Menu()
    ex.show()
    sys.exit(app.exec_())
