from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk

class DataTree(ttk.Treeview):
    def __init__(self,mstr):
        super().__init__(mstr,columns=("Numero","Name","SetName","Number","Rarity","Quantity","Foil"),show="headings")        
        self.heading("Numero",text="№ п/п")
        self.column("Numero",width=50,stretch=False,anchor="center")
        self.heading("Name", text="Название",command=lambda: self.sort(1, False))
        self.heading("SetName", text="Сет",command=lambda: self.sort(2, False))
        self.heading("Number", text="Номер",command=lambda: self.sort(3, False))
        self.column("Number",width=50,stretch=False,anchor="center")
        self.heading("Rarity", text="Редкость")
        self.column("Rarity",width=75,stretch=False,anchor="center")
        self.heading("Quantity", text="Количество")
        self.column("Quantity",width=80,stretch=False,anchor="center")
        self.heading("Foil", text="Foil")
        self.column("Foil",width=50,stretch=False,anchor="center")                    
    
    def sort(self,column,reverse):
        data=self.master.master.data.getFilteredData()
        data.sort(reverse=reverse,key=lambda k:k[column])
        self.master.master.currentData=data
        self.fillTree(data)
        self.heading(column, command=lambda: self.sort(column, not reverse))
    
    def fillTree(self,data):
        tabdata=list()
        i=1
        for v in data:
            tabdata.append((i,)+v[1:6]+v[17:18])
            i+=1
        for r in self.get_children():
            self.delete(r)
        i=1
        for v in tabdata:
            self.insert("", END,iid=i, values=v)
            i+=1
            
class ImageForm(Toplevel):
    def __init__(self,title,path):
        super().__init__()
        self.title=title
        img=Image.open(path)
        self.geometry("350x500")
        self.resizable(False,False)    
        self.imgLabel=ttk.Label(self)
        self.imgLabel.pack(anchor="center",expand=True)
        self.img=ImageTk.PhotoImage(img)
        self.imgLabel.config(image=self.img)
        
class FilterForm(Toplevel):
    def __init__(self,mstr):
        super().__init__()        
        self.master=mstr
        self.initWindow()
        self.initFilters()
        
    def initWindow(self):
        self.title("Фильтры")
        self.minsize(500,620)
        self.resizable(False,False)
    
    def initFilters(self):
        self.setFilter=CBoxFilter(self,"Сет:",self.master.setVar,self.master.setNonVar,self.master.data.getAttributesList(2),0)
        self.rarityFilter=CBoxFilter(self,"Редкость:",self.master.rarityVar,self.master.rarityNonVar,self.master.data.getAttributesList(4),4)
        self.superTypeFilter=CBoxFilter(self,"Супертип:",self.master.superTypeVar,self.master.superTypeNonVar,self.master.data.getAttributesList(6),8)
        self.typeFilter=CBoxFilter(self,"Тип:",self.master.typeVar,self.master.typeNonVar,self.master.data.getAttributesList(7),12)
        self.underTypeFilter=CBoxFilter(self,"Подтип:",self.master.underTypeVar,self.master.underTypeNonVar,self.master.data.getAttributesList(8),16)
        self.statsFilter=StatsFilter(self,20,self.master.manaVar,self.master.strengthVar,self.master.enduranceVar,self.master.loyaltyVar)
        self.descriptionFilter=EntryFilter(self,"Описание:",self.master.descriptionVar,23)
        self.colorFilter=ColorsFilter(self,26,self.master.colorVar,self.master.imgpath)
        self.artistFilter=CBoxFilter(self,"Художник:",self.master.artistVar,self.master.artistNonVar,self.master.data.getAttributesList(15),28)
        self.designFilter=CBoxFilter(self,"Оформление:",self.master.designVar,self.master.designNonVar,self.master.data.getAttributesList(16),32)
                
        self.applyButton=ttk.Button(self,text="Применить",command=self.master.filterData)
        self.resetButton=ttk.Button(self,text="Сброс",command=self.resetFilter)
        self.blankLabel=ttk.Label(self,text=" ")
        self.blankLabel.grid(row=36,column=0,columnspan=5)
        self.applyButton.grid(row=37,column=3)
        self.resetButton.grid(row=37,column=4)

    def resetFilter(self):        
        if(self.colorFilter.whiteLabel.currentState):
            self.colorFilter.whiteLabel.imgSwap()
        if(self.colorFilter.blueLabel.currentState):
            self.colorFilter.blueLabel.imgSwap()
        if(self.colorFilter.blackLabel.currentState):
            self.colorFilter.blackLabel.imgSwap()
        if(self.colorFilter.redLabel.currentState):
            self.colorFilter.redLabel.imgSwap()
        if(self.colorFilter.greenLabel.currentState):
            self.colorFilter.greenLabel.imgSwap()
        if(self.colorFilter.noncolLabel.currentState):
            self.colorFilter.noncolLabel.imgSwap()
        self.master.clearFilters()
            
