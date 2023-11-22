def eingabe():
    a=float(input("Bitte die Länge des Rechtecks in cm eingeben:"))
    b=float(input("Bitte die Breite des Rechtecks in cm eingeben:"))
    return a,b

def kalk(a,b):
    U=2*a+2*b # Umfang ermitteln
    A=a*b #Fläche ermitteln
    return U,A

def ausgabe(a,b,U,A):
    print("Der Rechteck mit der Länge",a,"und der Breite",b)
    print("hat einen Umfang:",U, "cm")
    print("und eine Fläche von:",A,"cm².")

# Hauptprogramm
# EINGABE
Länge, Breite = eingabe()

# VERARBEITUNG
Umfang, Fläche=kalk(Länge,Breite)

# AUSGABE
ausgabe(Länge, Breite, Umfang, Fläche)
