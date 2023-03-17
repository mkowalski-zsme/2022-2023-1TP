#1. Napisz funkcję, która zwraca sumę elementów listy (krotki)
def suma(arg) -> float:
    s = 0
    pass
    return s

print(suma([3,4,56,3,2,45]))
#2. Napisz funkcję, która zwraca średnią elementów listy (krotki)
def srednia(arg) -> float:
    s = suma(arg)
    #a co z zerem???
    return s / len(arg)
print(srednia([3,4,56,3,2,45]))
#3. Napisz funkcję, która sprawdza (zwraca True / False) czy z podanych długości odcinków można zbudować trójkąt
def triangle(a,b,c):
    pass
#4. Napisz funkcję, która sprawdza (zwraca true / false) czy liczba jest pierwsza
def prime(liczba):
    pass
#5a. Napisz funkcję, która oblicza NWD dwóch liczb
def NWD(a,b):
    pass
#5b. Napisz funkcję, która oblicza NWW dwóch liczb
#6. Napisz funkcję, która zwraca listę dzielników liczby (faktoryzacja).
def f(liczba) -> list:
    pass
"""
dla liczba < 1 -> []

f(1) -> [1]
f(3) -> [3]
f(13) -> [13]
f(20) -> [2,2,5]

"""

#7. Napisz definicję funkcji liniowej spełniającej zależność: Y = a*X + b


def fun_lin(a: float,b: float,X: list) -> list:
    pass

X = list(range(-100,100))

Y = fun_lin(2,3,X)

#Narysuj wykres funkcji Y

