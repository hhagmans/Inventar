import pygame, sys, random, Bag2D, Items, copy
from pygame.locals import *

class Rechteck(pygame.sprite.Sprite):            
    """erstellt ein Rechteck uebergebener Groesse und Farbe an uebergebenem Ort"""
                                               
    def __init__(self,ort,groesse,farbe):
        pygame.sprite.Sprite.__init__(self)
        image_surface = pygame.surface.Surface(groesse)
        image_surface.fill(farbe)
        self.image = image_surface.convert() 
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = ort
        self.ort = ort
      
    def scroll(self, terrainPos):
        self.rect.centerx = self.ort[0] - terrainPos   
        
def create_map(beginn,ende):
    """erstellt Map mit bis zu 3 Items von Spalte beginn bis Spalte ende"""    
    
    items = pygame.sprite.Group() 
    orte = []                          
    for i in range(3):                 
        spalte = random.randint(beginn,ende)
        ort  = [spalte * 128 + 20, 570] 
        if not (ort in orte) and ort[0] > 45:        
            orte.append(ort)          
            item = Rechteck(ort, itemGroesse,itemFarbe)
            items.add(item)
    return items

def updateItems(map0, map1):
    """erstellt aus 2 Maps die aktuelle Map"""
    items = pygame.sprite.Group()      
    for it in map0:
        items.add(it)
    for it in map1:
        items.add(it)
    return items

def animate():
    """loescht den alten Bildschirm und zeichnet alles neu"""
    screen.fill([255, 255, 255])               
    pygame.display.update(items.draw(screen)) 
    screen.blit(spieler.image, spieler.rect)
    if inventarOn == True: 
        iAnzeigen()
    pygame.display.flip()

def iAnzeigen():
    """Inventar anzeigen"""
    texte = Tasche.anzeigen(inventarNr)
    abstandh = 100
    abstandv = 25
    textpos = [0,25]
    linienposh = [0,17]
    linienposv = [100,17]
    screen.blit(itemMenu.image, itemMenu.rect)
    if click == True and pos <> None and mousepos[1] <= 25 + 25 * taschengroesse:
        screen.blit(itemU.image, itemU.rect)
    screen.blit (texte [0][0],[0,0])
    del texte [0][0]
    pygame.draw.line(screen, (0, 0, 0), linienposh, (640,linienposh[1]))
    linienposh[1] += abstandv
    for zeile in texte:
        pygame.draw.line(screen, (0, 0, 0), linienposh, (640,linienposh[1]))
        for i in range(0,5):
            pygame.draw.line(screen, (0, 0, 0), (linienposv[0]-5,linienposv[1]), (linienposv[0]-5,(25 + 25 * taschengroesse)-9))
            linienposv[0] += abstandh
            text = zeile [i]
            textpos[0] += abstandh
            screen.blit(text,textpos)
        linienposv[0] += abstandh
        pygame.draw.line(screen, (0, 0, 0), (linienposv[0]-5,linienposv[1]), (linienposv[0]-5,(25 + 25 * taschengroesse)-9))
        textpos[1] += abstandv
        textpos[0] = 0
        linienposv[0] = 0
        linienposh[1] += abstandv
    
def getPos(pos):
    """ermittelt das Item mittels uebergebener Mausposition"""
    if pos [1] >25:                 
        x = (pos[0] - 100) / 100
        y = (pos[1] - 17) / 25
    try:
        if  Tasche.getItem(inventarNr-1,[y,x]) <> None:
            return [y,x]
        else:
            print "Kein Item vorhanden"
    except:
        print "Kein Item vorhanden"
        
    
def getPosV(neupos):
    """ermittelt das Item mittels uebergebener Mausposition fuer verschieben"""
    global pos
    altpos = copy.copy (pos)
    if neupos [1] >25: 
        x = (neupos[0] - 100) / 100
        y = (neupos[1] - 17) / 25
    if altpos [1] >25:
        xa = (altpos[0] - 100) / 100
        ya = (altpos[1] - 17) / 25
    try:
            return [y,x]
    except:
        print "Item bereits auf Slot"

def loeschen(pos):  
    """loescht uebergebenes Item aus aktuellem Beutel"""                           
    Tasche.entfernen(inventarNr-1,pos)
    
def verschieben(altpos,neupos):  
    """verschiebt uebergebenes Item von altem Beutel in aktuellen Beutel"""
    item = Tasche.getItem(altInventarNr-1,altpos)
    if item.stapelbar == True:
        Tasche.verschiebenS(altInventarNr,inventarNr,altpos,neupos)
    else:
        Tasche.verschieben(altInventarNr,inventarNr,altpos,neupos)

