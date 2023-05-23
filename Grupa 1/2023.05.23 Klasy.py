class Osoba:
    #imie nazwisko wiek adres nr_telefonu

    def __init__(self,imie,nazwisko,wiek):
        self.imie = imie
        self.nazwisko = nazwisko
        if wiek<0: wiek = 0

        self.wiek = wiek
        self.nr_telefonu = 0

    def __str__(self):
        return "Imię: "+self.imie+"\nNazwisko: "+self.nazwisko+"\nWiek: "+str(self.wiek)


    def setName(self,imie,nazwisko = ""):
        self.imie = imie
        if nazwisko != "":
            self.nazwisko = nazwisko


    def Print(self):
        print(self.imie,self.nazwisko,self.wiek,end=" ")
        if self.nr_telefonu != 0:
            print(self.nr_telefonu,end = "")
        print()

    def isMature(self):
        if self.wiek>=18: return True
        else: return False

    def Fun():
        print("hello")
        





ob1 = Osoba("Jan","Nowak",23)
ob2 = Osoba("Kasia","Iksińska",32)
ob1.nr_telefonu = "1234324123"

# ob1.imie = "Jan"
# ob1.nazwisko = "Nowak"

# ob2.imie = "Kasia"
# ob2.nazwisko = "Kowalska"

# print(ob1.imie,ob1.nazwisko,ob1.wiek)
# print(ob2.imie,ob2.nazwisko,ob2.wiek)
ob2.setName("Asia","Kowalska")

ob2.Print()
ob1.Print()

print(ob1)
print(ob2)

Osoba.Fun()