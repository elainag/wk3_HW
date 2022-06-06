from models.player import *


class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        Player.choice = ["rock", "paper", "scissors"]


def who_wins(player1, player2):
    if player1.choice == player2.choice:
        return None

    elif player1.choice == "rock" and player2.choice == "scissors":
        return player1

    elif player1.choice == "scissors" and player2.choice == "paper":
        return player2

    elif player1.choice == "paper" and player2.choice == "rock":
        return player1
