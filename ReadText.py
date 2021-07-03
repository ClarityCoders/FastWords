import cv2
import mss
import numpy as np
import pytesseract

class ReadText:
    def __init__(self):
        self.SCT = mss.mss()
        self.dimensions = {
            'left': 600,
            'top': 690,
            'width': 400,
            'height': 50
        }

    def ReadScreen(self):
        scr = self.SCT.grab(self.dimensions)
        img = np.array(scr)
        color = cv2.cvtColor(img, cv2.IMREAD_COLOR)

        cv2.imshow("The result", color)
        cv2.waitKey(0)
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        text = pytesseract.image_to_string(color).replace('\x0c','')
        if text == '':
            print("Nothing")
        print(text)

if __name__ == "__main__":
    # Testing class
    screen = ReadText()
    screen.ReadScreen()