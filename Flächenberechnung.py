def berechne_rechteck_fläche(länge, breite):
    fläche = länge * breite
    return fläche

def berechne_rechteck_umfang(länge, breite):
    umfang = 2 * (länge + breite)
    return umfang

# Beispielwerte
länge = float(input("Gib die Länge des Rechtecks ein: "))
breite = float(input("Gib die Breite des Rechtecks ein: "))

# Flächen- und Umfangsberechnung aufrufen
fläche = berechne_rechteck_fläche(länge, breite)
umfang = berechne_rechteck_umfang(länge, breite)

# Ergebnisse ausgeben
print("Die Fläche des Rechtecks beträgt:", fläche)
print("Der Umfang des Rechtecks beträgt:", umfang)
