# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '8.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):


 def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(20, 10, 491, 361))
        self.textBrowser_2.setObjectName("textBrowser_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        f = open("listss.txt", "r")
        listx=[]

        while True:
            line=f.readline()
            l=line.replace("\n","")
            l=l.replace("_"," ")
            listx.append(l)
            if not line:
                break
        listx.remove('')
      

        import xlrd
        excel_workbook = xlrd.open_workbook('new.xls')

        listy=[]
        # for i in list:
        #   print(i)
        #   x="'"+i+"'"
        #   df = pd.read_excel(file, usecols=x)
        #   display(df)
        excel_worksheet_2020 = excel_workbook.sheet_by_index(0)
        for i in range(0,193):
            for z in range(0,len(listx)-1):
                if (excel_worksheet_2020.cell_value(0, i))==listx[z]:
                    for y in range(0,36):
                        if excel_worksheet_2020.cell_value(y, i)==1:
                            listy.append(excel_worksheet_2020.cell_value(y, 0))
                            
                            
        uniquelist = []
        newlist=[]
        for i in listy:
            if i not in uniquelist:
                uniquelist.append(i)
        for i in uniquelist:
            newlist.append([i,listy.count(i)])
        from operator import itemgetter


        newlist = sorted(newlist, key=itemgetter(1),reverse=True)
        open('listss.txt', 'w').close()
        y = [' '.join([str(c) for c in lst]) for lst in newlist]
        z='\n'.join([str(item)for item in y])
        print(z)
        self.retranslateUi(MainWindow,z)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        open('listss.txt', 'w').close()
    

    
 def retranslateUi(self, MainWindow,x):
                

                _translate = QtCore.QCoreApplication.translate
                MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
                self.textBrowser_2.setHtml(_translate("MainWindow", x))
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())