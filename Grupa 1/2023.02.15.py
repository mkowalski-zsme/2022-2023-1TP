def dodaj(a,b):
    return a+b

def podziel(a,b):
    if b == 0:
        #print("nie można dzielić przez zero!")
        return "Inf"
    else:
        return a/b
    
    
def sekwencja(a,b,c):
    i = a
    while i<b:
        print(i,end=",")
        i += c

def czyPierwsza(a):
    i=2
    while i < a**0.5:
        if a % i == 0:
            return False
        i+=1
    return True


def pierwsze(a,b):
    i = a
    while i<b:
        if czyPierwsza(i):
            print(i,end=",")
        i += 1

pierwsze(2,100000)
