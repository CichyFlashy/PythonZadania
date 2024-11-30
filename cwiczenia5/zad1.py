def min_value(lst: list[float]) -> float:
    min_val = lst[0]  
    for num in lst:  
        if num < min_val:  
            min_val = num
    return min_val


def max_value(lst: list[float], wynik: list[float]) -> None:
    max_val = lst[0]  
    for num in lst:  
        if num > max_val:  
            max_val = num
    wynik[0] = max_val  


lst = [4.5, 1.2, 8.3]
max_v = [0]  
min_v = min_value(lst)
max_value(lst, max_v)

print(min_v, max_v[0])