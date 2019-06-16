from player import Player
from deck import Deck
import time


class Game:
    # Game class. A place for methods related to the game.
    def __init__(self):
        self.player_list = []
        self.pause_time = 2

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
                new_player_name = input(f'~~ Anyone else playing? [no] ')

            if len(new_player_name) == 0:
                # exit player input prompt
                break
            else:
                # add the entered player name to the player list
                new_player = Player(new_player_name)
                self.player_list.append(new_player)
            print('players: ', self.get_player_names(self.player_list))

        # add the dealer last
        dealer = Player("dealer", "dealer")
        self.player_list.append(dealer)

    def print_player_hands(self):
        for player in self.player_list:
            print(
                f'{player.name} (${player.bank}) [{player.hand.bet_amount}]: {player.hand.cards} --> {player.hand.total}')

    def bets_loop(self):
        for player in self.player_list:
            print(f'~~~~~~~~~~ {player.name}\'s turn to bet ~~~~~~~~~~')
            if player.type != "dealer":
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
            if player.type == "dealer":
                # deal only one card to the dealer (equivalent of the typical face down card)
                player.hit(self.deck)
            else:
                player.hit(self.deck, 2)
        print('~~~~~~~~~~ End of deal loop ~~~~~~~~~~')

    def start_round(self):
        # prepare a new deck for the new round
        self.deck = Deck()
        # prepare a new blank hand for each player in the new round
        for player in self.player_list:
            player.new_hand()
        print('~~~~~~~~~~ new round ready ~~~~~~~~~~')

    def hit_or_stand_loop(self):
        self.print_player_hands()
        for player in self.player_list:
            # say whose turn it is
            print(
                f'~~~~~~~~~~ {player.name}\'s turn to hit or stay ~~~~~~~~~~')
            if player.type == "dealer":
                # reveal the dealer's 'face down' card by dealing a card
                player.hit(self.deck)
                self.print_player_hands()
                time.sleep(self.pause_time)
                # dealer must hit up to at least 16
                while player.hand.total < 16:
                    player.hit(self.deck)
                    self.print_player_hands()
                    time.sleep(self.pause_time)
            else:
                # player can hit or stand
                # check if the user's hit/stand input is valid
                # prompt players for input, they can hit (get another card) or stand (take no more cards)
                # a player can hit until they bust or stand
                while player.hand.status == "standing":
                    player_move_choice = input('Stand (s) / Hit (h) ')
                    if player_move_choice == 's':
                        # stand
                        # move on to next player
                        break
                    elif player_move_choice == 'h':
                        # hit
                        # add a card to this player's hand
                        player.hit(self.deck)
                        self.print_player_hands()
                    else:
                        # unrecognized input
                        print(
                            f'~~ What was that? "{player_move_choice}?" Press "s" if you want to stand and not take any more cards. Press "h" if you want another card.')
            print(f'~~~~~~~~~~ End of {player.name}\'s turn ~~~~~~~~~~')
            self.print_player_hands()
        print('~~~~~~~~~~ End of hit/stand loop ~~~~~~~~~~')

    def make_payouts(self):
        dealer = self.player_list[-1]
        for player in self.player_list:
            # no need to compare the dealer to itself
            if player.type != "dealer":
                if dealer.hand.status == "busted":
                    # payout will be double the bet to each player still standing if the dealer is busted
                    if player.hand.status == "standing":
                        player.hand.payout_multiplier = 2
                elif dealer.hand.status == "standing" and player.hand.status == "standing":
                    if player.hand.total > dealer.hand.total:
                        # player wins double their bet
                        player.hand.payout_multiplier = 2
                    elif player.hand.total == dealer.hand.total:
                        # player keeps their bet amount in a tie with the dealer
                        pass
                    else:
                        # otherwise, the player must have a lower total than the dealer. They lose their bet
                        player.hand.payout_multiplier = 0
                # player loses their bet if they busted, no matter what
                if player.hand.status == "busted":
                    player.hand.multiplyer = 0
            player.bank += (player.hand.payout_multiplier *
                            player.hand.bet_amount)

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
            # loop through players to hit or stand
            self.hit_or_stand_loop()
            self.make_payouts()
            self.print_player_hands()

            break
        print('~~~~~~~~~~ End of round ~~~~~~~~~~')
