import openpyxl as xl

studbook = xl.load_workbook("student info.xlsx")
stsheet = studbook["Sheet1"]
fname = stsheet["a2"]
lname = stsheet["b2"]
studclas =  stsheet["c2"]
studroll = stsheet["d2"]
submb = stsheet["e2"]
subippe = stsheet["f2"]


if fname.value == None or lname.value == None or studclas.value == None or studroll.value == None or submb.value == None or subippe.value == None:
    infname = input("Enter Ur First Name : " ).upper()
    inlname = input("Enter Ur Last Name : " ).upper()
    instudclass = input("Enter Ur section : ").upper()
    inroll = int(input("Enter Ur Roll.NO. : " ))
    insubmb = input("Maths Or Bio : " ).upper()
    insubippe = input("IP OR PE : " ).upper()
    
    fname.value = infname
    lname.value = inlname
    studclas.value = instudclass
    studroll.value = inroll
    submb.value = insubmb
    subippe.value = insubippe

calname = f"12{studclas.value}{studroll.value} {fname.value} {lname.value}"

studbook.save("student info.xlsx")
