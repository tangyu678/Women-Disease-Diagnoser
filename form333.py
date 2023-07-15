

from PyQt5 import QtCore, QtGui, QtWidgets
from form444 import Ui_MainWindow
list3=[]

class Ui_page3(object):
    def nextw3(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        if self.vaginal_discharge.isChecked() == True:
          
            list3.append("vaginal_discharge")
     
            
        if self.increased_vaginal_discharge.isChecked() == True:
         
            list3.append("increased_vaginal_discharge")
    
        
        if self.foulsmelling_vaginal_discharge.isChecked() == True:
      
            list3.append("foulsmelling_vaginal_discharge")
               
        if self.abnormal_vaginal_discharge.isChecked() == True:
       
            list3.append("abnormal_vaginal_discharge")
     
            
        if self.vaginal_dryness.isChecked() == True:
        
            list3.append("vaginal_dryness")
   
            
        if self.vaginal_itching.isChecked() == True:

            list3.append("vaginal_itching")

            
        if self.vaginal_burning.isChecked() == True:
   
            list3.append("vaginal_burning")
  
            
        if self.vaginal_irritation.isChecked() == True:

            list3.append("vaginal_irritation")
    
            
        if self.vaginal_odour.isChecked() == True:

            list3.append("vaginal_odour")
 
            
        if self.vaginal_inflammation.isChecked() == True:

            list3.append("vaginal_inflammation")

            
        if self.vulval_itch.isChecked() == True:
 
            list3.append("vulval_itch")
 
            
        if self.vulval_inflammation.isChecked() == True:

            list3.append("vulval_inflammation")
 
            
        if self.cervix_inflammation.isChecked() == True:

            list3.append("cervix_inflammation")
        if self.recurrent_utis.isChecked() == True:

            list3.append("recurrent_utis")

        if self.inability_to_get_pregnant.isChecked() == True:

            list3.append("inability_to_get_pregnant")

            
        if self.infertility.isChecked() == True:

            list3.append("infertility")

            
        if self.subfertility.isChecked() == True:

            list3.append("subfertility")

            
        if self.sexual_dysfunction.isChecked() == True:
            list3.append("sexual_dysfunction")

            
            
        if self.postmenopausal_bleeding.isChecked() == True:
            list3.append("postmenopausal_bleeding")
            
        if self.abnormal_vaginal_bleeding.isChecked() == True:
            list3.append("abnormal_vaginal_bleeding")
                        
        if self.spotting.isChecked() == True:
            list3.append("spotting")
            
            
        if self.lump_near_vaginal_opening.isChecked() == True:
            list3.append("lump_near_vaginal_opening")
            
            
        if self.vaginal_erythema.isChecked() == True:
            list3.append("vaginal_erythema")
            
            
        if self.cervical_motion_tenderness.isChecked() == True:
            list3.append("cervical_motion_tenderness")
            
        if self.irregular_uterine_bleeding.isChecked() == True:
            list3.append("irregular_uterine_bleeding")
        file = open('listss.txt','a')
        for l in list3:
          file.write(l+"\n")
        file.close()
   

            
        
  
    def setupUi(self, page3):
        page3.setObjectName("page3")
        page3.resize(781, 532)
        self.centralwidget = QtWidgets.QWidget(page3)
        self.centralwidget.setObjectName("centralwidget")
        self.page3_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.page3_2.setGeometry(QtCore.QRect(20, 0, 701, 471))
        self.page3_2.setAutoFillBackground(True)
        self.page3_2.setTitle("")
        self.page3_2.setObjectName("page3_2")
        self.vaginal_discharge = QtWidgets.QCheckBox(self.page3_2)
        self.vaginal_discharge.setGeometry(QtCore.QRect(10, 10, 491, 21))
        self.vaginal_discharge.setObjectName("vaginal_discharge")
        self.increased_vaginal_discharge = QtWidgets.QCheckBox(self.page3_2)
        self.increased_vaginal_discharge.setGeometry(QtCore.QRect(10, 30, 451, 21))
        self.increased_vaginal_discharge.setObjectName("increased_vaginal_discharge")
        self.foulsmelling_vaginal_discharge = QtWidgets.QCheckBox(self.page3_2)
        self.foulsmelling_vaginal_discharge.setGeometry(QtCore.QRect(10, 50, 491, 21))
        self.foulsmelling_vaginal_discharge.setObjectName("foulsmelling_vaginal_discharge")
        self.abnormal_vaginal_discharge = QtWidgets.QCheckBox(self.page3_2)
        self.abnormal_vaginal_discharge.setGeometry(QtCore.QRect(10, 70, 691, 21))
        self.abnormal_vaginal_discharge.setObjectName("abnormal_vaginal_discharge")
        self.vaginal_dryness = QtWidgets.QCheckBox(self.page3_2)
        self.vaginal_dryness.setGeometry(QtCore.QRect(20, 110, 51, 31))
        self.vaginal_dryness.setObjectName("vaginal_dryness")
        self.vaginal_itching = QtWidgets.QCheckBox(self.page3_2)
        self.vaginal_itching.setGeometry(QtCore.QRect(80, 110, 51, 31))
        self.vaginal_itching.setObjectName("vaginal_itching")
        self.vaginal_irritation = QtWidgets.QCheckBox(self.page3_2)
        self.vaginal_irritation.setGeometry(QtCore.QRect(240, 110, 61, 31))
        self.vaginal_irritation.setObjectName("vaginal_irritation")
        self.vaginal_burning = QtWidgets.QCheckBox(self.page3_2)
        self.vaginal_burning.setGeometry(QtCore.QRect(150, 110, 81, 31))
        self.vaginal_burning.setObjectName("vaginal_burning")
        self.vulval_itch = QtWidgets.QCheckBox(self.page3_2)
        self.vulval_itch.setGeometry(QtCore.QRect(10, 150, 331, 31))
        self.vulval_itch.setObjectName("vulval_itch")
        self.label = QtWidgets.QLabel(self.page3_2)
        self.label.setGeometry(QtCore.QRect(10, 90, 121, 16))
        self.label.setObjectName("label")
        self.vulval_inflammation = QtWidgets.QCheckBox(self.page3_2)
        self.vulval_inflammation.setGeometry(QtCore.QRect(10, 170, 331, 31))
        self.vulval_inflammation.setObjectName("vulval_inflammation")
        self.vaginal_inflammation = QtWidgets.QCheckBox(self.page3_2)
        self.vaginal_inflammation.setGeometry(QtCore.QRect(10, 130, 351, 31))
        self.vaginal_inflammation.setObjectName("vaginal_inflammation")
        self.cervix_inflammation = QtWidgets.QCheckBox(self.page3_2)
        self.cervix_inflammation.setGeometry(QtCore.QRect(10, 190, 331, 31))
        self.cervix_inflammation.setObjectName("cervix_inflammation")
        self.recurrent_utis = QtWidgets.QCheckBox(self.page3_2)
        self.recurrent_utis.setGeometry(QtCore.QRect(10, 210, 351, 31))
        self.recurrent_utis.setObjectName("recurrent_utis")
        self.inability_to_get_pregnant = QtWidgets.QCheckBox(self.page3_2)
        self.inability_to_get_pregnant.setGeometry(QtCore.QRect(10, 230, 421, 31))
        self.inability_to_get_pregnant.setObjectName("inability_to_get_pregnant")
        self.infertility = QtWidgets.QCheckBox(self.page3_2)
        self.infertility.setGeometry(QtCore.QRect(10, 250, 201, 31))
        self.infertility.setObjectName("infertility")
        self.sexual_dysfunction = QtWidgets.QCheckBox(self.page3_2)
        self.sexual_dysfunction.setGeometry(QtCore.QRect(10, 270, 361, 31))
        self.sexual_dysfunction.setObjectName("sexual_dysfunction")
        self.subfertility = QtWidgets.QCheckBox(self.page3_2)
        self.subfertility.setGeometry(QtCore.QRect(210, 250, 201, 31))
        self.subfertility.setObjectName("subfertility")
        self.postmenopausal_bleeding = QtWidgets.QCheckBox(self.page3_2)
        self.postmenopausal_bleeding.setGeometry(QtCore.QRect(10, 290, 361, 31))
        self.postmenopausal_bleeding.setObjectName("postmenopausal_bleeding")
        self.abnormal_vaginal_bleeding = QtWidgets.QCheckBox(self.page3_2)
        self.abnormal_vaginal_bleeding.setGeometry(QtCore.QRect(10, 310, 461, 31))
        self.abnormal_vaginal_bleeding.setObjectName("abnormal_vaginal_bleeding")
        self.spotting = QtWidgets.QCheckBox(self.page3_2)
        self.spotting.setGeometry(QtCore.QRect(10, 330, 541, 31))
        self.spotting.setObjectName("spotting")
        self.lump_near_vaginal_opening = QtWidgets.QCheckBox(self.page3_2)
        self.lump_near_vaginal_opening.setGeometry(QtCore.QRect(10, 350, 431, 31))
        self.lump_near_vaginal_opening.setObjectName("lump_near_vaginal_opening")
        self.vaginal_erythema = QtWidgets.QCheckBox(self.page3_2)
        self.vaginal_erythema.setGeometry(QtCore.QRect(10, 390, 431, 31))
        self.vaginal_erythema.setObjectName("vaginal_erythema")
        self.label_2 = QtWidgets.QLabel(self.page3_2)
        self.label_2.setGeometry(QtCore.QRect(10, 380, 251, 16))
        self.label_2.setObjectName("label_2")
        self.cervical_motion_tenderness = QtWidgets.QCheckBox(self.page3_2)
        self.cervical_motion_tenderness.setGeometry(QtCore.QRect(170, 390, 431, 31))
        self.cervical_motion_tenderness.setObjectName("cervical_motion_tenderness")
        self.vaginal_odour = QtWidgets.QCheckBox(self.page3_2)
        self.vaginal_odour.setGeometry(QtCore.QRect(320, 110, 61, 31))
        self.vaginal_odour.setObjectName("vaginal_odour")
        self.irregular_uterine_bleeding = QtWidgets.QCheckBox(self.page3_2)
        self.irregular_uterine_bleeding.setGeometry(QtCore.QRect(10, 410, 431, 31))
        self.irregular_uterine_bleeding.setObjectName("irregular_uterine_bleeding")
        self.next3 = QtWidgets.QPushButton(self.page3_2,clicked = lambda:self.nextw3())
        self.next3.setGeometry(QtCore.QRect(480, 430, 75, 23))
        self.next3.setCheckable(False)
        self.next3.setObjectName("next3")
        page3.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(page3)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 781, 22))
        self.menubar.setObjectName("menubar")
        page3.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(page3)
        self.statusbar.setObjectName("statusbar")
        page3.setStatusBar(self.statusbar)

        self.retranslateUi(page3)
        QtCore.QMetaObject.connectSlotsByName(page3)

    def retranslateUi(self, page3):
        _translate = QtCore.QCoreApplication.translate
        page3.setWindowTitle(_translate("page3", "MainWindow"))
        self.vaginal_discharge.setText(_translate("page3", "Do you have vaginal discharge?"))
        self.increased_vaginal_discharge.setText(_translate("page3", "Is your vaginal discharge a lot?"))
        self.foulsmelling_vaginal_discharge.setText(_translate("page3", "Does your vaginal discharge smell foul?"))
        self.abnormal_vaginal_discharge.setText(_translate("page3", "Has there been an abnormal change in your discharge?"))
        self.vaginal_dryness.setText(_translate("page3", "dry"))
        self.vaginal_itching.setText(_translate("page3", "itchy"))
        self.vaginal_irritation.setText(_translate("page3", "irritated"))
        self.vaginal_burning.setText(_translate("page3", "burning"))
        self.vulval_itch.setText(_translate("page3", "Is your vulva itchy?"))
        self.label.setText(_translate("page3", "Is your vagina:"))
        self.vulval_inflammation.setText(_translate("page3", "Is your vulva inflamed?"))
        self.vaginal_inflammation.setText(_translate("page3", "Is your vagina inflamed?"))
        self.cervix_inflammation.setText(_translate("page3", "Is your cervix inflamed?"))
        self.recurrent_utis.setText(_translate("page3", "Do you have recurrent UTIs?"))
        self.inability_to_get_pregnant.setText(_translate("page3", "Are you unable to get pregnant?"))
        self.infertility.setText(_translate("page3", "Are you infertile?"))
        self.sexual_dysfunction.setText(_translate("page3", "Do you experience sexual dysfunction?"))
        self.subfertility.setText(_translate("page3", "Are you subfertile?"))
        self.postmenopausal_bleeding.setText(_translate("page3", "Do you still bleed after menopause?"))
        self.abnormal_vaginal_bleeding.setText(_translate("page3", "Do you abnormally bleed from your vagina?"))
        self.spotting.setText(_translate("page3", "Do you bleed from your vagina other than menstruation?"))
        self.lump_near_vaginal_opening.setText(_translate("page3", "Do you have a lump located near vaginal opening?"))
        self.vaginal_erythema.setText(_translate("page3", "vaginal erythema"))
        self.label_2.setText(_translate("page3", "Do you possess the following:"))
        self.cervical_motion_tenderness.setText(_translate("page3", "cervical motion tenderness"))
        self.vaginal_odour.setText(_translate("page3", "smelly"))
        self.irregular_uterine_bleeding.setText(_translate("page3", "Do you experience irregular uterine bleeding?"))
        self.next3.setText(_translate("page3", "Next"))

f = open("listss.txt", "a")
for i in range(0, len(list3)-1):
    f.write(list3[i])
    f.write("\n\n\n\n                         ")
f.close()
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    page3 = QtWidgets.QMainWindow()
    ui = Ui_page3()
    ui.setupUi(page3)
    page3.show()
    sys.exit(app.exec_())
