import os
import msvcrt
import random

MAP_SIZE = int(input("Enter the map size you want: "))

PLAYER = 'P'
KEYS = [
    {'symbol': '1', 'position': [random.choice(range(MAP_SIZE)), random.choice(range(MAP_SIZE))], 'order': 1},
    {'symbol': '2', 'position': [random.choice(range(MAP_SIZE)), random.choice(range(MAP_SIZE))], 'order': 2},
    {'symbol': '3', 'position': [random.choice(range(MAP_SIZE)), random.choice(range(MAP_SIZE))], 'order': 3},
]
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

    for key in KEYS:
        while True:
            key_row = key['position'][0]
            key_col = key['position'][1]
            if (key_row != player_position[0] or key_col != player_position[1]) and game_map[key_row][key_col] == EMPTY:
                break

        game_map[key_row][key_col] = key['symbol']
        key['collected'] = False

    while True:
        door_row = random.randint(0, MAP_SIZE - 1)
        door_col = random.randint(0, MAP_SIZE - 1)
        if (door_row != player_position[0] or door_col != player_position[1]) and game_map[door_row][door_col] == EMPTY:
            break

    game_map[door_row][door_col] = DOOR

    return game_map

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def draw_map(game_map):
    clear_screen()
    print("=== THE ESCAPE GAME ===")
    print("Find Keys in order (1,2,3) first and get to the (D)oor")
    print()

    for row in game_map:
        print(' '.join(row))
    print()

    for key in KEYS:
        if not key['collected']:
            print(f"Collect {key['symbol']} (Order: {key['order']})")

    print(message)

    if all(key['collected'] for key in KEYS if key['order'] == 1) and all(key['collected'] for key in KEYS if key['order'] == 2) and all(key['collected'] for key in KEYS if key['order'] == 3):
        playing = False
        draw_game_won()

def draw_game_over():
    global playing
    clear_screen()
    print("=== GAME OVER ===")
    print("You failed to escape!")
    print()
    playing = False

def draw_game_won():
    global playing, message
    clear_screen()
    print("=== CONGRATULATIONS! ===")
    print("You have successfully escaped!")
    print()
    playing = False
    message = ""

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
        next_cell = game_map[next_position[0]][next_position[1]]

        if next_cell in [key['symbol'] for key in KEYS]:
            key_symbol = next_cell
            key_order = next(key['order'] for key in KEYS if key['symbol'] == key_symbol)

            if key_order == 1 or (key_order - 1 in [collected_key['order'] for collected_key in KEYS if collected_key['collected']]):
                game_map[next_position[0]][next_position[1]] = EMPTY
                key_collected = True

                for key in KEYS:
                    if key['symbol'] == key_symbol:
                        key['collected'] = True
                        break

                game_map[player_position[0]][player_position[1]] = EMPTY
                player_position = next_position
                game_map[player_position[0]][player_position[1]] = PLAYER
                message = f"You have acquired key {key_symbol}!"

                if all(key['collected'] for key in KEYS if key['order'] == 1) and all(key['collected'] for key in KEYS if key['order'] == 2) and all(key['collected'] for key in KEYS if key['order'] == 3):
                    playing = False
                    draw_game_won()

        elif next_cell == DOOR:
            if all(key['collected'] for key in KEYS):
                playing = False
                draw_game_won()
            else:
                message = "You need to collect all keys first"

        elif next_cell == EMPTY:
            game_map[player_position[0]][player_position[1]] = EMPTY
            player_position = next_position
            game_map[player_position[0]][player_position[1]] = PLAYER

        draw_map(game_map)

    if not playing:
        return

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