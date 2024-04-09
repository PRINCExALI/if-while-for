print('Таблица умножения')
a = int(input('Введите первое число от 1 до 10:'))
b = int(input('Введите второе число от 1 до 10,но больше первого:'))
for i in range(a, b + 1):
    for j in range(1, 11):
        print(i, 'x', j, '=', i * j)
print()

print('Сумма ряда')
b = int(input('Введите конечное число ряда:'))
s = 0
for j in range(1, b + 1):
    s += j
print('Сумма ряда от 1 до', b, 'равна:', s)

