print('Шифр цезаря:')
alfavit = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
smeschenie = 3
n = len(alfavit)
message = input("Введите слово: ")
result = ""
for i in message:
    mesto = alfavit.find(i)
    new_mesto = mesto + smeschenie
    if new_mesto >= n:
        new_mesto = new_mesto - n
    result += alfavit[new_mesto]

print("Результат: ", result)
print()

print('Дешифратор цезаря:')
alfavit = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
smeschenie = 3
n = len(alfavit)
message = input("Введите слово: ")
result = ""
for i in message:
    mesto = alfavit.find(i)
    new_mesto = mesto - smeschenie  # # Меняем знак + на знак -
    if new_mesto >= n:
        new_mesto = new_mesto - n
    result += alfavit[new_mesto]

print("Результат: ", result)
