

from PyQt5 import QtCore, QtGui, QtWidgets
from form333 import Ui_page3
list2=[]
class Ui_page2(object):
    def nextw2(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_page3()
        self.ui.setupUi(self.window)
        self.window.show()
        if self.abscense_of_menstruation.isChecked() == False:
         
            list2.append("abscense_of_menstruation")
        agemens=int(self.agemens.text())
        f = open("lisage.txt", "r")
        ageeee=int(f.read())
        if ageeee-agemens<9:
            list2.append("early_onset_of_menstruation")
        if ageeee-agemens>16:
            list2.append("delayed_puberty")
        open('lisage.txt', 'w').close()
        regularmenss=int(self.regularmens.currentIndex())
        if regularmenss==1 or regularmenss==2:
            list2.append("irregular_menstruation")
        flowmenss=int(self.flowmens.currentIndex())
        if flowmenss==2:
            list2.append("heavy_menstruation")
        daymens=self.daymens.currentIndex()
        longmens=int(self.longmens.text())
        if flowmenss ==0 and longmens<=2:
            list2.append("short_and_light_menstruation")
            
        
        
        if self.painful_menstruation.isChecked() == True:
           
            list2.append("painful_menstruation")
        
        
        if self.cramping.isChecked() == True:
           
            list2.append("cramping")
        
        if self.abnormal_menstruation.isChecked() == True:
           
            list2.append("abnormal_menstruation")
        file = open('listss.txt','a')
        for l in list2:
          file.write(l+"\n")
        file.close()
        
        
    def setupUi(self, page2):
        page2.setObjectName("page2")
        page2.resize(764, 383)
        self.centralwidget = QtWidgets.QWidget(page2)
        self.centralwidget.setObjectName("centralwidget")
        self.x = QtWidgets.QGroupBox(self.centralwidget)
        self.x.setGeometry(QtCore.QRect(50, -20, 681, 391))
        self.x.setAutoFillBackground(True)
        self.x.setTitle("")
        self.x.setObjectName("x")
        self.label = QtWidgets.QLabel(self.x)
        self.label.setGeometry(QtCore.QRect(440, 80, 47, 14))
        self.label.setObjectName("label")
        self.agemen = QtWidgets.QLabel(self.x)
        self.agemen.setGeometry(QtCore.QRect(30, 80, 301, 16))
        self.agemen.setObjectName("agemen")
        self.label_3 = QtWidgets.QLabel(self.x)
        self.label_3.setGeometry(QtCore.QRect(30, 100, 321, 16))
        self.label_3.setObjectName("label_3")
        self.longmens = QtWidgets.QLineEdit(self.x)
        self.longmens.setGeometry(QtCore.QRect(320, 270, 71, 20))
        self.longmens.setObjectName("longmens")
        self.agemens = QtWidgets.QLineEdit(self.x)
        self.agemens.setGeometry(QtCore.QRect(340, 80, 91, 20))
        self.agemens.setObjectName("agemens")
        self.abscense_of_menstruation = QtWidgets.QCheckBox(self.x)
        self.abscense_of_menstruation.setGeometry(QtCore.QRect(30, 50, 151, 31))
        self.abscense_of_menstruation.setObjectName("abscense_of_menstruation")
        self.regularmens = QtWidgets.QComboBox(self.x)
        self.regularmens.setGeometry(QtCore.QRect(30, 140, 601, 22))
        self.regularmens.setObjectName("regularmens")
        self.regularmens.addItem("")
        self.regularmens.addItem("")
        self.regularmens.addItem("")
        self.label_4 = QtWidgets.QLabel(self.x)
        self.label_4.setGeometry(QtCore.QRect(30, 120, 271, 16))
        self.label_4.setObjectName("label_4")
        self.flowmen = QtWidgets.QLabel(self.x)
        self.flowmen.setGeometry(QtCore.QRect(30, 170, 281, 16))
        self.flowmen.setObjectName("flowmen")
        self.flowmens = QtWidgets.QComboBox(self.x)
        self.flowmens.setGeometry(QtCore.QRect(30, 190, 601, 22))
        self.flowmens.setObjectName("flowmens")
        self.flowmens.addItem("")
        self.flowmens.addItem("")
        self.flowmens.addItem("")
        self.daysmen = QtWidgets.QLabel(self.x)
        self.daysmen.setGeometry(QtCore.QRect(30, 220, 341, 16))
        self.daysmen.setObjectName("daysmen")
        self.daymens = QtWidgets.QComboBox(self.x)
        self.daymens.setGeometry(QtCore.QRect(30, 240, 471, 22))
        self.daymens.setObjectName("daymens")
        self.daymens.addItem("")
        self.daymens.addItem("")
        self.label_7 = QtWidgets.QLabel(self.x)
        self.label_7.setGeometry(QtCore.QRect(30, 270, 281, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.x)
        self.label_8.setGeometry(QtCore.QRect(440, 270, 47, 14))
        self.label_8.setObjectName("label_8")
        self.painful_menstruation = QtWidgets.QCheckBox(self.x)
        self.painful_menstruation.setGeometry(QtCore.QRect(30, 300, 401, 18))
        self.painful_menstruation.setObjectName("painful_menstruation")
        self.cramping = QtWidgets.QCheckBox(self.x)
        self.cramping.setGeometry(QtCore.QRect(30, 320, 461, 18))
        self.cramping.setObjectName("cramping")
        self.abnormal_menstruation = QtWidgets.QCheckBox(self.x)
        self.abnormal_menstruation.setGeometry(QtCore.QRect(30, 340, 461, 18))
        self.abnormal_menstruation.setObjectName("abnormal_menstruation")
        self.next2 = QtWidgets.QPushButton(self.x,clicked = lambda:self.nextw2())
        self.next2.setGeometry(QtCore.QRect(330, 360, 75, 23))
        self.next2.setObjectName("next2")
        page2.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(page2)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 764, 22))
        self.menubar.setObjectName("menubar")
        page2.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(page2)
        self.statusbar.setObjectName("statusbar")
        page2.setStatusBar(self.statusbar)

        self.retranslateUi(page2)
        QtCore.QMetaObject.connectSlotsByName(page2)

    def retranslateUi(self, page2):
        _translate = QtCore.QCoreApplication.translate
        page2.setWindowTitle(_translate("page2", "MainWindow"))
        self.label.setText(_translate("page2", "years"))
        self.agemen.setText(_translate("page2", "How long have you been menstruating?"))
        self.label_3.setText(_translate("page2", "(Write 0 if less than a year.)"))
        self.abscense_of_menstruation.setText(_translate("page2", "Are you menstruating?"))
        self.regularmens.setItemText(0, _translate("page2", "Regular: periods happen at similar intervals of approximately 25 days"))
        self.regularmens.setItemText(1, _translate("page2", "Irregular: periods happen at widely ranging intervals (<21 or >35 days)"))
        self.regularmens.setItemText(2, _translate("page2", "Very Irregular periods: missed three or more periods in a row"))
        self.label_4.setText(_translate("page2", "Are your periods regular?"))
        self.flowmen.setText(_translate("page2", "How heavy is your flow?"))
        self.flowmens.setItemText(0, _translate("page2", "light"))
        self.flowmens.setItemText(1, _translate("page2", "normal: you need to change your tampon/pad after >3 or <8 hours"))
        self.flowmens.setItemText(2, _translate("page2", "heavy: you need to change your tampon/pad after <2 hours"))
        self.daysmen.setText(_translate("page2", "When is your flow the greatest?"))
        self.daymens.setItemText(0, _translate("page2", "first 1-2 days"))
        self.daymens.setItemText(1, _translate("page2", "consistent flow"))
        self.label_7.setText(_translate("page2", "How long do your periods last?"))
        self.label_8.setText(_translate("page2", "days"))
        self.painful_menstruation.setText(_translate("page2", "Do you have severe pain during your periods?"))
        self.cramping.setText(_translate("page2", "Do you suffer from cramping during menstruation?"))
        self.abnormal_menstruation.setText(_translate("page2", "Has your flow or regularity of periods suddenly changed?"))
        self.next2.setText(_translate("page2", "Next"))

f = open("listss.txt", "a")
for i in range(0, len(list2)-1):
    f.write(list2[i])
    f.write("\n\n\n\n                         ")
f.close()
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    page2 = QtWidgets.QMainWindow()
    ui = Ui_page2()
    ui.setupUi(page2)
    page2.show()
    sys.exit(app.exec_())
