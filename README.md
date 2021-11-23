# Python3 JetPack Joyride

## Table of Contents
- [Running](#running)
- [Controls](#controls)
- [Requirements Implemented](#requirements-implemented)
  - [OOPS Concepts](#oops-concepts)
  - [Movement](#movement)
  - [Background](#background)
  - [Enemy](#enemy)
  - [Obstacles](#obstacles)
    - [Fire Beams](#fire-beams)
    - [Magnet](#magnet)
  - [Boss Enemy](#boss-enemy)
  - [Score and Lives](#score-and-lives)
  - [Power-Ups](#power-ups)
    - [Speed boost](#speed-boost)
    - [Shield](#shield)
  - [Bonus](#bonus)
- [Directory Structure](#directory-structure)

## Running

- Install dependencies in `requirements.txt`
- Run game using `python3 main.py`

## Controls

| Key   | Function        |
| ----- | --------------- |
| w     | Up Movement     |
| a     | Left Movement   |
| d     | Right Movement  |
| q     | Quit game       |
| b     | Shoot Bullet    |
| Space | Activate Shield |
| f     | Activate Speed Boost |
## Requirements Implemented

### OOPS Concepts

- Inheritance
  - Mando & Boss class inherit from Person Class
  - EnemyBullet inherits from Bullet class
  - Coin and Magnet inherit from Obstacle class
- Polymorphism
  - Mando class overrides `move` method from parent class Person
  - EnemyBullet class overrides `move` method from oarent class Person
- Encapsulation
  - Class based approach to construct the game
- Abstraction
  - Methods are used for movement, collision detection

### Movement

- a for Left
- d for right
- w for Jetpack
- b for Bullets
- Gravity

### Background

- Scenery, Obstacles change as player moves
- Screen continuously moves
- Player can't go left from the screen
- Player can't go above sky or below ground

### Obstacles

#### Fire Beams

- Horizontal, Angled, Vertical Beams are implemented
- Beams can be removed by shooting bullets on them
- Player looses life when collided with Beam

#### Magnet

- Player is attracted towards magnet when he gets in range of magnet
- Magnet attracts using constant force

### Boss Enemy

- Follows Player allong Y axis
- Shoots ice balls which cost the player a life when hit
- Player's bullet costs the dragon a life
- Game Over when one of them loses all their lives 
### Score and Lives

- Score is increased by 100 when player collects a coin
- Score is increased by 50 when player shoots a beam
- Player has 5 lives

### Power-Ups

#### Speed boost

- Increased Game speed
- Lasts for 10s

#### Shield

- Lasts for 10s
- Passes through beams and enemies, but can still collect coins

### Bonus

- Implemented Colors

## Directory Structure

```
─ requirements.txt
─ README.md
─ src
	├── input.py
	└── main.py
	├── board.py
	├── landscape.py
	├── obstacle.py
	├── mando.py
	├── bullet.py
	├── enemy.py
	├── beam.py
	├── person.py
	├── Dragon.txt
```