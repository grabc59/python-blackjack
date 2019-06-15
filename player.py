from hand import Hand


class Player:
    # Player class
    def __init__(self, name):
        self.bank = 100
        self.name = name

    def new_hand(self):
        # reset player hand values
        self.hand = Hand()

    # hit function
    def hit(self, deck, qty=1):
        # add a card to the hand
        cards_delt = deck.deal(qty)
        self.hand.cards.extend(cards_delt)
        self.hand.calculate_total()

    # bet function
    def place_bet(self, bet_input):
        new_bank_balance = self.bank - bet_input
        if new_bank_balance >= 0:
            self.bank = new_bank_balance
            self.hand.set_bet(bet_input)
            return True
        else:
            return False