class CBoxFilter:
    def __init__(self,mstr,title,var,nonvar,vals,row):
        self.titleLabel=ttk.Label(mstr,text=title)
        self.filterLabel=ttk.Label(mstr,textvariable=var)
        self.filterNonLabel=ttk.Label(mstr,textvariable=nonvar)
        self.cbox=ttk.Combobox(mstr,values=vals,state="readonly",width=35)
        self.isButton=IsButton(mstr)
        self.addButton=AddButton(mstr,self.cbox,var,nonvar,self.isButton.nameState)
        self.clearButton=ClearButton(mstr,var,nonvar)
        self.titleLabel.grid(row=row,column=0,columnspan=5,sticky="w")
        self.filterLabel.grid(row=row+1,column=0,columnspan=5)
        self.filterNonLabel.grid(row=row+2,column=0,columnspan=5)
        self.cbox.grid(row=row+3,column=0)
        self.isButton.grid(row=row+3,column=2)
        self.addButton.grid(row=row+3,column=3)
        self.clearButton.grid(row=row+3,column=4)
        
class EntryFilter:
    def __init__(self,mstr,title,var,row):
        self.titleLabel=ttk.Label(mstr,text=title)
        self.filterLabel=ttk.Label(mstr,textvariable=var)
        self.filterEntry=ttk.Entry(mstr,width=35)
        self.addButton=AddButton(mstr,self.filterEntry,var,StringVar(),BooleanVar(value=True))
        self.clearButton=ClearButton(mstr,var,StringVar())
        self.titleLabel.grid(row=row,column=0,columnspan=5,sticky="w")
        self.filterLabel.grid(row=row+1,column=0,columnspan=5)
        self.filterEntry.grid(row=row+2,column=0)
        self.addButton.grid(row=row+2,column=3)
        self.clearButton.grid(row=row+2,column=4)

