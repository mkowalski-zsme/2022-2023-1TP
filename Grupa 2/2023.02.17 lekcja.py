#definicja funkcji
def Hello(imie): #argument formalny o nazwie imie
    print("Hello",imie)

#wywołanie funkcji
Hello("Jan") #argument aktualny o wartości "Jan"

def Dodaj(a,b):
    return a+b #zwrócenie wartości

def Dziel(a,b):
    if b != 0:
        return a/b #funkcja może zwracać wartości różnego typu np. liczbę
    else:
        return "Nie dziel przez zero!" #lub string

def lista(a,b,c):
    while a<b:
        print(a,end=", ")
        a+=c

print(Dodaj(4,5))
print(Dziel(3,0))
lista(1,100,3)
