from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
import sqlite3
from PIL import Image,ImageTk

database=sqlite3.connect("MTG.db")
dbcursor=database.cursor()
cols=("Numero","Name","SetName","Number","Rarity","Quantity","Foil")
condition=""

imgpath="Pictures\\"
index=0

root=Tk()
root.title("MTG CardBox")
root.iconbitmap(default="MTG.ico")
root.minsize(1200,800)

def closeRoot():
    root.destroy()
def showAbout():
    showinfo('О программе','Версия: 1.1.2\nДата изменения: 31.01.2024\nАвтор: Тимофей FaaZMaaR Волхонский')

mMain=Menu(root)
mProg=Menu(root,tearoff=0)
mGroup=Menu(root,tearoff=0)
mProg.add_command(label="О программе",command=showAbout)
mProg.add_separator()
mProg.add_command(label="Выход",command=closeRoot)

rargroupvar=StringVar()
setgroupvar=StringVar()
colorgroupvar=StringVar()
typegroupvar=StringVar()

class ValuesClass:
    def __init__(self,db,index):
        self.values=list()
        tmp=set()
        for v in db:
            if(v[index]!=None):
                tmp.add(v[index])
        for v in tmp:
            self.values.append(v)
        self.values.sort()
        self.values.insert(0,"")

def comfunc():
    rargroupvar.set("Common")
    selectData()
def uncomfunc():
    rargroupvar.set("Uncommon")
    selectData()
def rarfunc():
    rargroupvar.set("Rare")
    selectData()
def mythfunc():
    rargroupvar.set("Mythic")
    selectData()
def afrfunc():
    setgroupvar.set("Adventures in the Forgotten Realms")
    selectData()
def aerfunc():
    setgroupvar.set("Aether Revolt")
    selectData()
def c21func():
    setgroupvar.set("Commander 2021")
    selectData()
def m20func():
    setgroupvar.set("Core Set 2020")
    selectData()
def m21func():
    setgroupvar.set("Core Set 2021")
    selectData()
def ikofunc():
    setgroupvar.set("Ikoria: Lair of Behemoths")
    selectData()
def vowfunc():
    setgroupvar.set("Innistrad: Crimson Vow")
    selectData()
def midfunc():
    setgroupvar.set("Innistrad: Midnight Hunt")
    selectData()
def kldfunc():
    setgroupvar.set("Kaladesh")
    selectData()
def khmfunc():
    setgroupvar.set("Kaldheim")
    selectData()
def neofunc():
    setgroupvar.set("Kamigawa: Neon Dynasty")
    selectData()
def micfunc():
    setgroupvar.set("Midnight Hunt Commander")
    selectData()
def mh2func():
    setgroupvar.set("Modern Horizons 2")
    selectData()
def stxfunc():
    setgroupvar.set("Strixhaven: School of Mages")
    selectData()
def stafunc():
    setgroupvar.set("Strixhaven Mystical Archive")
    selectData()
def plistfunc():
    setgroupvar.set("The List")
    selectData()
def thbfunc():
    setgroupvar.set("Theros Beyond Death")
    selectData()
def eldfunc():
    setgroupvar.set("Throne of Eldraine")
    selectData()
def znrfunc():
    setgroupvar.set("Zendikar Rising")
    selectData()
def warfunc():
    setgroupvar.set("War of the Spark")
    selectData()
def whitefunc():
    colorgroupvar.set("White")
    selectData()
def bluefunc():
    colorgroupvar.set("Blue")
    selectData()
def blackfunc():
    colorgroupvar.set("Black")
    selectData()
def redfunc():
    colorgroupvar.set("Red")
    selectData()
def greenfunc():
    colorgroupvar.set("Green")
    selectData()
def multcolfunc():
    colorgroupvar.set("multi")
    selectData()
def noncolfunc():
    colorgroupvar.set("Noncolor")
    selectData()
def nonbaslandfunc():
    colorgroupvar.set("nonbase")
    selectData()
def baslandfunc():
    colorgroupvar.set("base")
    selectData()
def creaturefunc():
    typegroupvar.set("Существо") 
    selectData()   
def landfunc():
    typegroupvar.set("Земля")
    selectData()
def pwfunc():
    typegroupvar.set("Planeswalker")
    selectData()
def artfunc():
    typegroupvar.set("Артефакт")
    selectData()
def sorcfunc():
    typegroupvar.set("Волшебство")
    selectData()
def instfunc():
    typegroupvar.set("Мгновенное заклинание")
    selectData()
def enchfunc():
    typegroupvar.set("Чары")
    selectData()
def cleargroupfunc():
    rargroupvar.set("")
    setgroupvar.set("")
    colorgroupvar.set("")
    typegroupvar.set("")
    selectData()
    