def inventarTest(Nr):
    """Test bei Inventarwechsel"""
    global inventarNr, click        
    if inventarOn == True:          
        inventarNr = Nr
        if inventarNr <> altInventarNr:
            click = False
        else: click = True
            
pygame.init()
screen = pygame.display.set_mode([640,640])
pygame.display.set_caption("2D Test")
uhr = pygame.time.Clock()
spieler = Rechteck([20,550],[20,40],[0,100,100])
spielergruppe = pygame.sprite.Group()
spielergruppe.add(spieler)
taschengroesse = 3
Tasche = Bag2D.Tasche(taschengroesse,taschengroesse,taschengroesse,taschengroesse)
itemFarbe = [255,0,0]
itemGroesse = [10,20]
itemUFarbe = [180,180,255]
itemUGroesse = [100,25]                         # Initialisierungen
itemMenuFarbe = [255,220,220]
itemMenuGroesse = [640,(25 + 25 * taschengroesse)-7]
itemMenu = Rechteck([0,0],itemMenuGroesse,itemMenuFarbe)
click = False
map_position = 0
mousepos = [0,0]
aktID = 0
pos = None
neupos = None
startmap = create_map(0, 4)
map0 = create_map(10, 14)
map1 = create_map(5, 9)
inventarOn = False
inventarNr = 1
altInventarNr = -1
activeMap = 0
items = updateItems(startmap, map1)
itemListe = ([Items.Schwert(),Items.Dolch(),Items.Axt(),
Items.Ruestung(),Items.Hose(),Items.Handschuhe(),Items.Heiltrank(),
Items.Manatrank(),Items.Schriftrolle()])
pygame.key.set_repeat(1,10)

while True:
    uhr.tick(30)    # Framerate
    for event in pygame.event.get():                    # Eingabehandling
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN:          
            if event.key == pygame.K_LEFT:        
                map_position -= 5
            elif event.key == pygame.K_RIGHT:
                map_position += 5
            elif event.key == pygame.K_1:
                inventarTest(1)
            elif event.key == pygame.K_2:
                inventarTest(2)                     # zwischen Beuteln wechseln
            elif event.key == pygame.K_3:
                inventarTest(3)
            elif event.key == pygame.K_4:
                inventarTest(4)
            elif event.key == pygame.K_i:           # Inventar anzeigen
                if inventarOn == False:
                    inventarOn = True
                else: inventarOn = False
            elif event.key == pygame.K_e:           # gewaehltes Item entfernen
                if inventarOn == True:
                    try:
                        loeschen(pos)
                        pos = None
                    except:
                        print "Kein Item ausgewaehlt"
            elif event.key == pygame.K_v:           # gewaehltes Item in akt. Beutel verschieben
                if inventarOn == True:
                    #try:
                        mousepos = pygame.mouse.get_pos()
                        neupos = getPosV(mousepos)
                        verschieben(pos,neupos)
                        pos = None
                        neupos = None
                    #except:
                     #   print "Kein Item ausgewaehlt"
        if event.type == pygame.MOUSEBUTTONDOWN:
            if inventarOn == True:                 
                click = True                        # bei Mausklick Item waehlen
                mousepos = pygame.mouse.get_pos()
                upos = [((mousepos[0] / 100) * 100)-5,((mousepos[1]/ 25) *25)-7]
                if mousepos[1] > 17 and mousepos[0] >= 25 + 25 * taschengroesse:
                    itemU = Rechteck(upos,itemUGroesse,itemUFarbe)
                    pos = getPos(mousepos)
                else:
                    pos = None
                altInventarNr = inventarNr

                
    if map_position >=640 and activeMap == 0:
        activeMap = 1
        map0 = create_map(10, 14)
        items = updateItems(map0, map1)
    if map_position >=1280 and activeMap == 1:                        
        activeMap = 0                                   # Mapwechsel
        for it in map0:
            it.ort[0] = it.ort[0] - 1280   
        map_position = map_position - 1280
        map1 = create_map(5, 9)
        items = updateItems(map0, map1)
    
    for it in items:                       # Scrolling
        it.scroll(map_position)
        
    for it in items:
        items.remove(it)                   # Kollisionserkennung
        if pygame.sprite.spritecollide(it,spielergruppe,False):
            s = itemListe[random.randint(0,8)]
            s. ID = aktID
            aktID += 1
            Tasche.einfuegen(s)
        else:
            items.add(it)
    animate() # zeichnen