list_str = [i.strip("\n ") for i in open("data.txt")]

def convert_str(str_in):
    str_out = ""
    dict_convert = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9, }
    for key in dict_convert:
        count_key = str_in.count(key)
        key_1, key_2 = key[1:], key[:-1]
        if key in str_in:
            if str_out:
                count_key_out = str_out.count(key)
                if count_key_out == count_key:
                    str_out = str_out.replace(key, str(dict_convert[key]))
                else:
                    if count_key == str_out.count(key_1):
                        str_out = str_out.replace(key_1, str(dict_convert[key]))
                    elif count_key == str_out.count(key_2):
                        str_out = str_out.replace(key_2, str(dict_convert[key]))
            else:
                str_out = str_in.replace(key, str(dict_convert[key]))
    return str_out if str_out else str_in
list_str_convert = [convert_str(i) for i in list_str]
def get_sum(list_data):
    sum_all = 0
    for i in list_data:
        list_num_ = [j for j in i if j.isdigit()]
        if list_num_:
            sum_all += int(list_num_[0] + list_num_[-1])
    return sum_all
print(f"Решение задания 1: {get_sum(list_str)}")
print(f"Решение задания 2: {get_sum(list_str_convert)}")