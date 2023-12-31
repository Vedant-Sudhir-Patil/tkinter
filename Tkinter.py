import abc
from tkinter import *
from PIL import Image
import datetime as dt
import tkinter.messagebox as tmsg

def basic():
    root = Tk()
    # Title
    root.title("TKINTER Practise")
    # WidthxHeight
    root.geometry("777x534")
    # Width, Height
    root.minsize(430,200)
    root.maxsize(1200,988)

    def label():
        # Label

        # text - adds the text
        # bg - Background
        # fg - Foreground
        # font - sets the font
        # 1. font=("comicsansms",19,"bold")
        # 2. font="comicsansms 19 bold"

        # padx - x padding
        # pady - y padding
        # relief - border styling - SUNKEN, RAISED, GROOVE, RIDGE

        txt= Label(text='This is a sample for my Blood Bank  Management System', bg = "red", fg = "white", padx = 13, pady = 9, font="comicsansms 19 bold", relief = SUNKEN, borderwidth = 6)

        # Pack

        # anchor = nw, ne, sw, se
        # side = top, bottom, left, right
        # fill = X, Y
        # padx - x padding
        # pady - y padding

        txt.pack(side = TOP, anchor= "nw", fill = X )

    def button():
        # Buttons
        def Kiss():
            tmsg.showinfo("Nani ?!"," "*24+"ゴ\n"+" "*26+"ゴ\n"+"Kono Dio da "+" "*6+"ゴ\n"+" "*30+"ゴ\n"+" "*32+"ゴ\n")
        b1=Button(fg="red",borderwidth = 3,bg="pink" ,text="Click here for Jonathan", command = Kiss)
        b1.grid(row=3,column=1)

    def grid():
        # Grid - Cannot be used with Pack
        user = Label(root,text="Username :")
        password = Label(root,text="Password :")
        user.grid(row=0,column=0)
        password.grid(row=1,column=0)

    def variable():
        # Variable - BooleanVar, DoubleVar, IntVar, StringVar
        uservalue = StringVar()
        passvalue = StringVar()

        userentry = Entry(root, textvariable = uservalue)
        passentry = Entry(root, textvariable = passvalue)

        userentry.grid(row=0, column=1)
        passentry.grid(row=1, column=1)

        # Submit Button
        def getvals1():
            print(f"The Username is {uservalue.get()}")
            print(f"The Password is {passvalue.get()}")

        Button(text="Submit", command=getvals1).grid(row=2, column=1)

    def checkBox():
        # Checkbox
        check=IntVar()
        cButton=Checkbutton(text="Are you a JOJO Reference ?", variable=check)
        cButton.grid(row=4,column=1)

    def canvas():
        # Canvas
        canvas_width=777
        canvas_height=534
        can_widget=Canvas(root,width=canvas_width,height=canvas_height)
        can_widget.pack()

        # Canvas - line (x1,y1,x2,y2)
        can_widget.create_line(0,388,267,388,fill="red")
        
        # Canvas - Rectangle
        can_widget.create_rectangle(300,300,500,500)

        # Canvas - Text
        can_widget.create_text(400,400,text="I am here")

        # Canvas - Oval
        can_widget.create_oval(0,0,200,200)

    def bind():
        # Bind
        sub=Button(text="Click Here")
        sub.grid(row=2,column=0)
        def func(event):
            print(f"You clicked the button at {event.x},{event.y}")

        sub.bind('<Button-1>',func)
        sub.bind('<Double-1>',quit)

    def menu():
        # Menus and Submenus
        def func():
            print("One Piece, Does Exist!")
        # Message Box
        def help():
            # Message Box - Info box
            tmsg.showinfo("Help","Orewa Omayma Mamoru")
        def rate():
            # Message Box - Yes/No
            val=tmsg.askquestion("Answer the Following","Was your experience with this GUI Good ?")
            if val:
                msg="Great, Rate us on AppStore PLease."
            else:
                msg="Tell us what went wrong."
            tmsg.showinfo("Experience",msg)
        # Menus and Submenus -Dropdown menu
        mainmenu= Menu(root)
        m1=Menu(mainmenu,tearoff=0)
        m1.add_command(label="New File",command=func)
        m1.add_command(label="Open File",command=func)
        m1.add_separator()
        m1.add_command(label="Save",command=func)
        m1.add_command(label="Save As",command=func)
        mainmenu.add_cascade(label="File",menu=m1)
        m2=Menu(mainmenu,tearoff=0)
        m2.add_command(label="Undo",command=func)
        m2.add_command(label="Redo",command=func)
        m2.add_separator()
        m2.add_command(label="Cut",command=func)
        m2.add_command(label="Copy",command=func)
        m2.add_command(label="Paste",command=func)
        m2.add_separator()
        m2.add_command(label="Find",command=func)
        m2.add_command(label="Replace",command=func)
        mainmenu.add_cascade(label="Edit",menu=m2)
        mainmenu.add_command(label="Selection",command=func)
        mainmenu.add_command(label="View",command=func)
        mainmenu.add_command(label="Go",command=func)
        mainmenu.add_command(label="Run",command=func)
        mainmenu.add_command(label="Terminal",command=func)
        m3=Menu(mainmenu,tearoff=0)
        m3.add_command(label="Help",command=help)
        m3.add_command(label="Rate Us", command=rate)
        mainmenu.add_cascade(label="More", menu=m3)
        mainmenu.add_command(label="Exit",command=quit)
        root.config(menu=mainmenu)

    def slider():
        # Sliders
        def getdollar():
            tmsg.showinfo("Amount Credited",f"{slider.get()} Dollars have been Credited to your Account")
        Label(root,text=f"How Many Dollars :").grid(row=7, column=0)
        slider=Scale(root, from_=0, to=100, orient=HORIZONTAL,tickinterval=50)
        slider.set(69)
        slider.grid(row=7, column=1)
        fr=Frame(root,padx=22, pady=22)
        Button(root, text="Get Dollars!",bg="green",fg="white",padx=5, pady=5 , relief=SUNKEN, command=getdollar).grid(row=7,column=2)

    def radioButton():
        # Radio Button
        var=IntVar()
        var.set(1)
        Label(root,text="What would you like to have sir ?", font="lucidia 11 bold", justify=LEFT, padx=10).grid(row=5,column=1)
        radio=Radiobutton(root, text="Vada Pav",padx=14,variable=var, value=1).grid(row=6,column=0)
        radio=Radiobutton(root, text="Parantha",padx=14,variable=var, value=2).grid(row=6,column=1)
        radio=Radiobutton(root, text="Dosa",padx=14,variable=var, value=3).grid(row=6,column=2)
        radio=Radiobutton(root, text="Samosa",padx=14,variable=var, value=4).grid(row=6,column=3)

    def listBox():
        # List Box
        def add():
            global i
            lbx.insert(ACTIVE, f"{i}")
            i+=1
        i=0
        lbx=Listbox(root)
        lbx.pack()
        lbx.insert(END, "First item of our Listbox")

        Button(root, text="Add Item", command=add).pack()

    def scrollBar():
        # Scroll Bar
        # 1. widget(yscrollcommand=scrollbar.set)
        # 2. scrollbar.config(command=widget.yview)
        scrollbar=Scrollbar(root)
        scrollbar.pack(fill=Y,side=RIGHT,anchor=E)
        listbox= Listbox(root, yscrollcommand=scrollbar.set)
        for i in range(400):
            listbox.insert(END, f"Item No. {i}")
        listbox.pack()
        scrollbar.config(command=listbox.yview)

    def statusBar():
        # Status Bar
        def upload():
            statusvar.set("Busy...")
            sbar.update()
            import time
            time.sleep(2)
            statusvar.set("Ready Now")
        statusvar=StringVar()
        statusvar.set("Ready")
        sbar=Label(root,textvariable=statusvar,relief=SUNKEN,bg="purple",fg="white",anchor=W)
        sbar.pack(side=BOTTOM,fill=X)
        Button(root,text="Upload",command=upload,bg="blue",fg="white").pack(side=BOTTOM, anchor=E)

    def newWindow():
        # Opening new window in Tkinter
        def openwin():
            newWin=Toplevel(root)
            newWin.title("Shadow Clone")
            newWin.geometry("500x500")
            newWin.resizable(False, False)
            Label(newWin,text="This is a new window").pack()
            Button(newWin,text="Close Window",command=lambda: newWin.destroy()).pack()
        Button(root,text="Open New Window",command=openwin).pack(padx=20,pady=20)
    
    def extra():
        # Icon
        #root.wm_iconbitmap("1.ico")
        
        # Configure - Makes changes in root
        root.configure(bg="grey")
        
        # Width & Height of Laptop
        width=root.winfo_screenwidth()
        height=root.winfo_screenheight()
        print(f"{width}x{height}")
        
        # Destroy 
        Button(root,text="Close",command=root.destroy).pack()
        
        
    root.mainloop()

def oop():
    class GUI(Tk):
        def __init__(self):
            super().__init__()
            self.geometry("744x377")
            
        def status(self):
            self.var=StringVar()
            self.var.set("Ready")
            self.statusbar= Label(self,textvariable=self.var,relief=SUNKEN,anchor=W, bg="purple",fg="white")
            self.statusbar.pack(side=BOTTOM,fill=X)
        
        def click(self):
            tmsg.showinfo("Info ","Button Clicked")
        
        def createButton(self,inptext):
            Button(text=inptext,command=self.click).pack()

    if __name__=="__main__":
        window=GUI()
        window.status()
        window.createButton("Click Here")
        window.mainloop()






