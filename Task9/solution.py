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

def get_sum_recursion(list_in, old_summ = 0):
    list_start = list_in
    summ_all = list_in[-1] + old_summ
    new_list = get_next_list(list_start)
    if not any(new_list):
        return summ_all
    else:
        return get_sum_recursion(new_list, old_summ=summ_all)

def get_sum_wile(list_in):
    list_start = list_in
    summ_all = list_start[-1]
    cur_list = list_start
    while True:
        new_list = get_next_list(cur_list)
        if not any(new_list):
            break
        else:
            summ_all += new_list[-1]
            cur_list = new_list
    return summ_all
print(f"Решение задания 1 через while:{sum([get_sum_wile(i) for i in list_num])}")
print(f"Решение задания 2 через while:{sum([get_sum_wile(i[::-1]) for i in list_num])}")
print(f"Решение задания 1 рекурсией:{sum([get_sum_recursion(i) for i in list_num])}")
print(f"Решение задания 2 рекурсией:{sum([get_sum_recursion(i[::-1]) for i in list_num])}")
