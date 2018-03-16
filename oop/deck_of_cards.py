class Card:

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"{self.value} of {self.suit}"


class Deck:

    def __init__(self):

        suits = ("Hearts", "Diamonds", "Clubs", "Spades")
        values = ("A", "2", "3", "4", "5", "6", "7",
                  "8", "9", "10", "J", "Q", "K")

        self.cards = [Card(suit, value) for suit in suits for value in values]

    def __repr__(self):
        return f"Deck of {len(self.cards)} cards"

    def count(self):
        return len(self.cards)

    def _deal(self, amount):

        if self.count() == 0:
            raise ValueError("All cards have been dealt")

        actual = min(amount, self.count())

        return [self.cards.pop(-1) for i in range(actual)]

    def deal_card(self):
        return self._deal(1)[0]

    def deal_hand(self, amount):
        return self._deal(amount)

    def shuffle(self):
        from random import shuffle

        if self.count() != 52:
            raise ValueError("Only full decks can be shuffled")

        self.cards = shuffle(self.cards)
        return self.cards

# just some tests
# my_deck = Deck()
# print(my_deck.cards)
# print(my_deck.deal_card())
# my_deck.deal_hand(48)
# #print(my_deck.shuffle())
# print(my_deck.deal_hand(4))
