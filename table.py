from PyQt4.QtGui import * 
from PyQt4.QtCore import * 
import sys
import os

__author__ = 'pythonspot.com'

file_list=[]

def cellClick(row,col):
    print "Click on " + str(row) + " " + str(col)
    os.startfile(data_list[row][0])    

def table(data):
    global data_list
    data_list=data
    #app 	= QApplication(sys.argv)
    table 	= QTableWidget()
    tableItem 	= QTableWidgetItem()
 
    # initiate table
    table.setWindowTitle("QTableWidget Example @pythonspot.com")
    table.resize(10000,10000)
    table.setRowCount(len(data))
    table.setColumnCount(3)
    # set label
    table.setHorizontalHeaderLabels(QString("\t\tFunc\t\t;line no.;\t\tEnd no.").split(";"))
 
    # set data
    i=0
    for x in data:
        table.setItem(i,0, QTableWidgetItem(x[0].ljust(400)))
        table.setItem(i,1, QTableWidgetItem(x[1]))
        table.setItem(i,2, QTableWidgetItem(x[2])) 
        i+=1 
    # on click function
    #table.cellClicked.connect(cellClick)
 
    # show table
    #table.show()

    ##############################################################3
    #return app.exec_()
    return table
if __name__ == '__main__':
    main()
