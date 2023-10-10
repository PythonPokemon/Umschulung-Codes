# Benutzereingabe für Datenmenge in MB
datenmenge = float(input("Geben Sie die Datenmenge in MB ein: "))

# Benutzereingabe für Übertragungsrate in kbit/s
übertragungsrate = float(input("Geben Sie die Übertragungsrate in kbit/s ein: "))

# Berechnung der Übertragungszeit in Minuten
zeit = ((datenmenge * 1000) / (übertragungsrate / 8)) / 60

# Ausgabe der berechneten Übertragungszeit mit formatierter Ausgabe auf zwei Dezimalstellen
print("Es werden {0:.2f} Minuten für die Übertragung benötigt.".format(zeit))
