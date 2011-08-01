import pygame, sys, random, Bag, Items
from pygame.locals import *

Tasche = Bag.Tasche(3,3,3,3)
item = Items.Schwert()
item2 = Items.Heiltrank()
item3 = Items.Axt()
item4 = Items.Dolch()
Tasche.einfuegen(item3)
Tasche.einfuegen(item)
Tasche.einfuegen(item)
Tasche.einfuegen(item)
Tasche.einfuegen(item)
Tasche.einfuegen(item2)
Tasche.einfuegen(item2)
Tasche.einfuegen(item4)
Tasche.anzeigen()