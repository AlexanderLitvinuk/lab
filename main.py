#б

def convert(_data):
    convert_str = _data
    del_pos = 0
    for i in range(len(convert_str)):
        if convert_str[i] == " " or convert_str[i] == ":":
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
        return "часа"
    return "часов"


def get_day_time(_hours):
    
    if 0 <= _hours < 6:
        return "ночи"
    
    if 6 <= _hours < 12:
        return "утра"
    
    if 12 <= _hours < 18:
        return "дня"
    
    if 18 <= _hours < 24:
        return "вечера"


def main():
    stroka = str(input("Введите время: "))
    _hours, _mins = convert(stroka)
    print(checker(_mins, _hours))
    
if __name__ == "__main__":
    main()



"""
АЛГОРИТМ
-----------------------------------------------------------------
1. Полученная строка конвертируется в 2 строки - часы и минуты
2. Если 2 полученные строки соответствуют условию (содержат только цифры), то алгоритм продолжается, иначе программа оповещает об ошибке останавливается
3. 2 строки переводятся в целые числа (при выполнении условия 2 ошибка не может возникнуть)
4. Если значения минут и часов соответствуют реальным (0 < мин < 60 и 0 < часы < 24), алгоритм продолжается, иначе программа оповещает о неверных входных данных
5. Возвращается строка по следующему принципу:
5.1. Если значение минут равно нулю и значение часов равно 12 или 0, то возвращаются строки "Полдень" и "Полночь" соответственно
5.2. Если значение минут равно нулю и значение часов НЕ равно 12 или 0, то возвращается строка, построенная по такому принципу:
число часов + форма слова "час" для кол-ва часов + время дня + "ровно"
5.3. Если значение минут нулю не равно, то возвращается строка, построенная по такому принципу:
число часов + форма слова "час" для кол-ва часов + число минут + форма слова "минута" для кол-ва минут + время дня
6. Конец программы
"""
