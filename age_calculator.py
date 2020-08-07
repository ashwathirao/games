from tkinter import *
from datetime import date

root = Tk()
root.geometry("400x500")
root.title("MY AGE")


calculator=Text(root, bd=0,bg='light pink', height="50", width="50", font="Arial",)
scrollbar = Scrollbar(root, command=calculator.yview, cursor="heart")
calculator['yscrollcommand'] = scrollbar.set

#photo=PhotoImage(file="")
#myimage=Label(image=photo)
#myimage.grid(row=0,column=1)

def calculateAge():
    today=date.today()
    birthDate=date(int(yearEntry.get()),int(monthEntry.get()),int(dayEntry.get()))
    age=today.year-birthDate.year-((today.month,today.day)<(birthDate.month,birthDate.day))
    Label(text=f"{nameValue.get()} your age is {age}").grid(row=6,column=1)
    calculator.config(background=colourEntry.get())

Label(text="Name").grid(row=1,column=0,padx=90,pady=20)
Label(text="Year").grid(row=2,column=0,pady=20)
Label(text="Month").grid(row=3,column=0,pady=20)
Label(text="Day").grid(row=4,column=0,pady=20)
Label(text="fav colour").grid(row=5,column=0,pady=20)
nameValue=StringVar()
yearValue=StringVar()
monthValue=StringVar()
dayValue=StringVar()
colourValue=StringVar()
nameEntry=Entry(root,textvariable=nameValue)
yearEntry=Entry(root,textvariable=yearValue)
monthEntry=Entry(root,textvariable=monthValue)
dayEntry=Entry(root,textvariable=dayValue)
colourEntry=Entry(root,textvariable=colourValue)
nameEntry.grid(row=1,column=1,pady=10)
yearEntry.grid(row=2,column=1,pady=10)
monthEntry.grid(row=3,column=1,pady=10)
dayEntry.grid(row=4,column=1,pady=10)
colourEntry.grid(row=5,column=1,pady=10)
scrollbar.place(x=376,y=6, height=386)
calculator.place(x=6,y=6, height=370, width=370)
Button(font=("Verdana",8,'bold'),text="Calculate Age", width="12", height=4,bd=0, bg="#32de97", activebackground="#3c9d9b",fg='#ffffff', command=calculateAge).grid(row=6,column=1,pady=10)
root.mainloop()