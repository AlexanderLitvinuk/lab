#в краткой записи первым идёт ID, затем остальные параметры
#при создании экземпляра ID идёт после остальных параметров

#словарь мёртв

#теперь тут только список

import planet
from utils import to_int, to_int2, to_number, to_word

planet_list = []

commands_list = ["вывести", "создать", "удалить", "сортировать", "изменить", "прочесть", "записать", "список", "помощь"]

def menu():
    print("Введите ''помощь'', чтобы увидеть список возможных действий")
    inp = input("Выберите действие: ")
    while inp.lower() != "стоп":
        inp_lst = inp.split()
        command = to_word(inp_lst[0]).lower()
        props = inp_lst[1:]
        if len(props) == 0:
            props.append("")
        if command not in commands_list:
            print("Неверная команда")
        if command == "создать":
            if len(props) < 5:
                print("Недостаточно данных, чтобы создать планету")
            else:
                if len(props) == 5:
                    _idp = -1
                else:
                    _idp = to_int(props[5])
                add_planet(props[0], props[1], props[2], props[3], props[4], _idp)
        if command == "удалить":
            if len(props) == 0:
                print("Введите имя или ID для удаления")
            else:
                _idp = get_planet_id(props[0])
                if _idp != -1:
                    del planet_list[_idp]
        if command == "изменить": #цель поле значение
            if len(props) < 3:
                print("Цель изменения не определена")
            else:
                change_value(props[0], props[1], props[2])
        if command == "сортировать":
            _key = to_word(props[0])
            sort_planets(_key)
        if command == "вывести":
            print_database()
        if command == "прочесть":
            read_database()
        if command == "записать":
            write_database()
        if command == "список":
            print_list()
        if command == "помощь":
            help_menu()
        inp = input("Выберите действие: ")

def sort_planets(_key):
    key = to_word(_key)
    if key not in ("name", "имя", "название", "radius", "радиус", "mass", "масса", "length", "расстояние", "type", "тип"):
        print("Некорректное поле для поиска")
        return
    i = 0
    while i < len(planet_list):
        for j in range(len(planet_list)-1):
            if get_value(j, key) > get_value(j+1, key):
                planet_list[j], planet_list[j+1] = planet_list[j+1], planet_list[j]
            print(planet_list, i, j)
        i += 1

def get_value(index, _target):
    target = str(_target).lower()
    if target in ("name", "имя", "название"):
        return get_planet(index).name
    elif target in ("radius", "радиус"):
        return get_planet(index).radius
    elif target in ("mass", "масса"):
        return get_planet(index).mass
    if target in ("length", "расстояние"):
        return get_planet(index).length
    if target in ("type", "тип"):
        return get_planet(index).typep
    return -1

def change_value(index, _target, val):
    target = str(_target).lower()
    if target in ("name", "имя", "название"):
        get_planet(index).name = val
    elif target in ("radius", "радиус"):
        get_planet(index).radius = val
    elif target in ("mass", "масса"):
        get_planet(index).mass = val
    elif target in ("length", "расстояние"):
        get_planet(index).length = val
    elif target in ("type", "тип"):
        get_planet(index).type = val
    else:
        print("Указанное поле не найдено")


#работа с индексами и прочим

def get_planet(index):
    return planet_list[get_planet_id(index)]

def get_planet_id(index):
    i_str = to_word(index)
    i_num = get_planet_id_by_name(i_str)
    if i_num == -1:
        i_num = to_int2(index)
        if i_num < 0 or i_num >= len(planet_list):
            print("Не найдены ID или имя планеты")
            return -1
    return i_num

def get_planet_id_by_name(_name):
    name = str(_name)
    for i in range(len(planet_list)):
        if planet_list[i].name == name:
            return i
    return -1

def add_planet(name, radius, mass, length, typep, idp = -1):
    if -1 < idp < len(planet_list):
        planet_list[idp] = planet.Planet(name, radius, mass, length, typep)
    else:
        planet_list.append(planet.Planet(name, radius, mass, length, typep))



#для базы данных и вывода списка

def print_database():
    database = open("database.txt", "r", encoding = "utf-8")
    for i in database:
        print(i, end = "")
    print()
    database.close()

def read_database():
    planet_list.clear()
    database = open("database.txt", "r", encoding = "utf-8")
    data_lst = database.readlines()
    for i in range(len(data_lst)):
        s = data_lst[i].split(";")
        if len(s) < 5:
            print("Ошибка при прочтении строки " + str(i+1))
        else:
            add_planet(s[0], to_number(s[1]), to_number(s[2]), to_number(s[3]), s[4])
    database.close()

def write_database():
    database = open("database.txt", "w", encoding = "utf-8")
    for i in range(len(planet_list)):
        print(repr(planet_list[i]), file = database)
    database.close()

def print_list():
    for i in range(len(planet_list)):
        print("ID: " + str(i))
        print(planet_list[i])
        print()



#помощь

def help_menu():
    print("''вывести'' - показывает наполнение базы данных. Показывается краткая запись планет")
    print("''прочесть'' - считывает информацию о планетах из файла и записывает их в локальный список. Планеты, ID которых не затронуты в файле, не будут изменены")
    print("''записать'' - записывает информацию о планетах из списка в файл")
    print("''список'' - выводит локальный изменяемый список. Показывается полная запись планет")
    print("''создать'' - новая планета по списку следующих данных: имя, радиус, масса, расстояние до Солнца, ID. Последний пункт необязателен. При наложении ID планета пересоздаётся с новыми показателями")
    print("''удалить'' - удаляет планету по ID или имени")
    print("''изменить'' - изменяет значение внутри выбранной планеты. Первым идёт имя планеты, затем изменяемое поле (поддерживаются русские названия полей), затем новое значение поля")
    print("''сортировать'' - сортирует список по выбранному параметру. Также поддерживаются русские названия полей")
    print("''помощь'' - вывести меню помощи")
    print("''стоп'' - закрыть основное меню")
    print("Используйте ''_'', чтобы обозначить пробелы в названии новых планет!")
    print("Не забудьте прочесть содержимое файла и записать их обратно после обработки!")

menu()
