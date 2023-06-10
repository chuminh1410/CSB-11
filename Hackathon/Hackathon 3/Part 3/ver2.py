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
