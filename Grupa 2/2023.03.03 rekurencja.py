#Rozwiązanie iteracjyne

def Potega(a,n):
    #print("Wywołanie iteracyjnej funkcji potega z arg:",a,n)
    w = 1
    for i in range(n):
        w = w * a
    return w

print(Potega(2,0))
print(Potega(2,10))
print(Potega(2,15))

def Silnia(n):
    w = 1
    for i in range(1,n+1): #zakres od <1, n+1)
        w = w * i
    return w

print(Silnia(0))
print(Silnia(1))
print(Silnia(3))
print(Silnia(6))
print(Silnia(20))

#Rozwiązanie rekurencyjne

def PotegaR(a,n):
    #print("Wywołanie rekurencyjnej funkcji potega z arg:",a,n)
    if n==0: return 1
    else: return a*PotegaR(a,n-1)

print(PotegaR(2,0))
print(PotegaR(2,10))
print(PotegaR(2,15))

def SilniaR(n):
    if n == 0: return 1
    else: return n*SilniaR(n-1)

print(SilniaR(0))
print(SilniaR(1))
print(SilniaR(3))
print(SilniaR(6))
print(SilniaR(20))