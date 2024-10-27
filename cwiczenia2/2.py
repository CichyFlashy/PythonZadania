import random

numbers = [random.randint(1, 10) for _ in range(20)]

print('Wylosowane liczby: ', numbers)

for i in range(1, 11):
    counter = 0
    for x in numbers:
        if i == x:
            counter += 1
    print(f'{i} - {counter}')