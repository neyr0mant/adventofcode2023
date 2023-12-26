list_str = [i.strip("\n ").split('@') for i in open("input.txt")]
list_data = [[int(i) for i in i[0].split(",")] + [int(i) for i in i[1].split(",")] for i in list_str]
min_c, max_c = 200000000000000, 400000000000000
count = 0
for idx, i in enumerate(list_data):
    x_i, y_i,z_i,  v_i_x, v_i_y, v_i_z = i
    for j in list_data[idx+1:]:
        x_j, y_j,z_j,  v_j_x, v_j_y, v_j_z = j
        c = v_j_y*v_i_x - v_i_y*v_j_x
        if c != 0:
            t_j = (v_i_x*(y_i - y_j) + v_i_y*(x_j-x_i))/c
            #Потребуем чтобы пересечение было в будущем
            t_i = (x_j + v_j_x*t_j - x_i)/v_i_x
            if t_j > 0 and t_i > 0:
                x_intersection = x_j + v_j_x*t_j
                y_intersection = y_j + v_j_y*t_j
                if min_c <= x_intersection <= max_c and min_c <= y_intersection <= max_c:
                    count += 1
print(f"Решение задания 1:{count}")

