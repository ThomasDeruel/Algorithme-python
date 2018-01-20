import numpy as np
n=10
tab=np.empty(n, dtype="i")
i=0
index=i
max = tab[0]
while i<n:
    print("saisir l'élément ",i,end=": ")
    tab[i]=int(input())
    if(tab[i]>max):
        max=tab[i]
        index=i
    i=i+1
print("La valeur maximum se trouve à l'index %2d et vaut %2d"%(index,max))
    