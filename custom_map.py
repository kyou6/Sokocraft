import pygame
import sys
import tkinter as tk
from tkinter import simpledialog, messagebox, filedialog
import os

GRID_SIZE = 64
WHITE = (255, 255, 255)

pygame.init()

# Function to get grid size
def get_grid_size():
    root = tk.Tk()
    root.withdraw()

    # Prompt the user for width and height
    width = simpledialog.askinteger("Input", "Enter grid width (number of columns, max 24):", minvalue=1, maxvalue=24)
    height = simpledialog.askinteger("Input", "Enter grid height (number of rows, max 12):", minvalue=1, maxvalue=12)

    root.destroy()

    return width, height

# Function to load existing map
def load_map(filename):
    with open(filename, 'r') as f:
        height, width = map(int, f.readline().strip().split())
        game_map = [list(f.readline().strip()) for _ in range(height)]
    
    # Updates grid based on the imported map
    player_found = False  # Flag to check if a player exists in the imported map
    for y in range(height):
        for x in range(width):
            char = game_map[y][x]
            if char == 'W':
                game_map[y][x] = 'W'  # Wall
            elif char == 'P':
                game_map[y][x] = 'P'  # Player
                player_found = True  # Set flag if player is found
            elif char == 'G':
                game_map[y][x] = 'G'  # Goal
            elif char == 'B':
                game_map[y][x] = 'B'  # Box
            else:
                game_map[y][x] = 'N'  # Empty space
                
    return width, height, game_map, player_found  # Return player_found status

# Function to prompt user for map creation or import
def map_prompt():
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    choice = messagebox.askquestion("Map Options", "Do you want to create a New Map? (Yes for New, No for Import)")

    if choice == 'yes':
        return get_grid_size(), None  # Return grid size and None for map
    else:
        filename = filedialog.askopenfilename(title="Select a map file", filetypes=[("Map files", "*.dat")])
        if filename and os.path.isfile(filename):
            return None, load_map(filename)  # Return None for grid size and loaded map
        else:
            messagebox.showerror("Error", "Invalid filename or file does not exist.")
            sys.exit()

# Get user-defined grid size or load existing map
grid_size, loaded_map = map_prompt()
if loaded_map:
    GRID_WIDTH, GRID_HEIGHT, game_map, player_placed = loaded_map  # Update to include player_placed
else:
    GRID_WIDTH, GRID_HEIGHT = grid_size
    game_map = [['N' for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]

# Set up the display
screen = pygame.display.set_mode((GRID_WIDTH * GRID_SIZE, GRID_HEIGHT * GRID_SIZE))
pygame.display.set_caption("Map Builder")

# Load images after initializing the display
Image_Box_Outplace = pygame.image.load("source/box_no.png").convert()
Image_Goal = pygame.image.load("source/power.png").convert()
Image_Wall = pygame.image.load("source/wall.png").convert()
Image_Player = pygame.image.load("source/player.png").convert()

Image_Box_Outplace = pygame.transform.scale(Image_Box_Outplace, (64, 64))
Image_Goal = pygame.transform.scale(Image_Goal, (64, 64))
Image_Wall = pygame.transform.scale(Image_Wall, (64, 64))
Image_Player = pygame.transform.scale(Image_Player, (64, 64))

# Undo and Redo stacks
undo_stack = []
redo_stack = []

def save_state():
    # Save the current state of the game_map to the undo stack
    undo_stack.append([row[:] for row in game_map])  # Deep copy of the game_map
    if len(undo_stack) > 10:  # Limit the size of the undo stack
        undo_stack.pop(0)

def undo():
    if undo_stack:
        redo_stack.append([row[:] for row in game_map])  # Save current state to redo stack
        game_map[:] = undo_stack.pop()  # Restore the last state from undo stack

def redo():
    if redo_stack:
        save_state()  # Save current state to undo stack before redoing
        game_map[:] = redo_stack.pop()  # Restore the last state from redo stack

def draw_grid():
    for x in range(GRID_WIDTH):
        for y in range(GRID_HEIGHT):
            rect = pygame.Rect(x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE)
            if game_map[y][x] == 'W':
                screen.blit(Image_Wall, rect.topleft)  # Draw wall image
            elif game_map[y][x] == 'B':
                screen.blit(Image_Box_Outplace, rect.topleft)  # Draw box image
            elif game_map[y][x] == 'G':
                screen.blit(Image_Goal, rect.topleft)  # Draw goal image
            elif game_map[y][x] == 'P':
                screen.blit(Image_Player, rect.topleft)  # Draw player image
            else:
                pygame.draw.rect(screen, WHITE, rect)  # Draw empty space
            pygame.draw.rect(screen, (0, 0, 0), rect, 1)  # Draw grid lines

def save_map(filename):
    with open(filename, 'w') as f:
        f.write(f"{GRID_HEIGHT} {GRID_WIDTH}\n")
        for row in game_map:
            f.write("".join(row) + "\n")
    print(f"Map saved to {filename}")

def save_prompt():
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    # Check if there is at least one player in the game_map
    player_exists = any('P' in row for row in game_map)  # Check for 'P' in the grid

    if not player_exists:
        messagebox.showerror("Error", "Please place a player on the grid before saving.")
        return  # Exit the function if no player exists

    choice = messagebox.askquestion("Save Map", "Do you want to save the map before exiting?")
    
    if choice == 'yes':
        # Open file dialog with "map" folder as default location
        filename = filedialog.asksaveasfilename(initialdir="map", title="Save Map", defaultextension=".dat", filetypes=[("Map files", "*.dat")])
        if filename:
            save_map(filename)
    # Exit the program
    pygame.quit()
    sys.exit()

def main():
    current_object = 'W'  # Default to wall
    player_placed = False  # Track if the player has been placed
    player_position = None  # Initialize player position

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                save_prompt()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    current_object = 'W'  # Wall
                elif event.key == pygame.K_2:
                    current_object = 'B'  # Box
                elif event.key == pygame.K_3:
                    current_object = 'G'  # Goal
                elif event.key == pygame.K_4:
                    current_object = 'P'  # Set player
                elif event.key == pygame.K_5:
                    current_object = 'N'  # Delete mode (set to empty)
                elif event.key == pygame.K_z and pygame.key.get_mods() & pygame.KMOD_CTRL:  # Ctrl + Z
                    undo()
                elif event.key == pygame.K_y and pygame.key.get_mods() & pygame.KMOD_CTRL:  # Ctrl + Y
                    redo()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                grid_x = x // GRID_SIZE
                grid_y = y // GRID_SIZE
                if 0 <= grid_x < GRID_WIDTH and 0 <= grid_y < GRID_HEIGHT:
                    save_state()  # Save the state before making a change
                    if current_object == 'N':
                        game_map[grid_y][grid_x] = 'N'  # Delete the object
                        if player_placed and (grid_y, grid_x) == player_position:  # Check if deleting the player
                            player_placed = False  # Reset player placed status
                            player_position = None  # Reset player position
                    elif current_object == 'P':
                        if not player_placed:  # Check if player can be placed
                            game_map[grid_y][grid_x] = 'P'  # Place player
                            player_position = (grid_y, grid_x)  # Store player position
                            player_placed = True  # Set player placed status
                        else:
                            # If player is already placed, do not allow placing another
                            messagebox.showinfo("Info", "A player is already placed on the grid.")
                    elif current_object != 'P':
                        game_map[grid_y][grid_x] = current_object

        screen.fill(WHITE)
        draw_grid()
        pygame.display.flip()

if __name__ == "__main__":
    main()