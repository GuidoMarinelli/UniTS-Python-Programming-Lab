#
# File: exercise_4.py
#
# Author: G.Marinelli
#
# Date: 2023/05/30
#
# Version: 1.0
#
# Description: Lezione 6 - Input/Output: Soluzione Esercizio 4.
#

# Create un file di 'rubrica.txt' contenente:

text = '''
Paolino Paperino, 9, giugno, 1934, 89, M, paolino.paperin0@disney.org
Ron Weasley, 1, marzo, 1980, 43, M, ron_weasley80@hogwards.uk
Ramona Flowers, 18, ottobre, 2004, 19, F, ramona.fls@gmail.com
Madoka Ayukawa, 25, maggio, 1969, 54, F, madoka_sax@asahi_net.jp
'''

with open('rubrica.txt', 'w') as write_file:
    for line in text.split('\n'):
        write_file.write(f'{line}\n')


# 1. Leggete il file e organizzatelo in una struttura 'rubrica' a dizionari annidati:
print("Organizza il file in una struttura 'rubrica' a dizionari annidati.".upper())
with open('rubrica.txt', 'r') as file_read:
    file = file_read.read()
    print(file)

records = [record.split(',') for record in file.split('\n') if record != '']

rubrica = {}

for i, record in enumerate(records):
    values = {}
    
    name = record[0] 
    values['giorno'] = int(record[1])
    values['mese'] = record[2].strip()
    values['anno'] = int(record[3])
    values['età'] = int(record[4])
    values['sesso'] = record[5].strip()
    values['mail'] = record[6].strip()
    rubrica[name] = values
    
print(rubrica)


# 2. A partire dalla rubrica, costruire la lista delle età, ordinata in ordine crescente e visualizzate
# i nomi in ordine crescente di età
print('\nVisualizza la lista delle età in ordine crescente.'.upper())

age_list = [item['età'] for name, item in rubrica.items()]
age_list.sort()

for age in age_list:
    for name, value in rubrica.items():
        if age == value['età']:
            print(name, age)


# 3. Invertire l’ordine della lista precedentemente costruita e visualizzatela
print('\nVisualizza la lista delle età in ordine decrescente.'.upper())

age_list.sort(reverse=True)
print(age_list)


# 4. Utilizzare la rubrica per scrivere ad OGNI membro della rubrica un messaggio
print('\nUtilizza la rubrica per scrivere ad OGNI membro della rubrica un messaggio.'.upper())

for name, values in rubrica.items():
    if values['sesso'] == 'M':
        vowel = 'o'
    else:
        vowel = 'a'
    print(f"Car{vowel} {name},\n"
          f"sei nat{vowel} il {values['giorno']} di {values['mese']} del {values['anno']} e quindi a breve compirai {values['età']} anni.\n"
          f"Ti manderemo gli auguri a {values['mail']}\n""")
