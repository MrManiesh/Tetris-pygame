# -*- coding: utf-8 -*-

import pygame
import random
import json
from constants import *
from enums import GameState, GameMode
from tetromino import Tetromino, create_random_tetromino
from particle import Particle

class GameLogic:
    def __init__(self, game):
        self.game = game
        self.tetrominos = TETROMINOS
        self.soft_drop_score = SOFT_DROP_SCORE
        self.hard_drop_score = HARD_DROP_SCORE
    
    def spawn_piece(self):
        """Spawn a new tetromino piece"""
        if self.game.next_piece is None:
            self.game.next_piece = create_random_tetromino()
        
        self.game.current_piece = self.game.next_piece
        self.game.next_piece = create_random_tetromino()
        self.game.can_hold = True
        
        if self.is_collision(self.game.current_piece):
            self.game.state = GameState.GAME_OVER
    
    def is_collision(self, piece, dx=0, dy=0):
        """Check if a piece collides with walls or other pieces"""
        for x, y in piece.get_positions():
            new_x, new_y = x + dx, y + dy
            if (new_x < 0 or new_x >= GRID_WIDTH or 
                new_y >= GRID_HEIGHT or 
                (new_y >= 0 and self.game.grid[new_y][new_x] is not None)):
                return True
        return False
    
    def place_piece(self):
        """Place the current piece on the grid"""
        for x, y in self.game.current_piece.get_positions():
            if 0 <= y < GRID_HEIGHT and 0 <= x < GRID_WIDTH:
                self.game.grid[y][x] = self.game.current_piece.color
        
        # Create particles
        for x, y in self.game.current_piece.get_positions():
            if 0 <= y < GRID_HEIGHT and 0 <= x < GRID_WIDTH:
                for _ in range(PARTICLE_COUNT_PER_CELL):
                    self.game.particles.append(Particle(
                        GRID_OFFSET_X + x * CELL_SIZE + CELL_SIZE // 2,
                        GRID_OFFSET_Y + y * CELL_SIZE + CELL_SIZE // 2,
                        self.game.current_piece.color
                    ))
        
        self.clear_lines()
        self.spawn_piece()
    
    def clear_lines(self):
        """Clear completed lines and update score"""
        lines_to_clear = []
        for y in range(GRID_HEIGHT):
            if all(cell is not None for cell in self.game.grid[y]):
                lines_to_clear.append(y)
        
        if lines_to_clear:
            # Create explosion particles
            for y in lines_to_clear:
                for x in range(GRID_WIDTH):
                    for _ in range(EXPLOSION_PARTICLE_COUNT):
                        self.game.particles.append(Particle(
                            GRID_OFFSET_X + x * CELL_SIZE + random.randint(0, CELL_SIZE),
                            GRID_OFFSET_Y + y * CELL_SIZE + random.randint(0, CELL_SIZE),
                            self.game.grid[y][x]
                        ))
            
            # Remove lines
            for y in lines_to_clear:
                del self.game.grid[y]
                self.game.grid.insert(0, [None for _ in range(GRID_WIDTH)])
            
            # Update score
            lines_count = len(lines_to_clear)
            self.game.lines_cleared += lines_count
            self.game.score += LINE_SCORES.get(lines_count, 0) * self.game.level
            
            # Marathon bonus for finishing
            if self.game.game_mode.name == 'MARATHON' and self.game.lines_cleared >= MARATHON_TARGET_LINES:
                self.game.score += 5000  # Bonus for winning Marathon
            
            # Update level
            self.game.level = self.game.lines_cleared // LINES_PER_LEVEL + 1
            self.game.drop_speed = max(MIN_DROP_SPEED, 
                                     INITIAL_DROP_SPEED - (self.game.level - 1) * SPEED_INCREASE_PER_LEVEL)
    
    def get_ghost_position(self):
        """Get the ghost piece position (where piece will land)"""
        if not self.game.current_piece:
            return None
        
        ghost = self.game.current_piece.copy()
        
        while not self.is_collision(ghost, 0, 1):
            ghost.y += 1
        
        return ghost
    
    def hold_piece(self):
        """Hold the current piece for later use (fixed logic)"""
        if not self.game.can_hold:
            return

        if self.game.held_piece is None:
            # Store a copy of the current piece in hold
            self.game.held_piece = self.game.current_piece.copy()
            self.spawn_piece()
        else:
            # Swap: put current in hold, bring held to play
            temp = self.game.held_piece.copy()
            self.game.held_piece = self.game.current_piece.copy()
            self.game.current_piece = temp
            self.game.current_piece.reset_position()
            self.game.current_piece.rotation = 0
            self.game.current_piece.shape = TETROMINOS[self.game.current_piece.shape_type][0]

        self.game.can_hold = False
    
    def update_particles(self):
        """Update all particles"""
        self.game.particles = [p for p in self.game.particles if p.is_alive()]
        for particle in self.game.particles:
            particle.update()
    
    def auto_drop(self):
        """Handle automatic piece dropping"""
        current_time = pygame.time.get_ticks()
        if current_time - self.game.last_drop > self.game.drop_speed:
            if not self.is_collision(self.game.current_piece, 0, 1):
                self.game.current_piece.y += 1
            else:
                self.place_piece()
            self.game.last_drop = current_time
    
    def check_game_over_conditions(self):
        """Check if game over conditions are met based on game mode"""
        current_time = pygame.time.get_ticks()
        
        if self.game.game_mode == GameMode.TIME_ATTACK:
            if self.game.time_attack_start is not None:
                elapsed = current_time - self.game.time_attack_start
                if elapsed >= TIME_ATTACK_DURATION:
                    self.game.state = GameState.GAME_OVER
        elif self.game.game_mode == GameMode.MARATHON:
            if self.game.lines_cleared >= MARATHON_TARGET_LINES:
                self.game.state = GameState.GAME_OVER
    
    def reset_game(self):
        """Reset the game state"""
        self.game.grid = [[None for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
        self.game.current_piece = None
        self.game.next_piece = None
        self.game.held_piece = None
        self.game.can_hold = True
        self.game.score = 0
        self.game.lines_cleared = 0
        self.game.level = 1
        self.game.drop_speed = INITIAL_DROP_SPEED
        self.game.last_drop = pygame.time.get_ticks()
        self.game.particles = []
        self.spawn_piece()
    
    def load_high_scores(self):
        """Load high scores from file"""
        try:
            with open('high_scores.json', 'r') as f:
                return json.load(f)
        except:
            return {'classic': 0, 'time_attack': 0, 'marathon': 0}
    
    def save_high_scores(self):
        """Save high scores to file"""
        with open('high_scores.json', 'w') as f:
            json.dump(self.game.high_scores, f)
    
    def update(self):
        """Main update method"""
        self.update_particles()
        
        if self.game.state == GameState.PLAYING:
            self.auto_drop()
            self.check_game_over_conditions() 