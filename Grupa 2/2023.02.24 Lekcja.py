#
def czyPierwsza(liczba):
    if liczba<2: 
        return False
    i = 2
    while i*i <= liczba:
        if liczba % i == 0:
            return False
        i+=1
    return True

####

'''
i=2
while True:
    if czyPierwsza(i):
        print(i)
    i+=1
'''
dane = [1,2,3,54,6,3,3,4,5]

#1 Napisz funkcję, która zwraca sumę elementów listy (krotki)
def Suma(lista):
    s = 0
    for el in lista:
        s += el
    return s

print(Suma(dane))

#2 Napisz funkcję, która zwraca średnią elementów listy
def Srednia(lista):
    n = len(lista)
    if n == 0:
        return "NaN"
    return Suma(lista)/n

print(Srednia(dane))

#3 Napisz funkcję, która zwraca pozycję elementu w liście
def Szukaj(lista, szukany):
    p = 0
    for el in lista:
        if szukany == el:
            return p
        p+=1
    return "Brak"

print(Szukaj(dane,5))   

#4 Napisz funkcję, która rozkłada liczbę na czynniki pierwsze w postaci:

def Faktoryzacja(liczba):
    #
    print("...")
#np: Faktoryzacja(210) -> 2,3,5,7

#Sito Eratostenesa
def Sito(zakres):
    #Funkcja wyświetla liczb pierwsze z zakresu
    print()



