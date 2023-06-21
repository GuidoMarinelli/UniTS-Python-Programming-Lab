#
# File: exercise_7.py
#
# Author: G.Marinelli
#
# Date: 2023/06/21
#
# Version: 1.0
#
# Description: Lezione 12 - Unpacking, Decoratori, Generatori, Lambda: Soluzione Esercizio 7.
#

FURIOUS_FACE = "\U0001F621"  # Valore unicode per l'emoji della faccina furiosa
THUMBS_UP = "\U0001F44D"  # Valore unicode per l'emoji del pollice rivolto verso l'alto
SCARED_FACE = "\U0001F631"  # Valore unicode per l'emoji della faccina che urla di paura
HAND_THAT_GREETS = "\U0001F44B"  # Valore unicode per l'emoji della mano che saluta


def times_tables_generator(number):
    """Funzione che crea il generatore della tabellina per un numero dato."""
    n = 0
    while True:
        yield n * number
        n = n + 1


# Chiede all'utente quale tabellina generare
choice = True

while choice:
    try:
        number_selected = int(input("Con quale tabellina vuoi giocare? "))
    except ValueError:
        print(f" {FURIOUS_FACE} Devi inserire un numero maggiore o uguale a 1.")
    else:
        if number_selected < 1:
            print(f" {FURIOUS_FACE} Il numero inserito deve essere maggiore o uguale a 1.")
        else:
            generator = times_tables_generator(number_selected)
            choice = False

# Gestisce il prompt del titolo
if number_selected == 1:
    header = f"\n\t\t Tabellina dell'{number_selected}\n"
else:
    header = f"\n\t\t Tabellina del {number_selected}\n"

print(header.upper())
print("   Per terminare inserisci un intero negativo.\n\n")

# Loop che chiede in modo interattivo all'utente il valore da indovinare
sentinel = True

while sentinel:
    try:
        answer = int(input("Indovina il valore corrente nella tabellina: "))
    except ValueError:
        print(f" {FURIOUS_FACE} Hai sbagliato a digitare! Riprova!")

    else:
        value = next(generator)
        if answer == value:
            print(f" Bravo! {THUMBS_UP}")
        elif answer < 0:
            print(f" Alla prossima! {HAND_THAT_GREETS}")
            sentinel = False
        else:
            print(f" Hai Sbagliato! {SCARED_FACE} Il valore corretto è {value}")