def setGroupMenu():
    global mGroupSet,mGroupRare,mGroupColor,mGroupType,mGroup
    mGroup.delete(0,END)
    mGroupRare=Menu(root,tearoff=0)
    mGroupSet=Menu(root,tearoff=0)
    mGroupColor=Menu(root,tearoff=0)
    mGroupType=Menu(root,tearoff=0)
    
    vals=ValuesClass(alldata,4)
    if("Common" in vals.values):
        mGroupRare.add_command(label="Common",command=comfunc)
    if("Uncommon" in vals.values):
        mGroupRare.add_command(label="Uncommon",command=uncomfunc)
    if("Rare" in vals.values):
        mGroupRare.add_command(label="Rare",command=rarfunc)
    if("Mythic" in vals.values):
        mGroupRare.add_command(label="Mythic",command=mythfunc)
        
    vals=ValuesClass(alldata,2)
    if("Adventures in the Forgotten Realms" in vals.values):
        mGroupSet.add_command(label="Adventures in the Forgotten Realms",command=afrfunc)
    if("Aether Revolt" in vals.values):
        mGroupSet.add_command(label="Aether Revolt",command=aerfunc)
    if("Commander 2021" in vals.values):
        mGroupSet.add_command(label="Commander 2021",command=c21func)
    if("Core Set 2020" in vals.values):
        mGroupSet.add_command(label="Core Set 2020",command=m20func)
    if("Core Set 2021" in vals.values):
        mGroupSet.add_command(label="Core Set 2021",command=m21func)
    if("Ikoria: Lair of Behemoths" in vals.values):
        mGroupSet.add_command(label="Ikoria: Lair of Behemoths",command=ikofunc)
    if("Innistrad: Crimson Vow" in vals.values):
        mGroupSet.add_command(label="Innistrad: Crimson Vow",command=vowfunc)
    if("Innistrad: Midnight Hunt"in vals.values):
        mGroupSet.add_command(label="Innistrad: Midnight Hunt",command=midfunc)
    if("Kaladesh" in vals.values):
        mGroupSet.add_command(label="Kaladesh",command=kldfunc)
    if("Kaldheim" in vals.values):
        mGroupSet.add_command(label="Kaldheim",command=khmfunc)
    if("Kamigawa: Neon Dynasty" in vals.values):
        mGroupSet.add_command(label="Kamigawa: Neon Dynasty",command=neofunc)
    if("Midnight Hunt Commander" in vals.values):
        mGroupSet.add_command(label="Midnight Hunt Commander",command=micfunc)
    if("Modern Horizons 2" in vals.values):
        mGroupSet.add_command(label="Modern Horizons 2",command=mh2func)
    if("Strixhaven: School of Mages" in vals.values):
        mGroupSet.add_command(label="Strixhaven: School of Mages",command=stxfunc)
    if("Strixhaven Mystical Archive" in vals.values):
        mGroupSet.add_command(label="Strixhaven Mystical Archive",command=stafunc)
    if("The List" in vals.values):
        mGroupSet.add_command(label="The List",command=plistfunc)
    if("Theros Beyond Death" in vals.values):
        mGroupSet.add_command(label="Theros Beyond Death",command=thbfunc)
    if("Throne of Eldraine" in vals.values):
        mGroupSet.add_command(label="Throne of Eldraine",command=eldfunc)
    if("Zendikar Rising" in vals.values):
        mGroupSet.add_command(label="Zendikar Rising",command=znrfunc)
    if("War of the Spark" in vals.values):
        mGroupSet.add_command(label="War of the Spark",command=warfunc)
    
    vals=ValuesClass(alldata,14)
    if("White" in vals.values):
        mGroupColor.add_command(label="Белый",command=whitefunc)
    if("Blue" in vals.values):
        mGroupColor.add_command(label="Синий",command=bluefunc)
    if("Black" in vals.values):
        mGroupColor.add_command(label="Черный",command=blackfunc)
    if("Red" in vals.values):
        mGroupColor.add_command(label="Красный",command=redfunc)
    if("Green" in vals.values):
        mGroupColor.add_command(label="Зеленый",command=greenfunc)
    for v in vals.values:
        if("|" in v):
            mGroupColor.add_command(label="Многоцветный",command=multcolfunc)
            break
    if("Noncolor" in vals.values):
        mGroupColor.add_command(label="Бесцветный",command=noncolfunc)   
    for v in alldata:
        if((v[6]!="Базовая" and v[6]!="Базовая Снежная") and (v[7]=="Земля" or v[7]=="Артефакт Земля")):
            mGroupColor.add_command(label="Небазовая земля",command=nonbaslandfunc)
            break
    for v in alldata:
        if((v[6]=="Базовая") or (v[6]=="Базовая Снежная")):
            mGroupColor.add_command(label="Базовая земля",command=baslandfunc)
            break
    
    typevals=list()
    for v in alldata:
        if((v[7]=="Существо") or (v[7]=="Артефакт Существо") or (v[7]=="Чары Существо")):
            mGroupType.add_command(label="Существо",command=creaturefunc)
            break
    for v in alldata:
        if((v[7]=="Артефакт Земля") or (v[7]=="Земля")):
            mGroupType.add_command(label="Земля",command=landfunc)
            break
    vals=ValuesClass(alldata,7)
    if("Planeswalker" in vals.values):
        mGroupType.add_command(label="Planeswalker",command=pwfunc)
    if("Артефакт" in vals.values):
        mGroupType.add_command(label="Артефакт",command=artfunc)
    if("Волшебство" in vals.values):
        mGroupType.add_command(label="Волшебство",command=sorcfunc)
    if("Мгновенное заклинание" in vals.values):
        mGroupType.add_command(label="Мгновенное заклинание",command=instfunc)
    if("Чары" in vals.values):
        mGroupType.add_command(label="Чары",command=enchfunc)
    
    if(rargroupvar.get()==""):
        mGroup.add_cascade(label="Редкость",menu=mGroupRare)
    if(setgroupvar.get()==""):
        mGroup.add_cascade(label="Сет",menu=mGroupSet)
    if(colorgroupvar.get()==""):
        mGroup.add_cascade(label="Цвет",menu=mGroupColor)
    if(typegroupvar.get()==""):
        mGroup.add_cascade(label="Тип",menu=mGroupType)
    mGroup.add_command(label="Сброс",command=cleargroupfunc)

def setTabData():
    global tabdata
    tabdata=list()
    i=1
    for v in alldata:
        tabdata.append((i,)+v[1:6]+v[17:18])
        i+=1

def resetData():
    global alldata,tabdata
    dbcursor.execute(f"SELECT * FROM WorkTable")
    alldata=dbcursor.fetchall()
    setTabData()
    setGroupMenu()

resetData()

