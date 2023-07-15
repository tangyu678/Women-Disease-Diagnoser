

from PyQt5 import QtCore, QtGui, QtWidgets
from form555 import Ui_xxxx
list4=[]


    

class Ui_MainWindow(object):
    
    def nextw4(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_xxxx()
        self.ui.setupUi(self.window)
        self.window.show()
        
        if self.vomiting.isChecked() == True:
             list4.append('vomiting')


        if self.dark_urine.isChecked() == True:
             list4.append('dark_urine')


        if self.nausea.isChecked() == True:
             list4.append('nausea')


        if self.passing_excessive_amounts_of_gas.isChecked() == True:
             list4.append('passing_excessive_amounts_of_gas')


        if self.foul_smelling_urine.isChecked() == True:
             list4.append('foul_smelling_urine')


        if self.persistent_urge_to_urinate.isChecked() == True:
             list4.append('persistent_urge_to_urinate')


        if self.blood_in_urine.isChecked() == True:
             list4.append('blood_in_urine')


        if self.frequent_urge_to_urinate.isChecked() == True:
             list4.append('frequent_urge_to_urinate')


        if self.cloudy_urine.isChecked() == True:
             list4.append('cloudy_urine')


        if self.excessive_urination_at_night.isChecked() == True:
             list4.append('excessive_urination_at_night')


        if self.frequent_urination.isChecked() == True:
             list4.append('frequent_urination')


        if self.excess_sweating.isChecked() == True:
             list4.append('excess_sweating')


        if self.night_sweats.isChecked() == True:
             list4.append('night_sweats')


        if self.constipation.isChecked() == True:
             list4.append('constipation')


        if self.water_retention.isChecked() == True:
             list4.append('water_retention')


        if self.change_in_bowel_habits.isChecked() == True:
             list4.append('change_in_bowel_habits')


        if self.leaking_of_stool.isChecked() == True:
             list4.append('leaking_of_stool')


        if self.indigestion.isChecked() == True:
             list4.append('indigestion')


        if self.fluid_in_the_abdomen.isChecked() == True:
             list4.append('fluid_in_the_abdomen')


        if self.diarrhoea.isChecked() == True:
             list4.append('diarrhoea')


        if self.persistent_diarrhoea.isChecked() == True:
             list4.append('persistent_diarrhoea')


        if self.watery_diarrhoea.isChecked() == True:
             list4.append('watery_diarrhoea')


        if self.lump_in_the_abdomen.isChecked() == True:
             list4.append('lump_in_the_abdomen')


        if self.abdominal_distension.isChecked() == True:
             list4.append('abdominal_distension')



        if self.hot_flashes.isChecked() == True:
             list4.append('hot_flashes')


        if self.sensitivity_to_cold.isChecked() == True:
             list4.append('sensitivity_to_cold')


        if self.heat_intolerance.isChecked() == True:
             list4.append('heat_intolerance')


        if self.warm_skin.isChecked() == True:
             list4.append('warm_skin')


        if self.feeling_cold.isChecked() == True:
             list4.append('feeling_cold')


        if self.hand_tremor.isChecked() == True:
             list4.append('hand_tremor')


        if self.tremor.isChecked() == True:
             list4.append('tremor')


        if self.chills.isChecked() == True:
             list4.append('chills')


        if self.white_tongue.isChecked() == True:
             list4.append('white_tongue')


        if self.difficulty_swallowing.isChecked() == True:
             list4.append('difficulty_swallowing')


        if self.dry_cough.isChecked() == True:
             list4.append('dry_cough')


        if self.sore_throat.isChecked() == True:
             list4.append('sore_throat')


        if self.mouth_ulcer.isChecked() == True:
             list4.append('mouth_ulcer')


        if self.oral_thrush.isChecked() == True:
             list4.append('oral_thrush')


        if self.pneumonia.isChecked() == True:
             list4.append('pneumonia')


        if self.enlarged_thyroid.isChecked() == True:
             list4.append('enlarged_thyroid')


        if self.bloating.isChecked() == True:
             list4.append('bloating')


        if self.puffy_eyes.isChecked() == True:
             list4.append('puffy_eyes')


        if self.abnormal_protrusion_of_eyes.isChecked() == True:
             list4.append('abnormal_protrusion_of_eyes')


        if self.hearing_loss.isChecked() == True:
             list4.append('hearing_loss')


        if self.sense_of_incomplete_bladder_emptying.isChecked() == True:
             list4.append('sense_of_incomplete_bladder_emptying')


        if self.abdominal_fullness.isChecked() == True:
             list4.append('abdominal_fullness')
        file = open('listss.txt','a')
        for l in list4:
          file.write(l+"\n")
        file.close()

                    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(893, 535)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.page4 = QtWidgets.QGroupBox(self.centralwidget)
        self.page4.setGeometry(QtCore.QRect(10, -10, 881, 371))
        self.page4.setAutoFillBackground(True)
        self.page4.setTitle("")
        self.page4.setObjectName("page4")
        self.vomiting = QtWidgets.QCheckBox(self.page4)
        self.vomiting.setGeometry(QtCore.QRect(10, 30, 231, 21))
        self.vomiting.setObjectName("vomiting")
        self.dark_urine = QtWidgets.QCheckBox(self.page4)
        self.dark_urine.setGeometry(QtCore.QRect(10, 90, 271, 21))
        self.dark_urine.setObjectName("dark_urine")
        self.nausea = QtWidgets.QCheckBox(self.page4)
        self.nausea.setGeometry(QtCore.QRect(280, 30, 241, 21))
        self.nausea.setObjectName("nausea")
        self.passing_excessive_amounts_of_gas = QtWidgets.QCheckBox(self.page4)
        self.passing_excessive_amounts_of_gas.setGeometry(QtCore.QRect(10, 50, 301, 21))
        self.passing_excessive_amounts_of_gas.setObjectName("passing_excessive_amounts_of_gas")
        self.foul_smelling_urine = QtWidgets.QCheckBox(self.page4)
        self.foul_smelling_urine.setGeometry(QtCore.QRect(10, 70, 301, 21))
        self.foul_smelling_urine.setObjectName("foul_smelling_urine")
        self.persistent_urge_to_urinate = QtWidgets.QCheckBox(self.page4)
        self.persistent_urge_to_urinate.setGeometry(QtCore.QRect(280, 50, 271, 21))
        self.persistent_urge_to_urinate.setObjectName("persistent_urge_to_urinate")
        self.blood_in_urine = QtWidgets.QCheckBox(self.page4)
        self.blood_in_urine.setGeometry(QtCore.QRect(550, 70, 301, 21))
        self.blood_in_urine.setObjectName("blood_in_urine")
        self.frequent_urge_to_urinate = QtWidgets.QCheckBox(self.page4)
        self.frequent_urge_to_urinate.setGeometry(QtCore.QRect(550, 50, 311, 21))
        self.frequent_urge_to_urinate.setObjectName("frequent_urge_to_urinate")
        self.cloudy_urine = QtWidgets.QCheckBox(self.page4)
        self.cloudy_urine.setGeometry(QtCore.QRect(280, 90, 281, 21))
        self.cloudy_urine.setObjectName("cloudy_urine")
        self.excessive_urination_at_night = QtWidgets.QCheckBox(self.page4)
        self.excessive_urination_at_night.setGeometry(QtCore.QRect(280, 70, 301, 21))
        self.excessive_urination_at_night.setObjectName("excessive_urination_at_night")
        self.frequent_urination = QtWidgets.QCheckBox(self.page4)
        self.frequent_urination.setGeometry(QtCore.QRect(550, 30, 301, 21))
        self.frequent_urination.setObjectName("frequent_urination")
        self.excess_sweating = QtWidgets.QCheckBox(self.page4)
        self.excess_sweating.setGeometry(QtCore.QRect(550, 90, 271, 21))
        self.excess_sweating.setObjectName("excess_sweating")
        self.night_sweats = QtWidgets.QCheckBox(self.page4)
        self.night_sweats.setGeometry(QtCore.QRect(10, 110, 261, 21))
        self.night_sweats.setObjectName("night_sweats")
        self.constipation = QtWidgets.QCheckBox(self.page4)
        self.constipation.setGeometry(QtCore.QRect(280, 110, 261, 21))
        self.constipation.setObjectName("constipation")
        self.water_retention = QtWidgets.QCheckBox(self.page4)
        self.water_retention.setGeometry(QtCore.QRect(10, 150, 261, 21))
        self.water_retention.setObjectName("water_retention")
        self.change_in_bowel_habits = QtWidgets.QCheckBox(self.page4)
        self.change_in_bowel_habits.setGeometry(QtCore.QRect(10, 170, 271, 21))
        self.change_in_bowel_habits.setObjectName("change_in_bowel_habits")
        self.leaking_of_stool = QtWidgets.QCheckBox(self.page4)
        self.leaking_of_stool.setGeometry(QtCore.QRect(280, 150, 261, 21))
        self.leaking_of_stool.setObjectName("leaking_of_stool")
        self.indigestion = QtWidgets.QCheckBox(self.page4)
        self.indigestion.setGeometry(QtCore.QRect(550, 110, 261, 21))
        self.indigestion.setObjectName("indigestion")
        self.fluid_in_the_abdomen = QtWidgets.QCheckBox(self.page4)
        self.fluid_in_the_abdomen.setGeometry(QtCore.QRect(280, 170, 261, 21))
        self.fluid_in_the_abdomen.setObjectName("fluid_in_the_abdomen")
        self.diarrhoea = QtWidgets.QCheckBox(self.page4)
        self.diarrhoea.setGeometry(QtCore.QRect(10, 130, 261, 21))
        self.diarrhoea.setObjectName("diarrhoea")
        self.persistent_diarrhoea = QtWidgets.QCheckBox(self.page4)
        self.persistent_diarrhoea.setGeometry(QtCore.QRect(550, 130, 291, 21))
        self.persistent_diarrhoea.setObjectName("persistent_diarrhoea")
        self.watery_diarrhoea = QtWidgets.QCheckBox(self.page4)
        self.watery_diarrhoea.setGeometry(QtCore.QRect(280, 130, 261, 21))
        self.watery_diarrhoea.setObjectName("watery_diarrhoea")
        self.lump_in_the_abdomen = QtWidgets.QCheckBox(self.page4)
        self.lump_in_the_abdomen.setGeometry(QtCore.QRect(10, 190, 341, 21))
        self.lump_in_the_abdomen.setObjectName("lump_in_the_abdomen")
        self.abdominal_distension = QtWidgets.QCheckBox(self.page4)
        self.abdominal_distension.setGeometry(QtCore.QRect(550, 150, 301, 21))
        self.abdominal_distension.setObjectName("abdominal_distension")
        self.label = QtWidgets.QLabel(self.page4)
        self.label.setGeometry(QtCore.QRect(10, 10, 251, 16))
        self.label.setObjectName("label")
        self.hot_flashes = QtWidgets.QCheckBox(self.page4)
        self.hot_flashes.setGeometry(QtCore.QRect(10, 230, 291, 21))
        self.hot_flashes.setObjectName("hot_flashes")
        self.sensitivity_to_cold = QtWidgets.QCheckBox(self.page4)
        self.sensitivity_to_cold.setGeometry(QtCore.QRect(280, 250, 271, 21))
        self.sensitivity_to_cold.setObjectName("sensitivity_to_cold")
        self.heat_intolerance = QtWidgets.QCheckBox(self.page4)
        self.heat_intolerance.setGeometry(QtCore.QRect(550, 230, 271, 21))
        self.heat_intolerance.setObjectName("heat_intolerance")
        self.warm_skin = QtWidgets.QCheckBox(self.page4)
        self.warm_skin.setGeometry(QtCore.QRect(280, 230, 261, 21))
        self.warm_skin.setObjectName("warm_skin")
        self.feeling_cold = QtWidgets.QCheckBox(self.page4)
        self.feeling_cold.setGeometry(QtCore.QRect(10, 250, 261, 21))
        self.feeling_cold.setObjectName("feeling_cold")
        self.hand_tremor = QtWidgets.QCheckBox(self.page4)
        self.hand_tremor.setGeometry(QtCore.QRect(10, 310, 271, 21))
        self.hand_tremor.setObjectName("hand_tremor")
        self.tremor = QtWidgets.QCheckBox(self.page4)
        self.tremor.setGeometry(QtCore.QRect(550, 290, 241, 21))
        self.tremor.setObjectName("tremor")
        self.chills = QtWidgets.QCheckBox(self.page4)
        self.chills.setGeometry(QtCore.QRect(550, 250, 221, 21))
        self.chills.setObjectName("chills")
        self.white_tongue = QtWidgets.QCheckBox(self.page4)
        self.white_tongue.setGeometry(QtCore.QRect(280, 290, 261, 21))
        self.white_tongue.setObjectName("white_tongue")
        self.difficulty_swallowing = QtWidgets.QCheckBox(self.page4)
        self.difficulty_swallowing.setGeometry(QtCore.QRect(280, 210, 261, 21))
        self.difficulty_swallowing.setObjectName("difficulty_swallowing")
        self.dry_cough = QtWidgets.QCheckBox(self.page4)
        self.dry_cough.setGeometry(QtCore.QRect(280, 270, 261, 21))
        self.dry_cough.setObjectName("dry_cough")
        self.sore_throat = QtWidgets.QCheckBox(self.page4)
        self.sore_throat.setGeometry(QtCore.QRect(550, 270, 261, 21))
        self.sore_throat.setObjectName("sore_throat")
        self.mouth_ulcer = QtWidgets.QCheckBox(self.page4)
        self.mouth_ulcer.setGeometry(QtCore.QRect(550, 210, 291, 21))
        self.mouth_ulcer.setObjectName("mouth_ulcer")
        self.oral_thrush = QtWidgets.QCheckBox(self.page4)
        self.oral_thrush.setGeometry(QtCore.QRect(10, 270, 261, 21))
        self.oral_thrush.setObjectName("oral_thrush")
        self.pneumonia = QtWidgets.QCheckBox(self.page4)
        self.pneumonia.setGeometry(QtCore.QRect(10, 290, 261, 21))
        self.pneumonia.setObjectName("pneumonia")
        self.enlarged_thyroid = QtWidgets.QCheckBox(self.page4)
        self.enlarged_thyroid.setGeometry(QtCore.QRect(280, 310, 271, 21))
        self.enlarged_thyroid.setObjectName("enlarged_thyroid")
        self.bloating = QtWidgets.QCheckBox(self.page4)
        self.bloating.setGeometry(QtCore.QRect(10, 210, 281, 21))
        self.bloating.setObjectName("bloating")
        self.puffy_eyes = QtWidgets.QCheckBox(self.page4)
        self.puffy_eyes.setGeometry(QtCore.QRect(280, 330, 231, 21))
        self.puffy_eyes.setObjectName("puffy_eyes")
        self.abnormal_protrusion_of_eyes = QtWidgets.QCheckBox(self.page4)
        self.abnormal_protrusion_of_eyes.setGeometry(QtCore.QRect(10, 330, 271, 21))
        self.abnormal_protrusion_of_eyes.setObjectName("abnormal_protrusion_of_eyes")
        self.hearing_loss = QtWidgets.QCheckBox(self.page4)
        self.hearing_loss.setGeometry(QtCore.QRect(550, 310, 271, 21))
        self.hearing_loss.setObjectName("hearing_loss")
        self.sense_of_incomplete_bladder_emptying = QtWidgets.QCheckBox(self.page4)
        self.sense_of_incomplete_bladder_emptying.setGeometry(QtCore.QRect(550, 190, 331, 21))
        self.sense_of_incomplete_bladder_emptying.setObjectName("sense_of_incomplete_bladder_emptying")
        self.abdominal_fullness = QtWidgets.QCheckBox(self.page4)
        self.abdominal_fullness.setGeometry(QtCore.QRect(550, 170, 291, 21))
        self.abdominal_fullness.setObjectName("abdominal_fullness")
        self.bladder_spasm = QtWidgets.QCheckBox(self.page4)
        self.bladder_spasm.setGeometry(QtCore.QRect(280, 190, 261, 21))
        self.bladder_spasm.setObjectName("bladder_spasm")
        self.next4 = QtWidgets.QPushButton(self.page4, clicked = lambda:self.nextw4() )
        self.next4.setGeometry(QtCore.QRect(660, 330, 75, 23))
        self.next4.setObjectName("next4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 893, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.vomiting, self.puffy_eyes)
        MainWindow.setTabOrder(self.puffy_eyes, self.nausea)
        MainWindow.setTabOrder(self.nausea, self.passing_excessive_amounts_of_gas)
        MainWindow.setTabOrder(self.passing_excessive_amounts_of_gas, self.foul_smelling_urine)
        MainWindow.setTabOrder(self.foul_smelling_urine, self.persistent_urge_to_urinate)
        MainWindow.setTabOrder(self.persistent_urge_to_urinate, self.blood_in_urine)
        MainWindow.setTabOrder(self.blood_in_urine, self.frequent_urge_to_urinate)
        MainWindow.setTabOrder(self.frequent_urge_to_urinate, self.cloudy_urine)
        MainWindow.setTabOrder(self.cloudy_urine, self.excessive_urination_at_night)
        MainWindow.setTabOrder(self.excessive_urination_at_night, self.frequent_urination)
        MainWindow.setTabOrder(self.frequent_urination, self.excess_sweating)
        MainWindow.setTabOrder(self.excess_sweating, self.night_sweats)
        MainWindow.setTabOrder(self.night_sweats, self.constipation)
        MainWindow.setTabOrder(self.constipation, self.water_retention)
        MainWindow.setTabOrder(self.water_retention, self.change_in_bowel_habits)
        MainWindow.setTabOrder(self.change_in_bowel_habits, self.leaking_of_stool)
        MainWindow.setTabOrder(self.leaking_of_stool, self.indigestion)
        MainWindow.setTabOrder(self.indigestion, self.fluid_in_the_abdomen)
        MainWindow.setTabOrder(self.fluid_in_the_abdomen, self.diarrhoea)
        MainWindow.setTabOrder(self.diarrhoea, self.persistent_diarrhoea)
        MainWindow.setTabOrder(self.persistent_diarrhoea, self.watery_diarrhoea)
        MainWindow.setTabOrder(self.watery_diarrhoea, self.lump_in_the_abdomen)
        MainWindow.setTabOrder(self.lump_in_the_abdomen, self.abdominal_distension)
        MainWindow.setTabOrder(self.abdominal_distension, self.hot_flashes)
        MainWindow.setTabOrder(self.hot_flashes, self.sensitivity_to_cold)
        MainWindow.setTabOrder(self.sensitivity_to_cold, self.heat_intolerance)
        MainWindow.setTabOrder(self.heat_intolerance, self.warm_skin)
        MainWindow.setTabOrder(self.warm_skin, self.feeling_cold)
        MainWindow.setTabOrder(self.feeling_cold, self.hand_tremor)
        MainWindow.setTabOrder(self.hand_tremor, self.tremor)
        MainWindow.setTabOrder(self.tremor, self.chills)
        MainWindow.setTabOrder(self.chills, self.white_tongue)
        MainWindow.setTabOrder(self.white_tongue, self.difficulty_swallowing)
        MainWindow.setTabOrder(self.difficulty_swallowing, self.dry_cough)
        MainWindow.setTabOrder(self.dry_cough, self.sore_throat)
        MainWindow.setTabOrder(self.sore_throat, self.mouth_ulcer)
        MainWindow.setTabOrder(self.mouth_ulcer, self.oral_thrush)
        MainWindow.setTabOrder(self.oral_thrush, self.pneumonia)
        MainWindow.setTabOrder(self.pneumonia, self.enlarged_thyroid)
        MainWindow.setTabOrder(self.enlarged_thyroid, self.bloating)
        MainWindow.setTabOrder(self.bloating, self.dark_urine)
        MainWindow.setTabOrder(self.dark_urine, self.abnormal_protrusion_of_eyes)
        MainWindow.setTabOrder(self.abnormal_protrusion_of_eyes, self.hearing_loss)
        MainWindow.setTabOrder(self.hearing_loss, self.sense_of_incomplete_bladder_emptying)
        MainWindow.setTabOrder(self.sense_of_incomplete_bladder_emptying, self.abdominal_fullness)
        MainWindow.setTabOrder(self.abdominal_fullness, self.bladder_spasm)
        MainWindow.setTabOrder(self.bladder_spasm, self.next4)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.vomiting.setText(_translate("MainWindow", "vomiting"))
        self.dark_urine.setText(_translate("MainWindow", "dark urine"))
        self.nausea.setText(_translate("MainWindow", "nausea"))
        self.passing_excessive_amounts_of_gas.setText(_translate("MainWindow", "passing excessive amounts of gas"))
        self.foul_smelling_urine.setText(_translate("MainWindow", "foul smelling urine"))
        self.persistent_urge_to_urinate.setText(_translate("MainWindow", "persistent urge to urinate"))
        self.blood_in_urine.setText(_translate("MainWindow", "blood in urine"))
        self.frequent_urge_to_urinate.setText(_translate("MainWindow", "frequent urge to urinate"))
        self.cloudy_urine.setText(_translate("MainWindow", "cloudy urine"))
        self.excessive_urination_at_night.setText(_translate("MainWindow", "excessive urination at night"))
        self.frequent_urination.setText(_translate("MainWindow", "frequent urination"))
        self.excess_sweating.setText(_translate("MainWindow", "excess sweating"))
        self.night_sweats.setText(_translate("MainWindow", "night sweats"))
        self.constipation.setText(_translate("MainWindow", "constipation"))
        self.water_retention.setText(_translate("MainWindow", "water retention"))
        self.change_in_bowel_habits.setText(_translate("MainWindow", "change in bowel habits"))
        self.leaking_of_stool.setText(_translate("MainWindow", "leaking of stool"))
        self.indigestion.setText(_translate("MainWindow", "indigestion"))
        self.fluid_in_the_abdomen.setText(_translate("MainWindow", "fluid in the abdomen"))
        self.diarrhoea.setText(_translate("MainWindow", "diarrhoea"))
        self.persistent_diarrhoea.setText(_translate("MainWindow", "persistent diarrhoea"))
        self.watery_diarrhoea.setText(_translate("MainWindow", "watery diarrhoea"))
        self.lump_in_the_abdomen.setText(_translate("MainWindow", "lump in the abdomen"))
        self.abdominal_distension.setText(_translate("MainWindow", "abdominal distension"))
        self.label.setText(_translate("MainWindow", "Select the following syptoms you experience:"))
        self.hot_flashes.setText(_translate("MainWindow", "hot flashes"))
        self.sensitivity_to_cold.setText(_translate("MainWindow", "sensitivity to cold"))
        self.heat_intolerance.setText(_translate("MainWindow", "heat intolerance"))
        self.warm_skin.setText(_translate("MainWindow", "warm skin"))
        self.feeling_cold.setText(_translate("MainWindow", "feeling cold"))
        self.hand_tremor.setText(_translate("MainWindow", "hand tremor"))
        self.tremor.setText(_translate("MainWindow", "tremor"))
        self.chills.setText(_translate("MainWindow", "chills"))
        self.white_tongue.setText(_translate("MainWindow", "white tongue"))
        self.difficulty_swallowing.setText(_translate("MainWindow", "difficulty swallowing"))
        self.dry_cough.setText(_translate("MainWindow", "dry cough"))
        self.sore_throat.setText(_translate("MainWindow", "sore throat"))
        self.mouth_ulcer.setText(_translate("MainWindow", "mouth ulcer"))
        self.oral_thrush.setText(_translate("MainWindow", "oral thrush"))
        self.pneumonia.setText(_translate("MainWindow", "pneumonia"))
        self.enlarged_thyroid.setText(_translate("MainWindow", "enlarged thyroid"))
        self.bloating.setText(_translate("MainWindow", "bloating"))
        self.puffy_eyes.setText(_translate("MainWindow", "puffy eyes"))
        self.abnormal_protrusion_of_eyes.setText(_translate("MainWindow", "abnormal protrusion of eyes"))
        self.hearing_loss.setText(_translate("MainWindow", "hearing loss"))
        self.sense_of_incomplete_bladder_emptying.setText(_translate("MainWindow", "sense of incomplete bladder emptying"))
        self.abdominal_fullness.setText(_translate("MainWindow", "abdominal fullness"))
        self.bladder_spasm.setText(_translate("MainWindow", "bladder spasm"))
        self.next4.setText(_translate("MainWindow", "Next"))

f = open("listss.txt", "a")
for i in range(0, len(list4)-1):
    f.write(list4[i])
    f.write("\n\n\n\n                         ")
f.close()
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
