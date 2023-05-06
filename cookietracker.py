import pyautogui
import requests
import time
import cv2
import numpy
import pytesseract
from PIL import Image
from io import BytesIO


webhook_url = "yourwebhook"

# coords of cookies (edit depending on your res)
x, y, width, height = 203, 226, 300, 200

def detect_number():
    # ss
    screenshot = pyautogui.screenshot()

    # crop ss
    cropped_image = screenshot.crop((x, y, x + width, y + height))

    # conv to grayscale
    gray = cv2.cvtColor(numpy.array(cropped_image), cv2.COLOR_BGR2GRAY)

    # pre process ss
    blur = cv2.GaussianBlur(gray, (3,3), 0)
    thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

    # apply ocr
    number = pytesseract.image_to_string(thresh, config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789')

    # apply text recognition
    text = pytesseract.image_to_string(gray)

    return number.strip(), text.strip(), screenshot

# loop
while True:
    # get the number, text, and screenshot in the specified pixels
    number, text, screenshot = detect_number()

    # encode the image as bytes
    img_bytes = BytesIO()
    screenshot.save(img_bytes, format='PNG')
    img_bytes = img_bytes.getvalue()

    # webhook
    data = {
        "content": f"<@discordid>  {text}"
    }
    files = {'image': ('screenshot.png', img_bytes)}
    requests.post(webhook_url, data=data, files=files)

    # wait # seconds before sending to webhook again
    time.sleep(amount of time to wait in seconds)
