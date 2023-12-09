#https://adventofcode.com/2023/day/6
list_str = [i.strip("\n ").split(":") for i in open("input.txt")]
list_time = [i[1].replace("      ", "").split()for i in list_str]
data_1 = {}
for idx, i in enumerate(range(len(list_time[0]))):
    data_1.update({f"GAME {idx+1}": {"Time": int(list_time[0][idx]), "Distance": int(list_time[1][idx])}})
def get_answer(data_in):
    answer = 1
    for data_game in data_in.values():
        max_distance = data_game['Distance']
        max_time = data_game['Time']
        list_distance = []
        for t in range(max_time):
            list_distance.append(t*(max_time-t))
        count = len([i for i in list_distance if i > max_distance])
        answer *= count
    return answer

data_2 = {"SUPER GAME": {}}
for key, val in data_1.items():
    if not data_2["SUPER GAME"]:
        data_2["SUPER GAME"].update({"Time": val["Time"], "Distance": val["Distance"]})
    else:
        cur_time = str(data_2["SUPER GAME"]["Time"])
        cur_distance = str(data_2["SUPER GAME"]["Distance"])
        data_2["SUPER GAME"]["Time"] = int(cur_time + str(val["Time"]))
        data_2["SUPER GAME"]["Distance"] = int(cur_distance + str(val["Distance"]))
print(f"Решение задания 1:{get_answer(data_1)}")
print(f"Решение задания 2:{get_answer(data_2)}")


