from tkinter import *

def ifs():
    print("string found") 
    plsdefine.config(text="string Found")
#    w.config(text= "string found")


root = Tk()

plsdefine = Label(root, text="not Found")
plsdefine.grid(row=0,column=0)
cc = "Awd"
is_numeric = True

try:
    int(cc)
except ValueError:
    is_numeric = False

if is_numeric == True:
    print("Numeric")

else:
    ifs()
 


root.mainloop()

