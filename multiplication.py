#Programme réalisé par BOUKLIKHA Mohamed-Amine

#Etapes 1:
print("Je revise mes tables de multiplication")
nombre=int(input("Choisissez un nombre entier naturel non nul : "))
print("Pour arreter saisissez S")
result = 0
multiple=1
compteur = 1
while result != 'S':
    print(nombre, "X", multiple,"=")
    result=input()
    if result != 'S' and int(result)== nombre*multiple:
        multiple = multiple + 1
        compteur = compteur + 1
    else:
        print("C'est faux !")
if result == 'S':
    print("Vous avez",multiple,"bonnes réponses sur",compteur)


#Etapes 2 :
print("Je revise mes tables de multiplication")
nombre = str(input("Choisissez un nombre entier naturel non nul"))
print("Pour arreter saisissez S")
result = 0
multiple = 1
compteur = 1
while result != 'S':
    print(nombre, "X", multiple, "=")
    result = input()
    if result != 'S' and str(result) == nombre * multiple:
        multiple = multiple + 1
        compteur = compteur + 1
    else:
        print("C'est faux !")
if result == 'S':
    print("Vous avez", multiple, "bonnes réponses sur", compteur)

