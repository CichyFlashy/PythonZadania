from random import randint

list_of_numbers = [randint(0, 10) for _ in range(20)]
print(list_of_numbers)

subsets = [[]]
for i in list_of_numbers:
    new_subsets = [subset + [i] for subset in subsets]
    subsets.extend(new_subsets)

print("Liczba podzbiorów:", len(subsets))
print("Wszystkie podzbiory:")
for subset in subsets:
    print(subset)

