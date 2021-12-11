import keyboard
import time

def upgrademodual(modul,t):
    keyboard.press("command")
    keyboard.press("spacebar")
    keyboard.release("command")
    keyboard.release("spacebar")
    time.sleep(2)
    keyboard.write("terminal")
    keyboard.press_and_release("Enter")
    time.sleep(2)
    keyboard.write(f"pip3 install --upgrade {modul}")
    keyboard.press("Enter")
    verification("upgade",modul,t)
    

def installmodual(modul,t):
    keyboard.press("command")
    keyboard.press("spacebar")
    keyboard.release("command")
    keyboard.release("spacebar")
    time.sleep(2)
    keyboard.write("terminal")
    keyboard.press_and_release("Enter")
    time.sleep(2)
    keyboard.write(f"pip3 install {modul}")
    keyboard.press("Enter")
    time.sleep(5)
    verification("install",modul,t)
        
def verification(frmfun,modul,t):
    print("IF ITS SUCCESSFULL INSTALLED PRESS 'Y' OTHERWISE 'N'")
    verifing = input("ENTER HERE : ")
    if verifing.lower() == 'y':

        print("LETS GET NEW !") 
    elif verifing.lower() == 'n':
        t = t + 1
        print("retrying Trial NO. =" , t)
        if t == 3 :
            print("CHECK NETWORK CONNECTION !!")
            print("if promblem continues contract PRINCE GOYANI or try mannualy !!")
        if frmfun == "install":
            installmodual(modul,t)
        else:
            upgrademodual(modul,t)
    else:
        print("PLEASE ENTER CORRECTLY")
        verification(frmfun,modul,t)


print("GETTING STARTED !!! AFTER ONE MODUL INSTALLED ATTEND HERE !!!")
#keyboard.press("windows")
#keyboard.press("up")
#keyboard.release("windows")
#keyboard.release("up")

installmodual("pip",0)
upgrademodual("pip",0)
installmodual("keyboard",0)
installmodual("pyautogui",0)
installmodual("datetime",0)
installmodual("openpyxl",0)
