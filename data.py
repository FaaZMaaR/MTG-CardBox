import sqlite3

class MTGData:
    def __init__(self, path):
        self.db = sqlite3.connect(path)
        self.curs = self.db.cursor()
        self.filter = ""
        self.mainRequest = "\
            FROM \"card\"\
            LEFT JOIN \"set\" ON \"card\".\"set_id\" = \"set\".\"id\"\
            LEFT JOIN \"rarity\" ON \"card\".\"rarity_id\" = \"rarity\".\"id\"\
            LEFT JOIN \"supertype\" ON \"card\".\"stype_id\" = \"supertype\".\"id\"\
            LEFT JOIN \"type\" ON \"card\".\"type_id\" = \"type\".\"id\"\
            LEFT JOIN \"undertype\" ON \"card\".\"utype_id\" = \"undertype\".\"id\"\
            LEFT JOIN \"artist\" ON \"card\".\"artist_id\" = \"artist\".\"id\"\
            LEFT JOIN \"design\" ON \"card\".\"design_id\" = \"design\".\"id\"\
            LEFT JOIN \"card_color\" ON \"card\".\"id\" = \"card_color\".\"card_id\"\
            LEFT JOIN \"color\" ON \"card_color\".\"color_id\" = \"color\".\"id\"\
        "
        self.cardInfoRequest = """
            SELECT \"card\".\"name\",
            \"supertype\".\"name\", \"type\".\"name\", \"undertype\".\"name\",
            \"card\".\"manacost\", \"card\".\"strength\", \"card\".\"endurance\", \"card\".\"loyalty\",
            \"card\".\"description\",
            \"set\".\"short\", \"card\".\"number\"
            FROM \"card\"
            LEFT JOIN \"supertype\" ON \"card\".\"stype_id\" = \"supertype\".\"id\"
            LEFT JOIN \"type\" ON \"card\".\"type_id\" = \"type\".\"id\"
            LEFT JOIN \"undertype\" ON \"card\".\"utype_id\" = \"undertype\".\"id\"
            LEFT JOIN \"set\" ON \"card\".\"set_id\" = \"set\".\"id\"
        """
        self.otherSideInfoRequest = """
            SELECT \"other_side\".\"name\",
            \"supertype\".\"name\", \"type\".\"name\", \"undertype\".\"name\",
            \"other_side\".\"manacost\", \"other_side\".\"strength\", \"other_side\".\"endurance\", \"other_side\".\"loyalty\",
            \"other_side\".\"description\",
            \"set\".\"short\", \"other_side\".\"number\"
            FROM \"other_side\"
            LEFT JOIN \"supertype\" ON \"other_side\".\"stype_id\" = \"supertype\".\"id\"
            LEFT JOIN \"type\" ON \"other_side\".\"type_id\" = \"type\".\"id\"
            LEFT JOIN \"undertype\" ON \"other_side\".\"utype_id\" = \"undertype\".\"id\"
            LEFT JOIN \"set\" ON \"other_side\".\"set_id\" = \"set\".\"id\"
        """
        self.setRequest = """
            SELECT \"set\".\"name\"
            FROM \"set\"
            ORDER BY \"set\".\"name\" ASC;
        """
        self.rarityRequest = """
            SELECT \"rarity\".\"name\"
            FROM \"rarity\";
        """
        self.stypeRequest = """
            SELECT \"supertype\".\"name\"
            FROM \"supertype\";
        """
        self.typeRequest = """
            SELECT \"type\".\"name\"
            FROM \"type\";
        """
        self.utypeRequest = """
            SELECT \"undertype\".\"name\"
            FROM \"undertype\";
        """
        self.artistRequest = """
            SELECT \"artist\".\"name\"
            FROM \"artist\"\
            ORDER BY \"artist\".\"name\" ASC;
        """
        self.designRequest = """
            SELECT \"design\".\"name\"
            FROM \"design\";
        """
        self.searchName = ""
        self.filterSetIn = []
        self.filterSetEx = []
        self.filterRarityIn = []
        self.filterRarityEx = []
        self.filterStypeIn = []
        self.filterStypeEx = []
        self.filterTypeIn = []
        self.filterTypeEx = []
        self.filterUtypeIn = []
        self.filterUtypeEx = []
        self.filterArtistIn = []
        self.filterArtistEx = []
        self.filterDesignIn = []
        self.filterDesignEx = []
        self.filterManacostEq = []
        self.filterManacostGr = []
        self.filterManacostLess = []
        self.filterStrengthEq = []
        self.filterStrengthGr = []
        self.filterStrengthLess = []
        self.filterEnduranceEq = []
        self.filterEnduranceGr = []
        self.filterEnduranceLess = []
        self.filterLoyaltyEq = []
        self.filterLoyaltyGr = []
        self.filterLoyaltyLess = []
        self.filterDescription = []
        self.filterWhite = False
        self.filterBlue = False
        self.filterBlack = False
        self.filterRed = False
        self.filterGreen = False
        self.filterNoncolor = False
        self.groupSet = ""
        self.groupRarity = ""
        self.groupType = ""
        self.groupColor = ""
    
    def updateFilter(self):
        self.filter = ""
        
        if self.searchName != "":
            self.filter += "\"card\".\"name\" LIKE \'%" + self.searchName + "%\'"
        
        if self.groupSet == "":
            self.addInFil("\"set\".\"name\"", self.filterSetIn)
            self.addExFil("\"set\".\"name\"", self.filterSetEx)
        else:
            self.addSingleFil("\"set\".\"name\"", self.groupSet)
        
        if self.groupRarity == "":
            self.addInFil("\"rarity\".\"name\"", self.filterRarityIn)
            self.addExFil("\"rarity\".\"name\"", self.filterRarityEx)
        else:
            self.addSingleFil("\"rarity\".\"name\"", self.groupRarity)
        
        self.addInFil("\"supertype\".\"name\"", self.filterStypeIn)
        self.addExFil("\"supertype\".\"name\"", self.filterStypeEx)
        self.addInFil("\"type\".\"name\"", self.filterTypeIn)
        self.addExFil("\"type\".\"name\"", self.filterTypeEx)
        self.addInFil("\"undertype\".\"name\"", self.filterUtypeIn)
        self.addExFil("\"undertype\".\"name\"", self.filterUtypeEx)
        self.addInFil("\"artist\".\"name\"", self.filterArtistIn)
        self.addExFil("\"artist\".\"name\"", self.filterArtistEx)
        self.addInFil("\"design\".\"name\"", self.filterDesignIn)
        self.addExFil("\"design\".\"name\"", self.filterDesignEx)
        self.addEqFil("\"card\".\"manacost\"", self.filterManacostEq)
        self.addEqFil("\"card\".\"strength\"", self.filterStrengthEq)
        self.addEqFil("\"card\".\"endurance\"", self.filterEnduranceEq)
        self.addEqFil("\"card\".\"loyalty\"", self.filterLoyaltyEq)
        self.addGrFil("\"card\".\"manacost\"", self.filterManacostGr)
        self.addGrFil("\"card\".\"strength\"", self.filterStrengthGr)
        self.addGrFil("\"card\".\"endurance\"", self.filterEnduranceGr)
        self.addGrFil("\"card\".\"loyalty\"", self.filterLoyaltyGr)
        self.addLessFil("\"card\".\"manacost\"", self.filterManacostLess)
        self.addLessFil("\"card\".\"strength\"", self.filterStrengthLess)
        self.addLessFil("\"card\".\"endurance\"", self.filterEnduranceLess)
        self.addLessFil("\"card\".\"loyalty\"", self.filterLoyaltyLess)
        self.addSubstringFil("\"card\".\"description\"", self.filterDescription)
        self.addColorFil()
        if self.groupColor == "Белый":
            self.addSingleFil("\"color\".\"name\"", "White")
        if self.groupColor == "Синий":
            self.addSingleFil("\"color\".\"name\"", "Blue")
        if self.groupColor == "Черный":
            self.addSingleFil("\"color\".\"name\"", "Black")
        if self.groupColor == "Красный":
            self.addSingleFil("\"color\".\"name\"", "Red")
        if self.groupColor == "Зеленый":
            self.addSingleFil("\"color\".\"name\"", "Green")
        if self.groupColor == "Бесцветный":
            self.addNullFil("\"color\".\"name\"")
        if self.groupColor == "Небазовая земля":
            self.addNotSingleSubstringFil("\"supertype\".\"name\"", "Базовый")
            self.addSingleSubstringFil("\"type\".\"name\"", "Земля")
        if self.groupColor == "Базовая земля":
            self.addSingleSubstringFil("\"supertype\".\"name\"", "Базовый")
        if self.groupColor == "Фишка":
            self.addSingleSubstringFil("\"supertype\".\"name\"", "Фишка")
        if self.groupType == "Существо":
            self.addSingleSubstringFil("\"type\".\"name\"", "Существо")
        if self.groupType == "Земля":
            self.addSingleSubstringFil("\"type\".\"name\"", "Земля")
        if self.groupType == "Planeswalker":
            self.addSingleSubstringFil("\"type\".\"name\"", "Planeswalker")
        if self.groupType == "Волшебство":
            self.addSingleSubstringFil("\"type\".\"name\"", "Волшебство")
        if self.groupType == "Артефакт":
            self.addSingleSubstringFil("\"type\".\"name\"", "Артефакт")
        if self.groupType == "Мгновенное заклинание":
            self.addSingleSubstringFil("\"type\".\"name\"", "Мгновенное заклинание")
        if self.groupType == "Чары":
            self.addSingleSubstringFil("\"type\".\"name\"", "Чары")
        
    def clearFilter(self):
        self.filterSetIn = []
        self.filterSetEx = []
        self.filterRarityIn = []
        self.filterRarityEx = []
        self.filterStypeIn = []
        self.filterStypeEx = []
        self.filterTypeIn = []
        self.filterTypeEx = []
        self.filterUtypeIn = []
        self.filterUtypeEx = []
        self.filterArtistIn = []
        self.filterArtistEx = []
        self.filterDesignIn = []
        self.filterDesignEx = []
        self.filterManacostEq = []
        self.filterManacostGr = []
        self.filterManacostLess = []
        self.filterStrengthEq = []
        self.filterStrengthGr = []
        self.filterStrengthLess = []
        self.filterEnduranceEq = []
        self.filterEnduranceGr = []
        self.filterEnduranceLess = []
        self.filterLoyaltyEq = []
        self.filterLoyaltyGr = []
        self.filterLoyaltyLess = []
        self.filterDescription = []
        self.filterWhite = False
        self.filterBlue = False
        self.filterBlack = False
        self.filterRed = False
        self.filterGreen = False
        self.filterNoncolor = False
        self.updFilter()
        
    def clearGroup(self):
        self.groupSet = ""
        self.groupRarity = ""
        self.groupType = ""
        self.groupColor = ""
        self.updFilter()
            
    def addInFil(self, name, data):
        if len(data) > 0:
            if self.filter != "":
                self.filter += " AND "
            self.filter += name + " IN ("
            for k in data:
                self.filter += f"\'{k}\',"
            self.filter = self.filter.rstrip(",")
            self.filter += ")"
            
    def addExFil(self, name, data):
        if len(data) > 0:
            if self.filter != "":
                self.filter += " AND "
            self.filter += name + " NOT IN ("
            for k in data:
                self.filter += f"\'{k}\',"
            self.filter = self.filter.rstrip(",")
            self.filter += ")"
            
    def addEqFil(self, name, data):
        if len(data) > 0:
            if self.filter != "":
                self.filter += " AND "
            self.filter += "("
            for k in data:
                self.filter += f"{name} = {k} OR "
            self.filter = self.filter.rstrip(" OR ")
            self.filter += ")"
    
    def addGrFil(self, name, data):
        if len(data) > 0:
            if self.filter != "":
                self.filter += " AND "
            for k in data:
                self.filter += f"{name} > {k} AND "
            self.filter = self.filter.rstrip(" AND ")
    
    def addLessFil(self, name, data):
        if len(data) > 0:
            if self.filter != "":
                self.filter += " AND "
            for k in data:
                self.filter += f"{name} < {k} AND "
            self.filter = self.filter.rstrip(" AND ")
            
    def addSubstringFil(self, name, data):
        if len(data) > 0:
            if self.filter != "":
                self.filter += " AND "
            self.filter += "("
            for k in data:
                self.filter += f"{name} LIKE \'%{k}%\' OR "
            self.filter = self.filter.rstrip(" OR ")
            self.filter += ")"
            
    def addColorFil(self):
        if self.filterWhite or self.filterBlue or self.filterBlack or self.filterRed or self.filterGreen or self.filterNoncolor:
            if self.filter != "":
                self.filter += " AND "
            if self.filterNoncolor:
                self.filter += "\"color\".\"name\" IS NULL "
            else:
                colorList = ""
                if self.filterWhite:
                    if colorList != "":
                        colorList += ","
                    colorList += "\'White\'"
                if self.filterBlue:
                    if colorList != "":
                        colorList += ","
                    colorList += "\'Blue\'"
                if self.filterBlack:
                    if colorList != "":
                        colorList += ","
                    colorList += "\'Black\'"
                if self.filterRed:
                    if colorList != "":
                        colorList += ","
                    colorList += "\'Red\'"
                if self.filterGreen:
                    if colorList != "":
                        colorList += ","
                    colorList += "\'Green\'"
                self.filter += "\"color\".\"name\" IN (" + colorList + ") "
                
    def addSingleFil(self, name, filter):
        if filter != "":
            if self.filter != "":
                self.filter += " AND "
            self.filter += name + " = \'" + filter + "\'"
            
    def addNullFil(self, name):
        if self.filter != "":
            self.filter += " AND "
        self.filter += name + "IS NULL"
    
    def addSingleSubstringFil(self, name, filter):
        if self.filter != "":
            self.filter += " AND "
        self.filter += name + " LIKE \'%" + filter + "%\'"
        
    def addNotSingleSubstringFil(self, name, filter):
        if self.filter != "":
            self.filter += " AND "
        self.filter += "(" + name + " NOT LIKE \'%" + filter + "%\' OR " + name + " IS NULL)"
    
    def prepareMainRequest(self):
        request = self.mainRequest
        if self.filter != "":
            request += " WHERE " + self.filter
        request += " GROUP BY \"card\".\"id\" "
        colorCount = 0
        if self.filterWhite:
            colorCount += 1
        if self.filterBlue:
            colorCount += 1
        if self.filterBlack:
            colorCount += 1
        if self.filterRed:
            colorCount += 1
        if self.filterGreen:
            colorCount += 1
        if colorCount > 1:
            request += f"HAVING COUNT(DISTINCT \"color\".\"name\") = {colorCount}"
        if self.groupColor == "Многоцветный":
            if colorCount < 2:
                request += " HAVING"
            else:
                request += " AND"
            request += " COUNT(DISTINCT \"color\".\"name\") > 1"
        return request
    
    def fetchMainData(self):
        request = "SELECT \"card\".\"id\", \"card\".\"name\", \"set\".\"name\" AS \"setn\", \"card\".\"number\", \"rarity\".\"name\" AS \"rarn\", \"card\".\"quantity\", \"card\".\"foil\"" + self.prepareMainRequest()
        request += ";"
        print(request)
        self.curs.execute(request)
        return self.curs.fetchall()
    
    def fetchCardInfo(self, id):
        self.curs.execute(self.cardInfoRequest + " WHERE \"card\".\"id\" = " + str(id) + ";")
        result = self.curs.fetchall()
        self.curs.execute(self.otherSideInfoRequest + " WHERE \"other_side\".\"id\" = " + str(id) + ";")
        result += self.curs.fetchall()
        return result
    
    def fetchSetNames(self):
        self.curs.execute(self.setRequest)
        return self.curs.fetchall()
    
    def fetchRarityNames(self):
        self.curs.execute(self.rarityRequest)
        return self.curs.fetchall()
    
    def fetchStypeNames(self):
        self.curs.execute(self.stypeRequest)
        return self.curs.fetchall()
    
    def fetchTypeNames(self):
        self.curs.execute(self.typeRequest)
        return self.curs.fetchall()
    
    def fetchUtypeNames(self):
        self.curs.execute(self.utypeRequest)
        return self.curs.fetchall()
    
    def fetchArtistNames(self):
        self.curs.execute(self.artistRequest)
        return self.curs.fetchall()
    
    def fetchDesignNames(self):
        self.curs.execute(self.designRequest)
        return self.curs.fetchall()
    
    def fetchFilteredRarityNames(self):
        request = f"SELECT \"main\".\"rarn\" FROM (SELECT \"rarity\".\"name\" AS \"rarn\" {self.prepareMainRequest()}) AS \"main\" GROUP BY \"main\".\"rarn\";"
        self.curs.execute(request)
        return self.curs.fetchall()
    
    def fetchFilteredSetNames(self):
        request = f"SELECT \"main\".\"setn\" FROM (SELECT \"set\".\"name\" AS \"setn\" {self.prepareMainRequest()}) AS \"main\" GROUP BY \"main\".\"setn\" ORDER BY \"main\".\"setn\";"
        self.curs.execute(request)
        return self.curs.fetchall()
    
    def fetchFilteredColorsAndTypes(self):
        request = f"SELECT \"color\".\"name\", COUNT(DISTINCT \"color\".\"name\"), \"supertype\".\"name\", \"type\".\"name\" {self.mainRequest}"
        if self.filter != "":
            request += " WHERE " + self.filter
        request += " GROUP BY \"card\".\"id\""
        request += ";"
        self.curs.execute(request)
        return self.curs.fetchall()
    
    def fetchSetQuantity(self):
        request = f"SELECT \"main\".\"sn\", COUNT(*), SUM(\"main\".\"cq\") FROM (SELECT \"set\".\"name\" AS \"sn\", \"card\".\"quantity\" AS \"cq\" {self.prepareMainRequest()}) AS \"main\" GROUP BY \"main\".\"sn\""
        self.curs.execute(request)
        return self.curs.fetchall()
    
    def fetchRarityQuantity(self):
        request = f"SELECT \"main\".\"rn\", COUNT(*), SUM(\"main\".\"cq\") FROM (SELECT \"rarity\".\"name\" AS \"rn\", \"card\".\"quantity\" AS \"cq\" {self.prepareMainRequest()}) AS \"main\" GROUP BY \"main\".\"rn\""
        self.curs.execute(request)
        return self.curs.fetchall()
    
    def fetchSupertypeQuantity(self):
        request = f"SELECT \"main\".\"stn\", COUNT(*), SUM(\"main\".\"cq\") FROM (SELECT \"supertype\".\"name\" AS \"stn\", \"card\".\"quantity\" AS \"cq\" {self.prepareMainRequest()}) AS \"main\" GROUP BY \"main\".\"stn\""
        self.curs.execute(request)
        return self.curs.fetchall()

    def fetchTypeQuantity(self):
        request = f"SELECT \"main\".\"tn\", COUNT(*), SUM(\"main\".\"cq\") FROM (SELECT \"type\".\"name\" AS \"tn\", \"card\".\"quantity\" AS \"cq\" {self.prepareMainRequest()}) AS \"main\" GROUP BY \"main\".\"tn\""
        self.curs.execute(request)
        return self.curs.fetchall()
    
    def fetchUndertypeQuantity(self):
        request = f"SELECT \"main\".\"utn\", COUNT(*), SUM(\"main\".\"cq\") FROM (SELECT \"undertype\".\"name\" AS \"utn\", \"card\".\"quantity\" AS \"cq\" {self.prepareMainRequest()}) AS \"main\" GROUP BY \"main\".\"utn\""
        self.curs.execute(request)
        return self.curs.fetchall()
    
    def fetchColorQuantity(self):
        request = f"SELECT \"main\".\"cn\", COUNT(*), SUM(\"main\".\"cq\") FROM (SELECT \"color\".\"name\" AS \"cn\", \"card\".\"quantity\" AS \"cq\" {self.prepareMainRequest()}) AS \"main\" GROUP BY \"main\".\"cn\""
        self.curs.execute(request)
        return self.curs.fetchall()
    
    def fetchArtistQuantity(self):
        request = f"SELECT \"main\".\"an\", COUNT(*), SUM(\"main\".\"cq\") FROM (SELECT \"artist\".\"name\" AS \"an\", \"card\".\"quantity\" AS \"cq\" {self.prepareMainRequest()}) AS \"main\" GROUP BY \"main\".\"an\""
        self.curs.execute(request)
        return self.curs.fetchall()
    
    def fetchDesignQuantity(self):
        request = f"SELECT \"main\".\"dn\", COUNT(*), SUM(\"main\".\"cq\") FROM (SELECT \"design\".\"name\" AS \"dn\", \"card\".\"quantity\" AS \"cq\" {self.prepareMainRequest()}) AS \"main\" GROUP BY \"main\".\"dn\""
        self.curs.execute(request)
        return self.curs.fetchall()
    
    def fetchFoilQuantity(self):
        request = f"SELECT \"main\".\"fn\", COUNT(*), SUM(\"main\".\"cq\") FROM (SELECT \"card\".\"foil\" AS \"fn\", \"card\".\"quantity\" AS \"cq\" {self.prepareMainRequest()}) AS \"main\" GROUP BY \"main\".\"fn\""
        self.curs.execute(request)
        return self.curs.fetchall()
    
# WITH multi_color_cards AS (                           Это для дальнейшего решения проблемы сбора статистики по многоцветным картам
#     SELECT card_id
#     FROM card_color
#     GROUP BY card_id
#     HAVING COUNT(*) > 1
# )
# SELECT
#     c.name AS cn,
#     COUNT(DISTINCT cc.card_id) AS cards_count,
#     SUM(card.quantity) AS total_quantity
# FROM multi_color_cards mcc
# JOIN card_color cc ON mcc.card_id = cc.card_id
# JOIN color c ON cc.color_id = c.id
# JOIN card ON cc.card_id = card.id
# GROUP BY c.name;