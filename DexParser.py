import json
import requests
from Pokemon import Pokemon


class DexParser:

    def __init__(self, path):
        self.json = None
        self.path = path

    def _parse(self):
        pass

    def _jsonToPokemon(self):
        pass

    def getData(self):
        """
        Parses data from a json URL or file, and returns the data as a list of Pokemon objects.
        :return:
        """
        self._parse()
        return self._jsonToPokemon()


class DexFileParser(DexParser):

    def _parse(self):
        with open(self.path, 'r', encoding='utf-8') as f:
            self.json = json.load(f)

    def _jsonToPokemon(self):
        """
        Converts a json object to a Pokemon object
        :return: A list of Pokemon objects.
        """
        res = []
        for key, entry in self.json.items():
            p = Pokemon(entry)
            res.append(p)
        return res


class DexURLParser(DexParser):

    def _parse(self):
        req = requests.get(self.path)
        if req.status_code == 200:
            self.json = req.json()
        else:
            return None

    def _jsonToPokemon(self):
        """
        Converts a json object to a Pokemon object
        :return: A list of Pokemon objects.
        """
        res = []
        for key, entry in self.json.items():
            p = Pokemon(entry)
            res.append(p)
        return res
