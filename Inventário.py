import pyautogui
from time import sleep  
with open ('Imob1.txt','r') as arquivo:
    for linha in arquivo:
        codigo = linha.split(',')[0]
        serie = linha.split(',')[1]
        empresa = linha.split(',')[2]
        inv = linha.split(',')[3]
        pyautogui.click(287,300,duration=2)
        pyautogui.write(codigo)
        pyautogui.click(780,344,duration=1)
        pyautogui.click(285,327,duration=1)
        pyautogui.write(serie)
        pyautogui.click(667,641,duration=1)
        pyautogui.click(289,353,duration=1)
        pyautogui.click(288,364,duration=1)
        pyautogui.write(empresa)
        pyautogui.click(37,86,duration=1)
        pyautogui.click(643,570,duration=2)
        for _ in range(24):
            pyautogui.press('backspace')
        pyautogui.click(317,569,duration=1)
        pyautogui.write(inv)
        pyautogui.click(369,87,duration=1)
        sleep(2)
        



