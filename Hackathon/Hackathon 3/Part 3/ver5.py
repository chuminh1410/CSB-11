import os
import msvcrt
import random

MAP_SIZE = int(input("Enter the map size you want: "))

PLAYER = 'P'
KEY = 'K'
DOOR = 'D'
EMPTY = '-'

player_position = [0, 0]

key_position = [random.choice(range(MAP_SIZE)), random.choice(range(MAP_SIZE))]
door_position = [random.choice(range(MAP_SIZE)), random.choice(range(MAP_SIZE))]

playing = True
key_collected = False
message = ""

def initialize_map():
    game_map = [[EMPTY] * MAP_SIZE for _ in range(MAP_SIZE)]
    game_map[player_position[0]][player_position[1]] = PLAYER
    
    while True:
        key_row = random.randint(0, MAP_SIZE - 1)
        key_col = random.randint(0, MAP_SIZE - 1)
        if key_row != player_position[0] or key_col != player_position[1]:
            break

    while True:
        door_row = random.randint(0, MAP_SIZE - 1)
        door_col = random.randint(0, MAP_SIZE - 1)
        if (door_row != player_position[0] or door_col != player_position[1]) and (door_row != key_row or door_col != key_col):
            break

    game_map[key_row][key_col] = KEY
    game_map[door_row][door_col] = DOOR
    
    return game_map


def draw_map(game_map):
    os.system('cls' if os.name == 'nt' else 'clear')
    for row in game_map:
        print(' '.join(row))
    print()
    print("=== THE ESCAPE GAME ===")
    print("Use W/A/S/D to move (P)layer, press Q to quit")
    print("Find (K)ey first and get to the (D)oor")
    print(message)
    print()


def move_player(move):
    global playing, key_collected, message, player_position

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
            message = "Congratulations! You have successfully escaped!"
        elif game_map[next_position[0]][next_position[1]] == KEY:
            game_map[next_position[0]][next_position[1]] = EMPTY
            key_collected = True
            player_position = next_position
            message = "You have acquired the key!"
        elif game_map[next_position[0]][next_position[1]] == EMPTY:
            game_map[player_position[0]][player_position[1]] = EMPTY
            game_map[next_position[0]][next_position[1]] = PLAYER
            player_position = next_position

        draw_map(game_map)

    if not key_collected and game_map[player_position[0]][player_position[1]] == DOOR:
        message = "You need to find the key first"


game_map = initialize_map()

print("=== THE ESCAPE GAME ===")
print("Use W/A/S/D to move (P)layer, press Q to quit")
print("Find (K)ey first and get to the (D)oor")

while playing:
    draw_map(game_map)

    move = msvcrt.getch().decode('utf-8').upper()

    if move == 'Q':
        break
    move_player(move)
