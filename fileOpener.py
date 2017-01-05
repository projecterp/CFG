#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
import sys
from PyQt4.QtGui import *

def open(): 
  # Create an PyQT4 application object.
  a = QApplication(sys.argv)  
  # The QWidget widget is the base class of all user interface objects in PyQt4.
  w = QWidget()
  # Set window size.  
  w.resize(320, 240)  
  # Set window title 
  w.setWindowTitle("CFG")
 
  # Get filename using QFileDialog
  foldername = str(QFileDialog.getExistingDirectory(w, "Select Directory"))
  #filename = QFileDialog.getOpenFileName(w, 'Open File', 'C:\\')
  print foldername
  # Show window
  w.show()
  return foldername
  #sys.exit()
