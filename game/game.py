from models import Player, Computer, Round_Counter
from exceptions import InvalidInputError, InvalidRollError
from settings import GAME_LEVELS, GAME_LEVELS_CONVERT

# create a player
def get_name():
    name = input('Enter your name: ')
    return name

def create_player(name):
    player = Player(name)
    return player


#choosing game level, getting level data, printing player's choise
def offer_game_lvl():
    print('''Choose the level of game:
    1 - игра будет длинной в 5 раундов(режим short).
    2 - игра будет длинной в 8 раундов(режим medium).
    3 - игра будет длинной в 10 раундов(режим long).''')


def get_game_lvl():
    while True:
        try:
            user_input = input('Enter the number of option (1-3): ')
            if not user_input.isdigit():
                raise InvalidInputError("Error: Wrond data entered. Try again.")
            game_lvl =  int(user_input)

            if game_lvl < 1 or game_lvl > 3:
                raise InvalidInputError("Error: Wrond number entered. Try again.")
            return game_lvl
        
        except InvalidInputError as e:
            print(e)


def convert_lvl(game_lvl):
    if not game_lvl in GAME_LEVELS:
        return None
    rounds_count = GAME_LEVELS[game_lvl]
    lvl_name = GAME_LEVELS_CONVERT[rounds_count]
    return rounds_count, lvl_name


def show_lvl_info(rounds_count, lvl_name):
    print(f"You chose {lvl_name} level, you will play {rounds_count} rounds. Good luck!")


# intro function: creates and returns player and returns game level data

def intro():
    name = get_name()
    player = create_player(name)
    while True:
        offer_game_lvl()
        game_lvl = get_game_lvl()
        if game_lvl is None:
            print('Something went wrong. Please try again.')
            continue
        rounds_count, lvl_name = convert_lvl(game_lvl)
        show_lvl_info(rounds_count, lvl_name)
        return player, rounds_count