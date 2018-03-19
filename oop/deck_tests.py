from deck_of_cards import Card
from deck_of_cards import Deck
import unittest

class cardTest(unittest.TestCase):
	def setUp(self):
		self.card = Card("Hearts", 'A')

	def test_init(self):
		self.assertEqual(self.card.suit, "Hearts")
		self.assertEqual(self.card.value, "A")

	def test_repr(self):
		self.assertEqual(repr(self.card), "A of Hearts")

class deckTests(unittest.TestCase):
	def setUp(self):
		self.deck = Deck()

	def test_init(self):
		self.assertEqual(len(self.deck.cards), 52)
		self.assertIsInstance(self.deck.cards,list)

	def test_repr(self):
		self.assertEqual(repr(self.deck), "Deck of 52 cards")

	def test_count(self):
		self.assertEqual(self.deck.count(), 52)
		self.deck.cards.pop()
		self.assertEqual(self.deck.count(), 51)

	def test_dealcard(self):
		self.deck.deal_card()
		self.assertEqual(len(self.deck.cards), 51)
		
	def test_multipledeal(self):
		"""testing multiple draws"""
		hand = self.deck.deal_hand(10)
		self.assertEqual(len(self.deck.cards), 42)
		self.assertEqual(len(hand), 10)

	def test_toomanydeal(self):
		"""if too many cards are selected to draw only the remaining will be drawn"""
		remaining = len(self.deck.cards)
		hand = self.deck.deal_hand(100)
		self.assertFalse(self.deck.cards)
		self.assertEqual(len(hand), remaining)

	def test_nocardsleft(self):
		self.deck.deal_hand(len(self.deck.cards))
		with self.assertRaises(ValueError):
			self.deck._deal(1)

	def test_shufflefull(self):
		old = self.deck.cards.copy()
		self.assertIsNot(old, self.deck.shuffle())
		self.assertEqual(len(old), len(self.deck.shuffle()))

	def test_shuffle_not_full(self):
		self.deck.deal_card()
		with self.assertRaises(ValueError):
			self.deck.shuffle()


if __name__ == '__main__':
	unittest.main()