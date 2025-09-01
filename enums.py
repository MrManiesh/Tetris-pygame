# -*- coding: utf-8 -*-

from enum import Enum

class GameState(Enum):
    MENU = 1
    PLAYING = 2
    PAUSED = 3
    GAME_OVER = 4

class GameMode(Enum):
    CLASSIC = 1
    TIME_ATTACK = 2
    MARATHON = 3 