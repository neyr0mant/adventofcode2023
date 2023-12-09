list_str = [i.strip("\n ").split() for i in open("input.txt")]
list_num = []
for i in list_str:
    list_num.append([int(j) for j in i])
def get_sum(list_start):
    summ_all = list_start[-1]
    while True:
        len_l = len(list_start) - 1
        list_start = [list_start[idx+1] - i for idx, i in enumerate(list_start) if idx < len_l]
        if not any(list_start):
            break
        else:
            summ_all += list_start[-1]
    return summ_all
import time
t1 = time.time()
print(f"Решение задания 1:{sum([get_sum(i) for i in list_num])}")
t2 = time.time()
print(t2-t1)
t1 = time.time()
print(f"Решение задания 2:{sum([get_sum(i[::-1]) for i in list_num])}")
t2 = time.time()
print(t2-t1)