print("Willkommen in meinem ersten Spiel!")
name = input("Wie ist dein Name? ")
age = int(input("Wie alt bist du? "))  # Convert age to an integer

health = 20  # Increased health points

if age >= 18:
    print("Du bist alt genug!")

    wants_to_play = input("Willst du spielen? ").lower()
    if wants_to_play == "ja":
        print("Okay, dann lass uns spielen!")
        print("Du hast " + str(health) + " Lebenspunkte.")

        left_or_right = input("Erste Entscheidung... Links oder Rechts (links/rechts)? ").lower()
        if left_or_right == "links":
            ans = input("Schön, du folgst dem Weg und kommst an einen See... Möchtest du hindurch schwimmen oder drumherum laufen (hindurch/drumherum)? ")

            if ans == "drumherum":
                print("Du bist drumherum gegangen und hast die andere Seite des Sees erreicht.")
            elif ans == "hindurch":
                print("Du bist hindurch geschwommen und wurdest von einem Fisch gebissen, die verlierst 5 Lebenspunkte.")
                health -= 5

            ans = input("Du siehst ein Haus und einen Fluss. Wohin gehst du (fluss/haus)? ")
            if ans == "haus":
                print("Du hast das Haus erreicht und wirst von dem Besitzer gegrüßt, aber er mag dich nicht, deshalb verlierst du 5 Lebenspunkte.")
                health -= 5

                if health <= 0:
                    print("Du hast keine Lebenspunkte mehr und verlierst...")
                else:
                    print("Es geht weiter!")

                ans = input("Möchtest du etwas essen? (ja/nein) ")
                if ans == "ja":
                    print("Du isst etwas und fühlst dich gestärkt.")
                    health += 10  # Increased health points
                    print("Deine Lebenspunkte sind jetzt " + str(health) + ".")
                else:
                    print("Du gehst weiter.")

                ans = input("Du siehst einen Wald und einen Berg. Wohin gehst du (wald/berg)? ")
                if ans == "wald":
                    print("Du betrittst den Wald und triffst auf einen Bären. Du verlierst 10 Lebenspunkte.")
                    health -= 10

                    if health <= 0:
                        print("Du hast keine Lebenspunkte mehr und verlierst...")
                    else:
                        print("Es geht weiter!")

                    ans = input("Möchtest du einen Heiltrank trinken? (ja/nein) ")
                    if ans == "ja":
                        print("Du trinkst einen Heiltrank und fühlst dich wieder besser.")
                        health += 15  # Increased health points
                        print("Deine Lebenspunkte sind jetzt " + str(health) + ".")
                    else:
                        print("Du gehst weiter.")

                elif ans == "berg":
                    print("Du kletterst den Berg hinauf und findest einen Schatz. Du erhältst 20 Lebenspunkte.")
                    health += 20

                    print("Es geht weiter!")

                    ans = input("Möchtest du das Spiel noch einmal spielen? (ja/nein) ")
                    if ans == "ja":
                        print("Okay, lass uns nochmal spielen!")
                        # Hier kannst du den Code für eine erneute Spielrunde einfügen
                    else:
                        print("Auf Wiedersehen. Danke fürs Spielen!")

                else:
                    print("Ungültige Eingabe!")

            else:
                print("Du fällst in den Fluss und verlierst...")

        else:
            print("Du fällst herunter und stirbst...")

        ans = input("Möchtest du das Spiel noch einmal spielen? (ja/nein) ")
        if ans == "ja":
            print("Okay, lass uns nochmal spielen!")
            # Hier kannst du den Code für eine erneute Spielrunde einfügen
        else:
            print("Auf Wiedersehen. Danke fürs Spielen!")

    else:
        print("Okay, Auf Wiedersehen.")
else:
    print("Du bist noch nicht alt genug!")
