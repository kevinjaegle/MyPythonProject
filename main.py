print("Willkommen in meinem ersten Spiel!")
name = input("Wie ist dein Name? ")
age = int(input("Wie alt bist du? "))  # Convert age to an integer

print("Hallo " + name + "! Du bist " + str(age) + " Jahre alt.")  # Convert age back to a string for concatenation

if age >= 18:
    print("Du bist alt genug!")

    wants_to_play = input("Willst du spielen? ")
    if wants_to_play == "ja":
        print("Okay, dann lass uns spielen!")

else:
    print("Du bist noch nicht alt genug!")
