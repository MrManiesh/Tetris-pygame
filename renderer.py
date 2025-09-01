# -*- coding: utf-8 -*-

import pygame
from constants import *
from enums import GameState, GameMode

class Renderer:
    def __init__(self, game):
        self.game = game
        self.font = pygame.font.Font(None, 36)
        self.small_font = pygame.font.Font(None, 24)
        self.large_font = pygame.font.Font(None, 72)
    
    def render(self):
        """Main render method that calls appropriate render based on game state"""
        if self.game.state == GameState.MENU:
            self.render_menu()
        elif self.game.state == GameState.PLAYING:
            self.render_game()
        elif self.game.state == GameState.PAUSED:
            self.render_pause_screen()
        elif self.game.state == GameState.GAME_OVER:
            self.render_game_over()
    
    def render_game(self):
        """Render the main game screen"""
        # Draw a subtle vertical gradient background
        self.draw_background_gradient()
        self.draw_grid()
        self.draw_ui()
        self.draw_particles()
        self.draw_mode_info()
    
    def draw_background_gradient(self):
        """Draw a vertical gradient background for a modern look."""
        for y in range(SCREEN_HEIGHT):
            color = (
                int(30 + (y / SCREEN_HEIGHT) * 40),
                int(30 + (y / SCREEN_HEIGHT) * 60),
                int(50 + (y / SCREEN_HEIGHT) * 80)
            )
            pygame.draw.line(self.game.screen, color, (0, y), (SCREEN_WIDTH, y))
    
    def draw_grid(self):
        """Draw the game grid with pieces, rounded corners, and drop shadow."""
        # Drop shadow
        shadow_rect = pygame.Rect(GRID_OFFSET_X + 8, GRID_OFFSET_Y + 8, GRID_WIDTH * CELL_SIZE, GRID_HEIGHT * CELL_SIZE)
        shadow_surf = pygame.Surface((GRID_WIDTH * CELL_SIZE, GRID_HEIGHT * CELL_SIZE), pygame.SRCALPHA)
        pygame.draw.rect(shadow_surf, SHADOW, shadow_surf.get_rect(), border_radius=18)
        self.game.screen.blit(shadow_surf, (GRID_OFFSET_X + 8, GRID_OFFSET_Y + 8))
        # Main grid background
        grid_rect = pygame.Rect(GRID_OFFSET_X, GRID_OFFSET_Y, GRID_WIDTH * CELL_SIZE, GRID_HEIGHT * CELL_SIZE)
        pygame.draw.rect(self.game.screen, DARK_GRAY, grid_rect, border_radius=18)
        pygame.draw.rect(self.game.screen, PANEL_BORDER, grid_rect, 3, border_radius=18)
        # Draw grid cells
        for y in range(GRID_HEIGHT):
            for x in range(GRID_WIDTH):
                color = self.game.grid[y][x] if self.game.grid[y][x] else (30, 30, 50)
                cell_rect = pygame.Rect(GRID_OFFSET_X + x * CELL_SIZE, GRID_OFFSET_Y + y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                pygame.draw.rect(self.game.screen, color, cell_rect, border_radius=8)
                pygame.draw.rect(self.game.screen, GRAY, cell_rect, 1, border_radius=8)
        # Draw ghost piece (glow effect)
        ghost = self.game.logic.get_ghost_position()
        if ghost:
            for x, y in ghost.get_positions():
                if 0 <= y < GRID_HEIGHT and 0 <= x < GRID_WIDTH:
                    ghost_rect = pygame.Rect(GRID_OFFSET_X + x * CELL_SIZE, GRID_OFFSET_Y + y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                    glow_surf = pygame.Surface((CELL_SIZE, CELL_SIZE), pygame.SRCALPHA)
                    pygame.draw.rect(glow_surf, GLOW, glow_surf.get_rect(), border_radius=8)
                    self.game.screen.blit(glow_surf, ghost_rect.topleft)
        # Draw current piece (with white border)
        if self.game.current_piece:
            for x, y in self.game.current_piece.get_positions():
                if 0 <= y < GRID_HEIGHT and 0 <= x < GRID_WIDTH:
                    cell_rect = pygame.Rect(GRID_OFFSET_X + x * CELL_SIZE, GRID_OFFSET_Y + y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                    pygame.draw.rect(self.game.screen, self.game.current_piece.color, cell_rect, border_radius=8)
                    pygame.draw.rect(self.game.screen, WHITE, cell_rect, 2, border_radius=8)
    
    def draw_ui(self):
        """Draw the UI elements (score, next piece, held piece) with modern panels."""
        # Draw side panel with rounded corners and drop shadow
        panel_rect = pygame.Rect(60, 100, 320, 500)
        shadow_surf = pygame.Surface((320, 500), pygame.SRCALPHA)
        pygame.draw.rect(shadow_surf, SHADOW, shadow_surf.get_rect(), border_radius=24)
        self.game.screen.blit(shadow_surf, (panel_rect.x + 8, panel_rect.y + 8))
        panel_surf = pygame.Surface((320, 500), pygame.SRCALPHA)
        pygame.draw.rect(panel_surf, PANEL_BG, panel_surf.get_rect(), border_radius=24)
        pygame.draw.rect(panel_surf, PANEL_BORDER, panel_surf.get_rect(), 3, border_radius=24)
        # Score
        score_text = self.large_font.render(f"{self.game.score:,}", True, YELLOW)
        score_label = self.font.render("SCORE", True, LIGHT_GRAY)
        panel_surf.blit(score_label, (30, 30))
        panel_surf.blit(score_text, (30, 65))
        # Level
        level_label = self.font.render("LEVEL", True, LIGHT_GRAY)
        level_text = self.font.render(f"{self.game.level}", True, GREEN)
        panel_surf.blit(level_label, (30, 130))
        panel_surf.blit(level_text, (30, 165))
        # Lines
        lines_label = self.font.render("LINES", True, LIGHT_GRAY)
        lines_text = self.font.render(f"{self.game.lines_cleared}", True, CYAN)
        panel_surf.blit(lines_label, (30, 210))
        panel_surf.blit(lines_text, (30, 245))
        # Time Attack Timer
        if self.game.game_mode.name == 'TIME_ATTACK' and self.game.time_attack_start is not None:
            current_time = pygame.time.get_ticks()
            elapsed = current_time - self.game.time_attack_start
            remaining = max(0, (120000 - elapsed) // 1000)
            timer_label = self.font.render("TIME LEFT", True, LIGHT_GRAY)
            timer_text = self.font.render(f"{remaining:02d}s", True, RED if remaining <= 10 else YELLOW)
            panel_surf.blit(timer_label, (30, 290))
            panel_surf.blit(timer_text, (30, 325))
        # Next piece (with icon)
        next_label = self.font.render("NEXT", True, LIGHT_GRAY)
        panel_surf.blit(next_label, (200, 30))
        if self.game.next_piece:
            for i, row in enumerate(self.game.next_piece.shape):
                for j, cell in enumerate(row):
                    if cell == '#':
                        rect = pygame.Rect(220 + j * 20, 70 + i * 20, 18, 18)
                        pygame.draw.rect(panel_surf, self.game.next_piece.color, rect, border_radius=6)
                        pygame.draw.rect(panel_surf, WHITE, rect, 1, border_radius=6)
        # Held piece (with icon)
        hold_label = self.font.render("HOLD", True, LIGHT_GRAY)
        panel_surf.blit(hold_label, (200, 180))
        if self.game.held_piece:
            for i, row in enumerate(self.game.held_piece.shape):
                for j, cell in enumerate(row):
                    if cell == '#':
                        color = self.game.held_piece.color if self.game.can_hold else GRAY
                        rect = pygame.Rect(220 + j * 20, 220 + i * 20, 18, 18)
                        pygame.draw.rect(panel_surf, color, rect, border_radius=6)
                        pygame.draw.rect(panel_surf, WHITE, rect, 1, border_radius=6)
        self.game.screen.blit(panel_surf, (panel_rect.x, panel_rect.y))
    
    def draw_particles(self):
        """Draw all particles"""
        for particle in self.game.particles:
            particle.draw(self.game.screen)
    
    def render_menu(self):
        """Render the main menu"""
        self.game.screen.fill(BLACK)
        
        title = self.large_font.render("TETRIS", True, CYAN)
        title_rect = title.get_rect(center=(SCREEN_WIDTH // 2, 150))
        self.game.screen.blit(title, title_rect)
        
        subtitle = self.font.render("Feature Rich Edition", True, WHITE)
        subtitle_rect = subtitle.get_rect(center=(SCREEN_WIDTH // 2, 220))
        self.game.screen.blit(subtitle, subtitle_rect)
        
        # Game mode selection
        modes = [
            ("Classic Mode", GameMode.CLASSIC),
            ("Time Attack (2 min)", GameMode.TIME_ATTACK),
            ("Marathon (150 lines)", GameMode.MARATHON)
        ]
        
        for i, (mode_name, mode) in enumerate(modes):
            color = CYAN if self.game.game_mode == mode else WHITE
            text = self.font.render(mode_name, True, color)
            text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, 350 + i * 50))
            self.game.screen.blit(text, text_rect)
        
        # Instructions
        instructions = [
            "Use ARROW KEYS to move and rotate",
            "SPACE to hard drop",
            "C to hold piece",
            "P to pause",
            "ENTER to start game"
        ]
        
        for i, instruction in enumerate(instructions):
            text = self.small_font.render(instruction, True, LIGHT_GRAY)
            text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, 550 + i * 30))
            self.game.screen.blit(text, text_rect)
    
    def render_pause_screen(self):
        """Render the pause screen overlay"""
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        overlay.set_alpha(128)
        overlay.fill(BLACK)
        self.game.screen.blit(overlay, (0, 0))
        
        pause_text = self.large_font.render("PAUSED", True, WHITE)
        pause_rect = pause_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        self.game.screen.blit(pause_text, pause_rect)
        
        resume_text = self.font.render("Press P to resume", True, WHITE)
        resume_rect = resume_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 80))
        self.game.screen.blit(resume_text, resume_rect)
    
    def render_game_over(self):
        """Render the game over screen"""
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        overlay.set_alpha(200)
        overlay.fill(BLACK)
        self.game.screen.blit(overlay, (0, 0))
        
        # Show 'You Win!' if Marathon completed, else 'Game Over'
        if self.game.game_mode.name == 'MARATHON' and self.game.lines_cleared >= 150:
            game_over_text = self.large_font.render("YOU WIN!", True, GREEN)
        else:
            game_over_text = self.large_font.render("GAME OVER", True, RED)
        game_over_rect = game_over_text.get_rect(center=(SCREEN_WIDTH // 2, 200))
        self.game.screen.blit(game_over_text, game_over_rect)
        
        final_score = self.font.render(f"Final Score: {self.game.score:,}", True, WHITE)
        final_score_rect = final_score.get_rect(center=(SCREEN_WIDTH // 2, 300))
        self.game.screen.blit(final_score, final_score_rect)
        
        restart_text = self.font.render("Press ENTER to restart", True, WHITE)
        restart_rect = restart_text.get_rect(center=(SCREEN_WIDTH // 2, 400))
        self.game.screen.blit(restart_text, restart_rect)
        
        menu_text = self.font.render("Press ESC for menu", True, WHITE)
        menu_rect = menu_text.get_rect(center=(SCREEN_WIDTH // 2, 450))
        self.game.screen.blit(menu_text, menu_rect)

    def draw_mode_info(self):
        """Draw information about the current game mode at the top of the screen."""
        info = ""
        if self.game.game_mode.name == 'CLASSIC':
            info = "Classic: Play endlessly, speed increases every 10 lines."
        elif self.game.game_mode.name == 'TIME_ATTACK':
            info = "Time Attack: Score as high as possible in 2 minutes."
        elif self.game.game_mode.name == 'MARATHON':
            info = "Marathon: Clear 150 lines to win."
        if info:
            info_text = self.font.render(info, True, YELLOW)
            info_rect = info_text.get_rect(center=(SCREEN_WIDTH // 2, 40))
            self.game.screen.blit(info_text, info_rect)
        # Marathon progress bar
        if self.game.game_mode.name == 'MARATHON':
            progress = min(1.0, self.game.lines_cleared / 150)
            bar_x = SCREEN_WIDTH // 2 - 150
            bar_y = 70
            bar_width = 300
            bar_height = 20
            pygame.draw.rect(self.game.screen, GRAY, (bar_x, bar_y, bar_width, bar_height), 2)
            pygame.draw.rect(self.game.screen, GREEN, (bar_x, bar_y, int(bar_width * progress), bar_height))
            progress_text = self.small_font.render(f"{self.game.lines_cleared}/150 lines", True, WHITE)
            progress_rect = progress_text.get_rect(center=(SCREEN_WIDTH // 2, bar_y + bar_height // 2))
            self.game.screen.blit(progress_text, progress_rect) 