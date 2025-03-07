a = float(input("Inserisci la prima misura: "))
b = float(input("Inserisci la seconda misura: "))
c = float(input("Inserisci la terza misura: "))
if a + b > c and a + c > b and b + c > a:
    print("Le misure possono formare un triangolo.")
else:
    print("Le misure NON possono formare un triangolo.")