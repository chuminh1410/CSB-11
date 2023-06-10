import os
import msvcrt

MAP_SIZE = 5

PLAYER = 'P'
KEY = 'K'
DOOR = 'D'
EMPTY = '-'

player_position = [0, 0]

key_position = [2, 3]
door_position = [4, 2]

playing = True
key_collected = False

def initialize_map():
    game_map = [[EMPTY] * MAP_SIZE for _ in range(MAP_SIZE)]
    game_map[player_position[0]][player_position[1]] = PLAYER
    game_map[key_position[0]][key_position[1]] = KEY
    game_map[door_position[0]][door_position[1]] = DOOR
    return game_map

def draw_map(game_map):
    os.system('cls' if os.name == 'nt' else 'clear')
    for row in game_map:
        print(' '.join(row))
    print()
    
def move_player(move):
    global playing, key_collected

    if move == 'W':
        next_position = [player_position[0] - 1, player_position[1]]
    elif move == 'S':
        next_position = [player_position[0] + 1, player_position[1]]
    elif move == 'A':
        next_position = [player_position[0], player_position[1] - 1]
    elif move == 'D':
        next_position = [player_position[0], player_position[1] + 1]
    else:
        return

    if (
        0 <= next_position[0] < MAP_SIZE
        and 0 <= next_position[1] < MAP_SIZE
    ):
        if game_map[next_position[0]][next_position[1]] == DOOR and key_collected:
            playing = False
            print("Congrats escaping")
        elif game_map[next_position[0]][next_position[1]] == KEY:
            game_map[next_position[0]][next_position[1]] = EMPTY
            key_collected = True
            player_position[0], player_position[1] = next_position
            print("You have aquired the key")
        elif game_map[next_position[0]][next_position[1]] == EMPTY:
            game_map[player_position[0]][player_position[1]] = EMPTY
            player_position[0], player_position[1] = next_position
            game_map[player_position[0]][player_position[1]] = PLAYER

    draw_map(game_map)

    if not key_collected and game_map[player_position[0]][player_position[1]] == DOOR:
        print("You need to find the key first")


        
game_map = initialize_map()

while playing:
    draw_map(game_map)
    print("=== THE ESCAPE GAME ===")
    print("Use W/A/S/D to move (P)layer, press Q to quit")
    print("Find (K)ey first and get to the (D)oor")

    move = msvcrt.getch().decode('utf-8').upper()

    if move == 'Q':
        break
    move_player(move)
