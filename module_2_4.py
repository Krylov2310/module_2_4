task = 'Домашняя работа по уроку "Цикл for. Элементы списка. Полезные функции в цикле"'
avtor = 'Студент Крылов Эдуард Васильевич'
thanks = 'Благодарю за внимание :-)'
print()
print(task)
print(avtor)
print()
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print('Список чисел: ', numbers)
primes = []
not_primes = []
for i in numbers:
    if i == 1:
        # print('Нейтральное: ', i)
        continue
    is_prime = True
    for l in range(2, i):
        if i % l == 0:
            is_prime = False
            break
    if is_prime == True:
        # print('Простое: ', i)
        primes.append(i)
    else:
        # print('Не простое: ', i)
        not_primes.append(i)
print('Простые числа: ', primes)
print('Не простые числа: ', not_primes)
print()
print(thanks)