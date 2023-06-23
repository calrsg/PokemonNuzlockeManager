import sys
from PyQt6 import QtWidgets, QtCore, QtGui
from Dex import Dex, FileType, ImageFormat
from Pokemon import Pokemon

dex = Dex("Radical Red 3.1", FileType.URL, 'https://play.radicalred.net/data/pokedex.json',
          FileType.URL, 'https://play.radicalred.net/sprites/gen5/', ImageFormat.PNG)

print(dex.getMon("DODUO-SEVII"))
print(dex.getSprite(dex.getMon("DODUO-SEVII")))
