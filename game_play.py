import random

from decouple import config

from game import play_game

money = config('MY_MONEY')

play_game(1000)