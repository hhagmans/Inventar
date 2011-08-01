import pygame, sys, random, copy
from pygame.locals import * 

schriftgroesse = 25

class Tasche ():
    
    def __init__(self,g1,g2,g3,g4):                                     # gx = Anzahl Zeilen von Beutel x
        self.inhalt = [Beutel(g1),Beutel(g2), Beutel(g3), Beutel(g4)]
     
    def einfuegen(self,item):                               # Einfuegen des Items an erste freie Stelle
        Nr = self.platzFinden(item)
        pos = self.inhalt[Nr].platzFinden(item,self.inhalt[Nr-1]) 
        self.inhalt[Nr-1].einfuegen(item,pos)
        
    def entfernen(self,Nr,pos):                             # Entfernen des Items an Position pos in Beutel Nr
        self.inhalt[Nr-1].entfernen(pos)
        
    def verschieben(self,altNr,neuNr,altpos,neupos):        # Verschieben des Items von altpos in Beutel altNr nach neupos in Beutel neuNr
        item = self.inhalt[altNr-1].getItem(altpos)
        self.inhalt[altNr-1].entfernen(altpos)
        self.inhalt[neuNr-1].einfuegen(item,neupos)
    
    def platzFinden(self,item):                             # Gibt ersten Beutel mit genug Platz zurueck
        pos = None
        i = 0
        if item.stapelbar == True:
            while pos == None and i < 4:
                pos = self.inhalt[i].enthalten(self.inhalt[i],item)
                i += 1
            if pos == None:
                i = 0
                while pos == None and i < 4:
                    pos = self.inhalt[i].platzFinden(item,self.inhalt[i])
                    i += 1
        else:
            while pos == None and i < 4:
                pos = self.inhalt[i].platzFinden(item,self.inhalt[i])
                i += 1
        return i
                
    def anzeigen(self):
        for beutel in self.inhalt:
            print "\n"
            liste = []
            i = 0
            for zeile in beutel.spalte:
                for i in range(0,5):
                    item = zeile [i]
                    if item <> 0:
                        if item.stapelbar:
                            Text = item.nachricht + " x%i" %item.anzahl
                        else:
                            Text = item.nachricht
                        liste.append(Text)
                    else:
                        liste.append(item)
                print liste
                liste = []
       
class Beutel ():
    
    def __init__(self,anzahl):
        self.anzahl = anzahl
        self.spalte = []
        for i in range(anzahl):
            zeile = [0,0,0,0,0,0,0,0,0]
            self.spalte.append(zeile)
    
    def getItem(self,pos):                              # gibt Item an pos aus
        return self.spalte [pos[0]][pos[1]]
     
    def enthalten(self,Beutel,item):                                # gibt Index des uebergebenen items in Beutel Nr zurueck
        i = 0
        for zeile in Beutel.spalte:
            for it in zeile:
                if it <> 0 and item.name == it.name:
                    return [i,Beutel.spalte[i].index(it)]
            i += 1
     
    def einf(self,item,pos):
        i = pos[0]
        i2 = pos[1]
        for it in item.spalte:
            for it2 in it:
                if it2 == 1:
                    self.spalte [i][i2] = item
                i2 += 1
            i += 1
            i2 = pos[1]
          
    def einfuegen(self,item,pos):                       # fuegt uebergebenes Item in pos ein
        if item.stapelbar == True:
            if self.enthalten(self,item) <> None:
                pos = self.enthalten(self,item)
                self.spalte [pos[0]][pos[1]].anzahl += 1
            else:
                self.einf(item,pos)
        else:
            self.einf(item,pos)
                
    def entfernen(self,pos):                            # entfernt Item an pos
        item = self.getItem(pos)
        if item.stapelbar == True:
            self.spalte [pos[0]][pos[1]].anzahl -= 1
        else:
            i = pos[0]
            i2 = pos[1]
            for it in item.spalte:
                for it2 in it:
                    if it2 == 1:
                        self.spalte [i][i2] = 0
                    i2 += 1
                i += 1
                i2 = 0
    
    def itemProbe(self,pos,item,Beutel):                       # ueberprueft, ob das Item an pos passt
        i = pos[0]
        i2 = pos[1]
        erg = True
        for zeile in item.spalte:
            for it in zeile:                         
                if it == 1 and erg == True:
                    try:
                        if Beutel.spalte [i][i2] <> 0:        
                            erg = False
                    except:
                        erg = False
                else:
                    i2 += 1
            if erg == True:
                i += 1
                i2 = pos[1]
        return erg
        
    def platzFinden(self,item,Beutel):                          # findet ersten freien Index, in den das Item passt
        i = 0
        i2 = 0
        gefunden = False
        if gefunden == False:                      
            for zeile in Beutel.spalte:
                if gefunden == False:
                    for it in zeile:
                        if it == 0 and gefunden == False:
                            gefunden = self.itemProbe([i,i2],item,Beutel)
                            if gefunden == False:
                                i2 += 1
                    if gefunden == False:
                        i += 1
                        i2 = 0
        if gefunden == True:
            return [i,i2]
    