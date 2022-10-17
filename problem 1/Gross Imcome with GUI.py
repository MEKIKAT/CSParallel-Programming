from tkinter import *
from tkinter.font import BOLD


constList = ["Residential","Commercial","Industrial"]



def substrcation():
    cc = int(curwat.get())
    pc = int(prewat.get())

    if cc > pc:
        ttw = cc - pc
        decwat.config(text=ttw)
        print(ttw)
        constType(ttw)        
    else:
        decwat.config(text="Error")
        popEerr = Toplevel()
        popEerr.geometry("300x50")
        popEerr.title("ERROR INPUT")
        popEerr.configure(background='light blue')

        popMess = Label(popEerr, text="Current wattage must be higher",padx=20,pady=20, font=("Century Gothic",12,BOLD) , background="light blue")
        popMess.pack()

        curwat.delete(0, END)
        prewat.delete(0, END)
                    
        popEerr.resizable(False, False)
        print("Current wattage must be higher")
        popMess.after(3000, popEerr.destroy)
                


def constType(totalW):
    n = int(catcher.get())
    ccc = constList[n]
    youpicked =  ccc + " type "
    textOnframe.config(text=youpicked)
    print(youpicked)

    if totalW >= 100:
        if ccc == constList[0]:
            print("rate=18.75, tax=0.05, addCost=0")
            valuess = dict(rate=18.75, tax=0.05, addCost=0)
            vresOnFrame.config(text=f'Rate: {valuess["rate"]} Tax: {valuess["tax"]}  Additional Cost:{valuess["addCost"]}')
            
        elif ccc == constList[1]:
            print("rate=20.25, tax=0.1, addCost=200")
            valuess = dict(rate=20.25, tax=0.1, addCost=200)
            vresOnFrame.config(text=f'Rate: {valuess["rate"]} Tax: {valuess["tax"]}  Additional Cost:{valuess["addCost"]}')
            
        elif ccc == constList[2]:
            print("rate=22.75, tax=0.1, addCost=500")
            valuess = dict(rate=22.75, tax=0.1, addCost=500)
            vresOnFrame.config(text=f'Rate: {valuess["rate"]} Tax: {valuess["tax"]}  Additional Cost:{valuess["addCost"]}')
            
        else:
            return None
            print("")   

    elif totalW < 100:
        if ccc == constList[0]:
            print("rate=17.5, tax=0, addCost=0")
            valuess = dict(rate=17.5, tax=0, addCost=0)
            vresOnFrame.config(text=f'Rate: {valuess["rate"]} Tax: {valuess["tax"]}  Additional Cost:{valuess["addCost"]}')
            
        elif ccc == constList[1]:
            print("rate=19.75, tax=0.02, addCost=100")
            valuess = dict(rate=19.75, tax=0.02, addCost=100)
            vresOnFrame.config(text=f'Rate: {valuess["rate"]} Tax: {valuess["tax"]}  Additional Cost:{valuess["addCost"]}')
        elif ccc == constList[2]:
            print("rate=22.55, tax=0.05, addCost=300")
            valuess = dict(rate=22.55, tax=0.05, addCost=300)
            vresOnFrame.config(text=f'Rate: {valuess["rate"]} Tax: {valuess["tax"]}  Additional Cost:{valuess["addCost"]}')
            
        else:
            return None
            print("")
            
    else:
        print("Error")
    
    gmb = totalW * valuess["rate"]
    fmb = gmb + valuess["addCost"] + (gmb * valuess["tax"])
    resOnFrame.config(
        text=
        f'Gross Monthly :{gmb} kw/hr\n'+
        f'Final Monthly : {fmb} kw/hr'
    )
    print(fmb)

root = Tk()
root.geometry("400x250")
mainframe = LabelFrame(root,text="Result ",padx=80,pady=10,)
mainframe.grid(row=0,column=0,pady=10,padx=10, columnspan=5)

textOnframe = Label(mainframe, text= "Please Select Consumer type", font=("Century Gothic", 10))
textOnframe.grid(row=1, column=0,pady=10,padx=10)

vresOnFrame = Label(mainframe,text="Consumer Type Value will show here")
vresOnFrame.grid(row=3, column=0)

resOnFrame = Label(mainframe,
    text="Gross Monthly kw/hr\n"+
        "Final Monthly kw/hr"
)
resOnFrame.grid(row=2, column=0)


curwatLb = Label(root, text= "Current Wattage ")
curwatLb.grid(row=1, column=0)
curwat = Entry(root)
curwat.grid(row=2, column=0,padx=4,pady=2)  

prewatLb = Label(root, text= "Previews Wattage ")
prewatLb.grid(row=1, column=1)
prewat = Entry(root)
prewat.grid(row=2, column=1,padx=4,pady=2)

decwatLb = Label(root, text= "Total Wattage")
decwatLb.grid(row=1, column=2)

decwat = Label(root,text="------")
decwat.grid(row=2, column=2,padx=4,pady=2)

catcher = IntVar()
Residential = Radiobutton(root, text = "Residential" , variable=catcher, value=0, command=constType)
Residential.grid(row=3,column=0 ,padx= 10)
Commercial = Radiobutton(root,text = "Commercial", variable=catcher, value=1,command=constType)
Commercial.grid(row=3,column=1 ,padx= 10)
Industrial = Radiobutton(root,text = "Industrial", variable=catcher, value=2,command=constType)
Industrial.grid(row=3,column=2 ,padx= 10)

OKbtn = Button(root,text = "OK", command=substrcation)
OKbtn.grid(row=4,column=1 ,padx= 10)

root.resizable(False,False)
root.mainloop()