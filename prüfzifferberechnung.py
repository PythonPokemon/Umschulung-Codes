# Eingabe der Nummer als Zeichenkette
nummer = input("Bitte geben Sie die Nummer ein: ")

# Initialisierung der Summe
summe = 0

# Schleife von 0 bis 14
for i in range(15):
    zahl = int(nummer[i])
    
    # Wenn i modulo 2 = 0 ist, multipliziere die Zahl mit 2
    if i % 2 == 0:
        zahl *= 2
    
    # Berechne die Quersumme und addiere sie zur Summe hinzu
    summe += sum(int(digit) for digit in str(zahl))

# Berechne pz
pz = 10 - (summe % 10)

# Wenn pz 10 ist, setze es auf 0
if pz == 10:
    pz = 0

# Vergleiche pz mit der letzten Ziffer der Nummer
if pz == int(nummer[15]):
    print("Nummer gültig")
else:
    print("Nummer nicht gültig")
