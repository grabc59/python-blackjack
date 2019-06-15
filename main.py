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
#   [ ] automate hit vs stay
#   [ ] skip bet
#   [ ] 1 card face down
# end conditions
#   [x] calculate player hand values
#   [ ] win = highest hand <= 21
#   [ ] multiple players can win if tied
#   [ ] lose = over 21 or lower than the highest hand that is <= 21
#   [ ] highest hand = win


this_game = Game()
this_game.start()
