import numpy as np
n = 3
t = np.empty((n,n))
i = 0
while i<n :
    y=0
    while y<n :
        print('saisir l\'élément ligne',i,'colonne',y,end=": ")
        t[i][y] = int(input())
        y = y + 1
    i = 1 + i
i=0
print("les éléments du tableau vallent : ",end="")
while i<n :
    y=0
    while y<n :
        print(t[i][y], end=" |")
        y = y + 1
    i = 1 + i


    
    
