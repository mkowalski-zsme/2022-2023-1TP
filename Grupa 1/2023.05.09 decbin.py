def Dec2Bin(liczba):
    s = ''
    while liczba > 0:
        r = liczba % 2
        s = str(r) + s
        liczba //= 2
    return s

def Bin2Dec(text):
    x = 1
    liczba = 0
    for i in text[::-1]:
        if i == '1':
            liczba +=  x  
        x *= 2

    return liczba

print(Dec2Bin(123))

print(Bin2Dec('11111111'))
