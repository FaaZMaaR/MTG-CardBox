from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *

root=Tk()
root.title("MTG CardBox")
root.iconbitmap(default="C:\\Users\\User\\Desktop\\Programming\\MyProgs\\Python\\MTG Card Box\\MTG.ico")
root.minsize(800,600)

def closeRoot():
    root.destroy()
def showAbout():
    showinfo('О программе','Версия: 1.0\nДата изменения: 17.11.2023\nАвтор: Тимофей FaaZMaaR Волхонский')

mMain=Menu(root)
mProg=Menu(root,tearoff=0)
mProg.add_command(label="О программе",command=showAbout)
mProg.add_separator()
mProg.add_command(label="Выход",command=closeRoot)
mMain.add_cascade(label="Программа",menu=mProg)
mMain.add_command(label="Фильтр")
root.config(menu=mMain)

tabframe=ttk.Frame(root,borderwidth=3,relief=GROOVE)
attrframe=ttk.Frame(root,borderwidth=3,relief=GROOVE)
attrframe.place(relwidth=0.3,relheight=1,relx=0.7)
tabframe.place(relwidth=0.7,relheight=1,x=0)

button_1=ttk.Button(attrframe,text="Button 1")
button_1.pack()

people = [("Tom", 38, "tom@email.com"), ("Bob", 42, "bob@email.com"), ("Sam", 28, "sam@email.com")]
columns = ("name", "age", "email") 
tree = ttk.Treeview(tabframe,columns=columns, show="headings")
tree.pack(fill=BOTH, expand=1)
tree.heading("name", text="Имя")
tree.heading("age", text="Возраст")
tree.heading("email", text="Email")
for person in people:
    tree.insert("", END, values=person)

root.mainloop()