#definicja funkcji
def Hello(imie): #argument formalny o nazwie imie
    print("Hello",imie)

#wywołanie funkcji
Hello("Jan") #argument aktualny o wartości "Jan"

def Dodaj(a,b):
    return a+b #zwrócenie wartości

w = Dodaj(4,5)
print(w)

def Dziel(a,b):
    if b != 0:
        return a/b #funkcja może zwracać wartości różnego typu teraz liczba
    else:
        return "Nie dziel przez zero!" #lub string

print(Dziel(3,0))