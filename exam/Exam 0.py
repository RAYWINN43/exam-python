value = input("sasir la chaine de caractere ")

mots = value.split()
dernier=mots[-1]

nb_lettre = len([i for i in dernier if not i.isdigit()])
print("Le dernier mot est « ",dernier," » avec une longueur de",nb_lettre)