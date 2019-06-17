class Hand:
    # Hand class
    def __init__(self):
        self.total = 0
        self.cards = []
        self.bet_amount = 0
        self.status = "standing"
        self.payout_multiplier = 1
        self.earnings = 0

    def set_bet(self, bet_amount):
        self.bet_amount = bet_amount

    def set_status(self, status):
        self.status = status

    def calculate_earnings(self):
        self.earnings = self.bet_amount * self.payout_multiplier

    def calculate_total(self):
        # pass
        # number of aces in this hand. Aces will be processed last, after the subtotal is calculated so that we can determine if the value should be 1 or 11.
        aces = 0
        ace_total = 0
        # subtotal of non-ace cards
        subtotal = 0
        for i in self.cards:
            card_value = i[1]
            if card_value == 'J' or card_value == 'Q' or card_value == 'K':
                subtotal += 10
            elif card_value == 'A':
                # save aces for calculation after the subtotal is known
                aces += 1
            else:
                subtotal += card_value

        # decide each ace value in this hand
        for _ in range(aces):
            if 11 + subtotal <= 21:
                ace_total += 11
            else:
                ace_total += 1

        self.total = ace_total + subtotal
