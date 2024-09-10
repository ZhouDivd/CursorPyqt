import asyncio
import os
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QColorDialog
from PyQt5.QtGui import QColor, QPalette, QLinearGradient, QBrush
from PyQt5.QtCore import Qt
import edge_tts
import speech_recognition as sr
from pydub import AudioSegment
from pydub.silence import split_on_silence
from ui_main_window import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.voices = []
        self.subtitle_enabled = False
        self.voice_name_mapping = {
            "zh-CN-XiaoyiNeural": "小艺",
            "zh-CN-YunxiNeural": "云希",
            "zh-CN-YunjianNeural": "云健",
            "zh-CN-XiaoxiaoNeural": "晓晓",
            "en-US-JennyNeural": "Jenny",
            "en-US-GuyNeural": "Guy",
            "it-IT-ElsaNeural": "Elsa",
            "it-IT-IsabellaNeural": "Isabella",
        }
        self.color_options = ["默认", "浅色", "深色", "自定义", "蓝紫渐变", "日落渐变", "森林渐变", "海洋渐变"]
        
        self.setup_connections()
        self.setup_color_menu()
        
        # 初始化语音列表
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.init_voices())

    def setup_connections(self):
        self.languageComboBox.currentIndexChanged.connect(self.updateVoices)
        self.convertButton.clicked.connect(self.on_convert_clicked)
        self.speedSlider.valueChanged.connect(self.updateSpeedLabel)
        self.pitchSlider.valueChanged.connect(self.updatePitchLabel)
        self.subtitleCheckBox.stateChanged.connect(self.updateSubtitleState)

    def setup_color_menu(self):
        for color_option in self.color_options:
            action = self.viewMenu.addAction(color_option)
            action.triggered.connect(lambda checked, opt=color_option: self.changeColor(opt))

    async def init_voices(self):
        self.voices = await edge_tts.list_voices()
        self.updateVoices()

    def updateVoices(self):
        self.voiceComboBox.clear()
        selected_language = self.languageComboBox.currentText()
        if selected_language == "英语":
            filtered_voices = [v for v in self.voices if v['Locale'].startswith("en-")]
        elif selected_language == "简体中文":
            filtered_voices = [v for v in self.voices if v['Locale'].startswith("zh-")]
        elif selected_language == "意大利语":
            filtered_voices = [v for v in self.voices if v['Locale'].startswith("it-")]
        else:
            filtered_voices = []

        for voice in filtered_voices:
            display_name = self.voice_name_mapping.get(voice['ShortName'], voice['ShortName'])
            self.voiceComboBox.addItem(display_name, voice['ShortName'])

    def updateSpeedLabel(self, value):
        speed = 1 + (value / 100)
        self.speedValueLabel.setText(f"{speed:.2f}")

    def updatePitchLabel(self, value):
        self.pitchValueLabel.setText(f"{value}")

    def updateSubtitleState(self, state):
        self.subtitle_enabled = state == Qt.Checked

    def changeColor(self, color_option):
        # ... (保持原来的 changeColor 方法不变)

    #def updateWidgetColors(self, palette):
        # ... (保持原来的 updateWidgetColors 方法不变)

   # async def convertText(self):
        # ... (保持原来的 convertText 方法不变)

   # async def speech_to_subtitle(self, audio_file):
        # ... (保持原来的 speech_to_subtitle 方法不变)

   # def format_time(self, seconds):
        # ... (保持原来的 format_time 方法不变)

   # def on_convert_clicked(self):
       # asyncio.create_task(self.convertText())

if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication
    from qasync import QEventLoop

    app = QApplication(sys.argv)
    loop = QEventLoop(app)
    asyncio.set_event_loop(loop)

    main_window = MainWindow()
    main_window.show()

    with loop:
        loop.run_forever()