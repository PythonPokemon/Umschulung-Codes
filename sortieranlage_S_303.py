# Initialisieren von Zählvariablen für die verschiedenen Teile und Schäden
anzahlTeil1 = 0
anzahlTeil2 = 0
anzahlSchadenTeil1 = 0
anzahlSchadenTeil2 = 0

# Schleife, die 1000 Mal durchlaufen wird
for i in range(1001):
    # Benutzereingabe für die Teile-ID
    teileID = int(input("Teile-ID eingeben: "))
    
    # Überprüfen, ob die Teile-ID 1 ist
    if teileID == 1:
        # Wenn Teil 1, erhöhe die Anzahl der Teil-1-Teile um 1
        anzahlTeil1 += 1
        # Benutzereingabe für den Zustand von Teil 1
        zustand = input("Zustand von Teil 1 (Ok/Schaden): ")
        
        # Überprüfen, ob der Zustand von Teil 1 "Ok" ist
        if zustand == "Ok":
            print("Teil 1 in Lagerbox 1 gelagert.")
        else:
            # Wenn der Zustand von Teil 1 "Schaden" ist, erhöhe die Anzahl der beschädigten Teil-1-Teile um 1
            print("Teil 1 mit Schaden in Lagerbox Schaden gelagert.")
            anzahlSchadenTeil1 += 1
    else:
        # Wenn die Teile-ID nicht 1 ist (d.h. Teil 2), erhöhe die Anzahl der Teil-2-Teile um 1
        anzahlTeil2 += 1
        # Benutzereingabe für den Zustand von Teil 2
        zustand = input("Zustand von Teil 2 (Ok/Schaden): ")
        
        # Überprüfen, ob der Zustand von Teil 2 "Ok" ist
        if zustand == "Ok":
            print("Teil 2 in Lagerbox 2 gelagert.")
        else:
            # Wenn der Zustand von Teil 2 "Schaden" ist, erhöhe die Anzahl der beschädigten Teil-2-Teile um 1
            print("Teil 2 mit Schaden in Lagerbox Schaden gelagert.")
            anzahlSchadenTeil2 += 1

# Ausgabe der Gesamtanzahl und Anzahl der beschädigten Teile für Teil 1 und Teil 2
print("Gesamtanzahl Teile 1:", anzahlTeil1)
print("Anzahl Teile 1 mit Schaden:", anzahlSchadenTeil1)
print("Gesamtanzahl Teile 2:", anzahlTeil2)
print("Anzahl Teile 2 mit Schaden:", anzahlSchadenTeil2)
