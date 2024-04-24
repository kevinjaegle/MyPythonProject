# Python Tutorialreihe für Anfänger: Dein eigenes Abenteuerspiel erstellen

Wir werden ein Textbasiertes Abenteuerspiel – entwickeln. So kannst du nicht nur die Konzepte verstehen, sondern auch direkt anwenden und sehen, wie und wo sie im echten Projekt verwendet werden.

## Einführung und Setup

### Ziel des Projekts
Am Ende dieser Reihe wirst du ein vollständig funktionsfähiges Spiel haben, das du vorzeigen kannst. Dieses Spiel wird so gestaltet sein, dass es leicht erweiterbar ist, sodass du es nach Belieben anpassen und erweitern kannst.

### Für wen ist dieses Tutorial gedacht?
Dieses Tutorial ist ideal für Personen, die noch keine oder sehr wenig Erfahrung mit Programmieren haben und schnell in Python einsteigen möchten.

### Entwicklungsplattform
Wir werden Replit nutzen, eine browserbasierte Entwicklungsplattform, die keine Softwareinstallation erfordert. Alles, was du brauchst, ist ein Browser und eine Internetverbindung. Gehe auf [replit.com](https://replit.com) und richte dort ein Konto ein, wenn du noch keines hast. Wähle Python als deine bevorzugte Programmiersprache.

## Grundlegende Konzepte

### Druckausgabe in Python
Um in Python etwas in der Konsole auszugeben, verwenden wir die `print()` Funktion. Der Syntax ist sehr einfach:

```python
print("Hallo Welt!")
```

Diese Funktion zeigt alles, was du in Anführungszeichen setzt, in der Konsole an.

### Variablen und Datentypen
Python verwendet Variablen, um Daten zu speichern. Eine Variable kann als eine Art Behälter betrachtet werden, in dem Informationen gespeichert werden. Hier sind einige grundlegende Datentypen:

- **Strings (Zeichenketten)**: Text, umgeben von Anführungszeichen. Beispiel: `"Hallo"`.
- **Integer (Ganzzahlen)**: Ganze Zahlen ohne Dezimalpunkt. Beispiel: `5`.
- **Float (Fließkommazahlen)**: Zahlen mit Dezimalpunkt. Beispiel: `5.0`.
- **Boolean (Boolesche Werte)**: Wahrheitswerte, entweder `True` oder `False`.

### Benutzereingaben
Um Eingaben des Benutzers zu erhalten, verwenden wir die `input()` Funktion:

```python
name = input("Wie heißt du? ")
```

Dies fordert den Benutzer auf, seinen Namen einzugeben und speichert die Eingabe in der Variablen `name`.

## Das Spiel erstellen

### Spielstruktur
Unser Spiel wird ein textbasiertes "Wähle-dein-eigenes-Abenteuer"-Spiel sein. Das bedeutet, dass der Spieler zu Beginn des Spiels Entscheidungen trifft, die den Verlauf der Geschichte beeinflussen.

### Spielablauf
1. Der Spieler startet mit einer Gesundheitspunktzahl, z.B. 10.
2. Der Spieler wird gefragt, ob er nach links oder rechts gehen möchte.
3. Jede Entscheidung führt zu weiteren Situationen, in denen der Spieler weitere Entscheidungen treffen muss.
4. Das Ziel ist es, das Spiel zu überleben und das Abenteuer zu beenden.

### Beispiel für eine Spielsitzung
```python
print("Willkommen zu meinem ersten Spiel!")
name = input("Wie heißt du? ")
alter = int(input("Wie alt bist du? "))

if alter >= 18:
    print(f"Hallo {name}, du bist alt genug, um zu spielen!")
    gesundheit = 10
    print("Lass uns spielen!")
    richtung = input("Erste Entscheidung: Links oder rechts? (links/rechts) ")

    if richtung == "links":
        print("Du gehst nach links und erreichst einen See.")
        aktion = input("Schwimmst du über den See oder gehst du herum? (schwimmen/herum) ")
        if aktion == "schwimmen":
            print("Du hast es geschafft, aber ein Fisch hat dich gebissen. Du verlierst 5 Gesundheit.")
            gesundheit -= 5
        elif aktion == "herum":
            print("Du gehst sicher herum.")
    elif richtung == "rechts":


        print("Oh nein! Du bist in eine Falle getreten und hast sofort verloren.")

    print(f"Dein Abenteuer endet hier, {name}, mit {gesundheit} Gesundheitspunkten.")
else:
    print("Du bist leider zu jung, um zu spielen.")
```

## Abschluss
Durch dieses Projekt lernst du die Grundlagen von Python kennen und erhältst ein Gefühl dafür, wie du Programmierung in realen Projekten einsetzen kannst. Erweitere und modifiziere das Spiel nach deinen Wünschen und experimentiere mit verschiedenen Geschichten und Ergebnissen. Viel Spaß beim Coden und Spielen!
