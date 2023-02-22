#Funkcja licząca sumę elementów listy
def Suma(arg):
    s = 0
    for i in arg:
        s += i
    return s

#Funkcja licząca średnią elementów listy

def Srednia(arg):
    n = len(arg)
    if n == 0:
        return "NaN"
    
    return Suma(arg)/n


#Szukanie elementów w liście (wyszukiwanie sekwencyjne)
def Szukaj(arg,element):
    p = 0
    for i in arg:
        if i == element:
            return p
        p += 1
    return "Brak"

#Gra w zgadywanie liczby

def Gra(liczba):
    print("Zgadnij liczbę z zakresu 1 - 1000")
    while True:
        a = int(input("> "))
        if a == liczba:
            print("Gratulacje!")
            return
        elif a < liczba:
            print("Podaj większą niż",a)
        else:
            print("Podaj mniejszą niż",a)


#Wywołanie funkcji:

zmienna = [2,3,4,5,2,3,2,1,3,5,7,3,2]

print(Suma(zmienna))
print(Srednia(zmienna))
print(Szukaj(zmienna,6))
Gra(123)