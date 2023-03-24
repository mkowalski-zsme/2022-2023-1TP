""" naiwne
4 2 5 3 1 
2 4 5 3 1
2 4 3 5 1
2 3 4 1 5
2 3 1 4 5
2 1 3 4 5
1 2 3 4 5
"""
""" bubble
4 2 5 3 1 
2 4 3 1|5
2 3 1|4 5
2 1|3 4 5
1|2 3 4 5

O(n) = ((n-1)^2) / 2 = n^2
"""
""" select
4 2 5 3 1
1|2 5 3 4
1 2|3 5 4
1 2 3|4 5
-----------
3 2 3 2 1
1 2 3 2 3
"""

import random

dane = []
for i in range(10):
    dane.append(random.randint(0,10))

# dane = [2, 3, 8, 2, 4, 6, 6, 5, 1, 0]

print(dane) 
n = len(dane)
iter = 0
j=0
flaga = True
while flaga:
    i = 0
    flaga = False
    while i < n - 1 - j:
        if dane[i] > dane[i+1]:
            buff = dane[i]
            dane[i] = dane[i+1]
            dane[i+1] = buff
            flaga = True
            # dane[i], dane[i+1] = dane[i+1], dane[i]
        i+=1
        iter+=1    
    j+=1

print(iter)
print(dane)   