from PIL import Image
import pytesseract
import cv2
import os
import subprocess
from kivy.app import App
from kivy.uix.widget import Widget
from fpdf import FPDF
from kivy.properties import (
    NumericProperty, ReferenceListProperty, ObjectProperty
)

from kivy.vector import Vector
from kivy.clock import Clock

import sys

if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')


class MyBoxLayout(Widget):
    def submit_pressed(self, instance):
        Name = self.ids.Name.text  # Corrected line
        self.image_path = self.ids.file_chooser.selection and self.ids.file_chooser.selection[0] or ''
        if self.image_path:
            img = cv2.imread(self.image_path)
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            pytesseract.pytesseract.tesseract_cmd = r'C:\Users\rifat\miniconda3\envs\tf\Library\bin\tesseract.exe'
            os.environ['TESSDATA_PREFIX'] = r'c:\Users\rifat\miniconda3\envs\tf\lib\site-packages\pytesseract'
            text = pytesseract.image_to_string(gray, lang='Bengali')

            with open(f'{Name}.txt', 'w', encoding='utf-8') as file:
                file.write(text)


    def shere_text(self, instance):
        Name = self.ids.Name.text
        text_pth = f'{Name}.txt'
        #shere text file in whatsapp,mail,facebook,messenger


class MyApp(App):
    def build(self):
        return MyBoxLayout()


if __name__ == '__main__':
    MyApp().run()
