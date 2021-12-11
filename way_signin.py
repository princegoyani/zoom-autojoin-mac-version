try :
    
    #import pyautogui 
    import time
    import keyboard
    #from os import system
    from source import zoomid #, teachpass
    from inpt import calname
    import pyperclip as pc
   

    def inway(sid,typass,disname):
        pc.copy(typass)
      #  keyboard.press_and_release("Windows + d" ,2 )
      #  time.sleep(1)
        keyboard.press_and_release("command+space")
        time.sleep(2)
        keyboard.write("Zoom")
        time.sleep(2)
        keyboard.press_and_release("Enter")
        print(type(id) , type(typass))
       # time.sleep(10)
        print(sid , typass)
        time.sleep(15)
        keyboard.press_and_release("command+J")
        time.sleep(1)
        #pyautogui.click(wid/4.22287390,hgt/5.69620253)
        #time.sleep(1)
        #pyautogui.click(wid/2.678431,hgt/17.454545)
        #keyboard.press_and_releainse("Enter")
        #pyautogui.click(wid/1.4288,hgt/1.449)
        #pyautogui.click(wid/2.5580,hgt/2.67596819)
        #time.sleep(2)
        #keyboard.press_and_release("Enter")
        keyboard.write(sid)
        time.sleep(1)
        #pyautogui.click(wid/2,hgt/2.0210)
        
        [keyboard.press_and_release("tab") for i in range(2)]
        keyboard.press_and_release("command+a")
        keyboard.write(disname)
        time.sleep(2)
        #pyautogui.click(wid/2,hgt/2.3777)
        keyboard.press_and_release("Enter")
        time.sleep(8)
        keyboard.write(typass)
        keyboard.press_and_release("Enter")
          
    #pyautogui.moveTo(0,0,duration=0.00)
    #print(pyautogui.position())
    #pyautogui.click(693,361)
    #print(pyautogui.position())
    #keyboard.press_and_release(Key.cmd)


   # a = pyautogui.size()
   # wid = a.width
    #hgt = a.height


    #system("C:\\Users\\ok\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe")
    inway(str(zoomid), "svv123" , calname)



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
        time.sleep(10)
