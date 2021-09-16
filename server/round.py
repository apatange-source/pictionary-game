"""
Represents a round of the game, storing things like word, time, skips, drawing player and more.
"""
import time as t
from _thread import *
from .game import Game
from .chat import Chat


class Round(object):

    def __init__(self, word, player_drawing, players, game):
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

    def skip(self):
        """
        Returns true if round skipped threshold is met
        :return: bool
        """
        self.skips += 1
        if self.skips > len(self.players) - 2:
            self.skips = 0
            return True

        return False

    def get_scores(self):
        """
        Returns all the Player Scores
        :return: dict{Player: int}
        """
        return self.players_scores

    def get_score(self, player):
        """
        Returns the Score of the `player`
        :param player: Player
        :return: int
        """
        if player in self.players_scores:
            return self.players_scores[player]
        else:
            raise Exception("Player not in Score list!")
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
