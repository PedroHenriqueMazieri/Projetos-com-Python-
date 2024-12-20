import pyautogui
from time import sleep
with open ('Pasta5.txt','r') as arquivo:
    for linha in arquivo:
        empresa = linha.split('#')[0]
        mes = linha.split('#')[1]
        ano = linha.split('#')[2]
        tot = linha.split('#')[3]
        dia = linha.split('#')[4]
        debito = linha.split('#')[5]
        credito = linha.split('#')[6]
        custo2 = linha.split('#')[7]
        custo3 = linha.split('#')[8]
        valor = linha.split('#')[9]
        nlan = linha.split('#')[10]
        hist = linha.split('#')[11]
        desc = linha.split('#')[12]
        pyautogui.write(empresa)
        pyautogui.write(mes)
        pyautogui.press('enter')
        pyautogui.write(ano)
        pyautogui.write(tot)
        pyautogui.press('enter')
        break
with open ('Pasta5.txt','r') as arquivo:
    for linha in arquivo:
        empresa = linha.split('#')[0]
        mes = linha.split('#')[1]
        ano = linha.split('#')[2]
        tot = linha.split('#')[3]
        dia = linha.split('#')[4]
        debito = linha.split('#')[5]
        credito = linha.split('#')[6]
        custo2 = linha.split('#')[7]
        custo3 = linha.split('#')[8]
        valor = linha.split('#')[9]
        nlan = linha.split('#')[10]
        hist = linha.split('#')[11]
        desc = linha.split('#')[12]
        pyautogui.write(dia)
        sleep(0.7)
        pyautogui.write(debito)
        sleep(0.3)
        pyautogui.press('enter')
        pyautogui.write(credito)
        sleep(0.3)
        pyautogui.press('enter')
        sleep(0.3)
        pyautogui.write(custo2)
        sleep(0.3)
        pyautogui.write(custo3)
        sleep(0.3)
        pyautogui.press('enter')
        sleep(0.3)
        pyautogui.write(valor)
        sleep(0.3)
        pyautogui.write(nlan)
        sleep(0.3)
        pyautogui.press('enter')
        sleep(0.3)
        pyautogui.write(hist)
        sleep(0.3)
        pyautogui.press('enter')
        sleep(0.3)
        pyautogui.write(desc)
        sleep(0.3)