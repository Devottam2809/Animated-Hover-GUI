from tkinter import*

root=Tk()
root.geometry("300x500")
root.configure(bg="#141414")

def cmd():
   print("YOU CLICKED HERE")

def bttn(x,y,text,bcolor,fcolor):

    def on_enter(e):
        mybutton['background']=bcolor
        mybutton['foreground']=fcolor
    
    def on_leave(e):
        mybutton['background']=fcolor
        mybutton['foreground']=bcolor

    mybutton=Button(root,width=42,height=2,text=text,
    fg=bcolor,
    bg=fcolor,
    border=0,
    activeforeground=fcolor,
    activebackground=bcolor,
    command=cmd)
    mybutton.bind("<Enter>", on_enter)
    mybutton.bind("<Leave>", on_leave)

    mybutton.place(x=x,y=y)
bttn(0,0,"C L I C K","yellow","black")

root.mainloop()

# def cmd():
#   print("YOU CLICKED LENNOVO")
