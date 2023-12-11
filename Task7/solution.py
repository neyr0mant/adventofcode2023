#https://adventofcode.com/2023/day/7
list_str = [i.strip("\n ").split() for i in open("input.txt")]
dict_data = {i[0]:i[1] for i in list_str}
from collections import Counter

def get_key_max_rank(hand_, power_dict):
    key = ""
    max_rank = 0
    for i in hand_:
        rank_key = power_dict[i]
        if rank_key > max_rank:
            key = i
            max_rank = rank_key
    return key
def get_index_type(hand_in):
    list_power_hand = [[1, 1, 1, 1, 1], [1, 1, 1, 2], [1, 2, 2], [1, 1, 3], [2, 3], [1, 4], [5]]
    hand_dict = dict(Counter(hand_in))
    list_assert = list(hand_dict.values())
    list_assert.sort()
    return list_power_hand.index(list_assert), list_assert
def get_type_hand(hand_in, dict_power):
    hand_dict = dict(Counter(hand_in))
    index_type, list_assert = get_index_type(hand_in)
    if dict_power:
        count_j = hand_in.count("J")
        if count_j:
            count_max = list_assert[-1]
            key_assert = [card for card, count in hand_dict.items() if count == count_max]
            if "J" in key_assert and len(key_assert) == 1:
                key_replace = get_key_max_rank(hand_in, dict_power)
                replace_card = hand_in.replace("J", key_replace)
                index_type_replace = get_index_type(replace_card)[0]
            else:
                key_replace_dict = {card: rank for card, rank in dict_power.items() if card in key_assert}
                max_rank = max(list(key_replace_dict.values()))
                key_replace = [card for card, rank in key_replace_dict.items() if rank == max_rank][0]
                replace_card = hand_in.replace("J", key_replace)
                index_type_replace = get_index_type(replace_card)[0]
            return index_type_replace, hand_in
    return index_type, hand_in

def get_hand_power_id(hand, part = 1, joker_sort = ""):
    power_dict = {'2': 11, '3': 12, '4': 13, '5': 14, '6': 15, '7': 16, '8': 17, '9': 18, 'T': 19, 'J': 20, 'Q': 21,
                  'K': 22, 'A': 23} if part == 1 else {'J': 11, '2': 12, '3': 13, '4': 14, '5': 15, '6': 16, '7': 17,
                                                       '8': 18, '9': 19, 'T': 20, 'Q': 21, 'K': 22, 'A': 23}
    dict_power = {} if part == 1 else power_dict
    id_type_hand, hand = get_type_hand(hand, dict_power=dict_power)
    if joker_sort:
        id_type_hand = joker_sort
    id_big_card = "".join([str(power_dict[i]) for i in hand])
    return int(str(id_type_hand) + id_big_card), hand, id_type_hand

def get_answer(data_in, part=1):
    list_hand = list(data_in.keys())
    answer = 0
    list_hand.sort(key=lambda power: get_hand_power_id(power, part=part))
    rank_data = {}
    for idx, hand in enumerate(list_hand, start=1):
        if part == 1:
            answer += idx*int(dict_data[hand])
        else:
            res = get_hand_power_id(hand, part=part)
            hand_out, id_type_hand = res[1], res[2]
            res_get = rank_data.get(str(id_type_hand))
            if res_get:
                rank_data[str(id_type_hand)].append(hand)
            else:
                rank_data.update({str(id_type_hand):[hand]})
    if part == 2:
        rank_data_list = list(rank_data.keys())
        rank_data_list.sort()
        idx_all = 0
        for rank_type_hand in rank_data_list:
            list_hand_for_type = rank_data[rank_type_hand]
            list_hand_for_type.sort(key=lambda power: get_hand_power_id(power, part=2, joker_sort=rank_type_hand))
            for idx, hand_ in enumerate(list_hand_for_type,start=1):
                idx_all = idx if not idx_all else idx_all
                answer += idx_all*int(dict_data[hand_])
                idx_all += 1
    return answer
print(f"Решение задания 1:{get_answer(dict_data, part=1)}")
print(f"Решение задания 2:{get_answer(dict_data, part=2)}")






