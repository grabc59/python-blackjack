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
            # "suits": ["Diamonds", "Hearts", "Clubs", "Spades"],
            #  Diamonds: \u2666, Spades: \u2660, Hearts: \u2665, Clubs: \u2663
            "suits": [u"\u2666", u"\u2660", u"\u2665", u"\u2663"],
            "values": [2, 3, 4, 5, 6, 7, 8, 9, "J", "Q", "K", "A"]
        }

        self.create_cards()

    # create the cards in the deck based on the card components
    def create_cards(self):
        self.cards = []
        for i in self.card_components["suits"]:
            for j in self.card_components["values"]:
                self.cards.append({"suit": i, "value": j})
    # return a list of cards to be dealt

    def deal(self, qty):
        cards_to_deal = []
        for _ in range(qty):
            # pick a random card from the list of cards
            random_card_index = random.randint(0, len(self.cards)-1)
            random_card = self.cards.pop(random_card_index)
            cards_to_deal.append(random_card)
        return cards_to_deal
