import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from table import *

class Example(QWidget):
 def __init__(self,Data): 
    super(Example, self).__init__()
    self.data=Data
    self.initUI()
 
 def showTables(self,fileName):
     self.vBoxlayout1.removeWidget(self.tb1)
     self.tb1.deleteLater()
     self.tb1 = None
     self.vBoxlayout2.removeWidget(self.tb2)
     self.tb2.deleteLater()
     self.tb2 = None
     self.vBoxlayout3.removeWidget(self.tb3)
     self.tb3.deleteLater()
     self.tb3 = None
     self.tb1 =table(self.data[1][str(fileName)])
     self.tb2 =table(self.data[2][str(fileName)])
     self.tb3 =table(self.data[3][str(fileName)])
     #vBoxlayout1	= QVBoxLayout()
     self.vBoxlayout1.addWidget(self.tb1)
     #self.tab1.setLayout(vBoxlayout1)
     #vBoxlayout2	= QVBoxLayout()
     self.vBoxlayout2.addWidget(self.tb2)
     #self.tab2.setLayout(self.vBoxlayout2)
     #vBoxlayout2	= QVBoxLayout()
     self.vBoxlayout3.addWidget(self.tb3)
     #self.tab3.setLayout(self.vBoxlayout3)
     
 def item_click(self, item):
    print "Click on " + item.text()
    #os.startfile(item.data().toString())
    self.showTables(item.text())     
  
 def initUI(self):
     
    hbox = QHBoxLayout(self)
    topleft = QFrame()
    topleft.setFrameShape(QFrame.StyledPanel)
    bottom = QFrame()
    bottom.setFrameShape(QFrame.StyledPanel)
    splitter1 = QSplitter(Qt.Horizontal)
    
    self.tabs	= QTabWidget()
    #Create Table views
    self.tb1=table([])
    self.tb2=table([])
    self.tb3=table([])
    #List view
    listWidget = QListWidget()
    for x in self.data[0]:
       item = QListWidgetItem(x)
       listWidget.addItem(item)
    listWidget.itemClicked.connect(self.item_click)
 
    # Create tabs
    self.tab1	= QWidget()	
    self.tab2	= QWidget()
    self.tab3	= QWidget()

    # Resize width and height
    self.tabs.resize(2500,1500)
 
    # Set layout of first tab
    self.vBoxlayout1	= QVBoxLayout()
    self.vBoxlayout1.addWidget(self.tb1)
    self.tab1.setLayout(self.vBoxlayout1)   
    # Set layout of second tab
    self.vBoxlayout2	= QVBoxLayout()
    self.vBoxlayout2.addWidget(self.tb2)
    self.tab2.setLayout(self.vBoxlayout2)
    # Set layout of third tab
    self.vBoxlayout3	= QVBoxLayout()
    self.vBoxlayout3.addWidget(self.tb3)
    self.tab3.setLayout(self.vBoxlayout3)
 
    # Add tabs
    self.tabs.addTab(self.tab1,"Functions".center(50))
    self.tabs.addTab(self.tab2,"Calls".center(50))
    self.tabs.addTab(self.tab3,"Blocks".center(50)) 

   
    # Set title and show
    self.tabs.setWindowTitle('CFG')
    self.tabs.show()
    
    splitter1.addWidget(listWidget)
    splitter1.addWidget(self.tabs)
    splitter1.setSizes([50,200])
    splitter2 = QSplitter(Qt.Vertical)
    splitter2.addWidget(splitter1)
    #splitter2.addWidget(bottom)
    hbox.addWidget(splitter2)
    self.setLayout(hbox)
    QApplication.setStyle(QStyleFactory.create('Cleanlooks'))
    self.setGeometry(300, 300, 300, 200)
    self.setWindowTitle('QSplitter demo')
    self.show()

    
def main(data):
    app = QApplication(sys.argv)
    ex = Example(data)
    sys.exit(app.exec_())
if __name__ == '__main__':
   main()
