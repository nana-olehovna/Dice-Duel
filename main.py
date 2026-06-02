from game.game import play_game
from game.score import save_results, get_results
from game.utils import ValidateInputMixin
from game.settings import MAIN_MENU_OPTIONS


#    Main game scenario
def game_scenario():
    date, player, rounds_count = play_game()
    save_results(date, player, rounds_count)


#    App
def game():
    print("Hi, this is a simple way to find out how lucky you are")
    options = ValidateInputMixin()
    while True:
        valid_option = options.validate_input(MAIN_MENU_OPTIONS)
        if valid_option == 1:
            game_scenario()
        elif valid_option == 2: 
            get_results()
        else:
            print("Already leaving? Hope, you will have a better luck today! See you.")
            break


#RUN THE CODE
game()




