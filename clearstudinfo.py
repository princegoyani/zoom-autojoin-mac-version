import openpyxl as xl

def clearall():
    fname.value = None 
    lname.value = None
    studclas.value = None
    studroll.value = None
    submb.value = None
    subippe.value = None
    
    studbook.save("student info.xlsx")


studbook = xl.load_workbook("student info.xlsx")
stsheet = studbook["Sheet1"]
fname = stsheet["a2"]
lname = stsheet["b2"]
studclas =  stsheet["c2"]
studroll = stsheet["d2"]
submb = stsheet["e2"]
subippe = stsheet["f2"]

clearall()

