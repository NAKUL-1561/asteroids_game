# Asteroids Game in Python

A classic Asteroids arcade game built with Pygame while following the Boot.dev game development course. The idea was to learn how game loops, physics, collision detection, and sprite management actually work by building something from scratch rather than just reading about it.

The player controls a ship, dodges incoming asteroids, and shoots them down to score points. Asteroids split into smaller pieces when hit, the player has multiple lives, and the whole thing runs at 60 FPS with a proper game loop.

---

## Features

* Smooth 60 FPS gameplay with delta-time movement
* Player ship with rotation, forward/backward movement, and shooting
* Asteroids that spawn from screen edges at random angles and speeds
* Asteroid splitting — large asteroids break into two smaller, faster ones
* Collision detection between player, asteroids, and shots
* Lives system with respawn timer and countdown display
* Score tracking with on-screen HUD
* Game state and event logging to JSONL files for debugging and analysis
* Clean object-oriented design using inheritance and sprite groups

---

## Tech Stack

* Python 3.13
* Pygame
* Object-Oriented Programming (inheritance, polymorphism)
* Vector math for movement and rotation
* JSONL for game state logging
* `uv` for dependency management
* Git & GitHub

---

## Skills Highlighted

This project helped me improve and demonstrate skills in:

* Game development fundamentals (game loop, delta time, frame rate control)
* 2D physics and vector math (velocity, rotation, directional movement)
* Collision detection using distance-based circle checks
* Object-oriented design with base classes and inheritance
* Sprite group management in Pygame
* State management (lives, score, respawn timers)
* Event-driven programming
* Logging and debugging game state with structured data
* Writing clean, modular Python code
* Git version control

---

## Controls

| Key | Action |
|-----|--------|
| `W` | Move forward |
| `S` | Move backward |
| `A` | Rotate left |
| `D` | Rotate right |
| `Space` | Shoot |

---

## Project Structure

```
.
├── main.py              # Entry point — game loop, HUD, and collision logic
├── player.py            # Player ship — movement, rotation, shooting, respawn
├── asteroid.py          # Asteroid — movement and split mechanic
├── asteroidfield.py     # Spawns asteroids from random screen edges
├── shot.py              # Projectile fired by the player
├── circleshape.py       # Base class for all circular game objects
├── constants.py         # All game constants (speed, radius, cooldowns, etc.)
├── logger.py            # Logs game state and events to JSONL files
├── pyproject.toml       # Project metadata and dependencies
└── README.md
```

---

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/NAKUL-1561/asteroids_game.git
cd asteroids_game
```

### 2. Set up the environment

This project uses `uv` for dependency management. If you don't have it:

```bash
pip install uv
```

Then sync the dependencies:

```bash
uv sync
```

Or install directly with pip:

```bash
pip install pygame==2.6.1
```

### 3. Run the game

```bash
python main.py
```

---

## How It Works

1. The game loop runs at 60 FPS using `pygame.time.Clock`
2. Every frame, the player input is read and the ship moves/rotates accordingly
3. Asteroids spawn from random edges on a timer and drift across the screen
4. When a shot hits an asteroid, the asteroid splits into two smaller ones (unless it's already the smallest size)
5. If the player collides with an asteroid, they lose a life and respawn after a 1.5 second cooldown
6. The game ends when all lives are gone

The logger module captures game state snapshots once per second and logs events like asteroid hits and splits to JSONL files — useful for debugging or analyzing gameplay after the fact.

---

## What I Learned

This project was a great way to understand how games work at a low level. Writing the game loop myself, handling delta time properly, and getting collision detection right taught me way more than any tutorial could.

The most interesting part was probably the asteroid splitting mechanic — figuring out how to rotate the velocity vector at random angles to make the fragments fly apart naturally was a fun math problem. I also got a much better feel for how OOP patterns like inheritance and sprite groups can keep game code organized.

---

## Future Improvements

* Add a start screen and game over screen
* Implement increasing difficulty over time
* Add sound effects and background music
* Track and display high scores
* Add power-ups and shields
* Screen wrapping for the player and asteroids
* Deploy as a standalone executable with PyInstaller

---

## Author

Made by **Nakul** while learning game development and Python programming.
