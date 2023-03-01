#rekurencja
#rozwiązania iteracyjne:
def Potega(a,n):
    w = 1
    for i in range(n):
        w = w * a
    return w 

def Silnia(n):
    w = 1
    for i in range(1,n+1):
        w = w * i
    return w

#rozwiązania rekurencyjne
def PotegaR(a,n):
    if n == 0: return 1
    else: return a * PotegaR(a,n-1)
    
def SilniaR(n):
    if n == 0: return 1
    else: return n * SilniaR(n-1)

for i in range(15):
    print(Potega(2,i),PotegaR(2,i))

for i in range(15):
    print(Silnia(i),SilniaR(i))
