"""
Represents a round of the game, storing things like word, time, skips, drawing player and more.
"""
import time as t
from _thread import *
from .game import Game
from .chat import Chat


class Round(object):

    def __init__(self, word, player_drawing, players):
        """
        init object
        :param word: str
        :param player_drawing: Player
        :param players: Player[]
        """
        self.word = word
        self.player_drawing = player_drawing
        self.player_guessed = []
        self.skips = 0
        self.players_scores = {player: 0 for player in players}
        self.time = 75
        self.chat = Chat(self)
        start_new_thread(self.time_thread, ())

    def time_thread(self):
        """
        Runs in a thread to keep track of time
        :return: None
        """
        while self.time > 0:
            t.sleep(1)
            self.time -= 1
        self.end_round("Time is up!")

    def guess(self, player, wrd):
        """
        :returns bool if player got guess correct
        :param player: Player
        :param wrd: str
        :return: bool
        """
        correct = wrd == self.word
        if correct:
            self.player_guessed.append(player)
            # TODO implement scoring system

    def player_left(self, player):
        """
        removes player that left from scores and list
        :param player: Player
        :return: None
        """
        # TODO
        if player in self.player_scores:
            del self.players_scores[player]

        if player in self.player_guessed:
            del self.player_guessed[player]

        if player == self.player_drawing:
            self.end_round("Drawing Player Left")

    def end_round(self, msg):
        # TODO implement end round functionality
        pass
