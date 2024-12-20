import pyautogui
from time import sleep  
with open ('chavea.txt','r') as arquivo:
    for linha in arquivo:
        codigo = linha.split(',')[0]
        pyautogui.click(479,367,duration=4)
        pyautogui.write(codigo)
        pyautogui.click(416,659,duration=4)
        pyautogui.click(898,561,duration=4)
        pyautogui.click(1722,140,duration=4)
        pyautogui.click(1507,830,duration=2)
        pyautogui.click(1062,670,duration=4)
        pyautogui.click(753,30,duration=4)
        pyautogui.click(1289,383,duration=4)
        for _ in range(55):
          pyautogui.press('backspace')
        pyautogui.click(660,468,duration=4)



