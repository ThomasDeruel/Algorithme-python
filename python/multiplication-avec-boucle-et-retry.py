print('Multiplication de 2 entiers positifs')
r = 'oui'
while r == 'oui':
    print('Saisir 2 entiers positifs.')
    a,b = int(input('saisir A : ')),int(input('saisir B : '))
    while a<0 or b<0:
        print('Saisir les 2 entiers positifs.')
        a = int(input('saisir A : '))
        b = int(input('saisir B : '))
    p=0
    sb=b
    while b!=0 :
        p=p+a
        b=b-1
    print(a, 'multiplier par ',sb,'= ',a*sb)
    r =input("Voulez-vous recommencer ? (oui/non) : ")
print('Au revoir.')