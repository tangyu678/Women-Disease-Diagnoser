# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '7.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
list7=[]
from finaldialogue import Ui_MainWindow


class Ui_y77(object):
    def nextw7(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()
#         if self.opportunistic_infection.isChecked() == True:
#              list6.append('opportunistic_infection')
#                 
        if self.sensation_of_pins_and_needles.isChecked() == True:
             list7.append('sensation_of_pins_and_needles')


        if self.skin_burning_sensation.isChecked() == True:
             list7.append('skin_burning_sensation')


        if self.thickening_of_skin.isChecked() == True:
             list7.append('thickening_of_skin')


        if self.dimpled_skin_like_an_orange_peel.isChecked() == True:
             list7.append('dimpled_skin_like_an_orange_peel')


        if self.thickening_of_skin_on_vulva.isChecked() == True:
             list7.append('thickening_of_skin_on_vulva')


        if self.dark_patches_of_skin_in_folds_and_creases.isChecked() == True:
             list7.append('dark_patches_of_skin_in_folds_and_creases')


        if self.puffy_skin.isChecked() == True:
             list7.append('puffy_skin')


        if self.cyst.isChecked() == True:
             list7.append('cyst')


        if self.pus.isChecked() == True:
             list7.append('pus')


        if self.swelling.isChecked() == True:
             list7.append('swelling')


        if self.lesion.isChecked() == True:
             list7.append('lesion')


        if self.body_odour.isChecked() == True:
             list7.append('body_odour')


        if self.red_blotches.isChecked() == True:
             list7.append('red_blotches')


        if self.itchiness_around_anus.isChecked() == True:
             list7.append('itchiness_around_anus')


        if self.redness.isChecked() == True:
             list7.append('redness')


        if self.oily_skin.isChecked() == True:
             list7.append('oily_skin')


        if self.acne.isChecked() == True:
             list7.append('acne')


        if self.groin_sores.isChecked() == True:
             list7.append('groin_sores')


        if self.warts.isChecked() == True:
             list7.append('warts')


        if self.genital_sores.isChecked() == True:
             list7.append('genital_sores')


        if self.swollen_lymph_nodes.isChecked() == True:
             list7.append('swollen_lymph_nodes')


        if self.skin_ulcer.isChecked() == True:
             list7.append('skin_ulcer')


        if self.puckering.isChecked() == True:
             list7.append('puckering')


        if self.dry_skin.isChecked() == True:
             list7.append('dry_skin')


        if self.itching.isChecked() == True:
             list7.append('itching')


        if self.skin_rashes.isChecked() == True:
             list7.append('skin_rashes')




        if self.pain_breast.isChecked() == True:
             list7.append('pain_breast')


        if self.pain_groin.isChecked() == True:
             list7.append('pain_groin')


        if self.pain_back.isChecked() == True:
             list7.append('pain_back')


        if self.pain_pelvis.isChecked() == True:
             list7.append('pain_pelvis')


        if self.pain_joints.isChecked() == True:
             list7.append('pain_joints')


        if self.pain_bladder.isChecked() == True:
             list7.append('pain_bladder')


        if self.pain_side_part_of_the_body.isChecked() == True:
             list7.append('pain_side_part_of_the_body')


        if self.pain_abdomen.isChecked() == True:
             list7.append('pain_abdomen')


        if self.pain_rectum.isChecked() == True:
             list7.append('pain_rectum')


        if self.pain_vagina.isChecked() == True:
             list7.append('pain_vagina')


        if self.pain_lower_abdomen.isChecked() == True:
             list7.append('pain_lower_abdomen')


        if self.pain_genital_area.isChecked() == True:
             list7.append('pain_genital_area')


        if self.pain_lower_back.isChecked() == True:
             list7.append('pain_lower_back')


        if self.pain_muscles.isChecked() == True:
             list7.append('pain_muscles')


        if self.flaccid_muscles.isChecked() == True:
             list7.append('flaccid_muscles')


        if self.c_sexual_intercourse.isChecked() == True:
             list7.append('c_sexual_intercourse')


        if self.c_swallowing.isChecked() == True:
             list7.append('c_swallowing')


        if self.c_defacating.isChecked() == True:
             list7.append('c_defacating')


 

        if self.muscle_weakness.isChecked() == True:
             list7.append('muscle_weakness')
        file = open('listss.txt','a')
        for l in list7:
          file.write(l+"\n")
        file.close()  

    def setupUi(self, y77):
        y77.setObjectName("y77")
        y77.resize(872, 416)
        self.centralwidget = QtWidgets.QWidget(y77)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(0, 0, 861, 411))
        self.groupBox.setAcceptDrops(False)
        self.groupBox.setAutoFillBackground(True)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 10, 541, 16))
        self.label.setObjectName("label")
        self.sensation_of_pins_and_needles = QtWidgets.QCheckBox(self.groupBox)
        self.sensation_of_pins_and_needles.setGeometry(QtCore.QRect(590, 90, 271, 18))
        self.sensation_of_pins_and_needles.setObjectName("sensation_of_pins_and_needles")
        self.skin_burning_sensation = QtWidgets.QCheckBox(self.groupBox)
        self.skin_burning_sensation.setGeometry(QtCore.QRect(350, 90, 251, 18))
        self.skin_burning_sensation.setObjectName("skin_burning_sensation")
        self.thickening_of_skin = QtWidgets.QCheckBox(self.groupBox)
        self.thickening_of_skin.setGeometry(QtCore.QRect(30, 90, 261, 18))
        self.thickening_of_skin.setObjectName("thickening_of_skin")
        self.dimpled_skin_like_an_orange_peel = QtWidgets.QCheckBox(self.groupBox)
        self.dimpled_skin_like_an_orange_peel.setGeometry(QtCore.QRect(350, 190, 341, 18))
        self.dimpled_skin_like_an_orange_peel.setObjectName("dimpled_skin_like_an_orange_peel")
        self.thickening_of_skin_on_vulva = QtWidgets.QCheckBox(self.groupBox)
        self.thickening_of_skin_on_vulva.setGeometry(QtCore.QRect(590, 150, 291, 18))
        self.thickening_of_skin_on_vulva.setObjectName("thickening_of_skin_on_vulva")
        self.dark_patches_of_skin_in_folds_and_creases = QtWidgets.QCheckBox(self.groupBox)
        self.dark_patches_of_skin_in_folds_and_creases.setGeometry(QtCore.QRect(30, 150, 361, 18))
        self.dark_patches_of_skin_in_folds_and_creases.setObjectName("dark_patches_of_skin_in_folds_and_creases")
        self.puffy_skin = QtWidgets.QCheckBox(self.groupBox)
        self.puffy_skin.setGeometry(QtCore.QRect(30, 110, 321, 18))
        self.puffy_skin.setObjectName("puffy_skin")
        self.cyst = QtWidgets.QCheckBox(self.groupBox)
        self.cyst.setGeometry(QtCore.QRect(590, 170, 211, 18))
        self.cyst.setObjectName("cyst")
        self.pus = QtWidgets.QCheckBox(self.groupBox)
        self.pus.setGeometry(QtCore.QRect(350, 110, 231, 18))
        self.pus.setObjectName("pus")
        self.swelling = QtWidgets.QCheckBox(self.groupBox)
        self.swelling.setGeometry(QtCore.QRect(590, 70, 171, 21))
        self.swelling.setObjectName("swelling")
        self.lesion = QtWidgets.QCheckBox(self.groupBox)
        self.lesion.setGeometry(QtCore.QRect(590, 110, 141, 18))
        self.lesion.setObjectName("lesion")
        self.body_odour = QtWidgets.QCheckBox(self.groupBox)
        self.body_odour.setGeometry(QtCore.QRect(30, 170, 211, 18))
        self.body_odour.setObjectName("body_odour")
        self.red_blotches = QtWidgets.QCheckBox(self.groupBox)
        self.red_blotches.setGeometry(QtCore.QRect(30, 70, 221, 18))
        self.red_blotches.setObjectName("red_blotches")
        self.itchiness_around_anus = QtWidgets.QCheckBox(self.groupBox)
        self.itchiness_around_anus.setGeometry(QtCore.QRect(350, 130, 201, 18))
        self.itchiness_around_anus.setObjectName("itchiness_around_anus")
        self.redness = QtWidgets.QCheckBox(self.groupBox)
        self.redness.setGeometry(QtCore.QRect(590, 50, 211, 18))
        self.redness.setObjectName("redness")
        self.oily_skin = QtWidgets.QCheckBox(self.groupBox)
        self.oily_skin.setGeometry(QtCore.QRect(350, 30, 221, 18))
        self.oily_skin.setObjectName("oily_skin")
        self.acne = QtWidgets.QCheckBox(self.groupBox)
        self.acne.setGeometry(QtCore.QRect(590, 30, 151, 18))
        self.acne.setObjectName("acne")
        self.groin_sores = QtWidgets.QCheckBox(self.groupBox)
        self.groin_sores.setGeometry(QtCore.QRect(30, 130, 231, 18))
        self.groin_sores.setObjectName("groin_sores")
        self.warts = QtWidgets.QCheckBox(self.groupBox)
        self.warts.setGeometry(QtCore.QRect(350, 170, 181, 18))
        self.warts.setObjectName("warts")
        self.genital_sores = QtWidgets.QCheckBox(self.groupBox)
        self.genital_sores.setGeometry(QtCore.QRect(590, 130, 171, 18))
        self.genital_sores.setObjectName("genital_sores")
        self.swollen_lymph_nodes = QtWidgets.QCheckBox(self.groupBox)
        self.swollen_lymph_nodes.setGeometry(QtCore.QRect(350, 150, 231, 18))
        self.swollen_lymph_nodes.setObjectName("swollen_lymph_nodes")
        self.skin_ulcer = QtWidgets.QCheckBox(self.groupBox)
        self.skin_ulcer.setGeometry(QtCore.QRect(30, 190, 171, 18))
        self.skin_ulcer.setObjectName("skin_ulcer")
        self.puckering = QtWidgets.QCheckBox(self.groupBox)
        self.puckering.setGeometry(QtCore.QRect(350, 70, 211, 18))
        self.puckering.setObjectName("puckering")
        self.dry_skin = QtWidgets.QCheckBox(self.groupBox)
        self.dry_skin.setGeometry(QtCore.QRect(30, 30, 201, 18))
        self.dry_skin.setObjectName("dry_skin")
        self.itching = QtWidgets.QCheckBox(self.groupBox)
        self.itching.setGeometry(QtCore.QRect(350, 50, 181, 18))
        self.itching.setObjectName("itching")
        self.skin_rashes = QtWidgets.QCheckBox(self.groupBox)
        self.skin_rashes.setGeometry(QtCore.QRect(30, 50, 211, 18))
        self.skin_rashes.setObjectName("skin_rashes")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(30, 210, 411, 16))
        self.label_2.setObjectName("label_2")
        self.pain_breast = QtWidgets.QCheckBox(self.groupBox)
        self.pain_breast.setGeometry(QtCore.QRect(30, 230, 181, 18))
        self.pain_breast.setObjectName("pain_breast")
        self.pain_groin = QtWidgets.QCheckBox(self.groupBox)
        self.pain_groin.setGeometry(QtCore.QRect(700, 230, 221, 18))
        self.pain_groin.setObjectName("pain_groin")
        self.pain_back = QtWidgets.QCheckBox(self.groupBox)
        self.pain_back.setGeometry(QtCore.QRect(700, 250, 171, 18))
        self.pain_back.setObjectName("pain_back")
        self.pain_pelvis = QtWidgets.QCheckBox(self.groupBox)
        self.pain_pelvis.setGeometry(QtCore.QRect(30, 250, 141, 18))
        self.pain_pelvis.setObjectName("pain_pelvis")
        self.pain_joints = QtWidgets.QCheckBox(self.groupBox)
        self.pain_joints.setGeometry(QtCore.QRect(190, 270, 241, 18))
        self.pain_joints.setObjectName("pain_joints")
        self.pain_bladder = QtWidgets.QCheckBox(self.groupBox)
        self.pain_bladder.setGeometry(QtCore.QRect(190, 250, 231, 18))
        self.pain_bladder.setObjectName("pain_bladder")
        self.pain_side_part_of_the_body = QtWidgets.QCheckBox(self.groupBox)
        self.pain_side_part_of_the_body.setGeometry(QtCore.QRect(360, 270, 221, 18))
        self.pain_side_part_of_the_body.setObjectName("pain_side_part_of_the_body")
        self.pain_abdomen = QtWidgets.QCheckBox(self.groupBox)
        self.pain_abdomen.setGeometry(QtCore.QRect(360, 250, 201, 18))
        self.pain_abdomen.setObjectName("pain_abdomen")
        self.pain_rectum = QtWidgets.QCheckBox(self.groupBox)
        self.pain_rectum.setGeometry(QtCore.QRect(550, 230, 201, 18))
        self.pain_rectum.setObjectName("pain_rectum")
        self.pain_vagina = QtWidgets.QCheckBox(self.groupBox)
        self.pain_vagina.setGeometry(QtCore.QRect(360, 230, 151, 18))
        self.pain_vagina.setObjectName("pain_vagina")
        self.pain_lower_abdomen = QtWidgets.QCheckBox(self.groupBox)
        self.pain_lower_abdomen.setGeometry(QtCore.QRect(550, 250, 221, 18))
        self.pain_lower_abdomen.setObjectName("pain_lower_abdomen")
        self.pain_genital_area = QtWidgets.QCheckBox(self.groupBox)
        self.pain_genital_area.setGeometry(QtCore.QRect(190, 230, 211, 18))
        self.pain_genital_area.setObjectName("pain_genital_area")
        self.pain_lower_back = QtWidgets.QCheckBox(self.groupBox)
        self.pain_lower_back.setGeometry(QtCore.QRect(30, 270, 171, 18))
        self.pain_lower_back.setObjectName("pain_lower_back")
        self.pain_muscles = QtWidgets.QCheckBox(self.groupBox)
        self.pain_muscles.setGeometry(QtCore.QRect(550, 270, 231, 18))
        self.pain_muscles.setObjectName("pain_muscles")
        self.flaccid_muscles = QtWidgets.QCheckBox(self.groupBox)
        self.flaccid_muscles.setGeometry(QtCore.QRect(260, 290, 201, 18))
        self.flaccid_muscles.setObjectName("flaccid_muscles")
        self.c_sexual_intercourse = QtWidgets.QCheckBox(self.groupBox)
        self.c_sexual_intercourse.setGeometry(QtCore.QRect(260, 330, 401, 18))
        self.c_sexual_intercourse.setObjectName("c_sexual_intercourse")
        self.c_swallowing = QtWidgets.QCheckBox(self.groupBox)
        self.c_swallowing.setGeometry(QtCore.QRect(30, 330, 321, 18))
        self.c_swallowing.setObjectName("c_swallowing")
        self.c_defacating = QtWidgets.QCheckBox(self.groupBox)
        self.c_defacating.setGeometry(QtCore.QRect(260, 350, 271, 18))
        self.c_defacating.setObjectName("c_defacating")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(30, 310, 791, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(30, 290, 281, 16))
        self.label_4.setObjectName("label_4")
        self.muscle_weakness = QtWidgets.QCheckBox(self.groupBox)
        self.muscle_weakness.setGeometry(QtCore.QRect(480, 290, 241, 18))
        self.muscle_weakness.setObjectName("muscle_weakness")
        self.next7 = QtWidgets.QPushButton(self.groupBox, clicked = lambda:self.nextw7())
        self.next7.setGeometry(QtCore.QRect(760, 330, 75, 23))
        self.next7.setObjectName("next7")
        self.c_urination = QtWidgets.QCheckBox(self.groupBox)
        self.c_urination.setGeometry(QtCore.QRect(30, 350, 421, 18))
        self.c_urination.setObjectName("c_urination")
        self.label.raise_()
        self.sensation_of_pins_and_needles.raise_()
        self.skin_burning_sensation.raise_()
        self.thickening_of_skin.raise_()
        self.dimpled_skin_like_an_orange_peel.raise_()
        self.thickening_of_skin_on_vulva.raise_()
        self.puffy_skin.raise_()
        self.cyst.raise_()
        self.pus.raise_()
        self.swelling.raise_()
        self.lesion.raise_()
        self.body_odour.raise_()
        self.red_blotches.raise_()
        self.itchiness_around_anus.raise_()
        self.redness.raise_()
        self.oily_skin.raise_()
        self.acne.raise_()
        self.groin_sores.raise_()
        self.warts.raise_()
        self.genital_sores.raise_()
        self.swollen_lymph_nodes.raise_()
        self.skin_ulcer.raise_()
        self.puckering.raise_()
        self.dry_skin.raise_()
        self.itching.raise_()
        self.skin_rashes.raise_()
        self.label_2.raise_()
        self.pain_breast.raise_()
        self.pain_groin.raise_()
        self.pain_back.raise_()
        self.pain_pelvis.raise_()
        self.pain_joints.raise_()
        self.pain_bladder.raise_()
        self.pain_side_part_of_the_body.raise_()
        self.pain_abdomen.raise_()
        self.pain_rectum.raise_()
        self.pain_vagina.raise_()
        self.pain_lower_abdomen.raise_()
        self.pain_genital_area.raise_()
        self.pain_lower_back.raise_()
        self.pain_muscles.raise_()
        self.flaccid_muscles.raise_()
        self.c_sexual_intercourse.raise_()
        self.c_swallowing.raise_()
        self.c_defacating.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.muscle_weakness.raise_()
        self.next7.raise_()
        self.dark_patches_of_skin_in_folds_and_creases.raise_()
        self.c_urination.raise_()
        y77.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(y77)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 872, 22))
        self.menubar.setObjectName("menubar")
        y77.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(y77)
        self.statusbar.setObjectName("statusbar")
        y77.setStatusBar(self.statusbar)

        self.retranslateUi(y77)
        QtCore.QMetaObject.connectSlotsByName(y77)

    def retranslateUi(self, y77):
        _translate = QtCore.QCoreApplication.translate
        y77.setWindowTitle(_translate("y77", "MainWindow"))
        self.label.setText(_translate("y77", "Select the applicable skin conditions:"))
        self.sensation_of_pins_and_needles.setText(_translate("y77", "sensation of pins and needles"))
        self.skin_burning_sensation.setText(_translate("y77", "skin burning sensation"))
        self.thickening_of_skin.setText(_translate("y77", "thickening of skin"))
        self.dimpled_skin_like_an_orange_peel.setText(_translate("y77", "dimpled skin (like an orange peel)"))
        self.thickening_of_skin_on_vulva.setText(_translate("y77", "thickening of skin on vulva"))
        self.dark_patches_of_skin_in_folds_and_creases.setText(_translate("y77", "dark patches of skin in folds and creases"))
        self.puffy_skin.setText(_translate("y77", "puffy skin changes on the shin"))
        self.cyst.setText(_translate("y77", "cyst"))
        self.pus.setText(_translate("y77", "pus"))
        self.swelling.setText(_translate("y77", "swelling"))
        self.lesion.setText(_translate("y77", "lesion"))
        self.body_odour.setText(_translate("y77", "body odour"))
        self.red_blotches.setText(_translate("y77", "red blotches"))
        self.itchiness_around_anus.setText(_translate("y77", "itchiness around anus"))
        self.redness.setText(_translate("y77", "redness"))
        self.oily_skin.setText(_translate("y77", "oily skin"))
        self.acne.setText(_translate("y77", "acne"))
        self.groin_sores.setText(_translate("y77", "groin sores"))
        self.warts.setText(_translate("y77", "warts"))
        self.genital_sores.setText(_translate("y77", "genital sores"))
        self.swollen_lymph_nodes.setText(_translate("y77", "swollen lymph nodes"))
        self.skin_ulcer.setText(_translate("y77", "skin ulcer"))
        self.puckering.setText(_translate("y77", "puckering of the skin"))
        self.dry_skin.setText(_translate("y77", "dry skin"))
        self.itching.setText(_translate("y77", "itching"))
        self.skin_rashes.setText(_translate("y77", "skin rashes"))
        self.label_2.setText(_translate("y77", "Where do you experience pain?"))
        self.pain_breast.setText(_translate("y77", "breast"))
        self.pain_groin.setText(_translate("y77", "groin"))
        self.pain_back.setText(_translate("y77", "back"))
        self.pain_pelvis.setText(_translate("y77", "pelvis"))
        self.pain_joints.setText(_translate("y77", "joints"))
        self.pain_bladder.setText(_translate("y77", "bladder"))
        self.pain_side_part_of_the_body.setText(_translate("y77", "side part of the body"))
        self.pain_abdomen.setText(_translate("y77", "abdomen"))
        self.pain_rectum.setText(_translate("y77", "rectum"))
        self.pain_vagina.setText(_translate("y77", "vagina"))
        self.pain_lower_abdomen.setText(_translate("y77", "lower abdomen"))
        self.pain_genital_area.setText(_translate("y77", "genital area"))
        self.pain_lower_back.setText(_translate("y77", "lower back"))
        self.pain_muscles.setText(_translate("y77", "muscles"))
        self.flaccid_muscles.setText(_translate("y77", "flaccid muscles"))
        self.c_sexual_intercourse.setText(_translate("y77", "during sexual intercourse"))
        self.c_swallowing.setText(_translate("y77", "while swallowing"))
        self.c_defacating.setText(_translate("y77", "while defacating"))
        self.label_3.setText(_translate("y77", "Select the circumstances in which you experience the pain:"))
        self.label_4.setText(_translate("y77", "Tick the relevant options:"))
        self.muscle_weakness.setText(_translate("y77", "muscle weakness"))
        self.next7.setText(_translate("y77", "Next"))
        self.c_urination.setText(_translate("y77", "during urination"))

f = open("listss.txt", "a")
for i in range(0, len(list7)-1):
    f.write(list7[i])
    f.write("      ")
f.close()
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    y77 = QtWidgets.QMainWindow()
    ui = Ui_y77()
    ui.setupUi(y77)
    y77.show()
    sys.exit(app.exec_())