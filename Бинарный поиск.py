import random

num = [a**1 for a in range(1, 100)]
win = random.choice(num)
def bin_search():
    n = int(input('Угадайте число от 1 до 100:'))
    if n == win:
        print('вы отгадали число,поздравляю!!!')
    else:
        if n < win:
            print('загаданное число больше')
            bin_search()
        else:
            if n > win:
                print('загаданное число меньше')
                bin_search()
    return win


bin_search()
