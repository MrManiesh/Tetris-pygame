# -*- coding: utf-8 -*-

# Screen and Display Constants
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
GRID_WIDTH = 10
GRID_HEIGHT = 20
CELL_SIZE = 32
GRID_OFFSET_X = 420
GRID_OFFSET_Y = 90

# Neon Night Theme Colors
BLACK = (18, 22, 38)
WHITE = (240, 240, 255)
GRAY = (60, 70, 100)
DARK_GRAY = (28, 32, 54)
LIGHT_GRAY = (180, 200, 255)
RED = (255, 80, 120)
GREEN = (80, 255, 180)
BLUE = (80, 200, 255)
CYAN = (0, 255, 255)
MAGENTA = (255, 120, 255)
YELLOW = (255, 255, 120)
ORANGE = (255, 180, 80)
PURPLE = (180, 120, 255)

# Tetromino colors (pastel neon)
TETROMINO_COLORS = {
    'I': (0, 255, 255),    # Neon Cyan
    'O': (255, 255, 180),  # Pastel Yellow
    'T': (200, 120, 255),  # Neon Purple
    'S': (120, 255, 180),  # Neon Green
    'Z': (255, 120, 180),  # Neon Pink
    'J': (120, 180, 255),  # Neon Blue
    'L': (255, 200, 80)    # Neon Orange
}

# UI Colors
PANEL_BG = (24, 28, 48, 230)
PANEL_BORDER = (100, 120, 200)
GLOW = (0, 255, 255, 60)
SHADOW = (0, 0, 0, 120)
PROGRESS_BG = (40, 50, 80)
PROGRESS_FG = (80, 255, 180)

# Tetromino shapes
TETROMINOS = {
    'I': [
        ['.....',
         '..#..',
         '..#..',
         '..#..',
         '..#..'],
        ['.....',
         '.....',
         '####.',
         '.....',
         '.....']
    ],
    'O': [
        ['.....',
         '.....',
         '.##..',
         '.##..',
         '.....']
    ],
    'T': [
        ['.....',
         '.....',
         '.#...',
         '###..',
         '.....'],
        ['.....',
         '.....',
         '.#...',
         '.##..',
         '.#...'],
        ['.....',
         '.....',
         '.....',
         '###..',
         '.#...'],
        ['.....',
         '.....',
         '.#...',
         '##...',
         '.#...']
    ],
    'S': [
        ['.....',
         '.....',
         '.##..',
         '##...',
         '.....'],
        ['.....',
         '.#...',
         '.##..',
         '..#..',
         '.....']
    ],
    'Z': [
        ['.....',
         '.....',
         '##...',
         '.##..',
         '.....'],
        ['.....',
         '..#..',
         '.##..',
         '.#...',
         '.....']
    ],
    'J': [
        ['.....',
         '.#...',
         '.#...',
         '##...',
         '.....'],
        ['.....',
         '.....',
         '#....',
         '###..',
         '.....'],
        ['.....',
         '.##..',
         '.#...',
         '.#...',
         '.....'],
        ['.....',
         '.....',
         '###..',
         '..#..',
         '.....']
    ],
    'L': [
        ['.....',
         '..#..',
         '..#..',
         '.##..',
         '.....'],
        ['.....',
         '.....',
         '###..',
         '#....',
         '.....'],
        ['.....',
         '##...',
         '.#...',
         '.#...',
         '.....'],
        ['.....',
         '.....',
         '..#..',
         '###..',
         '.....']
    ]
}

# Game Settings
INITIAL_DROP_SPEED = 1000  # milliseconds
MIN_DROP_SPEED = 50
SPEED_INCREASE_PER_LEVEL = 50
LINES_PER_LEVEL = 10

# Scoring
LINE_SCORES = {1: 100, 2: 300, 3: 500, 4: 800}
SOFT_DROP_SCORE = 1
HARD_DROP_SCORE = 2

# Game Mode Settings
TIME_ATTACK_DURATION = 120000  # 2 minutes in milliseconds
MARATHON_TARGET_LINES = 150

# Particle Settings
PARTICLE_LIFE = 60
PARTICLE_COUNT_PER_CELL = 3
EXPLOSION_PARTICLE_COUNT = 5 