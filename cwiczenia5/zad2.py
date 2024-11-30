
def analiza(lst: list[int]) -> tuple[int, float, float]:
    sum_of_elements = sum(lst)
    if len(lst) % 2 == 0:
        lst.sort()
        median = (lst[len(lst)//2] + lst[len(lst)//2-1])/2
    else:
        lst.sort()
        median = lst[len(lst)//2]
    average = sum_of_elements / len(lst)
    return (sum_of_elements, median, average)

lst = [2, 3, 4, 7]
suma, med, sr = analiza(lst)
print(f"Suma: {suma}, średnia: {sr}, mediana: {med}")

