# def run():
#     print("Szybkie bieganie")


# osoba = {'imie': 'kasia', 'wiek':23, 'funkcja': run}

# print(osoba['imie'])
# print(osoba['wiek'])

# osoba['funkcja']()


class Osoba:
    def __init__(self, imie, nazwisko, wiek):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek

    def Print(self):
        print("Imię: "+self.imie+" Nazwisko: "+self.nazwisko+" wiek: "+str(self.wiek))



osoba1 = Osoba("Jan","Nowak", 23)
osoba2 = Osoba("Adam", "Kowalski", 32)

# print(osoba1.imie, osoba1.nazwisko, osoba1.wiek)
# print(osoba2.imie, osoba2.nazwisko, osoba2.wiek)

# osoba1.Print()
# osoba2.Print()

def Nwd(a,b):
    while a != b:
        if a>b: a-=b
        else: b -= a
    return a

class Ulamek:
    def __init__(self, licznik, mianownik):
        self.licznik = licznik
        if mianownik == 0:
            self.mianownik = 1
        else: 
            self.mianownik = mianownik

    def Print(self):
        print(str(self.licznik)+"/"+str(self.mianownik))
    
    def Wartosc(self):
        if self.mianownik == 0: return None
        return self.licznik / self.mianownik

    def Normalizuj(self):
        nwd = Nwd(self.licznik, self.mianownik)

        self.licznik //= nwd
        self.mianownik //= nwd


zm1 = Ulamek(6,12)
zm1.Print()
print(zm1.Wartosc())
zm1.Normalizuj()
zm1.Print()

        