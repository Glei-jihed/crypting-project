from tkinter import *
from tkinter import messagebox
import base64 
import os

def decrypt():
    password=code.get()
    
    if password == "adminadmin":
        screen2=Toplevel(screen)
        screen2.title("decryption")
        screen2.geometry("400x300")
        screen2.configure(bg="#00bd56")
        
        message = text1.get(1.0,END)
        decode_message = message.encode("ascii")
        base64_bytes = base64.b64decode(decode_message)
        
        decrypt = base64_bytes.decode("ascii")
        
        Label(screen2,text="ENCRYPT",font="arial",fg="white",bg="#00bd56").place(x=10,y=0)
        text2=Text(screen2,font="rebote 10",bg="white",relief=GROOVE,wrap=WORD,bd=0)
        text2.place(x=10,y=40,width=380,height=150)
        text2.insert(END,decrypt)
    elif password=="":
       messagebox.showerror("encryption","Enter  the  Password")
    elif password!="adminadmin":
        messagebox.showerror("encryption","Invalid Password")
    
def encrypt():
    password=code.get()
    
    if password == "adminadmin":
        screen1=Toplevel(screen)
        screen1.title("encryption")
        screen1.geometry("400x300")
        screen1.configure(bg="#ed3833")
        
        message = text1.get(1.0,END)
        encode_message= message.encode("ascii")
        base64_bytes = base64.b64encode(encode_message)
        
        encrypt = base64_bytes.decode("ascii")
        
        Label(screen1,text="ENCRYPT",font="arial",fg="white",bg="#ed3833").place(x=10,y=0)
        text2=Text(screen1,font="rebote 10",bg="white",relief=GROOVE,wrap=WORD,bd=0)
        text2.place(x=10,y=40,width=380,height=150)
        text2.insert(END,encrypt)
    elif password=="":
       messagebox.showerror("encryption","Enter  the  Password")
    elif password!="adminadmin":
        messagebox.showerror("encryption","Invalid Password")
        
         
def main_screen():
    global screen
    global code
    global text1
    
    screen=Tk()
    screen.geometry("375x500")
    #icon
    
    def reset():
        code.set("")
        text1.delete(1.0,END)
    
    
    screen.title("DAT@Cryptor.")
    Label(text="_ENTER YOUR DATA FOR ENCRYPTION OR DECRYPTION :",fg="black",font=("calbri",9)).place(x=10,y=30)
    text1=Text(font=("Arial",12),fg="white",bg="black",wrap=WORD)
    text1.place(x=10,y=50,width=355,height=150)
    Label(text="_ENTER YOUR SECRET CODE :",fg="black",font=("calbri",9)).place(x=10,y=200)
    code = StringVar()
    Entry(textvariable=code,width=19,bd=0,bg="black",fg="white",font=("Arial",25),show="*").place(x=10,y=230)
    Button(text="ENCRYPT",height=2,width=23,bg="#ed3833",fg="white",bd=0,command=encrypt).place(x=10,y=295)
    Button(text="DECRYPT",height=2,width=23,bg="#00bd56",bd=0,fg="white",command=decrypt).place(x=199,y=295)
    Button(text="RESET",height=2,width=46,bg="#1089ff",bd=0,fg="white",command=reset).place(x=25,y=350)
    Label(text="© Copyright 2023 -- Created by GLEI Jihed",fg="black",font=("calbri",9)).place(x=67,y=475)
    
    
    screen.mainloop()
      
main_screen()
     