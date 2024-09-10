from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLabel, QHBoxLayout, QCheckBox, QPushButton, QSlider, QProgressBar, QAction, QMenu
from PyQt5.QtGui import QIcon

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(20, 20, 20, 20)
        self.gridLayout.setSpacing(20)

        # 语言选择
        self.languageLabel = QtWidgets.QLabel("语言:", self.centralwidget)
        self.gridLayout.addWidget(self.languageLabel, 0, 0)
        self.languageComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.languageComboBox.addItems(["英语", "简体中文", "意大利语"])
        self.gridLayout.addWidget(self.languageComboBox, 0, 1)

        # 语音选择
        self.voiceLabel = QtWidgets.QLabel("语音:", self.centralwidget)
        self.gridLayout.addWidget(self.voiceLabel, 1, 0)
        self.voiceComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.gridLayout.addWidget(self.voiceComboBox, 1, 1)

        # 感情选择
        self.emotionLabel = QtWidgets.QLabel("感情:", self.centralwidget)
        self.gridLayout.addWidget(self.emotionLabel, 2, 0)
        self.emotionComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.emotionComboBox.addItems(["正常", "高兴", "悲伤", "生气"])
        self.gridLayout.addWidget(self.emotionComboBox, 2, 1)

        # 语速调节
        self.speedLabel = QtWidgets.QLabel("语速:", self.centralwidget)
        self.gridLayout.addWidget(self.speedLabel, 3, 0)
        speedLayout = QHBoxLayout()
        self.speedSlider = QSlider(QtCore.Qt.Horizontal, self.centralwidget)
        self.speedSlider.setRange(-100, 100)
        self.speedSlider.setValue(0)
        self.speedValueLabel = QLabel("1.0", self.centralwidget)
        speedLayout.addWidget(self.speedSlider)
        speedLayout.addWidget(self.speedValueLabel)
        self.gridLayout.addLayout(speedLayout, 3, 1)

        # 语调调节
        self.pitchLabel = QtWidgets.QLabel("语调:", self.centralwidget)
        self.gridLayout.addWidget(self.pitchLabel, 4, 0)
        pitchLayout = QHBoxLayout()
        self.pitchSlider = QSlider(QtCore.Qt.Horizontal, self.centralwidget)
        self.pitchSlider.setRange(-100, 100)
        self.pitchSlider.setValue(0)
        self.pitchValueLabel = QLabel("0", self.centralwidget)
        pitchLayout.addWidget(self.pitchSlider)
        pitchLayout.addWidget(self.pitchValueLabel)
        self.gridLayout.addLayout(pitchLayout, 4, 1)

        # 语音质量选择
        self.qualityLabel = QtWidgets.QLabel("语音质量:", self.centralwidget)
        self.gridLayout.addWidget(self.qualityLabel, 5, 0)
        self.qualityComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.qualityComboBox.addItems(["低质量", "中等质量", "高质量"])
        self.gridLayout.addWidget(self.qualityComboBox, 5, 1)

        # 字幕转换选项
        self.subtitleCheckBox = QCheckBox("生成字幕文件", self.centralwidget)
        self.gridLayout.addWidget(self.subtitleCheckBox, 6, 0, 1, 2)

        # 文本输入
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setPlaceholderText("请输入要转换的文本")
        self.gridLayout.addWidget(self.textEdit, 7, 0, 1, 2)

        # 转换按钮
        self.convertButton = QPushButton("转换", self.centralwidget)
        self.gridLayout.addWidget(self.convertButton, 8, 0, 1, 2)

        # 进度条
        self.audio_progress_label = QLabel("语音转换进度:", self.centralwidget)
        self.gridLayout.addWidget(self.audio_progress_label, 9, 0)
        self.audio_progress = QProgressBar(self.centralwidget)
        self.gridLayout.addWidget(self.audio_progress, 9, 1)

        self.subtitle_progress_label = QLabel("字幕转换进度:", self.centralwidget)
        self.gridLayout.addWidget(self.subtitle_progress_label, 10, 0)
        self.subtitle_progress = QProgressBar(self.centralwidget)
        self.gridLayout.addWidget(self.subtitle_progress, 10, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        # 菜单栏
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        MainWindow.setMenuBar(self.menubar)

        self.viewMenu = QMenu("视图", self.menubar)
        self.menubar.addMenu(self.viewMenu)

        self.ttsMenu = QMenu("文字转语音", self.menubar)
        self.menubar.addMenu(self.ttsMenu)

        self.openTTSAction = QAction("打开文字转语音", MainWindow)
        self.ttsMenu.addAction(self.openTTSAction)

        # 状态栏
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "语音转文字"))
        MainWindow.setWindowIcon(QIcon('./QT2VISTA/ICON.png'))