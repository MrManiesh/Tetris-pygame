# -*- coding: utf-8 -*-

import pygame
from enums import GameState, GameMode

class InputHandler:
    def __init__(self, game):
        self.game = game
        # Input timing variables
        self.key_delay = 150  # milliseconds before key repeat starts
        self.key_repeat = 50  # milliseconds between key repeats
        self.last_key_time = 0
        self.last_key = None
    
    def handle_events(self):
        """Handle all pygame events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            
            if event.type == pygame.KEYDOWN:
                self.handle_keydown(event.key)
        
        return True
    
    def handle_keydown(self, key):
        """Handle key press events"""
        if key == pygame.K_ESCAPE:
            self.handle_escape()
        elif key == pygame.K_p:
            self.handle_pause()
        elif key == pygame.K_UP:
            self.handle_rotate()
        elif key == pygame.K_RETURN:
            self.handle_enter()
        # --- Move/Drop/Hard Drop/Hold only on KEYDOWN ---
        if self.game.state == GameState.PLAYING and self.game.current_piece:
            if key == pygame.K_LEFT:
                if not self.game.logic.is_collision(self.game.current_piece, -1, 0):
                    self.game.current_piece.x -= 1
            elif key == pygame.K_RIGHT:
                if not self.game.logic.is_collision(self.game.current_piece, 1, 0):
                    self.game.current_piece.x += 1
            elif key == pygame.K_DOWN:
                if not self.game.logic.is_collision(self.game.current_piece, 0, 1):
                    self.game.current_piece.y += 1
                    self.game.score += self.game.logic.soft_drop_score
            elif key == pygame.K_SPACE:
                while not self.game.logic.is_collision(self.game.current_piece, 0, 1):
                    self.game.current_piece.y += 1
                    self.game.score += self.game.logic.hard_drop_score
                self.game.logic.place_piece()
            elif key == pygame.K_c:
                self.game.logic.hold_piece()
    
    def handle_escape(self):
        """Handle ESC key"""
        if self.game.state == GameState.PLAYING:
            self.game.state = GameState.MENU
        elif self.game.state == GameState.MENU:
            return False
    
    def handle_pause(self):
        """Handle P key for pause/resume"""
        if self.game.state == GameState.PLAYING:
            self.game.state = GameState.PAUSED
        elif self.game.state == GameState.PAUSED:
            self.game.state = GameState.PLAYING
    
    def handle_rotate(self):
        """Handle UP key for rotation"""
        if self.game.state == GameState.PLAYING and self.game.current_piece:
            original_rotation = self.game.current_piece.rotation
            self.game.current_piece.rotate()
            if self.game.logic.is_collision(self.game.current_piece):
                self.game.current_piece.rotation = original_rotation
                self.game.current_piece.shape = self.game.logic.tetrominos[self.game.current_piece.shape_type][self.game.current_piece.rotation]
    
    def handle_enter(self):
        """Handle ENTER key"""
        if self.game.state == GameState.MENU:
            self.game.state = GameState.PLAYING
            if self.game.game_mode.name == 'TIME_ATTACK':
                self.game.time_attack_start = pygame.time.get_ticks()
            else:
                self.game.time_attack_start = None
            self.game.logic.reset_game()
        elif self.game.state == GameState.GAME_OVER:
            self.game.state = GameState.PLAYING
            if self.game.game_mode.name == 'TIME_ATTACK':
                self.game.time_attack_start = pygame.time.get_ticks()
            else:
                self.game.time_attack_start = None
            self.game.logic.reset_game()
    
    def handle_continuous_input(self):
        """Handle continuous key presses with timing"""
        keys = pygame.key.get_pressed()
        current_time = pygame.time.get_ticks()
        
        if self.game.state == GameState.MENU:
            self.handle_menu_input(keys, current_time)
        # No movement in PLAYING state here!
        elif self.game.state == GameState.GAME_OVER:
            self.handle_game_over_input(keys)
    
    def handle_menu_input(self, keys, current_time):
        """Handle input during menu state"""
        if keys[pygame.K_UP] and self.should_process_key(pygame.K_UP, current_time):
            self.game.game_mode = GameMode((self.game.game_mode.value - 2) % 3 + 1)
        elif keys[pygame.K_DOWN] and self.should_process_key(pygame.K_DOWN, current_time):
            self.game.game_mode = GameMode(self.game.game_mode.value % 3 + 1)
    
    def handle_gameplay_input(self, keys, current_time):
        """No movement here anymore!"""
        pass
    
    def handle_game_over_input(self, keys):
        """Handle input during game over state"""
        if keys[pygame.K_ESCAPE]:
            self.game.state = GameState.MENU
    
    def should_process_key(self, key, current_time):
        """Check if a key should be processed based on timing"""
        if key != self.last_key:
            # New key pressed
            self.last_key = key
            self.last_key_time = current_time
            return True
        else:
            # Same key held down
            if current_time - self.last_key_time > self.key_delay:
                # After initial delay, check repeat rate
                if current_time - self.last_key_time > self.key_repeat:
                    self.last_key_time = current_time
                    return True
        return False 