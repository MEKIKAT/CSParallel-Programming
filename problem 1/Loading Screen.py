from tkinter import *   

def load():
    Loading.after(3000,Loading.configure(text="Loading"))
    Loading.after(3000,Loading.configure(text="Loading..."))

root = Tk()
loading = True

Loading = Label(root, 
    text="Loading..."
)
Loading.pack()
load()
btn = Button(root, text="kk", command=load).pack()



root.mainloop()