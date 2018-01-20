print('Table de multiplication')
A1=10
B1=9
B=1
while B <= B1 :
    A=1
    while A<= A1 :
        print("%2d*%1d=%1d" % (A,B,A*B),end="") # %Xd : type entier(int), X indique le nombre de 'positions'
        A=A+1
    print("")
    B=B+1