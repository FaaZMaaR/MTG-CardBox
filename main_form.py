from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
from PIL import Image,ImageTk

from data import MTGData
import widgets

class MainForm(Tk):
    def __init__(self):
        super().__init__()
        self.data=MTGData("MTG.db")
        self.currentData=list()
        self.selectedIndex=0
        self.imgpath="Pictures\\"
        self.initVars()  
        self.initWindow()
        self.initFrames()
        self.initTabFrame()
        self.initAttrFrame()
        self.initMenu()
        self.updateData()

    def initVars(self):
        self.nameVar=StringVar()
        self.superTypeVar=StringVar()
        self.typeVar=StringVar()
        self.underTypeVar=StringVar()
        self.manaVar=StringVar()
        self.strengthVar=StringVar()
        self.enduranceVar=StringVar()
        self.loyaltyVar=StringVar()
        self.setVar=StringVar()
        self.artistVar=StringVar()
        self.designVar=StringVar()
        self.colorVar=StringVar()
        self.descriptionVar=StringVar()
        self.rarityVar=StringVar()
        
        self.superTypeNonVar=StringVar()
        self.typeNonVar=StringVar()
        self.underTypeNonVar=StringVar()
        self.setNonVar=StringVar()
        self.artistNonVar=StringVar()
        self.designNonVar=StringVar()
        self.rarityNonVar=StringVar()
        
        self.groupRarity=StringVar()
        self.groupSet=StringVar()
        self.groupColor=StringVar()
        self.groupType=StringVar()
        
        self.flipbool=BooleanVar()
    
    def initWindow(self):
        self.title("MTG CardBox")
        self.iconbitmap(default="MTG.ico")
        self.minsize(1200,800)
        
    def initFrames(self):
        self.tabframe=ttk.Frame(self,borderwidth=3,relief=GROOVE)
        self.attrframe=ttk.Frame(self,borderwidth=3,relief=GROOVE)
        self.searchframe=ttk.Frame(self.tabframe,borderwidth=3,relief=GROOVE)
        self.tabframe.place(relwidth=0.7,relheight=1,x=0)
        self.attrframe.place(relwidth=0.3,relheight=1,relx=0.7)
        self.tabframe.columnconfigure(index=0,weight=20)
        self.tabframe.columnconfigure(index=1,weight=1)
        self.tabframe.rowconfigure(index=0,weight=10)
        #self.tabframe.rowconfigure(index=0,weight=1)
        self.attrframe.columnconfigure(index=0,weight=1)
        self.attrframe.columnconfigure(index=1,weight=1)
        self.attrframe.rowconfigure(index=0,weight=2)
        self.attrframe.rowconfigure(index=1,weight=1)
        self.attrframe.rowconfigure(index=2,weight=1)
        self.attrframe.rowconfigure(index=3,weight=8)
        self.searchframe=ttk.Frame(self.tabframe,borderwidth=3,relief=GROOVE)
        self.searchframe.grid(row=1,column=0,columnspan=2,sticky="ew")
        
    def initTabFrame(self):        
        self.datatree=widgets.DataTree(self.tabframe)
        self.datatree.grid(row=0,column=0,sticky="nsew")
        self.datatree.bind("<<TreeviewSelect>>",self.datatreeSelect)
        self.treescroll=ttk.Scrollbar(self.tabframe,orient=VERTICAL,command=self.datatree.yview)
        self.datatree.configure(yscroll=self.treescroll.set)
        self.treescroll.grid(row=0,column=1,sticky="ns")
        self.searchent=ttk.Entry(self.searchframe,width=60,textvariable=self.nameVar)
        self.searchbtn=ttk.Button(self.searchframe,text="Поиск",command=self.filterData)
        self.clearsearchbtn=ttk.Button(self.searchframe,text="Сброс",command=self.onClearSearchButtonClick)
        self.searchent.pack(side=LEFT)
        self.searchbtn.pack(side=LEFT)
        self.clearsearchbtn.pack(side=LEFT)        
        
    def initAttrFrame(self):
        self.imglbl=ttk.Label(self.attrframe,anchor="center",cursor="hand2")
        self.namelbl=ttk.Label(self.attrframe,anchor="w")
        self.typelbl=ttk.Label(self.attrframe,anchor="w")
        self.manalbl=ttk.Label(self.attrframe,anchor="e")
        self.strendlbl=ttk.Label(self.attrframe,anchor="e")
        self.descrlbl=ttk.Label(self.attrframe,anchor="center",wraplength=330)
        self.flipbtn=ttk.Button(self.attrframe,text="Сменить",state=DISABLED,command=self.onFlipbtnClick)
        self.imglbl.bind("<ButtonPress>",self.onImgPress)
        self.imglbl.grid(row=0,column=0,columnspan=2)
        self.namelbl.grid(row=1,column=0,sticky="nsew")
        self.manalbl.grid(row=1,column=1,sticky="nsew")
        self.typelbl.grid(row=2,column=0,sticky="nsew")
        self.strendlbl.grid(row=2,column=1,sticky="nsew")
        self.descrlbl.grid(row=3,column=0,columnspan=2,sticky="nsew")
        self.flipbtn.grid(row=4,column=0,columnspan=2,sticky="ns")
    
    def initMenu(self):
        self.mMain=Menu(self)
        self.mProg=Menu(self,tearoff=0)
        self.mGroup=Menu(self,tearoff=0)
        self.mProg.add_command(label="О программе",command=self.showAbout)
        self.mProg.add_separator()
        self.mProg.add_command(label="Выход",command=self.close)
        self.mMain.add_cascade(label="Программа",menu=self.mProg)
        self.mMain.add_command(label="Фильтр",command=self.showFilter)
        self.mMain.add_cascade(label="Группировка",menu=self.mGroup)
        self.mMain.add_command(label="Статистика",command=self.showStats)
        self.config(menu=self.mMain)
    
    def datatreeSelect(self,evt): 
        self.selectedIndex=int(self.datatree.selection()[0])-1
        self.flipbool.set(False)      
        if(self.currentData[self.selectedIndex][18]!=None):
            dsid=self.currentData[self.selectedIndex][18]
            self.osidedata=self.data.getOtherSideData(dsid)
        self.fillAttrFrame(self.currentData[self.selectedIndex])
        if(self.currentData[self.selectedIndex][18]!=None):
            self.flipbtn.config(state=ACTIVE)
        else:
            self.flipbtn.config(state=DISABLED)
        
    def fillAttrFrame(self,data):
        img=Image.open(self.imgpath+data[0])
        img=img.resize((int(img.width/1.75),int(img.height/1.75)))
        self.cardimg=ImageTk.PhotoImage(img)
        self.imglbl.config(image=self.cardimg)
        self.namelbl.config(text=data[1])
        self.descrlbl.config(text="")
        if(data[13]!=None):
            self.descrlbl.config(text=data[13])        
        typetext=""
        if(data[6]!=None):typetext+=data[6]+" "
        if(data[7]!=None):typetext+=data[7]
        if(data[8]!=None):typetext+=" - "+data[8]
        self.typelbl.config(text=typetext)
        self.manalbl.config(text="")
        if(data[9]!=None):self.manalbl.config(text=data[9])
        strendloytext=""
        if(data[10]!=None):strendloytext+=str(data[10])
        if(data[11]!=None):strendloytext+="/"+str(data[11])
        if(data[12]!=None):strendloytext+=str(data[12])
        self.strendlbl.config(text=strendloytext)
    
    def updateData(self):
        self.data.updateFilter()
        self.currentData=self.data.getFilteredData()
        self.datatree.fillTree(self.currentData)
        self.initGroupMenu()
    
    def filterData(self):
        self.data.searchName=self.nameVar.get()
        self.data.filterSet=self.setVar.get()+"!"+self.setNonVar.get()
        self.data.filterRar=self.rarityVar.get()+"!"+self.rarityNonVar.get()
        self.data.filterSuptyp=self.superTypeVar.get()+"!"+self.superTypeNonVar.get()
        self.data.filterTyp=self.typeVar.get()+"!"+self.typeNonVar.get()
        self.data.filterUndtyp=self.underTypeVar.get()+"!"+self.underTypeNonVar.get()
        self.data.filterMana=self.manaVar.get()
        self.data.filterStr=self.strengthVar.get()
        self.data.filterEnd=self.enduranceVar.get()
        self.data.filterLoy=self.loyaltyVar.get()
        self.data.filterDescr=self.descriptionVar.get()
        self.data.filterCol=self.colorVar.get()
        self.data.filterArt=self.artistVar.get()+"!"+self.artistNonVar.get()
        self.data.filterDesign=self.designVar.get()+"!"+self.designNonVar.get()
        self.data.groupRar=self.groupRarity.get()
        self.data.groupSet=self.groupSet.get()
        self.data.groupCol=self.groupColor.get()
        self.data.groupTyp=self.groupType.get()        
        self.updateData()
        
    def clearFilters(self):
        self.superTypeVar.set("")
        self.typeVar.set("")
        self.underTypeVar.set("")
        self.manaVar.set("")
        self.strengthVar.set("")
        self.enduranceVar.set("")
        self.loyaltyVar.set("")
        self.setVar.set("")
        self.artistVar.set("")
        self.designVar.set("")
        self.colorVar.set("")
        self.descriptionVar.set("")
        self.rarityVar.set("")
        self.superTypeNonVar.set("")
        self.typeNonVar.set("")
        self.underTypeNonVar.set("")
        self.setNonVar.set("")
        self.artistNonVar.set("")
        self.designNonVar.set("")
        self.rarityNonVar.set("")
        self.filterData()
    
    def onClearSearchButtonClick(self):
        self.nameVar.set("")
        self.filterData()
    
    def onFlipbtnClick(self):
        if(not self.flipbool.get()):
            self.flipbool.set(True)        
            self.fillAttrFrame(self.osidedata[0])
        else:
            self.flipbool.set(False)
            self.fillAttrFrame(self.currentData[self.selectedIndex])
    
    def onImgPress(self,evt):
        if(self.flipbool.get()):
            title=self.osidedata[0][1]
            path=self.imgpath+self.osidedata[0][0]
        else:
            title=self.currentData[self.selectedIndex][1]
            path=self.imgpath+self.currentData[self.selectedIndex][0]
        imgForm=widgets.ImageForm(title,path)
    
    def close(self):
        self.destroy()
        
    def showAbout(self):
        showinfo('О программе','Версия: 2.0.0\nДата изменения: 22.11.2024\nАвтор: Тимофей FaaZMaaR Волхонский')
    
    def showFilter(self):
        filterForm=widgets.FilterForm(self)
    
    def showStats(self):
        statsForm=widgets.StatsForm(self)
    
    def initGroupMenu(self):        
        self.mGroup.delete(0,END)
        self.mGroupRare=Menu(self,tearoff=0)
        self.mGroupSet=Menu(self,tearoff=0)
        self.mGroupColor=Menu(self,tearoff=0)
        self.mGroupType=Menu(self,tearoff=0)

        vals=self.data.getAttributesList(4)
        if("Common" in vals):
            self.mGroupRare.add_command(label="Common",command=lambda:self.selectRarGroup("Common"))
        if("Uncommon" in vals):
            self.mGroupRare.add_command(label="Uncommon",command=lambda:self.selectRarGroup("Uncommon"))
        if("Rare" in vals):
            self.mGroupRare.add_command(label="Rare",command=lambda:self.selectRarGroup("Rare"))
        if("Mythic" in vals):
            self.mGroupRare.add_command(label="Mythic",command=lambda:self.selectRarGroup("Mythic"))
            
        vals=self.data.getAttributesList(2)
        if("Adventures in the Forgotten Realms" in vals):
            self.mGroupSet.add_command(label="Adventures in the Forgotten Realms",command=lambda:self.selectSetGroup("Adventures in the Forgotten Realms"))
        if("Aether Revolt" in vals):
            self.mGroupSet.add_command(label="Aether Revolt",command=lambda:self.selectSetGroup("Aether Revolt"))
        if("Commander 2021" in vals):
            self.mGroupSet.add_command(label="Commander 2021",command=lambda:self.selectSetGroup("Commander 2021"))
        if("Core Set 2020" in vals):
            self.mGroupSet.add_command(label="Core Set 2020",command=lambda:self.selectSetGroup("Core Set 2020"))
        if("Core Set 2021" in vals):
            self.mGroupSet.add_command(label="Core Set 2021",command=lambda:self.selectSetGroup("Core Set 2021"))
        if("Ikoria: Lair of Behemoths" in vals):
            self.mGroupSet.add_command(label="Ikoria: Lair of Behemoths",command=lambda:self.selectSetGroup("Ikoria: Lair of Behemoths"))
        if("Innistrad: Crimson Vow" in vals):
            self.mGroupSet.add_command(label="Innistrad: Crimson Vow",command=lambda:self.selectSetGroup("Innistrad: Crimson Vow"))
        if("Innistrad: Midnight Hunt"in vals):
            self.mGroupSet.add_command(label="Innistrad: Midnight Hunt",command=lambda:self.selectSetGroup("Innistrad: Midnight Hunt"))
        if("Kaladesh" in vals):
            self.mGroupSet.add_command(label="Kaladesh",command=lambda:self.selectSetGroup("Kaladesh"))
        if("Kaldheim" in vals):
            self.mGroupSet.add_command(label="Kaldheim",command=lambda:self.selectSetGroup("Kaldheim"))
        if("Kamigawa: Neon Dynasty" in vals):
            self.mGroupSet.add_command(label="Kamigawa: Neon Dynasty",command=lambda:self.selectSetGroup("Kamigawa: Neon Dynasty"))
        if("Midnight Hunt Commander" in vals):
            self.mGroupSet.add_command(label="Midnight Hunt Commander",command=lambda:self.selectSetGroup("Midnight Hunt Commander"))
        if("Modern Horizons 2" in vals):
            self.mGroupSet.add_command(label="Modern Horizons 2",command=lambda:self.selectSetGroup("Modern Horizons 2"))
        if("Strixhaven: School of Mages" in vals):
            self.mGroupSet.add_command(label="Strixhaven: School of Mages",command=lambda:self.selectSetGroup("Strixhaven: School of Mages"))
        if("Strixhaven Mystical Archive" in vals):
            self.mGroupSet.add_command(label="Strixhaven Mystical Archive",command=lambda:self.selectSetGroup("Strixhaven Mystical Archive"))
        if("The List" in vals):
            self.mGroupSet.add_command(label="The List",command=lambda:self.selectSetGroup("The List"))
        if("Theros Beyond Death" in vals):
            self.mGroupSet.add_command(label="Theros Beyond Death",command=lambda:self.selectSetGroup("Theros Beyond Death"))
        if("Throne of Eldraine" in vals):
            self.mGroupSet.add_command(label="Throne of Eldraine",command=lambda:self.selectSetGroup("Throne of Eldraine"))
        if("Zendikar Rising" in vals):
            self.mGroupSet.add_command(label="Zendikar Rising",command=lambda:self.selectSetGroup("Zendikar Rising"))
        if("War of the Spark" in vals):
            self.mGroupSet.add_command(label="War of the Spark",command=lambda:self.selectSetGroup("War of the Spark"))
                
        vals=self.data.getAttributesList(14)
        if("White" in vals):
            self.mGroupColor.add_command(label="Белый",command=lambda:self.selectColGroup("White"))
        if("Blue" in vals):
            self.mGroupColor.add_command(label="Синий",command=lambda:self.selectColGroup("Blue"))
        if("Black" in vals):
            self.mGroupColor.add_command(label="Черный",command=lambda:self.selectColGroup("Black"))
        if("Red" in vals):
            self.mGroupColor.add_command(label="Красный",command=lambda:self.selectColGroup("Red"))
        if("Green" in vals):
            self.mGroupColor.add_command(label="Зеленый",command=lambda:self.selectColGroup("Green"))
        for v in vals:
            if("|" in v):
                self.mGroupColor.add_command(label="Многоцветный",command=lambda:self.selectColGroup("multi"))
                break
        if("Noncolor" in vals):
            self.mGroupColor.add_command(label="Бесцветный",command=lambda:self.selectColGroup("Noncolor"))
        allvals=self.data.getFilteredData()
        for v in allvals:
            if((v[6]!="Базовая" and v[6]!="Базовая Снежная") and (v[7]=="Земля" or v[7]=="Артефакт Земля")):
                self.mGroupColor.add_command(label="Небазовая земля",command=lambda:self.selectColGroup("nonbase"))
                break
        for v in allvals:
            if((v[6]=="Базовая") or (v[6]=="Базовая Снежная")):
                self.mGroupColor.add_command(label="Базовая земля",command=lambda:self.selectColGroup("base"))
                break
        
        for v in allvals:
            if((v[7]=="Существо") or (v[7]=="Артефакт Существо") or (v[7]=="Чары Существо")):
                self.mGroupType.add_command(label="Существо",command=lambda:self.selectTypGroup("Существо"))
                break
        for v in allvals:
            if((v[7]=="Артефакт Земля") or (v[7]=="Земля")):
                self.mGroupType.add_command(label="Земля",command=lambda:self.selectTypGroup("Земля"))
                break
        vals=self.data.getAttributesList(7)
        if("Planeswalker" in vals):
            self.mGroupType.add_command(label="Planeswalker",command=lambda:self.selectTypGroup("Planeswalker"))
        if("Артефакт" in vals):
            self.mGroupType.add_command(label="Артефакт",command=lambda:self.selectTypGroup("Артефакт"))
        if("Волшебство" in vals):
            self.mGroupType.add_command(label="Волшебство",command=lambda:self.selectTypGroup("Волшебство"))
        if("Мгновенное заклинание" in vals):
            self.mGroupType.add_command(label="Мгновенное заклинание",command=lambda:self.selectTypGroup("Мгновенное заклинание"))
        if("Чары" in vals):
            self.mGroupType.add_command(label="Чары",command=lambda:self.selectTypGroup("Чары"))
        
        if(self.data.groupRar==""):
            self.mGroup.add_cascade(label="Редкость",menu=self.mGroupRare)
        if(self.data.groupSet==""):
            self.mGroup.add_cascade(label="Сет",menu=self.mGroupSet)
        if(self.data.groupCol==""):
            self.mGroup.add_cascade(label="Цвет",menu=self.mGroupColor)
        if(self.data.groupTyp==""):
            self.mGroup.add_cascade(label="Тип",menu=self.mGroupType)
        self.mGroup.add_command(label="Сброс",command=self.clearGroup)
        
    def selectRarGroup(self,name):
        self.groupRarity.set(name)
        self.filterData()
    def selectSetGroup(self,name):
        self.groupSet.set(name)
        self.filterData()
    def selectColGroup(self,name):
        self.groupColor.set(name)
        self.filterData()
    def selectTypGroup(self,name):
        self.groupType.set(name)
        self.filterData()
    def clearGroup(self):
        self.groupRarity.set("")
        self.groupSet.set("")
        self.groupColor.set("")
        self.groupType.set("")
        self.filterData()