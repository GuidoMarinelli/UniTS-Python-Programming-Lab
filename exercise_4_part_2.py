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


def update_rubrica(filetxt, new_contact):
    """Funzione che aggiorna un file 'rubrica' passatole."""
    with open(filetxt, 'a') as textwritefile:
        textwritefile.write(new_contact)


parser = argparse.ArgumentParser(prog="exercise_4_part_2.py",
                                 description="Chiede e aggiunge un nuovo elemento nel file rubrica.txt",
                                 epilog="G.Marinelli, 2023/06/07")

parser.add_argument('-f', '--filename', default='rubrica.txt', help='Nome del file da cui leggere/scrivere la rubrica')
parser.add_argument('-n', '--name', default=None, help='Nome del contatto da inserire nella rubrica')
parser.add_argument('-s', '--surname', default=None, help='Cognome del contatto da inserire nella rubrica')
parser.add_argument('-d', '--day', default=None, help='Giorno di nascita del contato')
parser.add_argument('-m', '--month', default=None, help='Mese di nascita del contatto')
parser.add_argument('-y', '--year', default=None, help='Anno di nascita del contatto')
parser.add_argument('-a', '--age', default=None, help='Età del contatto')
parser.add_argument('-g', '--gender', default=None, help='Sesso/genere del conatto')
parser.add_argument('-e', '--email', default=None, help='Indirizzo e-mail del contatto')

args = parser.parse_args()

filename = args.filename
name = args.name
surname = args.surname
day = args.day
month = args.month
year = args.year
age = args.age
gender = args.gender
email = args.email

contact = f'{name} {surname}, {day}, {month}, {year}, {age}, {gender}, {email}\n'
update_rubrica(filename, contact)
