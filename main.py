# main.py
import random


class Deck:
    # Deck class
    # contains 52 cards, 2-10,J,Q,K,A of hearts, diamonds, clubs, spades
    # J,Q,K count for 10
    # A counts as either 1 or 11
    # this is pretty static, no inputs required
    def __init__(self):

        # these are the possible combinations that make up the deck
        self.card_components = {
            "suits": ["Diamonds", "Hearts", "Clubs", "Spades"],
            "values": [2, 3, 4, 5, 6, 7, 8, 9, "Jack", "Queen", "King", "Ace"]
        }

        self.create_cards()

    # create the cards in the deck based on the card components
    def create_cards(self):
        self.cards = []
        for i in self.card_components["suits"]:
            for j in self.card_components["values"]:
                self.cards.append([i, j])

    # return a list of cards to be dealt
    def deal(self, qty):
        cards_to_deal = []
        for i in range(qty):
            # pick a random card from the list of cards
            cards_to_deal.append(random.choice(self.cards))
        return cards_to_deal


class Hand:
    # Hand class
    # Initially contains 2 random cards from the deck
    def __init__(self, player):
        # add card twice
        self.player = player


class Player:
    # Player class
    def __init__(self, player_type, deck):
        self.bank = 100
        self.hand = []
        self.player_type = player_type
        # deal 2 cards to each player
        self.hit(deck, 2)

    # hit function
    def hit(self, deck, qty):
        # add a card to the hand, call deck.deal
        cards_delt = deck.deal(qty)
        for i in cards_delt:
            self.hand.append(i)

    # stand function
    def stand(self):
        pass

    # bet function

    # track each players money


# create a deck
our_deck = Deck()

# create players
dealer = Player("dealer", our_deck)
player1 = Player("human", our_deck)
player_list = [dealer, player1]

print('Let\'s play Blackjack')

# run the game until an end condition is met
while True:

    # prompt players for input, they can hit (get another card) or stay (take no more cards)

    # place bets

    for player in player_list:
        print(player.hand)

    break
