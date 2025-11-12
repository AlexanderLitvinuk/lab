#б

def convert(_data):
    convert_str = _data
    _mins = _hours = -1
    del_pos = 0
    for i in range(len(convert_str)):
        if not convert_str[i].isdigit():
            del_pos = i
    return convert_str[:del_pos], convert_str[del_pos+1:]



def correct_checker(_data):
    check_str = str(_data)
    isnum = True
    j = 0
    
    if len(check_str) == 0:
        return False
    
    while j < len(check_str) and isnum:
        isnum = check_str[j].isdigit()
        j += 1
    
    return isnum


def checker(mins, hours):
    
    if not(correct_checker(mins) and correct_checker(hours)):
        return("Ошибка распознования введённых значений.")
    
    mins = int(mins)
    hours = int(hours)
    
    if mins < 0 or mins > 59:
        return("Введено некорректное значение: количество минут должно распологаться в промежутке от 0 до 59.")
    
    if hours < 0 or hours > 23:
        return("Введено некорректное значение: количество часов должно распологаться в промежутке от 0 до 23.")
    
    return worker(mins, hours)



def worker(mins, hours):
    
    if mins == 0:
        
        if hours == 12:
            return "Полдень"
        if hours == 0:
            return "Полночь"
        return str(hours) + " " + get_form_hours(hours) + " " + get_day_time(hours) + " ровно"
    
    return str(hours) + " " + get_form_hours(hours) + " " + str(mins) + " " + get_form_mins(mins) + " " + get_day_time(hours)




def get_form_mins(_mins):
    if _mins % 10 == 1 and _mins // 10 != 1:
        return "минута"
    
    elif 2 <= _mins % 10 <= 4 and _mins // 10 != 1:
        return "минуты"
    
    return "минут"


def get_form_hours(_hours):
    if _hours % 10 == 1 and _hours // 10 != 1:
        return "час"
    elif 2 <= _hours % 10 <= 4 and _hours // 10 != 1:
        return "часы"
    return "часов"


def get_day_time(_hours):
    
    if 0 <= _hours <= 5:
        return "ночи"
    
    if 6 <= _hours <= 12:
        return "утра"
    
    if 12 <= _hours <= 18:
        return "дня"
    
    if 18 <= _hours <= 23:
        return "вечера"


def main():
    stroka = str(input("Введите время: "))
    _hours, _mins = convert(stroka)
    print(checker(_mins, _hours))
    
if __name__ == "__main__":
    main()



"""
main: получает строку, прогоняет через convert, отправляет вывод convert'а, выводит checker
convert: принимает строку и возвращает 2 строки после разбивки
checker: проверяет числа на соответствие условию и корректность ввода. если ввод корректный, return'ит worker, иначе возвращает ошибку
correct_checker: проверяет верность двух строк, полученных при разбивке
worker: обрабатывает и return'ит строку согласно условию, пользуясь get_form_mins, get_form_hours, get_daytime
get_form_mins = get_form_hours, возвращают корректную форму для числа минут и часов соответственно
get_daytime: возвращает время суток по часам
"""
