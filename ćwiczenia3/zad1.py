from random import randint

list_size = int(input("Podaj długość pierwszej listy: "))
second_list_size = int(input("Podaj dlugość drugiej listy: "))

first_list = [randint(1, 10) for _ in range(list_size)]
second_list = [randint(1, 10) for _ in range(second_list_size)]

print(first_list)
print(second_list)

common = set(first_list) & set(second_list)

print(common)