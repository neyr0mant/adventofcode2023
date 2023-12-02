dict_data = {}
for i in open("data.txt"):
    str_ = i.strip("\n ")
    index_game = str_.split(":")[0].split()[1]
    dict_data.update({index_game: {}})
    list_game = str_.split(":")[1:][0].replace(";", ",").split(",")
    for j in list_game:
        list_j = j.split()
        key_1, key_2 = list_j[0], list_j[1]
        if key_1.isdigit():
            if dict_data[index_game].get(key_2):
                dict_data[index_game][key_2].append(int(key_1))
            else:
                dict_data[index_game].update({key_2: [int(key_1)]})
        else:
            if dict_data[index_game].get(key_1):
                dict_data[index_game][key_1].append(int(key_2))
            else:
                dict_data[index_game].update({key_1: [int(key_2)]})
dict_rule = {"red":12, 'green':13, 'blue':14}
set_not_impossible_game = set()
all_summ_game = 0
for game, data_game in dict_data.items():
    game = int(game)
    all_summ_game += game
    for key, count in dict_rule.items():
        data_game_for_key = data_game.get(key)
        if data_game_for_key:
            if max(data_game_for_key) > count:
                set_not_impossible_game.add(game)
                break
power = 0
for game, data_game in dict_data.items():
    list_max = []
    for key, list_count in data_game.items():
        list_max.append(max(list_count))
    power_game = 1
    for i in list_max:
        power_game *=i
    power +=power_game
print(f"Решение задания 1: {all_summ_game - sum(set_not_impossible_game)}")
print(f"Решение задания 2: {power}")

