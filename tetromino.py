# -*- coding: utf-8 -*-

import random
from constants import TETROMINOS, TETROMINO_COLORS, GRID_WIDTH

class Tetromino:
    def __init__(self, shape_type):
        self.shape_type = shape_type
        self.rotation = 0
        self.x = GRID_WIDTH // 2 - 2
        self.y = 0
        self.shape = TETROMINOS[shape_type][self.rotation]
        self.color = TETROMINO_COLORS[shape_type]
    
    def rotate(self):
        self.rotation = (self.rotation + 1) % len(TETROMINOS[self.shape_type])
        self.shape = TETROMINOS[self.shape_type][self.rotation]
    
    def get_positions(self):
        positions = []
        for i, row in enumerate(self.shape):
            for j, cell in enumerate(row):
                if cell == '#':
                    positions.append((self.x + j, self.y + i))
        return positions
    
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
    
    def reset_position(self):
        self.x = GRID_WIDTH // 2 - 2
        self.y = 0
    
    def copy(self):
        new_piece = Tetromino(self.shape_type)
        new_piece.rotation = self.rotation
        new_piece.x = self.x
        new_piece.y = self.y
        new_piece.shape = self.shape
        return new_piece

def create_random_tetromino():
    """Create a random tetromino piece"""
    shape_type = random.choice(list(TETROMINOS.keys()))
    return Tetromino(shape_type) 