def add_everything_up(a, b):
    try:
        return a + b
    except:
        if isinstance(a, int) or isinstance(a, float) and isinstance(b, str):
            return str(a) + b
        if isinstance(b, int) or isinstance(b, float) and isinstance(a, str):
            return  a + str(b)



print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(round(add_everything_up(123.456, 7), 3))
print(add_everything_up('строка1', 'строка2'))
