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
            "values": [2, 3, 4, 5, 6, 7, 8, 9, "J", "Q", "K", "A"]
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
        for _ in range(qty):
            # pick a random card from the list of cards
            random_card_index = random.randint(0, len(self.cards)-1)
            random_card = self.cards.pop(random_card_index)
            cards_to_deal.append(random_card)
        return cards_to_deal


class Hand:
    # Hand class
    def __init__(self):
        self.total = 0
        self.busted = False
        self.cards = []
        self.bet_amount = 0

    def set_bet(self, bet_amount):
        self.bet_amount = bet_amount

    def calculate_total(self):
        # pass
        # number of aces in this hand. Aces will be processed last, after the subtotal is calculated so that we can determine if the value should be 1 or 11.
        aces = 0
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

        if (aces * 11) + subtotal <= 21:
            self.total = (aces * 11) + subtotal
        else:
            self.total = (aces * 1) + subtotal


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


class Game:
    # Game class. A place for methods related to the game.
    def __init__(self):
        self.player_list = []

    # return a list of player names
    def get_player_names(self, player_list):
        player_names = []
        for player in player_list:
            player_names.append(player.name)
        return player_names

    # get user input on who's playing
    def populate_players(self):
        while True:
            if len(self.player_list) == 0:
                # if there are no players yet...
                new_player_name = input(
                    f'~~ Who\'s in? (type one player at a time) ')
            else:
                # to add more players...
                new_player_name = input(f'~~ Anyone else? [no] ')

            if len(new_player_name) == 0:
                # exit player input prompt
                break
            else:
                # add the entered player name to the player list
                new_player = Player(new_player_name)
                self.player_list.append(new_player)
            print('players: ', self.get_player_names(self.player_list))

        # add the dealer last
        dealer = Player("dealer")
        self.player_list.append(dealer)

    def print_player_hands(self):
        for player in self.player_list:
            print(
                f'{player.name} (${player.bank}) [{player.hand.bet_amount}]: {player.hand.cards} --> {player.hand.total}')

    def bets_loop(self):
        for player in self.player_list:
            # loop until the player enters a valid bet amount
            while True:
                # prompt for input for bet amount
                bet_input = input(f'{player.name}\'s bet: ')
                try:
                    # check if input is a number
                    bet_input = int(bet_input)
                except ValueError:
                    # return error if input was not a number
                    print('Error - enter an integer amount to bet')
                    continue
                else:
                    if bet_input <= 0:
                        print('Bet value must be greater than 0.')
                    else:
                        # if input was good, attempt to place bet
                        if player.place_bet(bet_input):
                            break
                        else:
                            print('Error - insufficient funds')
            self.print_player_hands()
        print('~~~~~~~~~~ End of bets loop ~~~~~~~~~~')

    def print_instructions(self):
        print('~~ Let\'s play Blackjack')
        print('~~ Closest to 21 wins. Ace is 1 or 11.')

    # deal two cards to each player
    def deal_loop(self):
        for player in self.player_list:
            player.hit(self.deck, 2)
        print('~~~~~~~~~~ End of deal loop ~~~~~~~~~~')

    def start_round(self):
        # prepare a new deck for the new round
        self.deck = Deck()
        # prepare a new blank hand for each player in the new round
        for player in self.player_list:
            player.new_hand()
        print('~~~~~~~~~~ new round ready ~~~~~~~~~~')

    def hit_or_stay_loop(self):
        for player in self.player_list:
            # say whose turn it is
            print(f'~~ {player.name}\'s turn')
            # player can hit or stay
            # check if the user's hit/stay input is valid
            self.print_player_hands()
            while True:
                # prompt players for input, they can hit (get another card) or stay (take no more cards)
                player_move_choice = input('Stay (s) / Hit (h) ')
                if player_move_choice == 's':
                    # stay
                    # move on to next player
                    break
                elif player_move_choice == 'h':
                    # hit
                    # add a card to this player's hand and move on to the next player
                    player.hit(self.deck)
                    print(player.hand.cards)
                    break
                else:
                    # unrecognized input
                    print(
                        f'~~ What was that? "{player_move_choice}?" Press "s" if you want to stay and not take any more cards. Press "h" if you want another card.')
        print('~~~~~~~~~~ End of hit/stay loop ~~~~~~~~~~')

    def start(self):
        # main game loop
        self.print_instructions()
        # prompt for player names
        self.populate_players()
        # loop until an end condition is met
        while True:
            # set hands to bets to blank values to clear any previous rounds
            self.start_round()
            self.deal_loop()
            # calculate the player hand total
            self.print_player_hands()
            # loop through players to place bets
            self.bets_loop()
            # loop through players to hit or stay
            self.hit_or_stay_loop()
            # player turns ends here
            break
        print('~~~~~~~~~~ End of round ~~~~~~~~~~')

# TODO:
# deck
#   [x] remove delt cards from the deck
# automated dealer logic
#   [ ] automate hit vs stay
#   [ ] skip bet
#   [ ] 1 card face down
# end conditions
#   [ ] calculate player hand values
#   [ ] win = highest hand <= 21
#   [ ] multiple players can win if tied
#   [ ] lose = over 21 or lower than the highest hand that is <= 21
#   [ ] highest hand = win


this_game = Game()
this_game.start()
