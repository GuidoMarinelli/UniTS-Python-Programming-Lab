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
        print(' \U0001F621 Devi inserire un numero maggiore o uguale a 1.')
    else:
        if number_selected < 1:
            print(' \U0001F621 Il numero inserito deve essere maggiore o uguale a 1.')
        else:
            generator = times_tables_generator(number_selected)
            choice = False

# Gestisce il prompt del titolo
if number_selected == 1:
    header = f"\n\t\t Tabellina dell'{number_selected}\n"
else:
    header = f"\n\t\t Tabellina del {number_selected}\n"

print(header.upper())
print('   Per terminare inserisci un intero negativo.\n\n')

# Loop che chiede in modo interattivo all'utente il valore da indovinare
sentinel = True

while sentinel:
    try:
        answer = int(input('Indovina il valore corrente nella tabellina: '))
    except ValueError:
        print(' \U0001F621 Hai sbagliato a digitare! Riprova!')

    else:
        value = next(generator)
        if answer == value:
            print(' Bravo! \U0001F44D')
        elif answer < 0:
            print(' Alla prossima! \U0001F44B')
            sentinel = False
        else:
            print(f' Hai Sbagliato! \U0001F631 Il valore corretto è {value}')
