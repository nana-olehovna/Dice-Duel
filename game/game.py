from datetime import datetime

from .models import Player, Computer
from .exceptions import InvalidRollError
from .settings import GAME_LEVELS, GAME_LEVELS_CONVERT, GAME_LEVEL_OPTIONS
from .score import count_round_score, save_score
from .utils import ValidateInputMixin, Round_Counter


def get_name():
    name = input('Enter your name: ')
    return name

def create_player(name):
    player = Player(name)
    return player

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
        get_lvl = ValidateInputMixin()
        game_lvl = get_lvl.validate_input(GAME_LEVEL_OPTIONS)
        if game_lvl is None:
            print('Something went wrong. Please try again.')
            continue
        rounds_count, lvl_name = convert_lvl(game_lvl)
        show_lvl_info(rounds_count, lvl_name)
        return player, rounds_count


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


def valuate_game_result(player):
    if player._score > 0:
        print("You are the WINNER!")
        if player._score > 6:
            print("WOW. That's what I call a Good Luck")
    elif player._score == 0:
        print("It's a draw. I offer you play again, just for clarity)))")
    else:
        print("Sorry. You lost this game")
        if player._score < -6:
            print("Oh... It's not your day, mate.")


def play_game():
    player, rounds_count = intro()
    bot = Computer()
    round_number = Round_Counter()
    play_rounds_loop(player, round_number, rounds_count, bot)
    print(f"{player.name}'s final score of the game is {player._score}")
    valuate_game_result(player)
    date = fetch_date()
    return date, player, rounds_count
