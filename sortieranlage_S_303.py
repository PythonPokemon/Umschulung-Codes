anzahlTeil1 = 0
anzahlTeil2 = 0
anzahlSchadenTeil1 = 0
anzahlSchadenTeil2 = 0

for i in range(1001):
    teileID = int(input("Teile-ID eingeben: "))
    
    if teileID == 1:
        anzahlTeil1 += 1
        zustand = input("Zustand von Teil 1 (Ok/Schaden): ")
        
        if zustand == "Ok":
            print("Teil 1 in Lagerbox 1 gelagert.")
        else:
            print("Teil 1 mit Schaden in Lagerbox Schaden gelagert.")
            anzahlSchadenTeil1 += 1
    else:
        anzahlTeil2 += 1
        zustand = input("Zustand von Teil 2 (Ok/Schaden): ")
        
        if zustand == "Ok":
            print("Teil 2 in Lagerbox 2 gelagert.")
        else:
            print("Teil 2 mit Schaden in Lagerbox Schaden gelagert.")
            anzahlSchadenTeil2 += 1

print("Gesamtanzahl Teile 1:", anzahlTeil1)
print("Anzahl Teile 1 mit Schaden:", anzahlSchadenTeil1)
print("Gesamtanzahl Teile 2:", anzahlTeil2)
print("Anzahl Teile 2 mit Schaden:", anzahlSchadenTeil2)
