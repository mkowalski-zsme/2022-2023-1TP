#import wymaganych bibliotek
import random
import matplotlib.pyplot as pl

#Generowanie danych

lista1 = [1,3,4,2,3,4,3,2,4,3]
print(lista1)
lista2 = list(range(-10,100,3))
print(lista2)

lista3 = []

'''
n = int(input("Podaj rozmiar danych: "))
for i in range(n):
    lista3.append(int(input("Wprowadź daną: ")))

print(lista3)
'''
def gen(arg):
    l = [4,6,8,0,9,6,5,-3,32,4,1]
    n = len(l)
    return l[arg % n]

lista4 = []
for i in range(10,100,3):
    lista4.append(gen(i))
print(lista4)

lista5 = []
for i in range(10):
    lista5.append(int(random.random()*100)-50)
print(lista5)

lista6 = []
for i in range(10):
    lista6.append(random.randint(0,10))
print(lista6)

lista7 = [random.randint(0,10) for i in range(100)]
print(lista7)



y = [1, 4, 9, 16, 25,3,4,6,3,3,4,5,63]
#x = [0,1,2,3,4,5,6,7,8,9,10,11,12]
x = list(range(5,len(y)+5))

pl.plot(x, y)
pl.show()