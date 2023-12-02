#https://adventofcode.com/2023/day/1
list_str = [i.strip("\n ") for i in open("data.txt")]
def get_fist_digit(str_in, reverse=False, part =1):
    dict_convert = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9,}
    for idx, i in enumerate(str_in):
        if i.isdigit():
            return i
        if part ==2:
            for key, val in dict_convert.items():
                key_ = key if not reverse else key[::-1]
                if key_ in str_in[:idx+1]:
                    return str(dict_convert[key])
print(f"Решение задания 1: {sum([(int(get_fist_digit(i)+get_fist_digit(i[::-1], reverse=True))) for i in list_str])}")
print(f"Решение задания 2: {sum([(int(get_fist_digit(i, part=2)+get_fist_digit(i[::-1], reverse=True, part=2))) for i in list_str])}")