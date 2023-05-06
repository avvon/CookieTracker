# CookieTracker
since im not very good at explaining, if you need help contact me on discord (Cow#7086)

Steps to get CookieTracker up and running!

Step 1:
Download and run tesseract-OCR (https://github.com/UB-Mannheim/tesseract/wiki)

Step 2:
in the control panel navigate to system and security > system > advanced system settings > environment variables
under system variables select the path variable click edit
from there add the path to the Tesseract-OCR installation folder (likely "C:\Program Files\Tesseract-OCR").

Step 3:
Install python (https://www.python.org/downloads)

Step 4:
Run the following commands in command prompt:
pip install opencv-python
pip install pytesseract
pip install pillow
pip install pyautogui

Step 5:
Change the following things in cookietracker.py:

webhook_url = "yourwebhook"

"content": f"<@discordid>  {text}"

time.sleep(amount of time to wait in seconds)

------------------------------------------------

If you are not using 1920x1080 for a resolution, or are not going to leave your browser in fullscreen (may also just be buggy for you)
you will also have to change "x, y, width, height = 203, 226, 300, 200"
the way you can figure out the x and y coordinates is by using pixelcheck.py which is in the CookieTracker-main folder
when you run the pixelcheck.py file it will constantly show the pixel coordinates of where your cursor is placed on the screen
you want to take the coordinates on the top left of the cookie display, while being above the unit
if this doesn't work just play around with it for a little and eventually it will work

side note: everything should be run through windows cmd unless you have a different way you would like to run them
