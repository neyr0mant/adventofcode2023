list_str = [i.strip("\n ").split() for i in open("input.txt")]
list_num = []
for i in list_str:
    list_num.append([int(j) for j in i])
def get_next_list(list_in):
    next_list = []
    for idx, i in enumerate(list_in):
        if idx < len(list_in)-1:
            next_list.append(list_in[idx+1] - i)
    return next_list
def get_sum(list_in, part = 1):
    list_start = list_in if part == 1 else list_in[::-1]
    summ_all = list_in[-1] if part ==1 else list_in[0]
    cur_list = list_start
    while True:
        new_list = get_next_list(cur_list)
        if not any(new_list):
            break
        else:
            summ_all += new_list[-1]
            cur_list = new_list
    return summ_all
print(f"Решение задания 1:{sum([get_sum(i) for i in list_num])}")
print(f"Решение задания 2:{sum([get_sum(i, part=2) for i in list_num])}")


