
# Space Dodge 🚀

**Space Dodge** is a fun arcade game where the player must dodge incoming enemies and shoot them while collecting points and coins. The game includes a level selection system and a special power-up ability.

---

## Table of Contents
- [Features](#features)
- [System Requirements](#system-requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [How to Play](#how-to-play)
- [Credits](#credits)

---

## Features
- **Level selection:** Choose from 5 levels through a sleek GUI interface.
- **Progressive difficulty:** Enemy speed increases with each level.
- **Special power-up:** Activated by pressing **P**, clearing all enemies from the screen (costs 10 coins).
- **Smooth shooting mechanics:** Fire bullets with a cooldown of 0.3 seconds.
- **In-game tracking:** Displays time, hits, current level, and coins collected.
- **Custom graphics and sound:** Engaging visuals and background music.

---

## System Requirements
- **Python 3.8+**
- **Libraries:**
  - `pygame`
  - `customtkinter`

---

## Installation
1. Make sure Python is installed on your machine. [Download Python here](https://www.python.org/downloads/).
2. Clone the repository:
   ```bash
   git clone https://github.com/your-username/space-dodge.git
   cd space-dodge
   ```
3. Install the required dependencies:
   ```bash
   pip install pygame customtkinter
   ```
4. Make sure all assets (images and sound files) are placed in the correct paths specified in the code.

---

## Usage
1. Run the game by launching the following command:
   ```bash
   python space_dodge.py
   ```
2. Use the level selector to choose your starting level and start playing!

---

## Project Structure
```
space-dodge/
│
├── space_dodge.py         # Main game logic and level selector
├── README.md              # Project documentation
├── assets/                # Images and sound files
│   ├── player.png         # Player spaceship image
│   ├── enemy.png          # Enemy image
│   ├── bullet.png         # Bullet image
│   └── theme.mp3          # Background music
```

---

## How to Play
1. **Movement:** Use the arrow keys to move your spaceship.
2. **Shooting:** Press **Space** to shoot bullets (cooldown: 0.3s).
3. **Power-up:** Press **P** to activate the special power and clear all enemies (requires 10 coins).
4. Avoid collisions with enemies; colliding will end the game.
5. Collect coins by shooting enemies.

---

## Credits
- **Developer:** [Your Name](https://github.com/your-username)  
- **Libraries used:**  
  - [pygame](https://www.pygame.org/news)  
  - [customtkinter](https://github.com/TomSchimansky/CustomTkinter)

---

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


## One last thing
**have fun!!!
