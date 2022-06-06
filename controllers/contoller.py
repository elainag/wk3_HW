from flask import render_template, request, redirect
from models.player import *
from models.game import who_wins, Game
from app import app


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/game")
def game_options():
    return render_template("game.html")


@app.route("/result", methods=["POST"])
def winner_is():
    player1 = Player("player1", request.form["player1.choice"])
    player2 = Player("player2", request.form["player2.choice"])
    winner = Game(player1, player2)
    return render_template("result.html", winner=winner)
