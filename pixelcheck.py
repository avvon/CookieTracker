import pyautogui

# Continuously print the position and color of the mouse on the screen
while True:
    x, y = pyautogui.position()
    pixel = pyautogui.screenshot().getpixel((x, y))
    print("Position: ({}, {}) Color: {}".format(x, y, pixel))
