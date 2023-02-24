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

i=2
while True:
    if czyPierwsza(i):
        print(i)
    i+=1

#1 Napisz funkcję, która zwraca sumę elementów listy (krotki)
def Suma(lista):
    s = 0
    #....
    return s

#2 Napisz funkcję, która zwraca średnią elementów listy

#3 Napisz funkcję, która zwraca pozycję elementu w liście
def Szukaj(lista, element):
    p = 0
    #....
    return p

#4 Napisz funkcję, która rozkłada liczbę na czynniki pierwsze w postaci:

def Faktoryzacja(liczba):
    #
    print("...")
#np: Faktoryzacja(210) -> 2,3,5,7

#Sito Eratostenesa
def Sito(zakres):
    #Funkcja wyświetla liczb pierwsze z zakresu




        