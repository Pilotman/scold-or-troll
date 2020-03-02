import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from twitterAPI import *

global BLFile
BLFile = 'defaultList.txt'
global username


def window():
   app = QApplication(sys.argv)
   win = QWidget()
            
   flo = QFormLayout()

   userIn = QLineEdit()
   userIn.textChanged.connect(userchanged)
   flo.addRow("Twitter user name without the @ ",userIn)
    
   BLIn = QLineEdit()
   BLIn.setText('defaultList.txt')
   BLIn.textChanged.connect(blackchanged)
   flo.addRow("Blacklist File", BLIn)

   button = QPushButton()
   button.setText('Check')
   flo.addRow("", button)
   button.clicked.connect(result) 

   win.setLayout(flo)
   win.setWindowTitle("Scold or Troll")
   win.show()
    
   sys.exit(app.exec_())

def result():
    #app = QApplication(sys.argv)
    global BLFile
    global username

    letext = '<h1>Checking user ' + username + ' for potential ill intent...</h1>'

    BL = Blacklist(BLFile)
    che = Checker(username)

    num_fol = che.numFol
    num_hits = che.checkNum(BL)

    letext += '<p>They follow ' + str(num_fol) + " people, " + str(num_hits) + ' of them are in the blacklist</p>'
    
    letext += '<p>Those include:</p>'
    
    formlist = listformat(che.listMatch(BL))

    letext += formlist

    d = QDialog()
    textBrowser = QTextBrowser()
    textBrowser.setHtml(letext)

    vbox = QVBoxLayout()
    vbox.addWidget(textBrowser)
    d.setLayout(vbox)
    d.resize(400,300)
    d.exec_()
    return

def userchanged(text):
   global username
   username = text
    
def blackchanged(text):
    global BLFile
    BLFile = text

def listformat(ls):
    ret = '\n'
    for i in ls:
        ret += '<p>- '+ str(i) + '</p>'
    return ret

if __name__ == '__main__':
   window()
   #result(1)
