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
    def setLaboratory(self, laboratory):
        self.laboratory = laboratory

    def getLaboratory(self):
        return self.laboratory

    def getRecipes(self, superPot, extremePot):
        # Creating a dictionary for super potions
        superPotions = {
            "Super Attack": ["Irit", "Eye of Newt"],
            "Super Strength": ["Kwuarm", "Limpwurt Root"],
            "Super Defence": ["Cadantine", "White Berries"],
            "Super Magic": ["Lantadyme", "Potato Cactus"],
            "Super Ranging": ["Dwarf Weed", "Wine of Zamorak"],
            "Super Necromancy": ["Arbuck", "Blood of Orcus"]
        }

        # Creating a dictionary for extreme potions
        extremePotions = {
            "Extreme Attack": ["Avantoe", "Super Attack"],
            "Extreme Strength": ["Dwarf Weed", "Super Strength"],
            "Extreme Defence": ["Lantadyme", "Super Defence"],
            "Extreme Magic": ["Ground Mud Rune", "Super Magic"],
            "Extreme Ranging": ["Grenwall Spike", "Super Ranging"],
            "Extreme Necromancy": ["Ground Miasma Rune", "Super Necromancy"]
        }

        if superPot in superPotions:
            return superPotions[superPot]
        elif extremePot in extremePotions:
            return extremePotions[extremePot]
        else:
            return "Not a known Recipe"


    def setRecipe(self, recipeSet):
        if isinstance(recipeSet, (str)):
            self.__recipeSet = recipeSet
        else:
            raise ValueError("Recipe must be a string value")

    # Implementing an if statement setter method to make sure that potions not with no recipe can not be made
    def mixPotion(self, recipe):
        if recipe in self.recipes:
            potion = self.laboratory.mixPotion(recipe)
            return potion
        else:
            return "Mix not found"

    def drinkPotion(self):
        def drinkPotion(potion):
            # check if it is an instance of the potion class and pass one parameter potion
            if isinstance(potion, Potion):
                #if it is an instance of the potion class then getName and getBoost are called
                return f"Potion: {potion.getName()} Gives: {potion.getBoost()} boost."
            else:
                return "Invalid potion."

    def collectReagent(self, reagent, amount):
        # if the instance is in Reagent and the amount is greater then zero
        if isinstance(reagent, Reagent) and isinstance(amount, int) and amount > 0:
            # Perform operations on the Reagent object based on the amount
            reagent.setAmount(amount)

            # this adds the reagent to the lab
            self.laboratory.addReagent(reagent, amount)
            return f"{amount} of {reagent.getName()} reagent have been added to the laboratory."
        else:
            return "Invalid reagent or amount."


    def refineReagents(self, reagent):
        self.laboratory.refineReagents()
        return reagent


class Laboratory():
    def __init__(self):
        # storing potions and reagents
        self.reagents = []
        self.potions = []

    def mixPotion(self, alchemist, recipe):
        # Assuming mixPotion function in Laboratory requires Alchemist object and a recipe
        if recipe in alchemist.getRecipes():
            potion = alchemist.mixPotion(recipe)
            self.potions.append(potion)
            return f"{recipe} has been Mixed."
        else:
            return "Mix not found"

    def addReagent(self, reagent, amount):
        for reagents in range(amount):
            self.reagents.append(reagent)
        return f"{amount} of {reagent.getName()} have been successfully added to the lab."


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
        return self.boost

    def setBoost(self, boostNew):
        self.boost = boostNew


class Reagent():
    def __init__(self):
        pass

    def refine(self):
        pass

    def getName(self):
        pass

    def getPotency(self, herbType, catalystType):
        # dictionary with all herb values
        herb = {"Airbuck": 2.6,
                "Avantoe": 3.0,
                "Cadantine": 1.5,
                "Dwarf Weed": 2.5,
                "Irit": 1.0,
                "Kwuarm": 1.2,
                "Lantadyme": 2.0,
                "Torstol": 4.5,
                }
        # Dictionary for all catalysts and their given value as a tuple
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
        # Returns the specific reagent and their key value pair from the dictionary
        if herbType in herb:
            return herb[herbType]
        elif catalystType in catalysts:
            return catalysts[catalystType][0]
        else:
            return "Not a known Reagent"

    def setPotency(self, potencyVal):
        if isinstance(potencyVal, (int, float)):
            self.__potency = potencyVal
        else:
            raise ValueError("Potency must be a number value")



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
