# CookieTracker
made in like an hour so probably bad <br>
since im not very good at explaining, if you need help contact me on discord (Cow#7086) <br><br>

Steps to get CookieTracker up and running!<br><br>

Step 1:<br>
Download and run tesseract-OCR (https://github.com/UB-Mannheim/tesseract/wiki)<br><br>

Step 2:<br>
in the control panel navigate to system and security > system > advanced system settings > environment variables<br>
under system variables select the path variable click edit<br>
from there add the path to the Tesseract-OCR installation folder (likely "C:\Program Files\Tesseract-OCR").<br><br>

Step 3:<br>
Install python (https://www.python.org/downloads)<br><br>

Step 4:<br>
Run the following commands in command prompt:<br>
pip install opencv-python<br>
pip install pytesseract<br>
pip install pillow<br>
pip install pyautogui<br><br>

Step 5:<br>
Change the following things in cookietracker.py:<br><br>

webhook_url = "yourwebhook"<br><br>

"content": f"<@discordid>  {text}"<br><br>

time.sleep(amount of time to wait in seconds)<br><br>

------------------------------------------------<br><br>

If you are not using 1920x1080 for a resolution, or are not going to leave your browser in fullscreen (may also just be buggy for you)<br>
you will also have to change "x, y, width, height = 203, 226, 300, 200"<br>
the way you can figure out the x and y coordinates is by using pixelcheck.py which is in the CookieTracker-main folder<br>
when you run the pixelcheck.py file it will constantly show the pixel coordinates of where your cursor is placed on the screen<br>
you want to take the coordinates on the top left of the cookie display, while being above the unit<br>
if this doesn't work just play around with it for a little and eventually it will work<br><br>

side note: on windows everything should be run through windows cmd unless you have a different way you would like to run them
