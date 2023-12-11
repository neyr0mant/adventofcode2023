#https://adventofcode.com/2023/day/8
list_str = [i.strip("\n ") for i in open("input.txt")]
dict_data = {}
for idx, str_ in enumerate(list_str):
    if idx == 0:
        list_rule = [0 if i == "L" else 1 for i in str_ ]
    else:
        if str_:
            key_list = str_.replace("(", "").replace(")", "").replace(",", "").replace(" =", "").split()
            dict_data.update({key_list[0]: [key_list[1], key_list[2]]})

import math

def get_list_gcd(list_gcd):
    lcm = 1
    for i in list_gcd:
        lcm = lcm*i//math.gcd(lcm, i)
    return lcm

def get_answer(rule, data, part=1):
    count_iter_1, list_cycle_for_key = 0, []
    if part == 1:
        count_iter_1 = 0
        start_key = "AAA"
        while True:
            find_z = False
            for rule_ in rule:
                if part == 1:
                    count_iter_1 += 1
                    cur_key = data[start_key][rule_]
                    if cur_key == "ZZZ":
                        find_z = True
                    else:
                        start_key = cur_key
            if find_z:
                break
    else:
        list_start_keys = [i for i in list(data.keys()) if i[-1] == "A"]
        for key in list_start_keys:
            count_iter = 0
            start_key = key
            dict_key_find = {}
            find_z = False
            while True:
                for rule_ in rule:
                    count_iter += 1
                    cur_key = data[start_key][rule_]
                    if cur_key[-1] == "Z":
                        key_id = start_key+str(rule_)
                        if key_id in dict_key_find.keys():
                            list_cycle_for_key.append(dict_key_find[key_id])
                            find_z = True
                            break
                        else:
                            dict_key_find.update({key_id: count_iter})
                    start_key = cur_key
                if find_z:
                    break
    return count_iter_1 if part == 1 else get_list_gcd(list_cycle_for_key)

print(f"Решение задания 1:{get_answer(list_rule, dict_data)}")
print(f"Решение задания 2:{get_answer(list_rule, dict_data, part=2)}")