def selectData():
    global alldata,tabdata,index,condition
    tmp=""
    index=0
    if(namevar.get()!=""):
        tmp+="Name LIKE \'%"+namevar.get()+"%\'"
    if(artistvar.get()!=""):
        if(tmp!=""):
            tmp+=" AND "
        artlist=artistvar.get().split("|")
        tmp+="Artist IN ("
        for k in artlist:
            tmp+=f"\'{k}\',"
        tmp=tmp.rstrip(",")
        tmp+=")"
    if(rarityvar.get()!=""):
        if(tmp!=""):
            tmp+=" AND "
        rarlist=rarityvar.get().split("|")
        tmp+="Rarity IN ("
        for k in rarlist:
            tmp+=f"\'{k}\',"
        tmp=tmp.rstrip(",")
        tmp+=")"
    if(setvar.get()!=""):
        if(tmp!=""):
            tmp+=" AND "
        setlist=setvar.get().split("|")
        tmp+="SetName IN ("
        for k in setlist:
            tmp+=f"\'{k}\',"
        tmp=tmp.rstrip(",")
        tmp+=")"
    if(designvar.get()!=""):
        if(tmp!=""):
            tmp+=" AND "
        designlist=designvar.get().split("|")
        tmp+="Design IN ("
        for k in designlist:
            tmp+=f"\'{k}\',"
        tmp=tmp.rstrip(",")
        tmp+=")"
    if(supertypevar.get()!=""):
        if(tmp!=""):
            tmp+=" AND "
        stypelist=supertypevar.get().split("|")
        tmp+="SuperType IN ("
        for k in stypelist:
            tmp+=f"\'{k}\',"
        tmp=tmp.rstrip(",")
        tmp+=")"
    if(typevar.get()!=""):
        if(tmp!=""):
            tmp+=" AND "
        typelist=typevar.get().split("|")
        tmp+="Type IN ("
        for k in typelist:
            tmp+=f"\'{k}\',"
        tmp=tmp.rstrip(",")
        tmp+=")"
    if(undertypevar.get()!=""):
        if(tmp!=""):
            tmp+=" AND "
        utypelist=undertypevar.get().split("|")
        tmp+="UnderType IN ("
        for k in utypelist:
            tmp+=f"\'{k}\',"
        tmp=tmp.rstrip(",")
        tmp+=")"
    if(descriptvar.get()!=""):
        if(tmp!=""):
            tmp+=" AND "
        descrlist=descriptvar.get().split("|")
        for k in descrlist:
            tmp+="Description LIKE \'%"+k+"%\' AND "
        tmp=tmp.rstrip(" AND ")
    if(manavar.get()!=""):
        if(tmp!=""):
            tmp+=" AND "
        manalist=manavar.get().split("|")
        for k in manalist:
            tmp+="ManaCost "+k+" AND "
        tmp=tmp.rstrip(" AND ")
    if(strengthvar.get()!=""):
        if(tmp!=""):
            tmp+=" AND "
        strlist=strengthvar.get().split("|")
        for k in strlist:
            tmp+="Strength "+k+" AND "
        tmp=tmp.rstrip(" AND ")
    if(endurancevar.get()!=""):
        if(tmp!=""):
            tmp+=" AND "
        endlist=endurancevar.get().split("|")
        for k in endlist:
            tmp+="Endurance "+k+" AND "
        tmp=tmp.rstrip(" AND ")
    if(loyaltyvar.get()!=""):
        if(tmp!=""):
            tmp+=" AND "
        loylist=loyaltyvar.get().split("|")
        for k in loylist:
            tmp+="Loyalty "+k+" AND "
        tmp=tmp.rstrip(" AND ")
    if(colorvar.get()!=""):
        if(tmp!=""):
            tmp+=" AND "
        tmp+="Color =\'"+colorvar.get()+"\'"
    if(rargroupvar.get()!=""):
        if(tmp!=""):
            tmp+=" AND "
        tmp+="Rarity =\'"+rargroupvar.get()+"\'"
    if(setgroupvar.get()!=""):
        if(tmp!=""):
            tmp+=" AND "
        tmp+="SetName =\'"+setgroupvar.get()+"\'"
    if(colorgroupvar.get()!=""):
        if(tmp!=""):
            tmp+=" AND "
        if(colorgroupvar.get()=="multi"):
            tmp+="Color IN ('Black|Green','Black|Red','Blue|Black','Blue|Black|Green','Blue|Green','Blue|Red','Blue|Red|Green','Red|Green','White|Black','White|Black|Red','White|Blue','White|Blue|Black|Red|Green','White|Blue|Red','White|Blue|Red|Green','White|Green','White|Red','White|Red|Green')"
        elif(colorgroupvar.get()=="nonbase"):
            tmp+="Type IN ('Земля','Артефакт Земля') AND (SuperType IS NULL OR SuperType NOT IN ('Базовая','Базовая Снежная'))"
        elif(colorgroupvar.get()=="base"):
            tmp+="SuperType IN ('Базовая','Базовая Снежная')"
        else:
            tmp+="Color =\'"+colorgroupvar.get()+"\'"
    if(typegroupvar.get()!=""):
        if(tmp!=""):
            tmp+=" AND "
        if(typegroupvar.get()=="Существо"):
            tmp+="Type IN ('Существо','Артефакт Существо','Чары Существо')"
        elif(typegroupvar.get()=="Земля"):
            tmp+="Type IN ('Земля','Артефакт Земля')"
        else:
            tmp+="Type =\'"+typegroupvar.get()+"\'"
    if(tmp!=""):
        dbcursor.execute(f"SELECT * FROM WorkTable WHERE {tmp}")
        alldata=dbcursor.fetchall()
        setTabData()
        for r in tree.get_children():
            tree.delete(r)
        for v in tabdata:
            tree.insert("", END,iid=index, values=v)
            index+=1
    else:
        resetData()
        for r in tree.get_children():
            tree.delete(r)        
        for v in tabdata:
            tree.insert("", END,iid=index, values=v)
            index+=1
    setGroupMenu()
    condition=tmp
    
def onColorButton():
    tmp=""
    if(whitebool.get()):
        tmp+="White|"
    if(bluebool.get()):
        tmp+="Blue|"
    if(blackbool.get()):
        tmp+="Black|"
    if(redbool.get()):
        tmp+="Red|"
    if(greenbool.get()):
        tmp+="Green|"
    colorvar.set(tmp.rstrip("|"))
    if(noncolbool.get()):
        noncollbl.imgswap()
def onNoncolorButton():
    tmp=""
    if(noncolbool.get()):
        tmp+="Noncolor"
    colorvar.set(tmp)
    if(whitebool.get()):
        whitelbl.imgswap()
    if(bluebool.get()):
        bluelbl.imgswap()
    if(blackbool.get()):
        blacklbl.imgswap()
    if(redbool.get()):
        redlbl.imgswap()
    if(greenbool.get()):
        greenlbl.imgswap()

