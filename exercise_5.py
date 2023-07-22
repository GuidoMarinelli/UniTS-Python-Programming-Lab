#
# File: exercise_5.py
#
# Author: G.Marinelli
#
# Date: 2023/06/07
#
# Version: 1.0
#
# Description: Lezione 8 - Object Oriented Programming (OOP): Soluzione esercizio 5.
#

class Rubrica:
    """Classe per rappresentare una rubrica."""

    def __init__(self):
        """Metodo della classe che inizializza la nuova istanza."""
        self.rubrica = {}
        self._file_txt = None
        self._file_content = None

    def read_file(self, file_txt):
        """Metodo che legge il contenuto di un file di testo."""
        self._file_txt = file_txt
        with open(self._file_txt, 'r') as f:
            self._file_content = f.read().strip('\n')

    def structure(self):
        """Metodo che organizza in una struttura a dizionari annidati 'rubrica'."""
        records = [record.split(',') for record in self._file_content.split('\n') if record != '']

        for i, record in enumerate(records):
            values = {}
            name = record[0]
            values['giorno'] = int(record[1])
            values['mese'] = record[2].strip()
            values['anno'] = int(record[3])
            values['età'] = int(record[4])
            values['sesso'] = record[5].strip()
            values['mail'] = record[6].strip()
            self.rubrica[name] = values

    def age_list_sorted(self):
        """Metodo che restituisce una lista ordinata delle età."""
        return sorted([item['età'] for name, item in self.rubrica.items()])

    def age_list_reverse(self):
        """Metodo che restituisce una lista ordinata delle età in ordine decrescente."""
        return sorted([item['età'] for name, item in self.rubrica.items()], reverse=True)

    @staticmethod
    def new_element():
        """Metodo interattivo che restituisce una stringa per un nuovo contatto."""
        name = input('Inserisci il nome e cognome del nuovo contatto: ')
        day = input('Inserisci il giorno di nascita del nuovo contatto: ')
        month = input('Inserisci il mese di nascita del nuovo contatto: ')
        year = input("Inserisci l'anno di nascita del nuovo contatto: ")
        age = input("Inserisci l'età del nuovo contatto: ")
        sex = input('Inserisci il sesso del nuovo contatto: ')
        mail = input("Inserisci l'indirizzo email del nuovo contatto: ")
        return f'{name}, {day}, {month}, {year}, {age}, {sex}, {mail}\n'

    def update_rubrica(self, new_element):
        """Metodo che aggiorna il file di testo rubrica."""
        with open(self._file_txt, 'r+') as textwritefile:
            data = textwritefile.read().strip('\n')
            textwritefile.seek(0, 0)
            textwritefile.write(data + '\n')
            textwritefile.write(new_element)

    def print_messages(self):
        """Metodo che stampa per OGNI elemento della rubrica il seguente messaggio."""
        for name, values in self.rubrica.items():
            if values['sesso'] == 'M':
                vowel = 'o'
            else:
                vowel = 'a'
            print(f"Car{vowel} {name},\n"
                  f"sei nat{vowel} il {values['giorno']} di {values['mese']} del {values['anno']} e quindi a "
                  f"breve compirai {values['età']} anni.\n"
                  f"Ti manderemo gli auguri a {values['mail']}\n")


rubrica = Rubrica()
rubrica.read_file('rubrica.txt')
rubrica.structure()
print(rubrica.rubrica)
print(rubrica.age_list_sorted())
print(rubrica.age_list_reverse())
rubrica.print_messages()
# contact = rubrica.new_element()
# rubrica.update_rubrica(contact)
