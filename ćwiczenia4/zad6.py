def czy_anagram(t1:str, t2:str):
    list_t1 = []
    list_t2 = []
    for i in t1:
        if i.isalpha():
            list_t1.append(i.lower())
    for i in t2:
        if i.isalpha():
            list_t2.append(i.lower())
    list_t1.sort()
    list_t2.sort()
    print(list_t1)
    print(list_t2)
    if list_t1 == list_t2:
        return True
    return False


print(czy_anagram("kolej", "olejk"))
print(czy_anagram("kolej", "kole"))
print(czy_anagram("kolej", "K O L E J"))
print(czy_anagram("Gregory House", "Huge ego, sorry"))