class StatsFilter:
    def __init__(self,mstr,row,*vars):
        self.titleLabel=ttk.Label(mstr,text="Характеристики:")
        self.filterFrame=ttk.Frame(mstr)
        self.manaLabel=ttk.Label(self.filterFrame,textvariable=vars[0])
        self.strengthLabel=ttk.Label(self.filterFrame,textvariable=vars[1])
        self.enduranceLabel=ttk.Label(self.filterFrame,textvariable=vars[2])
        self.loyaltyLabel=ttk.Label(self.filterFrame,textvariable=vars[3])
        self.cbox=ttk.Combobox(mstr,values=("Мана-стоимость","Сила","Выносливость","Верность"),state="readonly",width=35)
        self.compareButton=ttk.Button(mstr,text="=",command=self.onCompareButtonClick,width=5)
        self.valueEntry=ttk.Entry(mstr,width=8)
        self.addButton=ttk.Button(mstr,text="Добавить",command=self.onAddButtonClick)
        self.clearButton=ttk.Button(mstr,text="Очистить",command=self.onClearButtonClick)
        self.titleLabel.grid(row=row,column=0,columnspan=5,sticky="w")
        self.filterFrame.grid(row=row+1,column=0,columnspan=5)
        self.manaLabel.pack(side=LEFT)
        self.strengthLabel.pack(side=LEFT)
        self.enduranceLabel.pack(side=LEFT)
        self.loyaltyLabel.pack(side=LEFT)
        self.cbox.grid(row=row+2,column=0)
        self.compareButton.grid(row=row+2,column=1,padx=5)
        self.valueEntry.grid(row=row+2,column=2,padx=(0,5))
        self.addButton.grid(row=row+2,column=3)
        self.clearButton.grid(row=row+2,column=4)
        self.compareState=0
        self.compareVals=["=",">","<"]
        self.manavar=vars[0]
        self.strvar=vars[1]
        self.endvar=vars[2]
        self.loyvar=vars[3]
        
    def onCompareButtonClick(self):
        self.compareState=(self.compareState+1)%3
        self.compareButton.config(text=self.compareVals[self.compareState])
        
    def onAddButtonClick(self):  
              
        if(self.cbox.get()=="Мана-стоимость"):
            if(self.manavar.get()!=""):
                tmp=self.manavar.get()
                tmp+="|"+self.compareVals[self.compareState]+self.valueEntry.get()
                self.manavar.set(tmp)
            else:
                self.manavar.set(self.compareVals[self.compareState]+self.valueEntry.get())
        if(self.cbox.get()=="Сила"):
            if(self.strvar.get()!=""):
                tmp=self.strvar.get()
                tmp+="|"+self.compareVals[self.compareState]+self.valueEntry.get()
                self.strvar.set(tmp)
            else:
                self.strvar.set(self.compareVals[self.compareState]+self.valueEntry.get())
        if(self.cbox.get()=="Выносливость"):
            if(self.endvar.get()!=""):
                tmp=self.endvar.get()
                tmp+="|"+self.compareVals[self.compareState]+self.valueEntry.get()
                self.endvar.set(tmp)
            else:
                self.endvar.set(self.compareVals[self.compareState]+self.valueEntry.get())
        if(self.cbox.get()=="Верность"):
            if(self.loyvar.get()!=""):
                tmp=self.loyvar.get()
                tmp+="|"+self.compareVals[self.compareState]+self.valueEntry.get()
                self.loyvar.set(tmp)
            else:
                self.loyvar.set(self.compareVals[self.compareState]+self.valueEntry.get())
                
    def onClearButtonClick(self):
        self.manavar.set("")
        self.strvar.set("")
        self.endvar.set("")
        self.loyvar.set("")
        
class ColorsFilter:
    def __init__(self,mstr,row,var,path):
        self.titleLabel=ttk.Label(mstr,text="Цвет:")
        self.frame=ttk.Frame(mstr)
        self.titleLabel.grid(row=row,column=0,columnspan=5,sticky="w")
        self.frame.grid(row=row+1,column=0,columnspan=5,sticky="w")
        self.whiteLabel=ImgButton(self,"White",path)
        self.blueLabel=ImgButton(self,"Blue",path)
        self.blackLabel=ImgButton(self,"Black",path)
        self.redLabel=ImgButton(self,"Red",path)
        self.greenLabel=ImgButton(self,"Green",path)
        self.noncolLabel=ImgButton(self,"Noncolor",path)
        self.whiteLabel.pack(side=LEFT)
        self.blueLabel.pack(side=LEFT)
        self.blackLabel.pack(side=LEFT)
        self.redLabel.pack(side=LEFT)
        self.greenLabel.pack(side=LEFT)
        self.noncolLabel.pack(side=LEFT)
        self.colorVar=var
        
    def onColorButton(self):
        tmp=""
        if(self.whiteLabel.currentState):
            tmp+="White|"
        if(self.blueLabel.currentState):
            tmp+="Blue|"
        if(self.blackLabel.currentState):
            tmp+="Black|"
        if(self.redLabel.currentState):
            tmp+="Red|"
        if(self.greenLabel.currentState):
            tmp+="Green|"
        self.colorVar.set(tmp.rstrip("|"))
        if(self.noncolLabel.currentState):
            self.noncolLabel.imgSwap() 
                       
    def onNoncolorButton(self):
        tmp=""
        if(self.noncolLabel.currentState):
            tmp+="Noncolor"
        self.colorVar.set(tmp)
        if(self.whiteLabel.currentState):
            self.whiteLabel.imgSwap()
        if(self.blueLabel.currentState):
            self.blueLabel.imgSwap()
        if(self.blackLabel.currentState):
            self.blackLabel.imgSwap()
        if(self.redLabel.currentState):
            self.redLabel.imgSwap()
        if(self.greenLabel.currentState):
            self.greenLabel.imgSwap()

