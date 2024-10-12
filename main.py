def rest(a, b):   # вычисление остатка от деления
    if b == 0:
        raise ValueError('На ноль делить нельзя!')
    return a % b