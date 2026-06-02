import json


#counting score of current round
def count_round_score(player_round_score, bot_round_score):
    round_score = player_round_score - bot_round_score
    print(f"Your score in this round = {round_score}")
    return round_score


#rewriting player's score in player's data
def save_score(player, round_score):
    player.increase_score(round_score)


def open_results():
    with open('game/game_results.json', 'r', encoding='UTF-8') as file:
        results = json.load(file)
    return results


def add_results(results, date, player,rounds_count):
    results.append({
        "Date": date,
        "Name": player.name,
        "Rounds played": rounds_count,
        "Final score": player._score
    })
    with open('game/game_results.json', 'w', encoding='UTF-8') as file:
        json.dump(results,file,indent=4)


def save_results(date, player,rounds_count):
    results = open_results()
    add_results(results, date, player,rounds_count)


def get_results():
    results = open_results()
    for x in results:
        for a in x:
            print(f"{a}: {x[a]}")
        print('-------------------')
