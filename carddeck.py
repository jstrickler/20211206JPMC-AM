import random

class Card:
    def __init__(self, rank, suit):
        self._rank = rank
        self._suit = suit

    @property
    def rank(self):
        return self._rank

    @property
    def suit(self):
        return self._suit

    def __repr__(self):
        # Card('2', 'Spades')
        return f"Card('{self.rank}', '{self.suit}')"

    def __str__(self):
        return f"{self.suit}-{self.rank}"

class CardDeck:  #inherits from 'object'
    RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
    SUITS = 'Clubs Diamonds Hearts Spades'.split()

    def __init__(self, dealer):
        self._dealer = dealer
        self._make_deck()

    # getter methods
    # setter methods
    def _make_deck(self):
        self._cards = list()
        for suit in self.SUITS:
            for rank in self.RANKS:
                card = Card(rank, suit)
                self._cards.append(card)

    @property
    def cards(self):
        return self._cards

    @property
    def dealer(self):  # getter property
        return self._dealer

    @dealer.setter  # setter property
    def dealer(self, dealer):
        if isinstance(dealer, str):
            self._dealer = dealer
        else:
            bad_type = type(dealer).__name__
            raise TypeError(f"Dealer must be a string, not '{bad_type}'")

    # prop<TAB>
    @property
    def spam(self):
        return self._spam

    # props<TAB>
    @property
    def ham(self):
        return self._ham

    # self:python::this:java

    @ham.setter
    def ham(self, value):
        self._ham = value

    def draw(self):
        if len(self._cards) == 0:
            raise ValueError("No more cards")
        return self._cards.pop()

    def shuffle(self):
        random.shuffle(self._cards)

    def __repr__(self):  # interpreter
        my_class = type(self)
        my_name = my_class.__name__
        return f"{my_name}('{self.dealer}')"

    def __str__(self):  # eyeballs
        # CardDeck-Fred-47
        my_name = type(self).__name__
        return f"{my_name}-{self.dealer}-{len(self)}"

    def __len__(self):
        return len(self._cards)
