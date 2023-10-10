# Importieren des math-Moduls, um mathematische Funktionen wie sqrt() und pow() zu verwenden
import math

try:
    # Initialisieren der Variablen i mit 0
    i = 0

    # Benutzereingabe: Eine Ganzzahl einlesen und in der Variablen "zahl" speichern
    zahl = int(input("Geben Sie eine Zahl ein: "))
    
    # Eine Schleife, die solange läuft, wie i kleiner als zahl ist
    while i < zahl:
        # Überprüfen, ob i eine gerade Zahl ist (i % 2 == 0) und größer als 10
        if i % 2 == 0 and i > 10:
            # Wenn ja, berechne die Quadratwurzel von i und speichere das Ergebnis in "wert"
            wert = math.sqrt(i)
            # Gib eine Nachricht aus, die die Wurzel von i zeigt
            print("Die Wurzel von " + str(i) + " ist: " + str(wert))
        else:
            # Wenn i ungerade oder kleiner oder gleich 10 ist, berechne das Quadrat von i
            wert = math.pow(i, 2)
            # Gib eine Nachricht aus, die das Quadrat von i zeigt
            print("Das Quadrat von " + str(i) + " ist: " + str(wert))
        
        # Inkrementiere i um 1, um zur nächsten Zahl zu gehen
        i = i + 1

# Fehlerbehandlung: Wenn ein Fehler auftritt, wird dieser Teil des Codes ausgeführt
except Exception as e:
    # Gib eine Fehlermeldung aus, die den Fehler erklärt
    print("Es ist folgender Fehler aufgetreten: \n" + str(e))
