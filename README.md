# 🎮 Tetris - Feature Rich Edition

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![Pygame](https://img.shields.io/badge/Pygame-2.5.2-green.svg)](https://www.pygame.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Complete-brightgreen.svg)]()

A modern, feature-packed Tetris game built with Python and Pygame, featuring beautiful neon graphics, multiple game modes, and advanced gameplay mechanics.

https://user-images.githubusercontent.com/MrManiesh/Tetris-pygame/main/tetris-1.mp4

## ✨ Features

### 🎯 Game Modes
- **Classic Mode**: Traditional Tetris gameplay with increasing difficulty
- **Time Attack**: Race against the clock - 2 minutes to score high
- **Marathon**: Clear 150 lines to win with progress tracking

### 🎨 Visual Features
- **Neon Night Theme**: Stunning dark blue background with vibrant colors
- **Particle Effects**: Explosive particles when lines are cleared
- **Smooth Animations**: Fluid piece movement and rotations
- **Ghost Piece**: Shows where your piece will land
- **Modern UI**: Clean, professional interface with rounded panels

### 🎮 Gameplay Features
- **Hold Piece**: Store a piece for later use
- **Next Piece Preview**: See what's coming next
- **Hard Drop**: Instantly drop pieces
- **Soft Drop**: Faster downward movement
- **Wall Kicks**: Smart rotation system
- **Scoring System**: Points based on lines cleared and level

### 🏆 Advanced Features
- **High Score System**: Persistent high scores for each game mode
- **Pause Functionality**: Pause and resume anytime
- **Game Over Screen**: Final score display with restart options
- **Menu System**: Easy navigation between game modes

## 🚀 Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Quick Start
```bash
# Clone the repository
git clone https://github.com/MrManiesh/Tetris-pygame.git
cd tetris-game

# Install dependencies
pip install pygame numpy

# Run the game
python main.py
```

## 🎮 Controls

| Action | Key |
|--------|-----|
| Move Left/Right | Arrow Keys |
| Rotate | Up Arrow |
| Soft Drop | Down Arrow |
| Hard Drop | Space |
| Hold Piece | C |
| Pause/Resume | P |
| Menu Navigation | Up/Down Arrows |
| Start/Select | Enter |
| Exit | Escape |

## 🏗️ Project Structure

```
tetris/
├── main.py              # Main game entry point
├── constants.py          # Game constants and colors
├── enums.py             # Game state and mode enumerations
├── game_logic.py        # Core game mechanics
├── controls.py          # Input handling
├── renderer.py          # Graphics and UI rendering
├── tetromino.py         # Piece logic and behavior
└── particle.py          # Particle effects system
```

## 🎯 Game Modes Explained

### Classic Mode
- Traditional Tetris gameplay
- Speed increases every 10 lines cleared
- No time limit - play until you lose
- Perfect for learning and practice

### Time Attack
- 2-minute time limit
- Race against the clock to score high
- Strategic piece placement is crucial
- Great for quick gaming sessions

### Marathon
- Clear exactly 150 lines to win
- Progress bar shows completion
- Test your endurance and skill
- Ideal for long gaming sessions

## 🎨 Customization

### Colors and Themes
Modify `constants.py` to change:
- Background colors
- Tetromino colors
- UI panel colors
- Glow effects

### Game Settings
Adjust in `constants.py`:
- Drop speed
- Scoring multipliers
- Time limits
- Particle effects

## 🐛 Troubleshooting

### Common Issues

**"pygame module not found"**
```bash
pip install pygame
```

**"pygame.error: No available video device"**
- Ensure you have a display connected
- Try running on a different system

**Game runs slowly**
- Close other applications
- Update graphics drivers
- Lower system display scaling

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Inspired by classic Tetris
- Built with Pygame community support
- Special thanks to all contributors

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/MrManiesh/Tetris-pygame/issues)
- **Discussions**: [GitHub Discussions](https://github.com/MrManiesh/Tetris-pygame/discussions)
- **Email**: manishmatwacs@gmail.com

## 🌟 Star History

[![Star History Chart](https://api.star-history.com/svg?repos=yourusername/tetris-game&type=Date)](https://star-history.com/#MrManiesh/Tetris-pygame&Date)

---

**Made with ❤️ by Manish Choudhary**

*If you find this project helpful, please give it a ⭐ star!*
