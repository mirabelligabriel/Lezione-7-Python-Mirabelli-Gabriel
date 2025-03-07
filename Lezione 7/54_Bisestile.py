anno = int(input("Inserisci un anno: "))
if (anno % 4 == 0 and anno % 100 != 0) or (anno % 400 == 0):
    print("L'anno",anno, "è bisestile.")
else:
    print("L'anno", anno, "non è bisestile.")