def to_number(_s):
    s = str(_s)
    i = 0
    flag_dot = False
    while i < len(s):
        if s[i] == ",":
            s = s[:i] + "." + s[i+1:]
        if s[i] == "." and not flag_dot:
            flag_dot = True
        elif not s[i].isdigit():
            s = s[:i] + s[i+1:]
            i -= 1
        i += 1
    if len(s) == 0:
        return 0
    return float(s)

def to_word(_s):
    s = str(_s)
    i = 0
    flag = True
    while i < len(s) and flag:
        if s[i] != " ":
            s = s[i:]
            flag = False
        i += 1
    flag = True
    i = len(s) - 1
    while i > 0 and flag:
        if s[i] != " ":
            s = s[:i+1]
            flag = False
        i -= 1
    flag = True
    i = 0
    k = 0
    while i < len(s):
        if flag:
            if s[i] == " ":
                k = i
                flag = False
        else:
            if s[i] != " ":
                s = s[:k] + " " + s[i:]
                flag = True
                i -= (i - k)
        i += 1
    if len(s) == 0:
        return "не установлено"
    return s

def to_int(_s):
    s = str(_s)
    i = 0
    while i < len(s):
        if not s[i].isdigit():
            s = s[:i] + s[i+1:]
            i -= 1
        i += 1
    if len(s) == 0:
        return 0
    return int(s)