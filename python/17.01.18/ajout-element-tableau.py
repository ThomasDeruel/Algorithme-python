import numpy as np
n=5
i=0
tab = np.empty(n)
while i<n :
        tab[i] = (input("saisir un élément: "))
        print(tab[i])
        i = i+1
i=0
print("Les éléments du tableaux sont : ", end="")
while i<n :
        print(tab[i], end=" ")
        i=i+1
    