class IsButton(ttk.Button):
    def __init__(self,mstr):
        super().__init__(master=mstr,text="Является")
        self.nameState=BooleanVar(value=True)
        self.config(command=self.onButtonClick)
        
    def onButtonClick(self):
        if(self.nameState.get()):
            self.nameState.set(False)
            self.config(text="Не является")
        else:
            self.nameState.set(True)
            self.config(text="Является")

class AddButton(ttk.Button):
    def __init__(self,mstr,cb,var,nonvar,isbtnstate):
        super().__init__(master=mstr,text="Добавить")
        self.bindedCB=cb
        self.bindedVar=var
        self.bindedNonVar=nonvar
        self.bindedState=isbtnstate
        self.config(command=self.onButtonClick)
        
    def onButtonClick(self):
        if(self.bindedCB.get()!=""):
            if(self.bindedState.get()):
                if(self.bindedVar.get()!=""):
                    tmp=self.bindedVar.get()
                    tmp+="|"+self.bindedCB.get()
                    self.bindedVar.set(tmp)
                else:
                    self.bindedVar.set(self.bindedCB.get())
            else:
                if(self.bindedNonVar.get()!=""):
                    tmp=self.bindedNonVar.get()
                    tmp+="|"+self.bindedCB.get()
                    self.bindedNonVar.set(tmp)
                else:
                    self.bindedNonVar.set(self.bindedCB.get())

class ClearButton(ttk.Button):
    def __init__(self,mstr,var,nonvar):
        super().__init__(master=mstr,text="Очистить")
        self.bindedVar=var
        self.bindedNonVar=nonvar
        self.config(command=self.onButtonClick)
        
    def onButtonClick(self):
        self.bindedVar.set("")
        self.bindedNonVar.set("")
        
class ImgButton(ttk.Label):
    def __init__(self,mstr,text,path):
        super().__init__(master=mstr.frame)
        self.handler=mstr
        self.name=text
        self.path=path
        self.currentState=False
        self.image=PhotoImage(file=f"{self.path}Icons\\{self.name}T.png")
        self.config(image=self.image,cursor="hand2")
        self.bind("<Button-1>",self.onImgClick)
        
    def imgSwap(self):
        if(self.currentState):
            self.currentState=False
            self.image=PhotoImage(file=f"{self.path}Icons\\{self.name}T.png")
            self.config(image=self.image)
        else:
            self.currentState=True
            self.image=PhotoImage(file=f"{self.path}Icons\\{self.name}.png")
            self.config(image=self.image)
            
    def onImgClick(self,evt):
        self.imgSwap()
        if(evt.widget.name!="Noncolor"):
            self.handler.onColorButton()
        else:
            self.handler.onNoncolorButton()
            
