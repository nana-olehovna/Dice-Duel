# save_result(name, rounds, score): сохранение нового результата в game_results.json.

# get_results(): чтение всех результатов из файла и вывод в консоль.
#final score valuation


#counting score of current round
def count_round_score(player_round_score, bot_round_score):
    round_score = player_round_score - bot_round_score
    print(f"Your score in this round = {round_score}")
    return round_score


#rewriting player's score in player's data
def save_score(player, round_score):
    player.increase_score(round_score)
