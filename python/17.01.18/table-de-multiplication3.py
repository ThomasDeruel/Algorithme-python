print('Table de multiplication')
A1=10
B1=9
for B in range (1,B1+1) :
    for A in range(1,A1+1) :
        print("%2d*%1d=%2d" % (A,B,A*B),end=" ") # %Xd : type entier(int), X indique le nombre de 'positions'
    print("")