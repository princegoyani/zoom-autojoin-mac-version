from datetime import datetime as dt
import time
#stime=int(input("When to Start (time in 24 hour) :")) 
print("Wait till Time is match!!!")

cltime = { 8:30 , 9:20 , 10:10 , 11:00}

loop = 0
while True :
    if dt.now().hour < 12 :

        for i in cltime.keys():
            if dt.now().hour == i :
                if dt.now().minute == cltime[i] and loop > 0:
                    print("Class Stated !! ")
                    print("FILE EXECUTION STARTED !!")
                    exec(open("way_no_signin.py").read())
                    time.sleep(62)

                if dt.now().minute >= cltime[i] and loop == 0:
                    print("Class Stated !! ")
                    print("FILE EXECUTION STARTED !!")
                    exec(open("way_no_signin.py").read())
                    time.sleep(62)
                    loop = loop + 1 
    else:
        print("classes over !!! ")
        break

"""
else:
    if dt.now().hour == stime:
        print("Okay!! Lets GO!!")
        import way_no_signin
    else:
        print("Sorry its too early or late!!")
        print("Press Any Key to EXIT ")
        a = input()
"""
