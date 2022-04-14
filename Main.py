import json
import keyboard
from src.Automate import Auto

print('目前版本 Current version: CLI Dev Ver')

class Data:
    try:
        msg = open('msg.json', mode='r', encoding='utf-8')
        msg = json.load(msg)
    except:
        filename = 'msg.json'
        data = {
            "KEY1": "f3",
            "KEY1_MSG": "We can push",
            "KEY2": "f4",
            "KEY2_MSG": "Come back", 
            "KEY3": "f5",
            "KEY3_MSG": "1 Cracked",
            "KEY4": "f6",
            "KEY4_MSG": "1 Shot",
            "KEY5": "f7",
            "KEY5_MSG": "1 Down",
            "KEY6": "f8",
            "KEY6_MSG": "What message do u want send?",
            "KEY7": "f9",
            "KEY7_MSG": "What message do u want send?",
            "KEY8": "f10",
            "KEY8_MSG": "What message do u want send?",
            "KEY9": "f11",
            "KEY9_MSG": "What message do u want send?",
            "KEY10": "f12",
            "KEY10_MSG": "What message do u want send?"
        }
        file = open(filename, 'w')
        json.dump(data, file, indent=4)
        file.close()

try:
    for number in range(10):
        number += 1
        keyboard.add_hotkey(Data.msg[f'KEY{number}'], Auto.auto_typing, args=[str(Data.msg[f'KEY{number}_MSG'])])

    keyboard.wait()
except AttributeError:
    print('安裝完成，請重新開啟此程式 Setup is complete, please reopen this program!')