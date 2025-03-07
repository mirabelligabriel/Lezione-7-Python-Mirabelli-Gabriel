mese = int(input("inserire il numero del mese "))
if mese == 2:
    print("Febbraio, 28 giorni.")
elif mese == 4 or mese == 6 or mese == 9 or mese == 11:
    print("Il mese ha 30 giorni.")
elif mese == 1 or mese == 3 or mese == 5 or mese == 7 or mese == 8 or mese == 10 or mese == 12:
    print("Il mese ha 31 giorni.")
else:
    print("Il numero inserito non è valido.")