class ImgButton(ttk.Label):
    def __init__(self,mstr,text,var):
        super().__init__(master=mstr)
        self.imgs=text
        self.boolvar=var
        self.image=PhotoImage(file=imgpath+"Icons\\"+self.imgs[0])
        self.config(image=self.image,cursor="hand2")
        self.bind("<Button-1>",self.onimgclick)
    def imgswap(self):
        if(self.boolvar.get()):
            self.boolvar.set(False)
            self.image=PhotoImage(file=imgpath+"Icons\\"+self.imgs[0])
            self.config(image=self.image)
        else:
            self.boolvar.set(True)
            self.image=PhotoImage(file=imgpath+"Icons\\"+self.imgs[1])
            self.config(image=self.image)
    def onimgclick(self,evt):
        self.imgswap()
        if(evt.widget.imgs[1]!="Noncolor.png"):
            onColorButton()
        else:
            onNoncolorButton()

class AddButton(ttk.Button):
    def __init__(self,mstr,cb,var):
        super().__init__(master=mstr,text="Добавить")
        self.bindedCB=cb
        self.bindedVar=var
        self.config(command=self.onButtonClick)
    def onButtonClick(self):
        if(self.bindedCB.get()!=""):
            if(self.bindedVar.get()!=""):
                tmp=self.bindedVar.get()
                tmp+="|"+self.bindedCB.get()
                self.bindedVar.set(tmp)
            else:
                self.bindedVar.set(self.bindedCB.get())

class ClearButton(ttk.Button):
    def __init__(self,mstr,var):
        super().__init__(master=mstr,text="Сброс")
        self.bindedVar=var
        self.config(command=self.onButtonClick)
    def onButtonClick(self):
        self.bindedVar.set("")

class StatsElementClass:
    def __init__(self,mstr,Row,*vars):
        self.statslbl=ttk.Label(mstr,text="Характеристики:")
        self.statsframe=ttk.Frame(mstr)
        self.chosenmanalbl=ttk.Label(self.statsframe,textvariable=vars[0])
        self.chosenstrlbl=ttk.Label(self.statsframe,textvariable=vars[1])
        self.chosenendlbl=ttk.Label(self.statsframe,textvariable=vars[2])
        self.chosenloylbl=ttk.Label(self.statsframe,textvariable=vars[3])
        self.statsCB=ttk.Combobox(mstr,values=("Мана-стоимость","Сила","Выносливость","Верность"),state="readonly",width=35)
        self.elgbtn=ttk.Button(mstr,text="=",command=self.onELGButtonClick,width=5)
        self.statent=ttk.Entry(mstr,width=8)
        self.addbtn=ttk.Button(mstr,text="Добавить",command=self.onAddButtonClick)
        self.clearbtn=ttk.Button(mstr,text="Сброс",command=self.onClearButtonClick)
        self.statslbl.grid(row=Row,column=0,columnspan=5,sticky="w")
        self.statsframe.grid(row=Row+1,column=0,columnspan=5)
        self.chosenmanalbl.pack(side=LEFT)
        self.chosenstrlbl.pack(side=LEFT)
        self.chosenendlbl.pack(side=LEFT)
        self.chosenloylbl.pack(side=LEFT)
        self.statsCB.grid(row=Row+2,column=0)
        self.elgbtn.grid(row=Row+2,column=1,padx=5)
        self.statent.grid(row=Row+2,column=2,padx=(0,5))
        self.addbtn.grid(row=Row+2,column=3)
        self.clearbtn.grid(row=Row+2,column=4)
        self.elgstate=0
        self.elgvals=["=",">","<"]
        self.manavar=vars[0]
        self.strvar=vars[1]
        self.endvar=vars[2]
        self.loyvar=vars[3]
    def onELGButtonClick(self):
        if(self.elgstate==0):
            self.elgbtn.config(text=">")
            self.elgstate=1
        elif(self.elgstate==1):
            self.elgbtn.config(text="<")
            self.elgstate=2
        elif(self.elgstate==2):
            self.elgbtn.config(text="=")
            self.elgstate=0
    def onAddButtonClick(self):        
        if(self.statsCB.get()=="Мана-стоимость"):
            if(self.manavar.get()!=""):
                tmp=self.manavar.get()
                tmp+="|"+self.elgvals[self.elgstate]+self.statent.get()
                self.manavar.set(tmp)
            else:
                self.manavar.set(self.elgvals[self.elgstate]+self.statent.get())
        if(self.statsCB.get()=="Сила"):
            if(self.strvar.get()!=""):
                tmp=self.strvar.get()
                tmp+="|"+self.elgvals[self.elgstate]+self.statent.get()
                self.strvar.set(tmp)
            else:
                self.strvar.set(self.elgvals[self.elgstate]+self.statent.get())
        if(self.statsCB.get()=="Выносливость"):
            if(self.endvar.get()!=""):
                tmp=self.endvar.get()
                tmp+="|"+self.elgvals[self.elgstate]+self.statent.get()
                self.endvar.set(tmp)
            else:
                self.endvar.set(self.elgvals[self.elgstate]+self.statent.get())
        if(self.statsCB.get()=="Верность"):
            if(self.loyvar.get()!=""):
                tmp=self.loyvar.get()
                tmp+="|"+self.elgvals[self.elgstate]+self.statent.get()
                self.loyvar.set(tmp)
            else:
                self.loyvar.set(self.elgvals[self.elgstate]+self.statent.get())
    def onClearButtonClick(self):
        self.manavar.set("")
        self.strvar.set("")
        self.endvar.set("")
        self.loyvar.set("")
supertypes=ValuesClass(alldata,6)
types=ValuesClass(alldata,7)
undertypes=ValuesClass(alldata,8)
sets=ValuesClass(alldata,2)
artists=ValuesClass(alldata,15)
designs=ValuesClass(alldata,16)
raritys=ValuesClass(alldata,4)

namevar=StringVar()
supertypevar=StringVar()
typevar=StringVar()
undertypevar=StringVar()
manavar=StringVar()
strengthvar=StringVar()
endurancevar=StringVar()
loyaltyvar=StringVar()
setvar=StringVar()
artistvar=StringVar()
designvar=StringVar()
colorvar=StringVar()
descriptvar=StringVar()
rarityvar=StringVar()

