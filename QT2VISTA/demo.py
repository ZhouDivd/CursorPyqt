import sys
#导入PyQt5
import PyQt5
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton
from PyQt5 import QtGui , QtCore, QtWidgets
from pyvistaqt import QtInteractor
import pyvista as pv

class MainWindow(QMainWindow):
    def __init__(self, parent=None, show=True):
        QMainWindow.__init__(self, parent)

        # 创建一个中心部件和一个垂直布局
        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)
       
        # 创建一个PyVista QtInteractor部件并添加到布局中
        self.plotter = QtInteractor(self)
        layout.addWidget(self.plotter.interactor)
        # 设置窗口标题
        self.setWindowTitle("VISTA2QT")
        self.plotter.sizeHint = (800, 600)
        #设置窗口背景为黑色
        self.plotter.background_color = "black"
        self.widget1 =  QWidget()
        self.widget1.setObjectName("widget1")
        self.Bt1 = QtWidgets.QPushButton(self.widget1)
        self.Bt1.setGeometry(QtCore.QRect(20, 100, 91, 41))
        self.Bt1.setObjectName("Bt1")
        #循环添加菜单，菜单栏为列表[File, Edit, View, Tools, Help],
        menu_bar = self.menuBar()
        for menu_name in ["File", "Edit", "View", "Tools", "Help"]:
            menu = menu_bar.addMenu(menu_name)
    
        #添加状态栏
        st=self.statusBar()
        #状态栏名为"statusBar"
        st.setObjectName("statusBar")
        #状态栏显示文本为"statusBar"
        st.showMessage("statusBar")
        #将状态栏添加到窗口中
        self.setStatusBar(st)
  
        # 设置中心部件
        self.setCentralWidget(central_widget)
        #设置pyvista布局为2*3
       
        # 创建一个示例3D圆柱体并添加到场景中
        
        cylinder = pv.Cylinder(radius=1, height=2, center=(0, 0, 0))

        self.plotter.add_mesh( cylinder)

        if show:
            self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())