class StatsForm(Toplevel):
    def __init__(self,mstr):
        super().__init__()
        self.master=mstr
        self.InitWindow()
        self.InitTables()
    def InitWindow(self):
        self.title("Статистика")
        self.minsize(500,950)
        self.resizable(False,False)
    def InitTables(self):
        self.sets=StatsTable(self,"Статистика по сетам","SELECT Setname, COUNT(*), SUM(Quantity) FROM WorkTable GROUP BY Setname;",self.master.data,3)
        self.rars=StatsTable(self,"Статистика по редкости","SELECT Rarity, COUNT(*), SUM(Quantity) FROM WorkTable GROUP BY Rarity;",self.master.data,2)
        self.suptyps=StatsTable(self,"Статистика по супертипам","SELECT SuperType, COUNT(*), SUM(Quantity) FROM WorkTable GROUP BY SuperType;",self.master.data,3)
        self.typs=StatsTable(self,"Статистика по типам","SELECT Type, COUNT(*), SUM(Quantity) FROM WorkTable GROUP BY Type;",self.master.data,3)
        self.undtyps=StatsTable(self,"Статистика по подтипам","SELECT UnderType, COUNT(*), SUM(Quantity) FROM WorkTable GROUP BY UnderType;",self.master.data,3)
        self.cols=StatsTable(self,"Статистика по цветам","SELECT Color, COUNT(*), SUM(Quantity) FROM WorkTable GROUP BY Color;",self.master.data,3)
        self.arts=StatsTable(self,"Статистика по художникам","SELECT Artist, COUNT(*), SUM(Quantity) FROM WorkTable GROUP BY Artist;",self.master.data,3)
        self.dsgs=StatsTable(self,"Статистика по оформлению","SELECT Design, COUNT(*), SUM(Quantity) FROM WorkTable GROUP BY Design;",self.master.data,3)
        self.foils=StatsTable(self,"Статистика по фойлу","SELECT Foil, COUNT(*), SUM(Quantity) FROM WorkTable GROUP BY Foil;",self.master.data,2)

class StatsTable:
    def __init__(self,mstr,tabname,request,data,height):
        self.lbl=ttk.Label(master=mstr,anchor="center",text=tabname)
        self.lbl.pack(side=TOP)
        self.frame=ttk.Frame(mstr)
        self.frame.pack(side=TOP)
        self.tree=StatsTree(self.frame,request,data,height)
        self.tree.pack(side=LEFT)
        self.treescroll=ttk.Scrollbar(self.frame,orient=VERTICAL,command=self.tree.yview)
        self.tree.configure(yscroll=self.treescroll.set)
        self.treescroll.pack(side=LEFT,fill=Y)

class StatsTree(ttk.Treeview):
    def __init__(self,mstr,request,data,height):
        super().__init__(master=mstr,columns=("Numer","Name","NoQuantity","Quantity"),show="headings",height=height)
        self.request=request
        self.heading("Numer",text="№ п/п")
        self.column("Numer",width=50,stretch=False,anchor="center")
        self.heading("Name",text="Наименование",command=lambda: self.sort(1, False))
        self.heading("NoQuantity",text="Без учета кол-ва",command=lambda: self.sort(2, False))
        self.column("NoQuantity",width=100,stretch=False,anchor="center")
        self.heading("Quantity",text="С учетом кол-ва",command=lambda: self.sort(3, False))
        self.column("Quantity",width=100,stretch=False,anchor="center")
        if(data.filter!=""):
            txt=request.replace("GROUP","WHERE "+data.filter+" GROUP")
        else:
            txt=request
        self.dbdata=data.getData(txt)
        self.refresh()
    def refresh(self):
        self.data=list()
        i=1
        for v in self.dbdata:
            self.data.append((i,)+v[:])
            i+=1
        for r in self.get_children():
            self.delete(r)
        for v in self.data:
            self.insert("",END,values=v)
    def sort(self,col,reverse):
        self.dbdata.sort(reverse=reverse,key=lambda k:k[col-1])
        self.refresh()
        self.heading(col, command=lambda: self.sort(col, not reverse))