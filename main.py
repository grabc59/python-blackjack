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
            cards_to_deal.append(random.choice(self.cards))
        return cards_to_deal


# track
# class Hand:
#     # Hand class
#     # Initially contains 2 random cards from the deck
#     def __init__(self):
#         # add card twice


class Player:
    # Player class
    def __init__(self, name):
        self.bank = 100
        self.hand = []
        self.name = name

    # hit function
    def hit(self, deck, qty=1):
        # add a card to the hand, call deck.deal
        cards_delt = deck.deal(qty)
        for i in cards_delt:
            self.hand.append(i)

    # stand function
    def stand(self):
        pass

    # bet function

    # track each players money


class Game:
    # Game class. A place for miscellaneous methods related to the game.
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
                    f'~~ Who\'s in? (type one player at a time)')
            else:
                # to add more players...
                new_player_name = input(f'~~ Anyone else? (type "no", if not)')
            # exit player input prompt
            if new_player_name == "no":
                break
            elif len(new_player_name) == 0:
                continue
            else:
                # add the entered player name to the player list
                new_player = Player(new_player_name)
                self.player_list.append(new_player)
            print(self.get_player_names(self.player_list))

        # add the dealer last
        dealer = Player("dealer")
        self.player_list.append(dealer)

    def print_player_hands(self):
        for player in self.player_list:
            print(
                f'{player.name} (${player.bank}) [{player.bet}]: {player.hand}')

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
                    print('Error - enter an integer amount to bet')
                    continue
                else:
                    new_bank_balance = player.bank - bet_input
                    if new_bank_balance >= 0:
                        player.bank = new_bank_balance
                        player.bet = bet_input
                        break
                    else:
                        print('Error - insufficient funds')
                        continue
            self.print_player_hands()

    def print_instructions(self):
        print('~~ Let\'s play Blackjack')
        print('~~ Closest to 21 wins. Ace is 1 or 11.')

    # deal two cards to each player
    def deal_loop(self):
        for player in self.player_list:
            player.hit(self.deck, 2)

    def reset(self):
        self.deck = Deck()
        for player in self.player_list:
            player.hand = []
            player.bet = 0

    def hit_or_stay_loop(self):
        for player in self.player_list:
            # say whose turn it is
            print(f'~~ {player.name}\'s turn')
            # need automated dealer logic
            # player can hit or stay
            # check if the user's hit/stay input is valid
            valid_move_choice = False
            while valid_move_choice == False:
                # prompt players for input, they can hit (get another card) or stay (take no more cards)
                player_move_choice = input('Stay (s) / Hit (h)')
                if player_move_choice == 's':
                    # stay
                    # move on to next player
                    valid_move_choice = True
                elif player_move_choice == 'h':
                    # hit
                    player.hit(self.deck, 1)
                    # add a card to this player's hand and move on to the next player
                    valid_move_choice = True
                    player.hit(self.deck, 1)
                else:
                    # unrecognized input
                    print(
                        f'~~ What was that? "{player_move_choice}?" Press "s" if you want to stay and not take any more cards. Press "h" if you want another card.')

    # main game loop

    def start(self):
        self.print_instructions()
        self.populate_players()
        # loop until an end condition is met
        while True:
            # set hands to bets to blank values to clear any previous rounds
            self.reset()
            self.deal_loop()
            self.print_player_hands()
            self.bets_loop()
            # loop through players to hit or stay
            self.hit_or_stay_loop()
            # calculate the player hand total
            # player turns ends here

            # place bets

            # break


this_game = Game()
this_game.start()
