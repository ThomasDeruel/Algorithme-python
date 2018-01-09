print('Multiplication de 2 entiers positifs')
r = 'oui'
while r == 'oui':
    print('Saisir 2 entiers positifs.')
    a,b = int(input('saisir A : ')),int(input('saisir B : '))
    while a<0 or b<0:
        print('Saisir les 2 entiers positifs.')
        a = int(input('saisir A : '))
        b = int(input('saisir B : '))
    print(a, 'multiplier par ',b,'= ',a*b)
    r =input("Voulez-vous recommencer ? Saisir 'oui' ou 'non' : ")
print('Au revoir.')