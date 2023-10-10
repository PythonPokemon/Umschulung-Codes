try:
    # Benutzereingabe für die Spannung (U) in Volt
    U = float(input("Geben Sie bitte die Spannung in Volt ein: \n"))
    
    # Benutzereingabe für die Stromstärke (I) in Ampere
    I = float(input("Geben Sie bitte die Stromstärke in Ampere ein: \n"))
    
    # Benutzereingabe für die Zeit (t) in Stunden
    t = float(input("Geben Sie bitte die Zeit in Stunden ein: \n"))
    
    # Berechnung des elektrischen Widerstands (R) mit Ohm'schem Gesetz (U / I)
    R = U / I
    
    # Berechnung der elektrischen Leistung (P) (U * I)
    P = U * I
    
    # Berechnung der elektrischen Arbeit (W) (U * I * t)
    W = U * I * t
    
    # Ausgabe der berechneten Werte mit formatierter Ausgabe auf zwei Dezimalstellen
    print("Der elektrische Widerstand beträgt: {0:.2f} Ohm".format(R))
    print("Die elektrische Leistung beträgt: {0:.2f} Watt".format(P))
    print("Die elektrische Arbeit beträgt: {0:.2f} Wh".format(W))

except Exception as e:
    # Fehlerbehandlung: Wenn ein Fehler auftritt, wird diese Anweisung ausgeführt
    print("Es ist folgender Fehler aufgetreten: \n" + str(e))
