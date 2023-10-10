# Eingabe der Betriebszugehörigkeit und des Umsatzes
try:
    bz = float(input("Bitte geben Sie Ihre Betriebszugehörigkeit (bz in Jahren) ein: "))
    umsatz = float(input("Bitte geben Sie Ihren Umsatz ein: "))
except ValueError:
    print("Bitte geben Sie gültige Zahlen ein.")
    exit(1)

# Festlegung der Standardwerte für den festen Anteil und den Prozentsatz
festerAnteil = 1700.00
prozent = 10

# Überprüfung der Betriebszugehörigkeit und Anpassung des festen Anteils
if 5 < bz <= 10:
    festerAnteil = 2100.00
elif bz > 10:
    festerAnteil = 2700.00

# Überprüfung des Umsatzes und Anpassung des Prozentsatzes
if 5000 < umsatz <= 10000:
    prozent = 15
elif umsatz > 10000:
    prozent = 23

# Berechnung des Bruttogehalts
brutto = festerAnteil + (umsatz * prozent / 100)

# Ausgabe des Bruttogehalts
print("Bruttogehalt:", brutto)
