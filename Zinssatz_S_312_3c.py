# Benutzereingabe für den Geldbetrag in Euro
betrag = float(input("Geben Sie den Geldbetrag in Euro ein: "))

# Benutzereingabe für den Zinssatz
zinssatz = float(input("Geben Sie den Zinssatz ein: "))

# Berechnung der Zinsen
zinsen = betrag * zinssatz / 100

# Ausgabe der berechneten Zinsen mit formatierter Ausgabe auf zwei Dezimalstellen
print("Es werden {0:.2f} Euro an Zinsen gezahlt.".format(zinsen))
