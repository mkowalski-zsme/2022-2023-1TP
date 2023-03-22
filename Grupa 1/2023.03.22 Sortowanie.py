# a = input("Podaj 1 liczbę: ")
# b = input("Podaj 2 liczbę: ")


# if float(a) > float(b):
#     print(a)
# else:
#     print(b)


"""
5 3 2 4 1
3 5 2 4 1
3 2 5 4 1
2 3 5 4 1
2 3 4 5 1
2 3 4 1 5
2 3 1 4 5
2 1 3 4 5
1 2 3 4 5
------------
5 3 2 4 1
3 2 4 1|5
2 3 1|4 5
2 1|3 4 5
1|2 3 4 5

"""
import random

#dane = [random.randint(0,10) for i in range(10)]
dane = [4, 6, 7, 4, 5, 10, 7, 1, 6, 4]

print(dane)

n = len(dane)
j = 0
zmiana = True
while zmiana:
    zmiana = False
    i = 0
    while i < n - 1 - j:
        if dane[i] > dane [i+1]:
            x = dane[i]
            dane[i] = dane[i+1]
            dane[i+1] = x
            zmiana = True
            # dane[i], dane[i+1] = dane[i+1] , dane[i]
        i+=1
    j+=1

print(dane)