class Schwert():
    """ Erstellt ein Item vom Typ Schwert"""
    def __init__(self):
        self.ID = 0
        self.name = "Schwert"
        zeile1 = [1]
        zeile2 = [1]
        self.spalte = [zeile1,zeile2]
        self.stapelbar = False
        
        
class Dolch():
    """ Erstellt ein Item vom Typ Dolch"""    
    def __init__(self):
        self.ID = 0
        self.name = "Dolch"
        zeile1 = [1]
        self.spalte = [zeile1]
        self.stapelbar = False
    
class Axt():
    """ Erstellt ein Item vom Typ Axt"""    
    def __init__(self):
        self.ID = 0
        self.name = "Axt"
        zeile1 = [1,1]
        zeile2 = [0,1]
        zeile3 = [0,1]
        self.spalte = [zeile1,zeile2,zeile3]
        self.stapelbar = False
    
class Ruestung():
    """ Erstellt ein Item vom Typ Ruestung"""    
    def __init__(self):
        self.ID = 0
        self.name = "Ruestung"
        zeile1 = [1,1]
        zeile2 = [0,1]
        self.spalte = [zeile1,zeile2]
        self.stapelbar = False

            
class Hose():
    """ Erstellt ein Item vom Typ Hose"""    
    def __init__(self):
        self.ID = 0
        self.name = "Hose"
        zeile1 = [1]
        zeile2 = [1]
        self.spalte = [zeile1,zeile2]
        self.stapelbar = False
            
class Handschuhe():
    """ Erstellt ein Item vom Typ Handschuhe"""    
    def __init__(self):
        self.ID = 0
        self.name = "Handschuhe"
        zeile1 = [1]
        self.spalte = [zeile1]
        self.stapelbar = False
            
class Heiltrank():
    """ Erstellt ein Item vom Typ Heiltrank"""    
    def __init__(self):
        self.ID = 0
        self.name = "Heiltrank"
        zeile1 = [1]
        self.spalte = [zeile1]
        self.stapelbar = True
        self.anzahl = 1
        self.maxanzahl = 20
            
class Manatrank():
    """ Erstellt ein Item vom Typ Manatrank"""    
    def __init__(self):
        self.ID = 0
        self.name = "Manatrank"
        zeile1 = [1]
        self.spalte = [zeile1]
        self.stapelbar = True
        self.anzahl = 1
        self.maxanzahl = 20
            
class Schriftrolle():
    """ Erstellt ein Item vom Typ Schriftrolle"""    
    def __init__(self):
        self.ID = 0
        self.name = "Schriftrolle"
        zeile1 = [1]
        self.spalte = [zeile1]
        self.stapelbar = True
        self.anzahl = 1
        self.maxanzahl = 20