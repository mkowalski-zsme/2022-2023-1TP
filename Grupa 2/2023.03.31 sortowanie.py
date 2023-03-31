"""
5 4 4 2 3 1
1|4 4 2 3 5
1 2|4 4 3 5
1 2 3|4 4 5
1 2 3 4|4 5
1 2 3 4 4|5

"""



def sortowanieB(arg):
    n = len(dane)
    iter = 0
    j=0
    flaga = True
    while flaga:
        i = 0
        flaga = False
        while i < n - 1 - j:
            if dane[i] > dane[i+1]:
                dane[i], dane[i+1] = dane[i+1], dane[i]
                flaga = True
            i+=1
            iter+=1    
        j+=1

    return iter

dane = [2, 3, 8, 2, 4, 6, 6, 5, 1, 0]

print(dane)

print(sortowanieB(dane))

print(dane)

