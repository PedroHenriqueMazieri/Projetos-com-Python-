import pyautogui
from time import sleep
with open ('Tax.txt','r') as arquivo:
    linhas = arquivo.readlines()
    for i, linha in enumerate(linhas):
        partes = linha.strip().split('#')
        if len(partes) >= 5:
            imposto = partes[0]
            lançamento = partes[1]
            situacao = partes[2]
            calculo = partes[3]
            aliquota = partes[4]
            # 1 Passo: digitar a aba de imposto
            pyautogui.write(imposto)
            pyautogui.press('enter',interval=1)
            # 2 Passo: digitar a aba de Lançamento
            pyautogui.write(lançamento)
            pyautogui.press('enter',interval=1)
            pyautogui.press('enter',interval=1)
            # 3 Passo: digitar a aba de situação tributária
            pyautogui.write(situacao)
            pyautogui.press('enter',interval=1)
            # 4 Passo: digitar a aba de cálculo
            pyautogui.write(calculo)
            pyautogui.press('enter',interval=1)
            # 5 Passo: digitar a aba de aliquota
            pyautogui.write(aliquota)
            pyautogui.press('enter',interval=1)
            # 6 Passo: Pular o vlr de imposto
            pyautogui.press('enter',interval=1)