whitebool=BooleanVar()
bluebool=BooleanVar()
blackbool=BooleanVar()
redbool=BooleanVar()
greenbool=BooleanVar()
noncolbool=BooleanVar()
flipbool=BooleanVar()

def setAttrFrame():
    global cardimg,index
    img=Image.open(imgpath+alldata[index][0])
    img=img.resize((int(img.width/1.75),int(img.height/1.75)))
    cardimg=ImageTk.PhotoImage(img)
    imglbl.config(image=cardimg)
    namelbl.config(text=alldata[index][1])
    descrlbl.config(text="")
    if(alldata[index][13]!=None):
        descrlbl.config(text=alldata[index][13])
    if(alldata[index][18]!=None):
        flipbtn.config(state=ACTIVE)
    else:
        flipbtn.config(state=DISABLED)
    typetext=""
    if(alldata[index][6]!=None):typetext+=alldata[index][6]+" "
    if(alldata[index][7]!=None):typetext+=alldata[index][7]
    if(alldata[index][8]!=None):typetext+=" - "+alldata[index][8]
    typelbl.config(text=typetext)
    manalbl.config(text="")
    if(alldata[index][9]!=None):manalbl.config(text=alldata[index][9])
    strendloytext=""
    if(alldata[index][10]!=None):strendloytext+=str(alldata[index][10])
    if(alldata[index][11]!=None):strendloytext+="/"+str(alldata[index][11])
    if(alldata[index][12]!=None):strendloytext+=str(alldata[index][12])
    strendlbl.config(text=strendloytext)
def onFlipbtnClick():
    global cardimg,index
    if(not flipbool.get()):
        flipbool.set(True)        
        img=Image.open(imgpath+osidedata[0][0])
        img=img.resize((int(img.width/1.75),int(img.height/1.75)))
        cardimg=ImageTk.PhotoImage(img)
        imglbl.config(image=cardimg)
        namelbl.config(text=osidedata[0][1])
        descrlbl.config(text=osidedata[0][13])
        typetext=""
        if(osidedata[0][6]!=None):typetext+=osidedata[0][6]+" "
        if(osidedata[0][7]!=None):typetext+=osidedata[0][7]
        if(osidedata[0][8]!=None):typetext+=" - "+osidedata[0][8]
        typelbl.config(text=typetext)
        manalbl.config(text="")
        if(osidedata[0][9]!=None):manalbl.config(text=osidedata[0][9])
        strendloytext=""
        if(osidedata[0][10]!=None):strendloytext+=str(osidedata[0][10])
        if(osidedata[0][11]!=None):strendloytext+="/"+str(osidedata[0][11])
        if(osidedata[0][12]!=None):strendloytext+=str(osidedata[0][12])
        strendlbl.config(text=strendloytext)
    else:
        flipbool.set(False)
        setAttrFrame()
def treeselect(evt):
    global index,osidedata   
    index=int(tree.selection()[0])
    flipbool.set(False)
    if(alldata[index][18]!=None):
        dsid=alldata[index][18]
        dbcursor.execute(f"SELECT * FROM OtherSide WHERE DoubleSideID={dsid}")
        osidedata=dbcursor.fetchall()
    setAttrFrame()
def onimgpress(evt):
    global incardimg
    imgwnd=Toplevel()
    if(flipbool.get()):
        imgwnd.title(osidedata[0][1])
        img=Image.open(imgpath+osidedata[0][0])
    else:
        imgwnd.title(alldata[index][1])
        img=Image.open(imgpath+alldata[index][0])
    imgwnd.geometry("350x500")
    imgwnd.resizable(False,False)    
    innerimg=ttk.Label(imgwnd)
    innerimg.pack(anchor="center",expand=True)
    incardimg=ImageTk.PhotoImage(img)
    innerimg.config(image=incardimg)
def onTypesButtonClick():
    if(stypeCB.get()!=""):
        if(supertypevar.get()!=""):
            tmp=supertypevar.get()
            tmp+="|"+stypeCB.get()
            supertypevar.set(tmp)
        else:
            supertypevar.set(stypeCB.get())
    if(typeCB.get()!=""):
        if(typevar.get()!=""):
            tmp=typevar.get()
            tmp+="|"+typeCB.get()
            typevar.set(tmp)
        else:
            typevar.set(typeCB.get())
    if(utypeCB.get()!=""):
        if(undertypevar.get()!=""):
            tmp=undertypevar.get()
            tmp+="|"+utypeCB.get()
            undertypevar.set(tmp)
        else:
            undertypevar.set(utypeCB.get())
def onCTypesButtonClick():
    supertypevar.set("")
    typevar.set("")
    undertypevar.set("")
def onFilterClearButtonClick():
    supertypevar.set("")
    typevar.set("")
    undertypevar.set("")
    manavar.set("")
    strengthvar.set("")
    endurancevar.set("")
    loyaltyvar.set("")
    setvar.set("")
    artistvar.set("")
    designvar.set("")
    colorvar.set("")
    descriptvar.set("")
    rarityvar.set("")
    if(whitebool.get()):
        whitelbl.imgswap()
    if(bluebool.get()):
        bluelbl.imgswap()
    if(blackbool.get()):
        blacklbl.imgswap()
    if(redbool.get()):
        redlbl.imgswap()
    if(greenbool.get()):
        greenlbl.imgswap()
    if(noncolbool.get()):
        noncollbl.imgswap()
    selectData()
  
