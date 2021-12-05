from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *

filename = None


def newFile():
    global filename 
    filename = "Untitled"
    Text.delete(0.0, END)

def saveFile():
    global filename
    t = Text.get(0.0,END)
    f = open(filename, 'w')
    f.write(t)
    f.close()

    def saveAs():
        f = asksaveasfile(mode='w', defaultextension='.txt')
        t = text.get(0.0,END)
        try:
            f.write(t.rstrip())
        except:
            showerror(title="Opps!", message="Unable to save file")

    def openFile():
        f = askopenfile(mode='r')
        t = f.read()
        text.delete(0.0,END)
        text.insert(0.0,t)

    root = Tk()
    root.title("My Python Text Editor")
    root.minsize(width=400, height=400)
    root.maxsize(width=400, height=400)

    text = Text(root, Width=400,height=400)
    text.pack()

    menubar = Menu(root)
    filemenu = Menu(menubar)
    filemenu.add_command(label="New", command=newFile)
    filemenu.add_command(label="Open", command=openFile)
    filemenu.add_command(Label="Save", command=saveFile)
    filemenu.add_command(Label="Save As", command=saveAs)
    filemenu.add_separator()
    filemenu.add_command(Label="Quit", command=root.quit)
    menubar.add_cascade(Label="File", menu=filemenu)

    root.config(menu=menubar)
    root.mainloop()