import json
import requests


class DexParser:

    def parse(self):
        pass


class DexFileParser(DexParser):
    def __init__(self, file):
        self.file = file

    def parse(self):
        with open(self.file, 'r', encoding='utf-8') as f:
            return json.load(f)


class DexURLParser(DexParser):
    def __init__(self, url):
        self.url = url

    def parse(self):
        req = requests.get(self.url)
        if req.status_code == 200:
            return req.text
        else:
            return None