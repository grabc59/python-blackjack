# main.py
import random
from deck import Deck
from hand import Hand
from player import Player
from game import Game

# TODO:
# deck
#   [x] remove delt cards from the deck
# automated dealer logic
#   [ ] skip dealer bet
#   [ ] dealer doesn't show bet or bank
#   [ ] consider making the dealer separate from the player_list
#   [x] automate hit vs stay
#   [x] 1 card face down
# end conditions
#   [ ] player is removed if they lose their bet and have $0 in the bank
#   [ ] if all players are out of money (except the dealer) start the game over
#   [x] calculate player hand values
#   [x] win = highest hand <= 21
#   [x] player bank receives double their bet if they win
#   [x] lose = over 21 or lower than dealer
#   [x] player does not receive turns for the hand if they bust
# general
#   [ ] player hands are printed when necessary
#   [ ] press enter after prompts to proceed instead of timer

this_game = Game()
this_game.start()
