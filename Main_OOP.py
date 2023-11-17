'''
File: Main_OOP.py
Description: A brief description of this Python module.
Author: Nick Ikeeboh
StudentID: 11046
EmailID: Ikeno001
This is my own work as defined by the University's Academic Misconduct Policy.
'''


class Alchemist():
    # Initiating Alchemist Class Objects
    def __init__(self):
        self.attack = 0
        self.strength = 0
        self.defense = 0
        self.magic = 0
        self.necromancy = 0
        self.ranged = 0
        self.recipes = []
        self.laboratory = Laboratory()

    # defining alchemist Class Methods
    def getLaboratory(self):
        pass

    def getRecipes(self):
        pass

    # Implementing an if statement to make sure that potions not with no recipe can not be made
    def mixPotion(self, recipe):
        if recipe in self.recipes:
            potion = self.laboratory.mixPotion(recipe)
            return potion
        else:
            return "Recipe not found"

    def drinkPotion(self):
        pass

    def collectReagent(self):
        pass

    def defineReagents(self):
        pass


class Laboratory():
    def __init__(self):
        pass

    def mixPotion(self):
        pass

    def addReagent(self):
        pass


class Potion():

    def __init__(self):
        pass

    def calculateBoost(self):
        pass

    def getName(self):
        pass

    def getStat(self):
        pass

    def getBoost(self):
        pass

    def setBoost(self):
        pass


class Reagent():
    def __init__(self):
        pass

    def refine(self):
        pass

    def getName(self):
        pass

    def getPotency(self, herb, catalysts):
        herb = {"Airbuck": 2.6,
                "Avantoe": 3.0,
                "Cadantine": 1.5,
                "Dwarf Weed": 2.5,
                "Irit": 1.0,
                "Kwuarm": 1.2,
                "Lantadyme": 2.0,
                "Torstol": 4.5,
                }
        catalysts = {
            "Eye of Newt": (4.3, 1.0),
            "Limpwurt Root": (3.6, 1.7),
            "White Berries": (1.2, 2.0),
            "Potato Cactus": (7.3, 0.1),
            "Wine of Zamorak": (1.7, 5.0),
            "Blood of Orcus": (4.5, 2.2),
            "Ground Mud Rune": (2.1, 6.7),
            "Grenwall Spike": (6.3, 4.9),
            "Ground Miasma Rune": (3.3, 5.2)
        }

    def setPotency(self):
        pass


class SuperPotion(Potion):
    def __init__(self, name, stat):
        super().__init__(name, stat)
        pass

    def calculateBoost(self):
        pass

    def getHerb(self):
        pass

    def getCatalyst(self):
        pass


class ExtremePotion(Potion):
    def __init__(self):
        super().__init__()
        pass

    def calculateBoost(self):
        pass

    def getReagent(self):
        pass

    def getPotion(self):
        pass


class Herb(Reagent):
    def __init__(self):
        super().__init__()
        pass

    def refine(self):
        pass

    def getGrimy(self):
        pass

    def setGrimy(self):
        pass


class Catalyst(Reagent):
    def __init__(self):
        super().__init__()
        pass

    def refine(self):
        pass

    def getQuality(self):
        pass
