x = int(input('entrez le 1er nombre : '))
y = int(input('entrez le 2eme nombre : '))
if x != y:
    if x > y:
        print('le plus grand des 2 nombres vaut',x)
    else:
        print('le plus grand des 2 nombres vaut',y)
else:
    print('les deux entiers sont égaux')