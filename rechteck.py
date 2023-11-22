import modrechteck as mr

# Hauptprogramm
# EINGABE
Länge, Breite = mr.eingabe()

# VERARBEITUNG
Umfang, Fläche=mr.kalk(Länge,Breite)

# AUSGABE
mr.ausgabe(Länge, Breite, Umfang, Fläche)
