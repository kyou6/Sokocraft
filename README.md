# Sokocraft
A Sokoban Minecraft-inspired game made on PyGame
<img width=100% src="https://github.com/user-attachments/assets/e79a84ae-5538-4d22-9a3f-5464153b54c0">

**Forked from:** [KIDJourney/Sokoban_Pygame](https://github.com/KIDJourney/Sokoban_Pygame)


## Table of Contents
- [What’s New?](#whats-new)
- [Features](#features)
- [How to Use](#how-to-use)
- [Files Overview](#files-overview)
- [Screenshot](#screenshot)
- [Requirements](#requirements)
- [Installation](#installation)
- [License](#license)


## What’s New?
### Major Enhancements:
1. **Custom Map Creation**
   - Users can create maps with a grid (max dimensions: 24x12).
   - Place objects like walls, boxes, goals, or players using keyboard shortcuts.
   - Save maps as `.dat` files to replace existing levels.

2. **Textures**
   - Replaced textures with Minecraft block-style graphics for a refreshed look.

3. **Enhanced UI**
   - New start screen for a polished user experience.

4. **Undo/Redo Functions**
   - Added undo (`Ctrl+Z`) and redo (`Ctrl+Y`) options to allow players to revert their moves during gameplay.


## Features

### Custom Map Creation
- **Grid-based Map Design:**
  - Maximum size: 24 (width) x 12 (height).
  - Object placement keys:
    - `1` = Wall (`W`)
    - `2` = Box (`B`)
    - `3` = Goal (`G`)
    - `4` = Player (`P`)
    - `5` = Empty space (`N`)
  - Option to import existing `.dat` map files for editing.
- **Save Functionality:**
  - Save created maps in `.dat` format.
  - Replace levels 1-3 in the game with custom designs.

### Textures
- Minecraft-style textures:
  - Walls
  - Boxes
  - Goals
  - Player character

### Game UI
- Redesigned start screen with interactive buttons:
  - Play Game
  - Help (currently under development)
  - Quit Game


## How to Use

### Custom Map Creation
1. Launch `custom_map.py`.
2. Choose between:
   - **New Map:** Specify grid size and start designing.
   - **Import Map:** Load an existing `.dat` file for editing.
3. Use the object placement keys to design your map.
4. Save your map using the save prompt.

### Undo/Redo During Gameplay
- **Undo:** Press `Ctrl + Z`.
- **Redo:** Press `Ctrl + Y`.


## Files Overview
- `main.py`: Main game logic, including movement and game state management.
- `custom_map.py`: Map creation and editing functionality.

## Screenshot
<p align="center">
<img width="640"src="https://github.com/user-attachments/assets/9dfe63ac-5d62-4bc8-aa54-0f3ccba6bfac">

## Requirements
- Python 3.8+
- `pygame` library
- `tkinter` (for GUI prompts)

## Installation
1. Clone the repository:

   ```bash
   git clone https://github.com/kyou6/Sokocraft.git
2. Install dependencies: Ensure that you have Python installed. Then, install Pygame:

    ```bash
    pip install pygame
3. Run the game:

    ```bash
    python main.py
4. To create or edit maps:

    ```bash
    python custom_map.py
## License

Copyright (C) 2013-2014 KIDJourney

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