def showfilter():
    global stypeCB,typeCB,utypeCB,whitelbl,bluelbl,blacklbl,redlbl,greenlbl,noncollbl
    
    filterwnd=Toplevel()
    filterwnd.title("Фильтрация")
    filterwnd.minsize(500,620)
    filterwnd.resizable(False,False)
    
    typeslbl=ttk.Label(filterwnd,text="Тип:")
    typesframe=ttk.Frame(filterwnd)
    chosenstypelbl=ttk.Label(typesframe,textvariable=supertypevar)
    chosentypelbl=ttk.Label(typesframe,textvariable=typevar)
    chosenutypelbl=ttk.Label(typesframe,textvariable=undertypevar)
    stypeCB=ttk.Combobox(filterwnd,values=supertypes.values,state="readonly",width=35)
    typeCB=ttk.Combobox(filterwnd,values=types.values,state="readonly",width=35)
    utypeCB=ttk.Combobox(filterwnd,values=undertypes.values,state="readonly",width=35)
    addTypes=ttk.Button(filterwnd,text="Добавить",command=onTypesButtonClick)
    clearTypes=ttk.Button(filterwnd,text="Сброс",command=onCTypesButtonClick)
    typeslbl.grid(row=0,column=0,columnspan=5,sticky="w")
    typesframe.grid(row=1,column=0,columnspan=5)
    chosenstypelbl.pack(side=LEFT)
    chosentypelbl.pack(side=LEFT)
    chosenutypelbl.pack(side=LEFT)
    stypeCB.grid(row=2,column=0)
    typeCB.grid(row=3,column=0)
    utypeCB.grid(row=4,column=0)
    addTypes.grid(row=3,column=3)
    clearTypes.grid(row=3,column=4)
    
    stats=StatsElementClass(filterwnd,5,manavar,strengthvar,endurancevar,loyaltyvar)    
    
    setslbl=ttk.Label(filterwnd,text="Сет:")
    chosensetlbl=ttk.Label(filterwnd,textvariable=setvar)
    setCB=ttk.Combobox(filterwnd,values=sets.values,state="readonly",width=35)
    addSet=AddButton(filterwnd,setCB,setvar)
    clearSet=ClearButton(filterwnd,setvar)
    setslbl.grid(row=8,column=0,columnspan=5,sticky="w")
    chosensetlbl.grid(row=9,column=0,columnspan=5)
    setCB.grid(row=10,column=0)
    addSet.grid(row=10,column=3)
    clearSet.grid(row=10,column=4)
    
    artistslbl=ttk.Label(filterwnd,text="Художник:")
    chosenartistlbl=ttk.Label(filterwnd,textvariable=artistvar)
    artistCB=ttk.Combobox(filterwnd,values=artists.values,state="readonly",width=35)
    addArtist=AddButton(filterwnd,artistCB,artistvar)
    clearArtist=ClearButton(filterwnd,artistvar)
    artistslbl.grid(row=11,column=0,columnspan=5,sticky="w")
    chosenartistlbl.grid(row=12,column=0,columnspan=5)
    artistCB.grid(row=13,column=0)
    addArtist.grid(row=13,column=3)
    clearArtist.grid(row=13,column=4)
    
    designslbl=ttk.Label(filterwnd,text="Оформление:")
    chosendesignlbl=ttk.Label(filterwnd,textvariable=designvar)
    designCB=ttk.Combobox(filterwnd,values=designs.values,state="readonly",width=35)
    addDesign=AddButton(filterwnd,designCB,designvar)
    clearDesign=ClearButton(filterwnd,designvar)
    designslbl.grid(row=14,column=0,columnspan=5,sticky="w")
    chosendesignlbl.grid(row=15,column=0,columnspan=5)
    designCB.grid(row=16,column=0)
    addDesign.grid(row=16,column=3)
    clearDesign.grid(row=16,column=4)
    
    colorslbl=ttk.Label(filterwnd,text="Цвет:")
    colorframe=ttk.Frame(filterwnd)
    colorslbl.grid(row=17,column=0,columnspan=5,sticky="w")
    colorframe.grid(row=18,column=0,columnspan=5,sticky="w")
    whitelbl=ImgButton(colorframe,["WhiteT.png","White.png"],whitebool)
    bluelbl=ImgButton(colorframe,["BlueT.png","Blue.png"],bluebool)
    blacklbl=ImgButton(colorframe,["BlackT.png","Black.png"],blackbool)
    redlbl=ImgButton(colorframe,["RedT.png","Red.png"],redbool)
    greenlbl=ImgButton(colorframe,["GreenT.png","Green.png"],greenbool)
    noncollbl=ImgButton(colorframe,["NoncolorT.png","Noncolor.png"],noncolbool)
    whitelbl.pack(side=LEFT)
    bluelbl.pack(side=LEFT)
    blacklbl.pack(side=LEFT)
    redlbl.pack(side=LEFT)
    greenlbl.pack(side=LEFT)
    noncollbl.pack(side=LEFT)
    
    descrslbl=ttk.Label(filterwnd,text="Описание:")
    chosendescrlbl=ttk.Label(filterwnd,textvariable=descriptvar)
    descrent=ttk.Entry(filterwnd,width=35)
    addDescr=AddButton(filterwnd,descrent,descriptvar)
    clearDescr=ClearButton(filterwnd,descriptvar)
    descrslbl.grid(row=19,column=0,columnspan=5,sticky="w")
    chosendescrlbl.grid(row=20,column=0,columnspan=5)
    descrent.grid(row=21,column=0)
    addDescr.grid(row=21,column=3)
    clearDescr.grid(row=21,column=4)
    
    rarslbl=ttk.Label(filterwnd,text="Редкость:")
    chosenrarelbl=ttk.Label(filterwnd,textvariable=rarityvar)
    rareCB=ttk.Combobox(filterwnd,values=raritys.values,state="readonly",width=35)
    addRarity=AddButton(filterwnd,rareCB,rarityvar)
    clearRarity=ClearButton(filterwnd,rarityvar)
    rarslbl.grid(row=22,column=0,columnspan=5,sticky="w")
    chosenrarelbl.grid(row=23,column=0,columnspan=5)
    rareCB.grid(row=24,column=0)
    addRarity.grid(row=24,column=3)
    clearRarity.grid(row=24,column=4)
    
    applybtn=ttk.Button(filterwnd,text="Применить",command=selectData)
    clearbtnf=ttk.Button(filterwnd,text="Сброс",command=onFilterClearButtonClick)
    blanklbl=ttk.Label(filterwnd,text=" ")
    blanklbl.grid(row=25,column=0,columnspan=5)
    applybtn.grid(row=26,column=3)
    clearbtnf.grid(row=26,column=4)

