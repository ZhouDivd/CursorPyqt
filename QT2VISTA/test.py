from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget,QPushButton
from PyQt5.QtGui import QPixmap
import sys
import cv2
import numpy as np
from PIL import Image
from Ui_Window import VISTA2QT
import pyvista as pv
class App(QMainWindow,VISTA2QT):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        #从新设置plotter的尺寸
        self.plotter.resize(1700, 600)
        self.Bt1.clicked.connect(self.Createcylinder)
    #按钮点击事件
    def Createcylinder(self):
        cylinder = pv.Cylinder()
        self.plotter.add_mesh(cylinder)
        self.plotter.show()
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec_())