# main.py
import random
from deck import Deck
from hand import Hand
from player import Player
from game import Game

# TODO:
# deck
# automated dealer logic
#   [x] skip dealer bet
#   [x] dealer doesn't show bet or bank
#   [x] consider making the dealer separate from the player_list
#   [x] remove delt cards from the deck
#   [x] automate hit vs stay
#   [x] 1 card face down
# end conditions
#   [ ] if all players are out of money (except the dealer) start the game over
#   [x] player is removed if they lose their bet and have $0 in the bank
#   [x] calculate player hand values
#   [x] win = highest hand <= 21
#   [x] player bank receives double their bet if they win
#   [x] lose = over 21 or lower than dealer
#   [x] player does not receive turns for the hand if they bust
# general
#   [ ] if there are no players, restart the game. This could apply to if all players are eliminated, or if no players were initially entered
#   [ ] remove unnecessary enter to continue after bet input or hit input, this may only be necessary for dealer where this may go fast
#   [ ] is hand.get_hand actually showing any thing different than hand.cards()?
#   [x] notify player when they bust
#   [x] player hands are printed when necessary
#   [x] press enter after prompts to proceed instead of timer

this_game = Game()
this_game.start()
