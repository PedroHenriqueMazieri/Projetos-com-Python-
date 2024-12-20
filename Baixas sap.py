import pyautogui
from time import sleep  
with open ('Pasta5.txt','r') as arquivo:
    for linha in arquivo:
        codigo = linha.split(',')[0]
        serie = linha.split(',')[1]
        pyautogui.click(200,868,duration=2)
        pyautogui.write(codigo)
        pyautogui.click(250,869,duration=2)
        pyautogui.write(serie)
        pyautogui.click(317,238,duration=2)
        pyautogui.click(1089,1012,duration=2)
        pyautogui.click(101,240,duration=2)
        sleep(2)     





       