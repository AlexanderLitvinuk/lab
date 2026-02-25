"""
Алгоритм.

1. Открывается "меню". Введённый список очищается от лишних символов кроме цифр.
2. Список рассматривается:
а) Если длина списка после очистки равна 0, программа выводит сообщение о неправильных данных и открывает меню снова.
б) Если введённый список состоит из 1 числа и это число равно 0, программа останавливается.
в) Если введённый список состоит из 1 числа и это число меньше 0, программа выводит сообщение о неправильных данных и открывает меню снова.
г) Если список состоит из 1 натурального числа, то создаётся список со случайным числом элементов, длиной равному введённому числу.
д) В ином случае, очищенный список будет использоваться как исходный для сортировки.
3. Выбор типа сортировки. Пользователь вводит число:
а) Если это не целое число, программа выводит сообщение о неправильных данных и открывает меню снова.
б) Если введённое число не входит в диапазон видов сортировок, программа выводит сообщение о неправильных данных и открывает меню снова.
в) В ином случае, работа продолжается.
4. По числу выбирается тип сортировки. 0 означает все типы сортировок.
5. Если выбран тип сортировки, выводится отсортированный список, количество сравнений и приравниваний в ходе этой сортировки.
6. Если выбраны все типы сортировки, то данные выводятся в виде таблицы
7. Конец программы.

Сортировка пузырьком:
1. Если последующий элемент меньше проверяемого, происходит обмен значений. Цикл проходит с первого до предпоследнего значения и повторяется n-1 раз.

Сортировка простым выбором:
1. С правой стороны находятся отсортированные значения массива.
2. Среди неотсортированных значений ищется наибольшее и перемещается в левый край правой части. Действие повторяется n-1 раз.

Сортировка вставками:
1. Выбирается число x из массива. Сначала это второй элемент.
2. Число x вставляется между числом, находящимся слева от первоначальной позиции числа x, при этом меньшим, чем x, и следующим за ним числом.
3. Операция повторяется n-1 раз, с каждым разом числом x становится следующее число.
"""


import random as r

def isnum(number):
    number_str = str(number)
    if number_str[0] == "-":
        number_str = number_str[1:]
    if len(number_str) < 1:
        return False
    ok = True
    i = 0
    while ok and i < len(number_str):
        ok = number_str[i].isdigit()
        i += 1
    return ok

def separate(inp_list):
    sep_list = []
    junk_list = []
    for i in range(len(inp_list)):
        if isnum(inp_list[i]):
            sep_list.append(int(inp_list[i]))
        else:
            junk_list.append(inp_list[i])
    return sep_list, junk_list

def newlist(length):
    lst = [r.randint(-1000, 1000) for _ in range(length)]
    return lst

#Меню

def menu():
    print("Введите список. Если требуется сгенерировать случайный список, введите только 1 число - количество элементов.\nВведите 0, чтобы остановить программу.")
    inp = input().split()
    list_num, junk = separate(inp)
    if len(list_num) == 0:
        print("Не удалось распознать ввод.")
        menu()
        return
    if len(list_num) == 1:
        if list_num[0] == 0:
            return
        if list_num[0] < 0:
            print("Не удалось распознать ввод.")
            menu()            
        list_itog = newlist(list_num[0])
    else:
        list_itog = list_num
    
    print("Выберите тип сортировки. 0 - все типы сортировки, 1 - пузырьком, 2 - простым выбором, 3 - вставками.")
    n = input()
    if(isnum(n)):
        n = int(n)
        if(n < 0 or n > 3):
            print("Неверный тип сортировки.")
            menu()
            return
    else:
        print("Невозможно распознать данные.")
        menu()
        return
    
    sort_info = []
    if n == 0:
        sort_all(list_itog)
    else:
        sort_info = sort_list(list_itog, n)
        if n == 3:
            temp = "\nКоличество вставок: "
        else:
            temp = "\nКоличество обменов: "
        print("Результаты сортировки:\nОтсортированный список: ", *sort_info[0], "\nКоличество сравнений: ", sort_info[1], temp, sort_info[2])


def sort_list(lst, sort_type):
    if sort_type == 1:
        otv = sort_bubble(lst)
    elif sort_type == 2:
        otv = sort_select(lst)
    elif sort_type == 3:
        otv = sort_insert(lst)
    else:
        otv = (lst, 0, 0)
    return otv

def sort_all(lst):
    sort_info = []
    sort_info.append(sort_bubble(lst.copy()))
    sort_info.append(sort_select(lst.copy()))
    sort_info.append(sort_insert(lst.copy()))
    print("======Результаты======".center(80))
    print("Вид сортировки".ljust(30), "Пузырьком".ljust(20), "Простым выбором".ljust(20), "Вставками".ljust(20))
    print("Кол-во сравнений".ljust(30), str(sort_info[0][1]).ljust(20), str(sort_info[1][1]).ljust(20), str(sort_info[2][1]).ljust(20))
    print("Кол-во обменов/вставок".ljust(30), str(sort_info[0][2]).ljust(20), str(sort_info[1][2]).ljust(20), str(sort_info[2][2]).ljust(20))

#Виды сортировок

def sort_bubble(sorted_list):
    prirav = srav = 0
    i = 0
    ok = True
    while i < len(sorted_list) - 1 and ok:
        ok = False
        for j in range(len(sorted_list) - 1):
            if sorted_list[j] > sorted_list[j+1]:
                sorted_list[j], sorted_list[j+1] = sorted_list[j+1], sorted_list[j]
                ok = True
                prirav += 1
            srav += 1
    return sorted_list, srav, prirav

def sort_select(sorted_list):
    prirav = srav = 0
    for i in range(len(sorted_list) -1, 0, -1):
        maxnum = sorted_list[i]
        maxpos = i
        for j in range(i):
            if sorted_list[j] > maxnum:
                maxnum = sorted_list[j]
                maxpos = j
            srav += 1
        sorted_list[maxpos], sorted_list[i] = sorted_list[i], sorted_list[maxpos]
        prirav += 1
    return sorted_list, srav, prirav

def sort_insert(sorted_list):
    prirav = srav = 0
    for i in range(1, len(sorted_list)):
        x = sorted_list[i]
        j = i
        while (j > 0 and sorted_list[j-1] > x):
            srav += 2
            sorted_list[j] = sorted_list[j-1]
            prirav += 1
            j -= 1
            print(sorted_list)
        sorted_list[j] = x
    return sorted_list, srav, prirav

def main():
    menu()
    
if __name__ == "__main__":
    main()
