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


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def draw_map(game_map):
    clear_screen()
    print("=== THE ESCAPE GAME ===")
    print("Find (K)ey first and get to the (D)oor")
    print()

    for row in game_map:
        print(' '.join(row))
    print()


def draw_game_over():
    clear_screen()
    print("=== GAME OVER ===")
    print("You failed to escape!")
    print()


def draw_game_won():
    clear_screen()
    print("=== CONGRATULATIONS! ===")
    print("You have successfully escaped!")
    print()


def move_player(move, game_map):
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

    if 0 <= next_position[0] < MAP_SIZE and 0 <= next_position[1] < MAP_SIZE:
        if game_map[next_position[0]][next_position[1]] == KEY:
            game_map[next_position[0]][next_position[1]] = EMPTY
            key_collected = True
            game_map[player_position[0]][player_position[1]] = EMPTY
            player_position = next_position
            game_map[player_position[0]][player_position[1]] = PLAYER
            message = "You have acquired the key!"
        elif game_map[next_position[0]][next_position[1]] == DOOR:
            if door_position[0] == player_position[0] and door_position[1] == player_position[1] and key_collected:
                playing = False
                draw_game_won()

            else:
                message = "You need to find the key first"
        elif game_map[next_position[0]][next_position[1]] == EMPTY:
            game_map[player_position[0]][player_position[1]] = EMPTY
            player_position = next_position
            game_map[player_position[0]][player_position[1]] = PLAYER

        draw_map(game_map)

    if not playing:
        return

    if door_position == player_position and key_collected:
        playing = False
        draw_game_won()





game_map = initialize_map()

clear_screen()
print("=== THE ESCAPE GAME ===")
print("Use W/A/S/D to move (P)layer, press Q to quit")
print("Find (K)ey first and get to the (D)oor")


while playing:
    draw_map(game_map)

    move = msvcrt.getch().decode('utf-8').upper()

    if move == 'Q':
        break
    move_player(move, game_map)

draw_game_over()
