from datetime import datetime

from .models import Player, Computer, Round_Counter
from .exceptions import InvalidInputError, InvalidRollError
from .settings import GAME_LEVELS, GAME_LEVELS_CONVERT
from .score import count_round_score, save_score, save_results, show_results

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


# player, rounds_count = intro()


#creating bot opponent
# bot = Computer()


#            temporary player data (DELETE this block)       
# player = Player('Nana')
# rounds_count = 5
#                                                            



#       GAME PROCESS


#definition and validation of moves

def roll_is_valid():
    while True:
        try:
            move_input = input('Roll the cube: (Press "Enter")')
            if move_input.strip() != "":
                raise InvalidRollError('Error: move was not make. Try again')
            return True
        except InvalidRollError as e:
            print(e)

def player_moves(player):
    roll_is_valid()
    if roll_is_valid:
        player_round_score = player.roll()
        print(f"You scored {player_round_score}")
        return player_round_score
#   else what????

def bot_moves(bot):
    bot_round_score = bot.roll()
    print(f"Computer scored {bot_round_score}")
    return bot_round_score


#saving date and time of game
def fetch_date():
    date = datetime.now()
    return date.strftime("%Y-%m-%d %H:%M:%S")

#definig round and game scenario

# round_number = Round_Counter()

def play_round(round_number, player, bot):
    while True:
        print(f"Round {round_number._value} started")
        player_round_score = player_moves(player)
        bot_round_score = bot_moves(bot)
        round_score = count_round_score (player_round_score, bot_round_score)
        if round_score == 0:
            print("Oops... Can't be equal. Always must be a winner. Play the same round again!")
            continue
        return round_score


def play_rounds_loop(player, round_number, rounds_count, bot):
    while round_number._value <= rounds_count:
        round_score = play_round(round_number, player, bot)
        save_score(player, round_score)
        print(f'''Round {round_number._value} finished
----------------------------------''')
        round_number.increase_round_number()


def play_game():
    player, rounds_count = intro()
    bot = Computer()
    round_number = Round_Counter()
    play_rounds_loop(player, round_number, rounds_count, bot)
    print(f"{player.name}'s final score of the game is {player._score}")
    date = fetch_date()
    return date, player, rounds_count




