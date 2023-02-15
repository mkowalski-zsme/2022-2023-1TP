#przykład funkcji, która zwraca sumę argumentów

def dodaj(a,b):
    return a+b

#przykład funkcji, która zwraca iloraz dwóch argumentów lub "NaN" jeśli dzielenie przez 0
def podziel(a,b):
    if b == 0:
        #print("nie można dzielić przez zero!")
        return "NaN"
    else:
        return a/b
    
#przykład funkcji, która wyświetla sekwencję liczb od a do b co skok c: 
def sekwencja(a,b,c):
    i = a
    while i<b:
        print(i,end=",")
        i += c
#funkcja sprawdzająca czy podana liczba jest pierwsza
def czyPierwsza(a):
    i=2
    while i <= a**0.5:
        if a % i == 0:
            return False
        i+=1
    return True

#funkcja, która generuje liczby pierwsze z określonego zakresu
def pierwsze(a,b):
    i = a
    while i<b:
        if czyPierwsza(i):
            print(i,end=",")
        i += 1

#wywołanie funkcji
pierwsze(2,100000)
