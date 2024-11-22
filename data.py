import sqlite3

class MTGData:
    def __init__(self,path):
        self.db=sqlite3.connect(path)
        self.curs=self.db.cursor()
        self.filter=""
        self.defaultRequest="SELECT * FROM WorkTable"
        self.searchName=""
        self.filterSet="!"
        self.filterRar="!"
        self.filterSuptyp="!"
        self.filterTyp="!"
        self.filterUndtyp="!"
        self.filterMana=""
        self.filterStr=""
        self.filterEnd=""
        self.filterLoy=""
        self.filterDescr=""
        self.filterCol=""
        self.filterArt="!"
        self.filterDesign="!"
        self.groupSet=""
        self.groupRar=""
        self.groupTyp=""
        self.groupCol=""
        
    def getData(self,request):
        self.curs.execute(request)
        return self.curs.fetchall()
    
    def getAllData(self):
        return self.getData(self.defaultRequest)
    
    def getFilteredData(self):
        request=self.defaultRequest
        if self.filter!="":
            request+=" WHERE "+self.filter
        print(self.filter)
        return self.getData(request)
    
    def getOtherSideData(self,id):
        return self.getData(f"SELECT * FROM OtherSide WHERE DoubleSideID={id}")
    
    def getAttributesList(self,index):
        
        """
        ## indexes:        
        0 - Image | 1 - Name | 2 - Set | 3 - Number | 4 - Rarity | 5 - Quantity        
        6 - SuperType | 7 - Type | 8 - UnderType | 9 - ManaCost | 10 - Strength        
        11 - Endurance | 12 - Loyalty | 13 - Description | 14 - Color | 15 - Artist        
        16 - Design | 17 - Foil | 18 - DoubleSideID
        """
        
        request=self.defaultRequest
        if self.filter!="":
            request+=" WHERE "+self.filter
        values=list()
        tmp=set()
        for v in self.getData(request):
            if(v[index]!=None):
                tmp.add(v[index])
        for v in tmp:
            values.append(v)
        values.sort()
        values.insert(0,"")
        return values
    
    def updateFilter(self):
        self.filter=""
        if(self.searchName!=""):
            self.filter+="Name LIKE \'%"+self.searchName+"%\'"
        self.addInFilter("Artist",self.filterArt)
        self.addInFilter("Rarity",self.filterRar)
        self.addInFilter("SetName",self.filterSet)
        self.addInFilter("Design",self.filterDesign)
        self.addInFilter("SuperType",self.filterSuptyp)
        self.addInFilter("Type",self.filterTyp)
        self.addInFilter("UnderType",self.filterUndtyp)        
        if(self.filterDescr!=""):
            if(self.filter!=""):
                self.filter+=" AND "
            descrlist=self.filterDescr.split("|")
            for k in descrlist:
                self.filter+="Description LIKE \'%"+k+"%\' AND "
            self.filter=self.filter.rstrip(" AND ")
        self.addNumFilter("ManaCost",self.filterMana)
        self.addNumFilter("Strength",self.filterStr)
        self.addNumFilter("Endurance",self.filterEnd)
        self.addNumFilter("Loyalty",self.filterLoy)
        self.addSingleFilter("Color",self.filterCol)
        self.addSingleFilter("Rarity",self.groupRar)
        self.addSingleFilter("SetName",self.groupSet)
        if(self.groupCol!=""):
            if(self.filter!=""):
                self.filter+=" AND "
            if(self.groupCol=="multi"):
                self.filter+="Color LIKE \'%|%\'"
            elif(self.groupCol=="nonbase"):
                self.filter+="Type IN ('Земля','Артефакт Земля') AND (SuperType IS NULL OR SuperType NOT IN ('Базовая','Базовая Снежная'))"
            elif(self.groupCol=="base"):
                self.filter+="SuperType IN ('Базовая','Базовая Снежная')"
            else:
                self.filter+="Color =\'"+self.groupCol+"\'"
        if(self.groupTyp!=""):
            if(self.filter!=""):
                self.filter+=" AND "
            if(self.groupTyp=="Существо"):
                self.filter+="Type IN ('Существо','Артефакт Существо','Чары Существо')"
            elif(self.groupTyp=="Земля"):
                self.filter+="Type IN ('Земля','Артефакт Земля')"
            else:
                self.filter+="Type =\'"+self.groupTyp+"\'"
                
    def addInFilter(self,name,filter):
        tmp=filter.split("!")
        if(tmp[0]!=""):
            if(self.filter!=""):
                self.filter+=" AND "
            list=tmp[0].split("|")
            self.filter+=name+" IN ("
            for k in list:
                self.filter+=f"\'{k}\',"
            self.filter=self.filter.rstrip(",")
            self.filter+=")"
        if(tmp[1]!=""):
            if(self.filter!=""):
                self.filter+=" AND "
            list=tmp[1].split("|")
            self.filter+="("+name+" NOT IN ("
            for k in list:
                self.filter+=f"\'{k}\',"
            self.filter=self.filter.rstrip(",")
            self.filter+=") OR "+name+" IS NULL)"
            
    def addNumFilter(self,name,filter):
        if(filter!=""):
            if(self.filter!=""):
                self.filter+=" AND "
            list=filter.split("|")
            for k in list:
                self.filter+=name+" "+k+" AND "
            self.filter=self.filter.rstrip(" AND ")
            
    def addSingleFilter(self,name,filter):
        if(filter!=""):
            if(self.filter!=""):
                self.filter+=" AND "
            self.filter+=name+" =\'"+filter+"\'"