def sum_range():
    print('Сумма последовательности чисел')
    a = int(input('Введите первое число:'))
    b = int(input('Введите последнее число:'))
    if a > b:
        print('Первое число должно быть меньше второго!')
        return
    s = 0
    for j in range(a, b + 1):
        s += j
    print('Сумма чисел от', a, 'до', b, 'равна:', s)


sum_range()
