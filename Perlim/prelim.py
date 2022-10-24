import os 
from tkinter import *

root = Tk()
root.title("Program")
#root.geometry("600x450")
root.configure(bg="grey")

def getname():
    os.system("cls")

    nam = StudentName.get()
    print(f'Student Name : {nam}\n^')
    Grading()

def Grading():
    prelim = int(prE.get()) 
    midterm = int(midE.get()) 
    final = int(finE.get()) 
    project = int(projE.get()) 
    attendance = int(sttE.get()) 
    

    final_grade = (prelim + midterm + final + project + attendance)/5
    print("Total grade :"+str(final_grade))
    result(int(final_grade))
    
def result(Fgr):

    if Fgr >= 98 and Fgr <= 100:
        print("exelent  1.00")
        
    elif Fgr >= 95 and Fgr <= 97:
        print("1.25 very satisfactory")
        
    elif Fgr >= 92 and Fgr <= 94:
        print("1.50 satisfactory")
        
    elif Fgr >= 89 and Fgr <= 91:
        print("1.75 fairly  satisfactory")
        
    elif Fgr >= 86 and Fgr <= 88:
        print("2.00 good")
        
    elif Fgr >= 83 and Fgr <= 85:
        print("2.25 fair")
        
    elif Fgr >= 77 and Fgr <= 79:
        print("2.75 bellow fair")
        
    elif Fgr >= 75 and Fgr <= 76:
        print("3.00 passed")
    else:
        print("INC or Grade is too high")
    
    
    



#UpperFrame
upperFrame = LabelFrame(root,text='Student Info')
upperFrame.grid(row=0,column=0)
#get name
student_askname = Label(upperFrame,text="Student Name : ")
student_askname.grid()
StudentName = Entry(upperFrame)
StudentName.grid()

#Grades
GFrame = LabelFrame(root,text='Grades')
GFrame.grid(row=1,column=0)

prL = Label(GFrame,text="Prelim Grade :")
prL.grid(row=0,column=0)
prE = Entry(GFrame)
prE.grid(row=1,column=0)


midL = Label(GFrame,text="Midterm Grade :")
midL.grid(row=0,column=1)
midE = Entry(GFrame)
midE.grid(row=1,column=1)

finL = Label(GFrame,text="Final Grade :")
finL.grid(row=2,column=0)
finE = Entry(GFrame)
finE.grid(row=3,column=0)

projL = Label(GFrame,text="Project Grade :")
projL.grid(row=2,column=1)
projE = Entry(GFrame)
projE.grid(row=3,column=1)

sttL = Label(GFrame,text="Attendance Grade :") 
sttL.grid(row=4,column=0,columnspan=2)
sttE = Entry(GFrame)
sttE.grid(row=5,column=0,columnspan=2)

SubBtn = Button(root,text="Submit",command=getname)
SubBtn.grid(row=2)




root.mainloop()