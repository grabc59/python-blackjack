from hand import Hand
import time


class Player:
    # Player class
    def __init__(self, name, type="normal player"):
        self.bank = 100
        self.name = name
        self.type = type

    def new_hand(self):
        # reset player hand values
        self.hand = Hand()

    # def stand(self):
    #     print(f'~~~~~~~~~~ {self.name} stands ~~~~~~~~~~')
    #     time.sleep(1.5)

    # hit function
    def hit(self, deck, qty=1):
        # add a card to the hand
        cards_delt = deck.deal(qty)
        self.hand.cards.extend(cards_delt)
        self.hand.calculate_total()
        self.check_hand_total()

    def check_hand_total(self):
        if self.hand.total > 21:
            print(f'~~~~~~~~~~ {self.name} busts! ~~~~~~~~~~')
            time.sleep(2)
            # bust
            self.hand.set_status("busted")
        elif self.hand.total == 21:
            print(f'~~~~~~~~~~ {self.name} got blackjack! ~~~~~~~~~~')
            time.sleep(1)
            self.hand.set_status("blackjack")
            time.sleep(2)

    def place_bet(self, bet_input):
        new_bank_balance = self.bank - bet_input
        if new_bank_balance >= 0:
            self.bank = new_bank_balance
            self.hand.set_bet(bet_input)
            return True
        else:
            return False
