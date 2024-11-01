import random

numbers = [random.randint(-10, 10) for _ in range(10)]

print('Wylosowane liczby:')
for i in numbers:
    print(i)


minimum = numbers[0]
for i in numbers:
    if i < minimum:
        minimum = i
print('Min: ', minimum)
#print(min(numbers))


maximum = numbers[0]
for i in numbers:
    if i > maximum:
        maximum = i
print('Max: ', maximum)
#print(max(numbers))

print('Średnia: ')
average = sum(numbers)/10.0
print(average)

counter_lowers = 0
counter_highers = 0
for i in numbers:
    if i < average:
        counter_lowers += 1
    elif i > average:
        counter_highers += 1
print('Liczba mniejszych od średniej: ', counter_lowers)
print('Liczba większych od średniej: ', counter_highers)


print('Odwrócona lista: ', numbers[::-1])









