print('Игра угадай число')
import random

num = [a**1 for a in range(1, 100)]
while 0 < 1:
    win = random.choice(num)
    c = int(input('Угадайте число от 1 до 100:'))
    if c < win:
        print('загаданное число больше')
    else:
        if c > win:
            print('загаданное число меньше')
        else:
            if c == win:
                print('вы отгадали число,поздравляю!!!')
                break
print()

#  2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97
print('Поиск простых чисел')
n = int(input('Введите число,до которого хотите увидеть ряд простых чисел: '))
a = [i for i in range(n + 1)]

a[1] = 0

i = 2
while i <= n:
    if a[i] != 0:
        j = i + i
        while j <= n:
            a[j] = 0
            j = j + i
    i += 1

a = set(a)
a.remove(0)

print(a)
