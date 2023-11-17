'''
File: Main_OOP.py
Description: A brief description of this Python module.
Author: Nick Ikeeboh
StudentID: 110411406
EmailID: Ikeno001
This is my own work as defined by the University's Academic Misconduct Policy.
'''


import unittest

from Main_OOP import Alchemist, Laboratory, Potion, SuperPotion, ExtremePotion, Reagent, Herb, Catalyst

class TestAlchemist(unittest.TestCase):
    def tryAlchemist(self):
        self.alchemist = Alchemist()

    def test_alchemist_attributes(self):
        self.assertEqual(self.alchemist.attack, 0)


class TestLaboratory(unittest.TestCase):
    def tryLab(self):
        self.laboratory = Laboratory(Alchemist())

    def test_laboratory_initialization(self):
        self.assertIsInstance(self.laboratory.alchemist, Alchemist)


class TestPotion(unittest.TestCase):
    def tryPotion(self):
        self.potion = Potion("TestPotion", "TestStat", 10)

    def test_potion_attributes(self):
        self.assertEqual(self.potion.getStat(), "TestStat")


class TestReagent(unittest.TestCase):
    def tryReagent(self):
        self.herb = Herb("TestHerb", 5)
        self.catalyst = Catalyst("TestCatalyst", 7, 8)

    def test_reagent_attributes(self):
        self.assertEqual(self.herb.getPotency(), 5)
        self.assertEqual(self.catalyst.getQuality(), 8)
        # Test other attributes or methods of Reagent class and its subclasses




unittest.main()
