class Schwert():
    
    def __init__(self):
        self.ID = 0
        self.name = "Schwert"
        zeile1 = [1]
        zeile2 = [1]
        self.spalte = [zeile1,zeile2]
        self.stapelbar = False
        self.nachricht = "%s" %self.name
        
    def __str__(self):
        return self.name
        
class Dolch():
    
    def __init__(self):
        self.ID = 0
        self.name = "Dolch"
        zeile1 = [1]
        self.spalte = [zeile1]
        self.stapelbar = False
        self.nachricht = "%s" %self.name
    
    def __str__(self):
        return self.name
    
class Axt():
    
    def __init__(self):
        self.ID = 0
        self.name = "Axt"
        zeile1 = [1,1]
        zeile2 = [0,1]
        zeile3 = [0,1]
        self.spalte = [zeile1,zeile2,zeile3]
        self.stapelbar = False
        self.nachricht = "%s" %self.name
    
    def __str__(self):
        return self.name
    
class Ruestung():
    
    def __init__(self):
        self.ID = 0
        self.name = "Ruestung"
        zeile1 = [1,1]
        zeile2 = [0,1]
        self.spalte = [zeile1,zeile2]
        self.stapelbar = False
        self.nachricht = "%s" %self.name
    
    def __str__(self):
        return self.name
            
class Hose():
    
    def __init__(self):
        self.ID = 0
        self.name = "Hose"
        zeile1 = [1]
        zeile2 = [1]
        self.spalte = [zeile1,zeile2]
        self.stapelbar = False
        self.nachricht = "%s" %self.name
    
    def __str__(self):
        return self.name
            
class Handschuhe():
    
    def __init__(self):
        self.ID = 0
        self.name = "Handschuhe"
        zeile1 = [1]
        self.spalte = [zeile1]
        self.stapelbar = False
        self.nachricht = "%s" %self.name
    
    def __str__(self):
        return self.name
            
class Heiltrank():
    
    def __init__(self):
        self.ID = 0
        self.name = "Heiltrank"
        zeile1 = [1]
        self.spalte = [zeile1]
        self.stapelbar = True
        self.anzahl = 1
        self.maxanzahl = 20
        self.nachricht = "%s" %self.name
    
    def __str__(self):
        return self.name
            
class Manatrank():
    
    def __init__(self):
        self.ID = 0
        self.name = "Manatrank"
        zeile1 = [1]
        self.spalte = [zeile1]
        self.stapelbar = True
        self.anzahl = 1
        self.maxanzahl = 20
        self.nachricht = "%s" %self.name
    
    def __str__(self):
        return self.name
            
class Schriftrolle():
    
    def __init__(self):
        self.ID = 0
        self.name = "Schriftrolle"
        zeile1 = [1]
        self.spalte = [zeile1]
        self.stapelbar = True
        self.anzahl = 1
        self.maxanzahl = 20
        self.nachricht = "%s" %self.name
            
    def __str__(self):
        return self.name