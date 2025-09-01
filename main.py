# -*- coding: utf-8 -*-

import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from enums import GameState, GameMode
from game_logic import GameLogic
from controls import InputHandler
from renderer import Renderer

class TetrisGame:
    def __init__(self):
        # Initialize Pygame
        pygame.init()
        pygame.mixer.init()
        
        # Set up display
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Tetris - Feature Rich Edition")
        self.clock = pygame.time.Clock()
        
        # Game state
        self.state = GameState.MENU
        self.game_mode = GameMode.CLASSIC
        
        # Game data
        self.grid = [[None for _ in range(10)] for _ in range(20)]
        self.current_piece = None
        self.next_piece = None
        self.held_piece = None
        self.can_hold = True
        
        self.score = 0
        self.lines_cleared = 0
        self.level = 1
        self.drop_speed = 1000
        self.last_drop = pygame.time.get_ticks()
        
        self.particles = []
        self.high_scores = {}
        self.time_attack_start = None  # Track start time for Time Attack
        
        # Initialize components
        self.logic = GameLogic(self)
        self.input_handler = InputHandler(self)
        self.renderer = Renderer(self)
        
        # Load high scores
        self.high_scores = self.logic.load_high_scores()
        
        # Spawn first piece
        self.logic.spawn_piece()
    
    def run(self):
        """Main game loop"""
        running = True
        
        while running:
            # Handle events
            running = self.input_handler.handle_events()
            
            # Handle continuous input
            self.input_handler.handle_continuous_input()
            
            # Update game logic
            self.logic.update()
            
            # Render everything
            self.renderer.render()
            
            # Update display
            pygame.display.flip()
            
            # Control frame rate
            self.clock.tick(60)
        
        # Save high scores before quitting
        mode_key = self.game_mode.name.lower()
        if self.score > self.high_scores.get(mode_key, 0):
            self.high_scores[mode_key] = self.score
            self.logic.save_high_scores()
        
        pygame.quit()

if __name__ == "__main__":
    game = TetrisGame()
    game.run() 