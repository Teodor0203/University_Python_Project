from tkinter import *
# 'Rama' jocului
root = Tk()
#buton cu text
def Click():    
    myLabel1=Label(root,text="Spanzuratoarea")
    myLabel1.grid(row=0,column=0)
   
#Am creat un buton
buton=Button(root,text="Da-i click",padx=50,command=Click)
#Aisarea pe ecran 
buton.grid(row=1,column=0)

root.mainloop()