mMain.add_cascade(label="Программа",menu=mProg)
mMain.add_command(label="Фильтр",command=showfilter)
mMain.add_cascade(label="Группировка",menu=mGroup)
root.config(menu=mMain)

tabframe=ttk.Frame(root,borderwidth=3,relief=GROOVE)
attrframe=ttk.Frame(root,borderwidth=3,relief=GROOVE)
attrframe.place(relwidth=0.3,relheight=1,relx=0.7)
tabframe.place(relwidth=0.7,relheight=1,x=0)
tabframe.columnconfigure(index=0,weight=20)
tabframe.columnconfigure(index=1,weight=1)
tabframe.rowconfigure(index=0,weight=10)
tabframe.rowconfigure(index=0,weight=1)
attrframe.columnconfigure(index=0,weight=1)
attrframe.columnconfigure(index=1,weight=1)
attrframe.rowconfigure(index=0,weight=2)
attrframe.rowconfigure(index=1,weight=1)
attrframe.rowconfigure(index=2,weight=1)
attrframe.rowconfigure(index=3,weight=8)
searchframe=ttk.Frame(tabframe,borderwidth=3,relief=GROOVE)

imglbl=ttk.Label(attrframe,anchor="center",cursor="hand2")
namelbl=ttk.Label(attrframe,anchor="w")
typelbl=ttk.Label(attrframe,anchor="w")
manalbl=ttk.Label(attrframe,anchor="e")
strendlbl=ttk.Label(attrframe,anchor="e")
descrlbl=ttk.Label(attrframe,anchor="center",wraplength=330)
flipbtn=ttk.Button(attrframe,text="Сменить",state=DISABLED,command=onFlipbtnClick)
imglbl.bind("<ButtonPress>",onimgpress)
imglbl.grid(row=0,column=0,columnspan=2)
namelbl.grid(row=1,column=0,sticky="nsew")
manalbl.grid(row=1,column=1,sticky="nsew")
typelbl.grid(row=2,column=0,sticky="nsew")
strendlbl.grid(row=2,column=1,sticky="nsew")
descrlbl.grid(row=3,column=0,columnspan=2,sticky="nsew")
flipbtn.grid(row=4,column=0,columnspan=2,sticky="ns")

def sort(col, reverse):
    alldata.sort(reverse=reverse,key=lambda k:k[col])
    setTabData()
    index=0
    for r in tree.get_children():
            tree.delete(r)        
    for v in tabdata:
        tree.insert("", END,iid=index, values=v)
        index+=1
    tree.heading(col, command=lambda: sort(col, not reverse))

tree=ttk.Treeview(tabframe,columns=cols,show="headings")
tree.grid(row=0,column=0,sticky="nsew")
tree.heading("Numero",text="№ п/п")
tree.column("Numero",width=50,stretch=False,anchor="center")
tree.heading("Name", text="Название",command=lambda: sort(1, False))
tree.heading("SetName", text="Сет",command=lambda: sort(2, False))
tree.heading("Number", text="Номер",command=lambda: sort(3, False))
tree.column("Number",width=50,stretch=False,anchor="center")
tree.heading("Rarity", text="Редкость")
tree.column("Rarity",width=75,stretch=False,anchor="center")
tree.heading("Quantity", text="Количество")
tree.column("Quantity",width=80,stretch=False,anchor="center")
tree.heading("Foil", text="Foil")
tree.column("Foil",width=50,stretch=False,anchor="center")
for v in tabdata:
    tree.insert("", END,iid=index, values=v)
    index+=1
tree.bind("<<TreeviewSelect>>",treeselect)
treescroll=ttk.Scrollbar(tabframe,orient=VERTICAL,command=tree.yview)
tree.configure(yscroll=treescroll.set)
treescroll.grid(row=0,column=1,sticky="ns")

def onClearSearchButtonClick():
    namevar.set("")
    selectData()

searchframe.grid(row=1,column=0,columnspan=2,sticky="ew")
searchent=ttk.Entry(searchframe,width=60,textvariable=namevar)
searchbtn=ttk.Button(searchframe,text="Поиск",command=selectData)
clearbtn=ttk.Button(searchframe,text="Сброс",command=onClearSearchButtonClick)
searchent.pack(side=LEFT)
searchbtn.pack(side=LEFT)
clearbtn.pack(side=LEFT)

class StatsTree(ttk.Treeview):
    def __init__(self,mstr,request,condition,cursor,height):
        super().__init__(master=mstr,columns=("Numer","Name","NoQuantity","Quantity"),show="headings",height=height)
        self.request=request
        self.heading("Numer",text="№ п/п")
        self.column("Numer",width=50,stretch=False,anchor="center")
        self.heading("Name",text="Наименование",command=lambda: self.sort(1, False))
        self.heading("NoQuantity",text="Без учета кол-ва",command=lambda: self.sort(2, False))
        self.column("NoQuantity",width=100,stretch=False,anchor="center")
        self.heading("Quantity",text="С учетом кол-ва",command=lambda: self.sort(3, False))
        self.column("Quantity",width=100,stretch=False,anchor="center")
        if(condition!=""):
            txt=request.replace("GROUP","WHERE "+condition+" GROUP")
            cursor.execute(f"{txt}")
        else:
            cursor.execute(f"{request}")
        self.dbdata=cursor.fetchall()
        self.data=list()
        i=1
        for v in self.dbdata:
            self.data.append((i,)+v[:])
            i+=1
        for v in self.data:
            self.insert("",END,values=v)
    def sort(self,col,reverse):
        self.dbdata.sort(reverse=reverse,key=lambda k:k[col-1])
        self.data=list()
        i=1
        for v in self.dbdata:
            self.data.append((i,)+v[:])
            i+=1
        for r in self.get_children():
            self.delete(r)        
        for v in self.data:
            self.insert("",END,values=v)
        self.heading(col, command=lambda: self.sort(col, not reverse))
        

