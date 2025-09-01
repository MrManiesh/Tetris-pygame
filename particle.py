# -*- coding: utf-8 -*-

import pygame
import random
from constants import PARTICLE_LIFE

class Particle:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.vx = random.uniform(-3, 3)
        self.vy = random.uniform(-5, -1)
        self.color = color
        self.life = PARTICLE_LIFE
        self.max_life = PARTICLE_LIFE
        self.size = random.randint(2, 4)
    
    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.vy += 0.2  # Gravity
        self.life -= 1
        self.size = max(0, self.size - 0.1)
    
    def draw(self, screen):
        if self.life > 0:
            alpha = int(255 * (self.life / self.max_life))
            color = (*self.color, alpha)
            surf = pygame.Surface((self.size * 2, self.size * 2), pygame.SRCALPHA)
            pygame.draw.circle(surf, color, (self.size, self.size), self.size)
            screen.blit(surf, (self.x - self.size, self.y - self.size))
    
    def is_alive(self):
        return self.life > 0 