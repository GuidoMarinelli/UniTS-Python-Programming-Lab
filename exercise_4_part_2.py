# File: exercise_4_part_2.py
#
# Author: G.Marinelli
#
# Date: 2023/06/07
#
# Version: 1.0
#
# Description: Lezione 7 - Command line: Soluzione esercizio 4 parte 2.
#
import argparse


def new_element():
    """
    Funzione che chiede in modo interattivo all’utente le informazioni necessarie ad aggiungere un nuovo elemento
    alla rubrica.
    """
    name = input('Inserisci il nome e cognome del nuovo contatto: ')
    day = input('Inserisci il giorno di nascita del nuovo contatto: ')
    month = input('Inserisci il mese di nascita del nuovo contatto: ')
    year = input("Inserisci l'anno di nascita del nuovo contatto: ")
    age = input("Inserisci l'età del nuovo contatto: ")
    sex = input('Inserisci il sesso del nuovo contatto: ')
    mail = input("Inserisci l'indirizzo email del nuovo contatto: ")
    return f'{name}, {day}, {month}, {year}, {age}, {sex}, {mail}\n'


def update_rubrica(file_txt, new_contact):
    """Funzione che aggiorna un file 'rubrica' passatole."""
    with open(file_txt, 'r+') as textwritefile:
        data = textwritefile.read().strip('\n')
        textwritefile.seek(0, 0)
        textwritefile.write(data + '\n')
        textwritefile.write(new_contact)


parser = argparse.ArgumentParser(prog="exercise_4_part_2.py",
                                 description="Chiede e aggiunge un nuovo elemento nel file rubrica.txt",
                                 epilog="G.Marinelli, 2023/06/07")
parser.add_argument('-n', '--file_name', default=None, help='Nome del file da cui leggere/scrivere la rubrica')

args = parser.parse_args()
file_rubrica = args.file_name

contact = new_element()
update_rubrica(file_rubrica, contact)
