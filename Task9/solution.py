list_str = [i.strip("\n ").split() for i in open("input.txt")]
list_num = [[int(j) for j in i] for i in list_str]
def get_sum(list_start):
    summ_all = list_start[-1]
    while True:
        if not any(list_start):
            break
        len_l = len(list_start) - 1
        list_start = [list_start[idx+1] - i for idx, i in enumerate(list_start) if idx < len_l]
        summ_all += list_start[-1]
    return summ_all
print(f"Решение задания 1:{sum([get_sum(i) for i in list_num])}")
print(f"Решение задания 2:{sum([get_sum(i[::-1]) for i in list_num])}")