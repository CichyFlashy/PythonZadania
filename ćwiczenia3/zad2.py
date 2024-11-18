string_of_words = """
Rybniczanie postawili na zawodników mających ekstraligowe doświadczenie, 
ale nie udało im się wyciągnąć żadnej czołowej gwiazdy ligi. 
Szybko zaczęto tę drużynę porównywać chociażby do Arged Malesy Ostrów Wielkopolski, 
czyli beniaminka z sezonu 2022, który zakończył rozgrywki bez choćby jednego punktu na koncie. 
Po 14 porażkach ostrowianie pożegnali się z PGE Ekstraligą.
Ja uważam, że duże punkty ligowe ROW zgarnie na własnym torze. 
Trudno sobie wyobrazić wygraną rybniczan na wyjeździe, bo w PGE Ekstralidze jest to trudne, 
a co dopiero dla beniaminka szytego przez Krzysztofa Mrozka na miarę naszych możliwości. 
Najważniejsza kwestia jest jednak taka, że nie ma co porównywać sytuacji tych dwóch drużyn, 
bo mamy zupełnie nowy regulamin. Co innego trzeba zrobić, aby się utrzymać."""

words = string_of_words.split()
words_dictionary = {}
for word in words:
    words_dictionary[word] = words_dictionary.get(word,0)+1

for key, value in words_dictionary.items():
    print(f"{key} : {value}")
