
#!/usr/bin/python
#Beginn des Quellcodes

#Import von Bibliotheken
import sys

#Variablendeklaration
frage1 = "Wann wurde Python entwickelt - am Anfang oder am Ende der 1990er Jahre? (Anfang/Ende)"
frage2 = "Von welcher Person wurde Python entwickelt?"
frage3 = "Unterstützt Python objektorientierte Programmierung?"
punkte = 0
richtig = "Sehr gut, das war korrekt!"
falsch = "Das war leider falsch."

def punkteFunktion() :
    """Weil diese Befehle öfter aufgerufen werden, werden sie für Verringerung der Redundanz als Funktion ausgelagert."""
    global punkte
    punkte += 1
    print(richtig)

#Beginn des Quiz'
print("Willkommen zu unserem heutigen kleinen Python-Quiz des Tages!")
start = input("Möchten Sie beginnen?")
start = start.lower()
if start == "ja" or start == "j" or start == "yes" or start == "y":
    print("Vielen Dank, dass Sie an unserem Quiz teilnehmen. Wir beginnen mit der 1. Frage: ")
    antwort1 = input(frage1)
    antwort1 = antwort1.lower()
    if antwort1 == "anfang" : 
        punkteFunktion()
    else :
        print(falsch)
    print("Kommen wir nun direkt zur 2. Frage: ")
    antwort2 = input(frage2)
    antwort2 = antwort2.lower()
    if "rossum" in antwort2 :
        punkteFunktion()
    else :
        print(falsch)
    print("Abschließend noch die letzte Frage: ")
    antwort3 = input(frage3)
    antwort3.lower()
    if antwort3 == "ja" or antwort3 == "j" or "antwort3" == "yes" or antwort3 == "y":
        punkteFunktion()
    else :
        print(falsch)
    print("Vielen Dank für Ihre Teilnahma am kleinen Python-Quiz des Tages. Sie haben " + str(punkte) + " Fragen richtig beantwortet. Bis zum nächsten Mal!")
    sys.exit(0)
elif start == "nein" or "n" in start:
    print("In Ordnung. Das Programm wird beendet. Bis zum nächsten Mal!")
    sys.exit(0)
else:
    print("Wir konnten Ihre Eingabe nicht lesen. Das Programm wird beendet. Bitte starten Sie es erneut und prüfen Ihre Eingabe.")
    sys.exit(0)