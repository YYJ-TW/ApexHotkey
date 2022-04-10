import pyautogui as auto

class Auto:
    def auto_typing(msg):
        auto.press("enter")
        auto.typewrite(msg) 
        auto.press("enter")