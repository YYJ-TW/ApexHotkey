import json
import keyboard
from src.Automate import Auto

class Data:
    with open('msg.json', mode='r', encoding='utf-8') as msg:
        msg = json.load(msg)

for number in range(10):
    number += 1
    keyboard.add_hotkey(Data.msg[f"KEY{number}"], Auto.auto_typing, args=[str(Data.msg[f'KEY{number}_MSG'])])
    
keyboard.wait()