def showstats():
    global dbcursor,condition
       
    statswnd=Toplevel()
    statswnd.title("Статистика")
    statswnd.minsize(500,950)
    statswnd.resizable(False,False)
    
    setlbl=ttk.Label(statswnd,anchor="center",text="Статистика по сетам")
    setlbl.pack(side=TOP)
    setframe=ttk.Frame(statswnd)
    setframe.pack(side=TOP)
    settree=StatsTree(setframe,"SELECT Setname, COUNT(*), SUM(Quantity) FROM WorkTable GROUP BY Setname;",condition,dbcursor,3)
    settree.pack(side=LEFT)
    settreescroll=ttk.Scrollbar(setframe,orient=VERTICAL,command=settree.yview)
    settree.configure(yscroll=settreescroll.set)
    settreescroll.pack(side=LEFT,fill=Y)
    
    
    rarlbl=ttk.Label(statswnd,anchor="center",text="Статистика по редкости")
    rarlbl.pack(side=TOP)
    rarframe=ttk.Frame(statswnd)
    rarframe.pack(side=TOP)
    rartree=StatsTree(rarframe,"SELECT Rarity, COUNT(*), SUM(Quantity) FROM WorkTable GROUP BY Rarity;",condition,dbcursor,2)
    rartree.pack(side=LEFT)
    rartreescroll=ttk.Scrollbar(rarframe,orient=VERTICAL,command=rartree.yview)
    rartree.configure(yscroll=rartreescroll.set)
    rartreescroll.pack(side=LEFT,fill=Y)
    
    suptyplbl=ttk.Label(statswnd,anchor="center",text="Статистика по супертипам")
    suptyplbl.pack(side=TOP)
    suptypframe=ttk.Frame(statswnd)
    suptypframe.pack(side=TOP)
    suptyptree=StatsTree(suptypframe,"SELECT SuperType, COUNT(*), SUM(Quantity) FROM WorkTable GROUP BY SuperType;",condition,dbcursor,3)
    suptyptree.pack(side=LEFT)
    suptyptreescroll=ttk.Scrollbar(suptypframe,orient=VERTICAL,command=suptyptree.yview)
    suptyptree.configure(yscroll=suptyptreescroll.set)
    suptyptreescroll.pack(side=LEFT,fill=Y)
    
    typlbl=ttk.Label(statswnd,anchor="center",text="Статистика по типам")
    typlbl.pack(side=TOP)
    typframe=ttk.Frame(statswnd)
    typframe.pack(side=TOP)
    typtree=StatsTree(typframe,"SELECT Type, COUNT(*), SUM(Quantity) FROM WorkTable GROUP BY Type;",condition,dbcursor,3)
    typtree.pack(side=LEFT)
    typtreescroll=ttk.Scrollbar(typframe,orient=VERTICAL,command=typtree.yview)
    typtree.configure(yscroll=typtreescroll.set)
    typtreescroll.pack(side=LEFT,fill=Y)
    
    undtyplbl=ttk.Label(statswnd,anchor="center",text="Статистика по подтипам")
    undtyplbl.pack(side=TOP)
    undtypframe=ttk.Frame(statswnd)
    undtypframe.pack(side=TOP)
    undtyptree=StatsTree(undtypframe,"SELECT UnderType, COUNT(*), SUM(Quantity) FROM WorkTable GROUP BY UnderType;",condition,dbcursor,3)
    undtyptree.pack(side=LEFT)
    undtyptreescroll=ttk.Scrollbar(undtypframe,orient=VERTICAL,command=undtyptree.yview)
    undtyptree.configure(yscroll=undtyptreescroll.set)
    undtyptreescroll.pack(side=LEFT,fill=Y)
    
    collbl=ttk.Label(statswnd,anchor="center",text="Статистика по цветам")
    collbl.pack(side=TOP)
    colframe=ttk.Frame(statswnd)
    colframe.pack(side=TOP)
    coltree=StatsTree(colframe,"SELECT Color, COUNT(*), SUM(Quantity) FROM WorkTable GROUP BY Color;",condition,dbcursor,3)
    coltree.pack(side=LEFT)
    coltreescroll=ttk.Scrollbar(colframe,orient=VERTICAL,command=coltree.yview)
    coltree.configure(yscroll=coltreescroll.set)
    coltreescroll.pack(side=LEFT,fill=Y)
    
    artlbl=ttk.Label(statswnd,anchor="center",text="Статистика по художникам")
    artlbl.pack(side=TOP)
    artframe=ttk.Frame(statswnd)
    artframe.pack(side=TOP)
    arttree=StatsTree(artframe,"SELECT Artist, COUNT(*), SUM(Quantity) FROM WorkTable GROUP BY Artist;",condition,dbcursor,3)
    arttree.pack(side=LEFT)
    arttreescroll=ttk.Scrollbar(artframe,orient=VERTICAL,command=arttree.yview)
    arttree.configure(yscroll=arttreescroll.set)
    arttreescroll.pack(side=LEFT,fill=Y)

    deslbl=ttk.Label(statswnd,anchor="center",text="Статистика по оформлению")
    deslbl.pack(side=TOP)
    desframe=ttk.Frame(statswnd)
    desframe.pack(side=TOP)
    destree=StatsTree(desframe,"SELECT Design, COUNT(*), SUM(Quantity) FROM WorkTable GROUP BY Design;",condition,dbcursor,3)
    destree.pack(side=LEFT)
    destreescroll=ttk.Scrollbar(desframe,orient=VERTICAL,command=destree.yview)
    destree.configure(yscroll=destreescroll.set)
    destreescroll.pack(side=LEFT,fill=Y)
    
    foillbl=ttk.Label(statswnd,anchor="center",text="Статистика по фойлу")
    foillbl.pack(side=TOP)
    foilframe=ttk.Frame(statswnd)
    foilframe.pack(side=TOP)
    foiltree=StatsTree(foilframe,"SELECT Foil, COUNT(*), SUM(Quantity) FROM WorkTable GROUP BY Foil;",condition,dbcursor,2)
    foiltree.pack(side=LEFT)
    foiltreescroll=ttk.Scrollbar(foilframe,orient=VERTICAL,command=foiltree.yview)
    foiltree.configure(yscroll=foiltreescroll.set)
    foiltreescroll.pack(side=LEFT,fill=Y)

mMain.add_command(label="Статистика",command=showstats)

root.mainloop()