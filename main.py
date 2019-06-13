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
    def __init__(self, name, deck):
        self.bank = 100
        self.hand = []
        self.name = name
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


class Game:
    # Game class. A place for miscellaneous methods related to the game.
    def __init__(self):
        self.deck = Deck()
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
            else:
                # add the entered player name to the player list
                new_player = Player(new_player_name, self.deck)
                self.player_list.append(new_player)
            print(self.get_player_names(self.player_list))

        # add the dealer last
        dealer = Player("dealer", self.deck)
        self.player_list.append(dealer)

    def print_player_hands(self):
        for player in self.player_list:
            print(f'{player.name}: {player.hand}')

    def start(self):
        while True:
            # initial display of hands
            self.print_player_hands()
            # start of turn
            for player in self.player_list:
                # say whose turn it is
                print(f'~~ {player.name}\'s turn')
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
                        # add a card to this player's hand and move on to the next player
                        valid_move_choice = True
                        player.hit(self.deck, 1)
                    else:
                        # unrecognized input
                        print(
                            f'~~ What was that? "{player_move_choice}?" Press "s" if you want to stay and not take any more cards. Press "h" if you want another card.')

                # calculate the player hand total
            # player turns ends here

            # place bets

            # break


this_game = Game()

# create players (now done in game.get_players)
# dealer = Player("dealer", this_game.deck)
# player1 = Player("human", this_game.deck)
# player_list = [dealer, player1]

print('~~ Let\'s play Blackjack')
print('~~ Closest to 21 wins. Ace is 1 or 11.')

this_game.populate_players()

# run the game until an end condition is met
this_game.start()
