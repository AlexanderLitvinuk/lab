#в краткой записи первым идёт ID, затем остальные параметры
#при создании экземпляра ID идёт после остальных параметров

#может, изменить коллекцию на список и добавить списковый айди как поле

#или вообще удалить айди как поле и сделать его исключительно глобальным...

import planet
from utils import to_int, to_number, to_word

global_id = -1
planet_list = {}

commands_list = ["вывести", "создать", "удалить", "сортировать", "изменить", "прочесть", "записать", "список"]

def menu():
    inp = input("Выберите действие: ")
    while inp.lower() != "стоп":
        inp_lst = inp.split()
        command = to_word(inp_lst[0]).lower()
        props = inp_lst[1:]
        if command not in commands_list:
            print("Неверная команда")
        if command == "создать":
            if len(props) < 5:
                print("Недостаточно данных, чтобы создать планету")
            else:
                if len(props) == 5:
                    _idp = get_free_id()
                else:
                    _idp = props[5]
                planet_list[_idp] = planet.Planet(props[0], props[1], props[2], props[3], props[4], _idp)
        if command == "удалить":
            if len(props) == 0:
                print("Введите имя или ID для удаления")
            else:
                _idp = get_planet(props[0])
                del planet_list[_idp]
        if command == "изменить": #цель поле значение
            if len(props) < 3:
                print("Цель изменения не определена")
            else:
                if not props[1] in get_planet(props[0]):
                    print("Запрашиваемое поле не найдено")
                else:
                    get_planet(props[0])[props(1)] = props(2)
        if command == "вывести":
            print_database()        
        if command == "прочесть":
            read_database()
        if command == "записать":
            write_database()
        if command == "список":
            print_list()
        if command == "удалить":
            if len(props) == 0:
                
        inp = input("Выберите действие: ")


def get_planet(index):
    if index.isdigit():
        i_num = to_number(index)
        return planet_list[i_num]
    else:
        i_str = to_word()
        return planet_list[get_planet_id_by_name(i_str)]

def get_planet_id_by_name(name):
    for i in planet_list:
        if planet_list[i].name == name:
            return i
    return 0

def get_free_id():
    i = 0
    while i not in planet_list:
        i += 1
    return i

def print_database():
    database = open("database.txt", "r", encoding = "utf-8")
    for i in database:
        print(i, end = "")
    print()
    database.close()

def read_database():
    database = open("database.txt", "r", encoding = "utf-8")
    for i in database:
        s = i.split(";")
        if len(s) >= 6:
            planet_list[s[0]] = planet.Planet(s[1], s[2], s[3], s[4], s[5], s[0])
    database.close()

def write_database():
    database = open("database.txt", "w", encoding = "utf-8")
    for i in planet_list:
        print(repr(planet_list[i]), file = database)
    database.close()

def print_list():
    for i in planet_list:
        print(planet_list[i])
        print()

def help_menu():
    print("''вывести'' - показывает наполнение базы данных. Показывается краткая запись планет")
    print("''прочесть'' - считывает информацию о планетах из файла и записывает их в локальный список. Планеты, ID которых не затронуты в файле, не будут изменены")
    print("''записать'' - записывает информацию о планетах из списка в файл")

menu()
