class Pokemon:

    def __init__(self, pokemon):
        self.key = pokemon["name"].lower()
        self.name = pokemon["name"]
        self.types = pokemon["types"]
        self.stats = pokemon["baseStats"]
        self.abilities = pokemon["abilities"]

    def __str__(self):
        return f"{self.name} \nTypes: {self.types} \nBase Stats: {self.stats} \nAbilities: {self.abilities}"
