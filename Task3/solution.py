#https://adventofcode.com/2023/day/3
list_str = [i.strip("\n ") for i in open("data.txt")]

def find_num_in_str(str_in, index):
    cur_symbol, len_str = str_in[index], len(str_in)
    str_left, str_right = '', ''
    cur_num = str_in[index] if str_in[index] else ""
    stop_l, stop_r = False, False
    i = 1
    while True:
        if not stop_l:
            if index-i >= 0:
                if str_in[index-i].isdigit():
                    str_left += str_in[index-i]
                else:
                    stop_l = True
            else:
                stop_l = True
        if not stop_r:
            if index+i < len_str:
                if str_in[index+i].isdigit():
                    str_right += str_in[index+i]
                else:
                    stop_r = True
            else:
                stop_r = True
        if stop_l and stop_r:
            break
        i += 1
    return [str_left[::-1] + cur_num + str_right] if cur_num.isdigit() else [str_left[::-1], str_right]
def get_answer(part=1):
    answer_1, answer_2 = 0, 0
    for number_str, cur_str in enumerate(list_str):
        for index_symbol, candidate in enumerate(cur_str):
            assertion_condition = candidate != "." and not candidate.isdigit() if part == 1 else (
                    candidate == "*")
            if assertion_condition:
                list_num = []
                for str_ in [list_str[number_str - 1], cur_str, list_str[number_str + 1]]:
                    for num in find_num_in_str(str_, index_symbol):
                        if num.isdigit():
                            if part == 2:
                                list_num.append(int(num))
                            else:
                                answer_1 += int(num)
                if len(list_num) == 2:
                    answer_2 += list_num[0]*list_num[1]
    return answer_1 if part == 1 else answer_2
import time
t_start = time.time()
for i in range(1000):
    get_answer(part=2)
t_finish = time.time()
print(f"Время выполнения за 1000 циклов составило: {t_finish- t_start}")
print(f"Решение задания 1:{get_answer(part=1)}")
print(f"Решение задания 2:{get_answer(part=2)}")








