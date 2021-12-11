try :

    # import pyautogui 
    import time
    import keyboard
    #from os import system
    from source import zoomid #, teachpass
    from inpt import calname
    import pyperclip as pc


    def way(id,typass,disname):
        pc.copy(typass)
        #  keyboard.press_and_release("Windows + d" ,2 )
        #  time.sleep(1)
        keyboard.press_and_release("command+space")
        time.sleep(2)
        keyboard.write("Zoom")
        time.sleep(5)
        keyboard.press_and_release("Enter")
        print(type(id) , type(typass))
        time.sleep(10)
        #pyautogui.click(wid/1.4288,hgt/1.449)
        #pyautogui.click(wid/2.0196353,hgt/2.073732)
        #time.sleep(8)
        keyboard.press_and_release("Enter")
        time.sleep(1)
        keyboard.write(id)
        #pyautogui.click(wid/2,hgt/2.0210)
        time.sleep(1)
        keyboard.press_and_release("tab")
        keyboard.press_and_release("command + a")
        keyboard.write(disname)
        #pyautogui.click(wid/2,hgt/2.3777)
        keyboard.press_and_release("Enter")
        time.sleep(10)
        keyboard.write(typass)
        keyboard.press_and_release("Enter")
        


    #pyautogui.moveTo(0,0,duration=0.00)
    #print(pyautogui.position())
    #pyautogui.click(693,361)
    #print(pyautogui.position())
    #keyboard.press_and_release(Key.cmd)



    #pyautogui.moveTo(0,0,duration=0.00)
    #print(pyautogui.position())
    #pyautogui.click(693,361)
    #print(pyautogui.position())
    #keyboard.press_and_release(Key.cmd)



    #system("C:\\Users\\ok\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe")
    
    
    way(str(zoomid), "svv123" , calname)





except:
    print("You Don't have Class Right NOW !!")
    print("Did u give Your Information Correctly?")
    i = input("Yes or No ?? --- ").lower()
    if i =="no" or i=="n":
        import clearstudinfo
        print("Now Your Information is Reset")
        print("Execute Program Again!!")
        time.sleep(10)
    else:
        print("IF any problem Try to restart program ")
        print("If any problem with programme")
        print("Contact : PRINCE GOYANI")
        time.sleep(50
