#!/usr/bin/env python3

"""
GUI for diabetes prediction.
"""
import sys

from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QLineEdit, QVBoxLayout, QHBoxLayout, QApplication, QMessageBox
from PyQt5.QtGui import QDoubleValidator, QFont
from PyQt5.QtCore import Qt, QLine

import diabetes

def test_input(self) -> None:
    """ test for diabetes"""
    my_dict = {"B":float(self.l1.text()), "C":float(self.l2.text()),"D":float(self.l3.text()), "E":float(self.l4.text()), "F": float(self.l5.text())}
    output = diabetes.check_input(my_dict)
    if output==0:
        self.results.setText("Diagnosis suggests that patient does not suffers from diabetes.")
    else:
        self.results.setText("Our diagnosis suggests patient does suffer from diabetes.\nPlease get checked soon.")
    self.results.setFont(QFont("Arial",14, weight=QFont.Bold))           
