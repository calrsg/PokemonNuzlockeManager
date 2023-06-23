import sys
from PyQt6 import QtWidgets, QtCore, QtGui
from DexParser import DexFileParser, DexURLParser

rrfile = DexFileParser('data/radicalred.json')
rrurl = DexURLParser('https://play.radicalred.net/data/pokedex.json')

# print(rrfile.parse())
# print(rrurl.parse())