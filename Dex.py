from Pokemon import Pokemon
from DexParser import DexURLParser, DexFileParser
from enum import Enum


class FileType(Enum):
    FILE = 1
    URL = 2


class ImageFormat(Enum):
    PNG = 1
    JPG = 2


class Dex:
    def __init__(self, name, dexType: FileType, dexPath, spriteType: FileType, spritePath, spriteImageFormat: ImageFormat):
        """
        Initializes a Pokedex object.
        :param name: Name of the Pokemon game, such as Firered, or Radical Red 3.1.
        :param dexType: FileType enum for local File or URL.
        :param dexPath: Path to the pokedex file or URL, eg. "C:/Users/username/Desktop/pokedex.json" or "https://play.radicalred.net/data/pokedex.json"
        :param spriteType: FileType enum for local File or URL.
        :param spritePath: Path to the sprite folder or URL, eg. "C:/Users/username/Desktop/sprites/" or "https://play.radicalred.net/sprites/gen5/"
        :param spriteImageFormat: ImageFormat enum for PNG or JPG.
        """
        self.name = name
        self.dexType = dexType
        if self.dexType == FileType.FILE:
            self.parser = DexFileParser(dexPath)
        if self.dexType == FileType.URL:
            self.parser = DexURLParser(dexPath)
        self.spriteType = spriteType
        self.spritePath = spritePath
        self.spriteImageFormat = spriteImageFormat

        self.dex = {}
        self.setDex(self.parser.getData())

    def getMon(self, name):
        """
        Returns a Pokemon object from the current Pokedex matching a name.
        :param name: A string matching a Pokemon's name.
        :return: a Pokemon object.
        """

        name = name.lower()
        return self.dex[name]

    def getSprite(self, pokemon: Pokemon):
        """
        Returns a sprite path (URL or FilePath) from the current Pokedex matching a Pokemon object.
        Type (URL or FilePath) will depend on current Pokedex configuration.
        :param pokemon: A Pokemon object.
        :return: a sprite.
        """
        if self.spriteType == FileType.FILE:
            # TODO: Implement file path details.
            pass
        if self.dexType == FileType.URL:
            return self.spritePath + pokemon.name.lower() + "." + self.spriteImageFormat.name.lower()

    def getAll(self):
        """
        Prints all Pokemon objects in the current Pokedex.
        Mainly for debugging.
        """
        for entry in self.dex:
            print(entry)

    def setDex(self, dex):
        """
        Sets the current Pokedex to a list of Pokemon objects.
        :param dex: A list of Pokemon objects.
        """
        # Add Pokemon objects to dex from a list of Pokemon objects
        # Uses lowercase name as the key
        for entry in dex:
            self.dex[entry.key] = entry
