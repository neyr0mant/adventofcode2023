#https://adventofcode.com/2023/day/10
list_str = [i.strip("\n ").split() for i in open("input.txt")]


class Pipeline:
    def __init__(self, list_data):
        self.matrix_pipline = list_data
        self.x_max = len(self.matrix_pipline[0][0])-1
        self.y_max = len(self.matrix_pipline)-1
        self.list_rule = [["-", "L" ,"F" , "S"], ["-", "J", "S", "7"], ["7", "S", "|", "F"], ["|", "L", "J", "S"]]
        self.count_step = 0
        for idx, i in enumerate(self.matrix_pipline):
            elem = i[0]
            if "S" in elem:
                self.coordinate_start = [elem.index("S"), idx]
        assert self.coordinate_start, "Не нашли точку старта!"
        description = (f"#######   МАТРИЦА ТРУБОПРОВОДА СОЗДАНА! #######\nНоль системы координат находится в верхнем "
                       f"левом углу, ось Y смотрит вниз, X - вправо\nПараметры:\nШирина: {self.x_max+1}, Высота: "
                       f"{self.y_max+1}, Точка старта: {self.coordinate_start}")
        print(description)
    @staticmethod
    def assert_borders(func):
        def wrapper(*args, **kwargs):
            self, x, y = args[0], args[1][0], args[1][1]
            list_potential = []
            try:
                list_x, list_y = ([x-1, y], [x+1, y]), ([x, y-1], [x, y+1])
                for x in list_x:
                    if 0 <= x <= self.x_max:
                        list_potential.append(x)
                    else:
                        list_potential.append(False)
                for y in list_y:
                    if 0 <= y <= self.y_max:
                        list_potential.append(y)
                    else:
                        list_potential.append(False)
            except Exception as e:
                if kwargs.get("error_assert"):
                    raise AssertionError(e)
                else:
                    return list_potential
            return func(*args, **kwargs)
        return wrapper
    def get_elem_for_coordinate(self, coordinate):
        if isinstance(coordinate, list):
            x, y = coordinate[0], coordinate[1]
            return self.matrix_pipline[y][0][x]
        else:
            return False
    def get_next_list_coordinate_for_symbol(self, list_potential_next_coordinate):
        list_potential_next_symbols = list(map(self.get_elem_for_coordinate, list_potential_next_coordinate))
        # Под конец всех проверок list_potential_next_coordinate должен быть заполнен ровно одной координатой
        list_assert_potential_next_coordinate = []
        for idx, potential_symbol in enumerate(list_potential_next_symbols):
            symbol_coordinate = list_potential_next_symbols[idx]
            if isinstance(symbol_coordinate, str):
                if symbol_coordinate in self.list_rule[idx]:
                    list_assert_potential_next_coordinate.append(list_potential_next_coordinate[idx])
        #Уберем невозможные пути
        return list_assert_potential_next_coordinate

    def get_only_potential_coordinate(self, coordinate):
        x, y = coordinate[0], coordinate[1]
        list_x, list_y = ([x-1, y], [x+1, y]), ([x, y-1], [x, y+1])
        list_only_potential_coordinate = []
        for coordinate_x in list_x:
            if 0 <= coordinate_x[0] <= self.x_max:
                list_only_potential_coordinate.append(coordinate_x)
            else:
                list_only_potential_coordinate.append(False)
        for coordinate_y in list_y:
            if 0 <= coordinate_y[1] <= self.y_max:
                list_only_potential_coordinate.append(coordinate_y)
            else:
                list_only_potential_coordinate.append(False)
        return list_only_potential_coordinate

    def get_visual_configuration(self, list_coordinate, cur_coordinate):
        list_only_symbol = [self.get_elem_for_coordinate(i) for i in list_coordinate]
        list_symbol_replace = [i if isinstance(i, str) else "." for i in list_only_symbol]
        left, right, up, down = list_symbol_replace
        cur = self.get_elem_for_coordinate(cur_coordinate)
        configuration = f"""##########################
        {up} 
      {left} {cur} {right}               
        {down} 
##########################"""
        return configuration

    def get_next_coordinate(self, start_coordinate, old_coordinate):
        list_potential_next_only_coordinate = self.get_only_potential_coordinate(start_coordinate)
        list_potential_next_coordinate_assert_rule = self.get_next_list_coordinate_for_symbol(
            list_potential_next_only_coordinate)

        list_assert_potential_next_coordinate = []
        if len(list_potential_next_coordinate_assert_rule) > 1:
            for potential_next_coordinate in list_potential_next_coordinate_assert_rule:
                if old_coordinate != potential_next_coordinate:
                    list_potential_next_only_coordinate = self.get_only_potential_coordinate(potential_next_coordinate)
                    list_candidate_assert_rule = self.get_next_list_coordinate_for_symbol(
                        list_potential_next_only_coordinate)
                    if start_coordinate in list_candidate_assert_rule:
                        list_assert_potential_next_coordinate.append(potential_next_coordinate)
        try:
            list_potential_symbol = [self.get_elem_for_coordinate(i) for i in list_assert_potential_next_coordinate]
            assertion_text = (f"Цепочек нашлось {len(list_assert_potential_next_coordinate)}, "
                              f"ждали 1,потенциальные символы :  {list_potential_symbol})")
            assert len(list_assert_potential_next_coordinate) == 1, assertion_text
        except AssertionError as e:
            print(f"Шагов сделано: {self.count_step}")
            print(f"Текущий символ: {self.get_elem_for_coordinate(start_coordinate)}")
            print(f"Пришли от символа: {self.get_elem_for_coordinate(old_coordinate)}")
            raise AssertionError(e)
        return list_assert_potential_next_coordinate
    def walk_pipline(self):
        list_start_allowed_only_coordinate = self.get_only_potential_coordinate(self.coordinate_start)
        list_start_allowed_assert_symbol = self.get_next_list_coordinate_for_symbol(list_start_allowed_only_coordinate)

        assert len(list_start_allowed_assert_symbol) == 2, "Кольцо не замкнуто!!!"
        #Т.К. кольцо без разницы какой конец круга возьмем
        start_place = list_start_allowed_assert_symbol[0]
        old_place = self.coordinate_start
        while True:
            self.count_step += 1
            next_place = self.get_next_coordinate(start_place, old_place)[0]
            old_place_visual = self.get_visual_configuration(list_start_allowed_only_coordinate, old_place)
            step_visual = (f"{old_place} {self.get_elem_for_coordinate(old_place)} ---> "
                           f"{start_place} {self.get_elem_for_coordinate(start_place)}")
            print(f"Шаг {self.count_step}\n{step_visual}")
            print(f"{old_place_visual}")
            if start_place != self.coordinate_start:
                old_place = start_place
                start_place = next_place
            else:
                print(f"Путешествие закончилось, количество шагов по ВСЕЙ цепочке {self.count_step}")
                return self.count_step // 2





lab = Pipeline(list_str)
start = lab.coordinate_start
print(lab.walk_pipline())




