# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '5.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
list5=[]
from form666 import Ui_MainWindow

class Ui_xxxx(object):
    def nextw5(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        if self.enlarged_breasts.isChecked() == True:
             list5.append('enlarged_breasts')


        if self.breast_lump.isChecked() == True:
             list5.append('breast_lump')


        if self.discomfort_in_breast.isChecked() == True:
             list5.append('discomfort_in_breast')


        if self.change_in_breast_structure.isChecked() == True:
             list5.append('change_in_breast_structure')


        if self.inverted_nipple.isChecked() == True:
             list5.append('inverted_nipple')


        if self.nipple_discharge.isChecked() == True:
             list5.append('nipple_discharge')


        if self.unwanted_hair.isChecked() == True:
             list5.append('unwanted_hair')


        if self.hair_loss.isChecked() == True:
             list5.append('hair_loss')


        if self.facial_hair.isChecked() == True:
             list5.append('facial_hair')

# 
#         if self.loss_of_scalp_hair.isChecked() == True:
#              list5.append('loss_of_scalp_hair')


        if self.brittle_nails.isChecked() == True:
             list5.append('brittle_nails')


        if self.dry_hair.isChecked() == True:
             list5.append('dry_hair')


        if self.excessive_hairiness.isChecked() == True:
             list5.append('excessive_hairiness')


        if self.inappropriate_male_features.isChecked() == True:
             list5.append('inappropriate_male_features')


        if self.pubic_hair.isChecked() == True:
             list5.append('pubic_hair')


        if self.deepening_of_voice.isChecked() == True:
             list5.append('deepening_of_voice')


        if self.abnormal_heart_rhythm.isChecked() == True:
             list5.append('abnormal_heart_rhythm')


        if self.weight_gain.isChecked() == True:
             list5.append('weight_gain')


        if self.high_cholestrol.isChecked() == True:
             list5.append('high_cholestrol')


        if self.fast_heart_rate.isChecked() == True:
             list5.append('fast_heart_rate')


        if self.weight_loss.isChecked() == True:
             list5.append('weight_loss')


        if self.severe_unintentional_weight_loss.isChecked() == True:
             list5.append('severe_unintentional_weight_loss')


        if self.high_blood_pressure.isChecked() == True:
             list5.append('high_blood_pressure')


        if self.slow_heart_rate.isChecked() == True:
             list5.append('slow_heart_rate')


        if self.irregular_heart_rate.isChecked() == True:
             list5.append('irregular_heart_rate')


        if self.palpitations.isChecked() == True:
             list5.append('palpitations')


        if self.slow_growth.isChecked() == True:
             list5.append('slow_growth')
        file = open('listss.txt','a')
        for l in list5:
          file.write(l+"\n")
        file.close()

        
    def setupUi(self, xxxx):
        xxxx.setObjectName("xxxx")
        xxxx.resize(852, 418)
        self.centralwidget = QtWidgets.QWidget(xxxx)
        self.centralwidget.setObjectName("centralwidget")
        self.page5 = QtWidgets.QGroupBox(self.centralwidget)
        self.page5.setGeometry(QtCore.QRect(20, 30, 811, 351))
        self.page5.setAcceptDrops(False)
        self.page5.setAutoFillBackground(True)
        self.page5.setTitle("")
        self.page5.setObjectName("page5")
        self.label = QtWidgets.QLabel(self.page5)
        self.label.setGeometry(QtCore.QRect(20, 10, 561, 16))
        self.label.setObjectName("label")
        self.enlarged_breasts = QtWidgets.QCheckBox(self.page5)
        self.enlarged_breasts.setGeometry(QtCore.QRect(20, 30, 261, 18))
        self.enlarged_breasts.setObjectName("enlarged_breasts")
        self.breast_lump = QtWidgets.QCheckBox(self.page5)
        self.breast_lump.setGeometry(QtCore.QRect(570, 30, 211, 18))
        self.breast_lump.setObjectName("breast_lump")
        self.discomfort_in_breast = QtWidgets.QCheckBox(self.page5)
        self.discomfort_in_breast.setGeometry(QtCore.QRect(290, 30, 301, 18))
        self.discomfort_in_breast.setObjectName("discomfort_in_breast")
        self.change_in_breast_structure = QtWidgets.QCheckBox(self.page5)
        self.change_in_breast_structure.setGeometry(QtCore.QRect(20, 50, 151, 18))
        self.change_in_breast_structure.setObjectName("change_in_breast_structure")
        self.inverted_nipple = QtWidgets.QCheckBox(self.page5)
        self.inverted_nipple.setGeometry(QtCore.QRect(290, 50, 111, 18))
        self.inverted_nipple.setObjectName("inverted_nipple")
        self.nipple_discharge = QtWidgets.QCheckBox(self.page5)
        self.nipple_discharge.setGeometry(QtCore.QRect(570, 50, 201, 18))
        self.nipple_discharge.setObjectName("nipple_discharge")
        self.unwanted_hair = QtWidgets.QCheckBox(self.page5)
        self.unwanted_hair.setGeometry(QtCore.QRect(290, 80, 281, 18))
        self.unwanted_hair.setObjectName("unwanted_hair")
        self.hair_loss = QtWidgets.QCheckBox(self.page5)
        self.hair_loss.setGeometry(QtCore.QRect(20, 80, 251, 18))
        self.hair_loss.setObjectName("hair_loss")
        self.facial_hair = QtWidgets.QCheckBox(self.page5)
        self.facial_hair.setGeometry(QtCore.QRect(570, 80, 241, 18))
        self.facial_hair.setObjectName("facial_hair")
        self.loss_of_scalp_hair = QtWidgets.QCheckBox(self.page5)
        self.loss_of_scalp_hair.setGeometry(QtCore.QRect(570, 100, 231, 18))
        self.loss_of_scalp_hair.setObjectName("loss_of_scalp_hair")
        self.brittle_nails = QtWidgets.QCheckBox(self.page5)
        self.brittle_nails.setGeometry(QtCore.QRect(20, 150, 261, 18))
        self.brittle_nails.setObjectName("brittle_nails")
        self.dry_hair = QtWidgets.QCheckBox(self.page5)
        self.dry_hair.setGeometry(QtCore.QRect(20, 100, 261, 18))
        self.dry_hair.setObjectName("dry_hair")
        self.excessive_hairiness = QtWidgets.QCheckBox(self.page5)
        self.excessive_hairiness.setGeometry(QtCore.QRect(290, 100, 271, 18))
        self.excessive_hairiness.setObjectName("excessive_hairiness")
        self.inappropriate_male_features = QtWidgets.QCheckBox(self.page5)
        self.inappropriate_male_features.setGeometry(QtCore.QRect(290, 170, 271, 18))
        self.inappropriate_male_features.setObjectName("inappropriate_male_features")
        self.pubic_hair = QtWidgets.QCheckBox(self.page5)
        self.pubic_hair.setGeometry(QtCore.QRect(20, 120, 261, 18))
        self.pubic_hair.setObjectName("pubic_hair")
        self.deepening_of_voice = QtWidgets.QCheckBox(self.page5)
        self.deepening_of_voice.setGeometry(QtCore.QRect(20, 170, 261, 18))
        self.deepening_of_voice.setObjectName("deepening_of_voice")
        self.abnormal_heart_rhythm = QtWidgets.QCheckBox(self.page5)
        self.abnormal_heart_rhythm.setGeometry(QtCore.QRect(20, 200, 271, 18))
        self.abnormal_heart_rhythm.setObjectName("abnormal_heart_rhythm")
        self.weight_gain = QtWidgets.QCheckBox(self.page5)
        self.weight_gain.setGeometry(QtCore.QRect(20, 310, 471, 18))
        self.weight_gain.setObjectName("weight_gain")
        self.high_cholestrol = QtWidgets.QCheckBox(self.page5)
        self.high_cholestrol.setGeometry(QtCore.QRect(290, 200, 271, 18))
        self.high_cholestrol.setObjectName("high_cholestrol")
        self.fast_heart_rate = QtWidgets.QCheckBox(self.page5)
        self.fast_heart_rate.setGeometry(QtCore.QRect(20, 240, 261, 18))
        self.fast_heart_rate.setObjectName("fast_heart_rate")
        self.weight_loss = QtWidgets.QCheckBox(self.page5)
        self.weight_loss.setGeometry(QtCore.QRect(20, 270, 331, 18))
        self.weight_loss.setObjectName("weight_loss")
        self.severe_unintentional_weight_loss = QtWidgets.QCheckBox(self.page5)
        self.severe_unintentional_weight_loss.setGeometry(QtCore.QRect(20, 290, 571, 18))
        self.severe_unintentional_weight_loss.setObjectName("severe_unintentional_weight_loss")
        self.high_blood_pressure = QtWidgets.QCheckBox(self.page5)
        self.high_blood_pressure.setGeometry(QtCore.QRect(20, 220, 271, 18))
        self.high_blood_pressure.setObjectName("high_blood_pressure")
        self.slow_heart_rate = QtWidgets.QCheckBox(self.page5)
        self.slow_heart_rate.setGeometry(QtCore.QRect(570, 220, 211, 18))
        self.slow_heart_rate.setObjectName("slow_heart_rate")
        self.irregular_heart_rate = QtWidgets.QCheckBox(self.page5)
        self.irregular_heart_rate.setGeometry(QtCore.QRect(290, 220, 261, 18))
        self.irregular_heart_rate.setObjectName("irregular_heart_rate")
        self.palpitations = QtWidgets.QCheckBox(self.page5)
        self.palpitations.setGeometry(QtCore.QRect(570, 200, 191, 18))
        self.palpitations.setObjectName("palpitations")
        self.slow_growth = QtWidgets.QCheckBox(self.page5)
        self.slow_growth.setGeometry(QtCore.QRect(290, 150, 261, 18))
        self.slow_growth.setObjectName("slow_growth")
        self.short_stature = QtWidgets.QCheckBox(self.page5)
        self.short_stature.setGeometry(QtCore.QRect(570, 150, 261, 18))
        self.short_stature.setObjectName("short_stature")
        self.next5 = QtWidgets.QPushButton(self.page5, clicked = lambda:self.nextw5())
        self.next5.setGeometry(QtCore.QRect(580, 310, 75, 23))
        self.next5.setObjectName("next5")
        xxxx.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(xxxx)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 852, 22))
        self.menubar.setObjectName("menubar")
        xxxx.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(xxxx)
        self.statusbar.setObjectName("statusbar")
        xxxx.setStatusBar(self.statusbar)

        self.retranslateUi(xxxx)
        QtCore.QMetaObject.connectSlotsByName(xxxx)

    def retranslateUi(self, xxxx):
        _translate = QtCore.QCoreApplication.translate
        xxxx.setWindowTitle(_translate("xxxx", "MainWindow"))
        self.label.setText(_translate("xxxx", "Select the applicable experiences and conditions:"))
        self.enlarged_breasts.setText(_translate("xxxx", "enlarged breasts"))
        self.breast_lump.setText(_translate("xxxx", "breast lump"))
        self.discomfort_in_breast.setText(_translate("xxxx", "discomfort in breast"))
        self.change_in_breast_structure.setText(_translate("xxxx", "change in breast texture"))
        self.inverted_nipple.setText(_translate("xxxx", "inverted nipple"))
        self.nipple_discharge.setText(_translate("xxxx", "nipple discharge"))
        self.unwanted_hair.setText(_translate("xxxx", "unwanted hair"))
        self.hair_loss.setText(_translate("xxxx", "hair loss"))
        self.facial_hair.setText(_translate("xxxx", "facial hair"))
        self.loss_of_scalp_hair.setText(_translate("xxxx", "loss of scalp hair"))
        self.brittle_nails.setText(_translate("xxxx", "brittle nails"))
        self.dry_hair.setText(_translate("xxxx", "dry hair"))
        self.excessive_hairiness.setText(_translate("xxxx", "excessive hairiness"))
        self.inappropriate_male_features.setText(_translate("xxxx", "inappropriate male features"))
        self.pubic_hair.setText(_translate("xxxx", "pubic hair"))
        self.deepening_of_voice.setText(_translate("xxxx", "deepening of voice"))
        self.abnormal_heart_rhythm.setText(_translate("xxxx", "abnormal heart rhythm"))
        self.weight_gain.setText(_translate("xxxx", "Have you gained weight?"))
        self.high_cholestrol.setText(_translate("xxxx", "high cholestrol"))
        self.fast_heart_rate.setText(_translate("xxxx", "fast heart rate"))
        self.weight_loss.setText(_translate("xxxx", "Have you lost weight?"))
        self.severe_unintentional_weight_loss.setText(_translate("xxxx", "Was the weight loss severe and unintentional?"))
        self.high_blood_pressure.setText(_translate("xxxx", "high blood pressure"))
        self.slow_heart_rate.setText(_translate("xxxx", "slow heart rate"))
        self.irregular_heart_rate.setText(_translate("xxxx", "irregular heart rate"))
        self.palpitations.setText(_translate("xxxx", "palpitations"))
        self.slow_growth.setText(_translate("xxxx", "slow growth"))
        self.short_stature.setText(_translate("xxxx", "short stature"))
        self.next5.setText(_translate("xxxx", "Next"))

f = open("listss.txt", "a")
for i in range(0, len(list5)-1):
    f.write(list5[i])
    f.write("\n\n\n\n                         ")
f.close()
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    xxxx = QtWidgets.QMainWindow()
    ui = Ui_xxxx()
    ui.setupUi(xxxx)
    xxxx.show()
    sys.exit(app.exec_())
