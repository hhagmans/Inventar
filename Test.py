import pygame, sys, random, Bag, Items
from pygame.locals import *

Tasche = Bag.Tasche(3,3,3,3)
item = Items.Schwert()
item2 = Items.Heiltrank()
item3 = Items.Axt()
item4 = Items.Dolch()
item5 = Items.Ruestung()
Tasche.einfuegen(item3)
Tasche.einfuegen(item)
Tasche.einfuegen(item2)
Tasche.einfuegen(item2)
Tasche.einfuegen(item4)
Tasche.einfuegen(item5)
result = True
try:
    if Tasche.inhalt[0].spalte [0][0].name <> "Axt":
        result = False
    if Tasche.inhalt[0].spalte [0][1].name <> "Axt":
        result = False
    if Tasche.inhalt[0].spalte [0][2].name <> "Schwert":
        result = False
    if Tasche.inhalt[0].spalte [0][3].name <> "Heiltrank" and Tasche.inhalt[0].spalte [0][3].anzahl <> 2:
        result = False
    if Tasche.inhalt[0].spalte [0][4].name <> "Dolch":
        result = False
    if Tasche.inhalt[0].spalte [1][1].name <> "Axt":
        result = False
    if Tasche.inhalt[0].spalte [1][2].name <> "Schwert":
        result = False
    if Tasche.inhalt[0].spalte [2][1].name <> "Axt":
        result = False
except:
    result = False
print result