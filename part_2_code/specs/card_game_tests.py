import unittest
from unittest import result
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    
    def setUp(self):
        self.card1 = Card('hearts', 1)
        self.card2 = Card('spades', 5)
        self.card_game = CardGame
        self.cards = [self.card1, self.card2]


    def test_check_for_ace(self):
        result = self.card_game.check_for_ace(self, self.card1)
        self.assertEqual(True, result)
    

    def test_check_for_ace_false(self):
        result = self.card_game.check_for_ace(self, self.card2)
        self.assertEqual(False, result)
    

    def test_highest_card(self):
        result = self.card_game.highest_card(self, self.card1, self.card2)
        self.assertEqual(self.card2, result)
    

    def test_highest_card_false(self):
        self.card3 = Card('hearts', 5)
        self.card4 = Card('spades', 1)
        result = self.card_game.highest_card(self, self.card3, self.card4)
        self.assertEqual(self.card3, result)

    def test_cards_total(self):
        result = self.card_game.cards_total(self, self.cards)
        self.assertEqual("You have a total of 6", result)