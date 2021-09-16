"""
Player object on the Server Side
"""
from .game import Game


class Player(object):
    def __init__(self, ip, name):
        """
        init the Player object
        :param ip: str
        :param name: str
        """
        self.game = None
        self.ip = ip
        self.name = name
        self.score = 0

    def set_game(self, game):
        """
        Sets the players Games association
        :param game: Game
        :return: None
        """
        self.game = game

    def update_score(self, x):
        """
        Updates a players score
        :param x: int
        :return: None
        """
        self.score += x

    def guess(self, wrd):
        """
        Makes a player guess
        :param wrd: str
        :return: bool
        """
        return self.game.player_guess(self, wrd)

    def disconnect(self):
        """
        Call to disconnect player
        :return:
        """
        pass

    def get_ip(self):
        """
        Returns the ip
        :return: ip
        """
        return self.ip

    def get_name(self):
        """
        Returns the player name
        :return: str
        """
        return self.name

    def get_score(self):
        """
        Returns the player scorer
        :return: int
        """
        return self.score
