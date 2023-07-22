#
# File: exercise_2.py
#
# Author: G.Marinelli
#
# Date: 2023/05/28
#
# Version: 1.0
#
# Description: Lezione 4 - Data Containers: Soluzione Esercizio 2.
#

# Partendo dal testo:
text = '''
Day after day, day after day,
We stuck, nor breath nor motion;
As idle as a painted ship
Upon a painted ocean.

Water, water, every where,
And all the boards did shrink;
Water, water, every where,
Nor any drop to drink.

The very deep did rot: O Christ!
That ever this should be!
Yea, slimy things did crawl with legs
Upon the slimy sea.

About, about, in reel and rout
The death-fires danced at night;
The water, like a witch's oils,
Burnt green, and blue and white.
'''


# 1. Contate le righe (di effettivo testo) che compongono l’estratto
count_rows = 0

for row in text.splitlines():
    if row != '':
        count_rows += 1

print(f'Il numero di righe di effettivo testo sono {count_rows}.')


# 2. Contate le parole che compongono l’estratto
count_words = 0

for word in text.split():
    count_words += 1

print(f"L'estratto è composto da {count_words} parole.")


# 3. Contate i caratteri che compongono l’estratto
count_chars = 0

for word in text.split():
    for char in word:
        count_chars += 1

print(f'Il numero di caratteri (compresi quelli di punteggiatura) sono {count_chars}')

# 4. Sostituite la parola  `water` con la parola `PYTHON` in tutti i versi
print(f"Sostituisce la parola 'water' con 'PYTHON: \n{text.replace('water', 'PYTHON')}")


# 5. Riscrivete il testo con tutte le parole in posizione pari scritte in maiuscolo
count = 0
text2 = ''''''

for sentence in text.splitlines():

    for word in sentence.split():
        count += 1

        if count % 2 == 0:
            text2 += word.upper() + ' '
        else:
            text2 += word + ' '

    text2 += '\n'

print(text2)


# 6. Riscrivete il testo, scrivendo a specchio il terzo verso di ogni strofa
text3 = ''''''

for i, sentence in enumerate(text.splitlines()):
    new_sentence = ''

    if i in [3, 8, 13, 18]:
        word_list = sentence.split()

        for j in range(len(word_list) - 1, -1, -1):
            new_sentence += word_list[j] + ' '

    else:
        new_sentence = sentence

    text3 += new_sentence + '\n'

print(text3)


# 7. Trovate eventuali parole che compaiono in tutte le strofe
new_text = ''''''
strofa1 = ''''''
strofa2 = ''''''
strofa3 = ''''''
strofa4 = ''''''

for sentence in text.splitlines():
    if sentence != '':
        for word in sentence.split():
            if word.endswith('!') or word.endswith(',') or word.endswith('.') or word.endswith(':') \
                    or word.endswith(';'):
                new_text += word[:-1] + ' '
            else:
                new_text += word + ' '
        new_text += '\n'

for i, sentence in enumerate(new_text.splitlines()):
    if i < 4:
        strofa1 += sentence
    if 4 <= i < 8:
        strofa2 += sentence
    if 8 <= i < 12:
        strofa3 += sentence
    if i >= 12:
        strofa4 += sentence

strofa1 = set(strofa1.split())
strofa2 = set(strofa2.split())
strofa3 = set(strofa3.split())
strofa4 = set(strofa4.split())

print(f'Parole che compaiono in tutte le strofe: {strofa1 & strofa2 & strofa3 & strofa4}')


# 8. Create la lista di tutte le parole che compaiono nel testo e ordinatela per lunghezza delle parole
# (la lista ordinata non deve contenere ripetizioni)
words_list = []
sorted_words_list = []

for word in text.split():
    if word.endswith('!') or word.endswith(',') or word.endswith('.') or word.endswith(':') or word.endswith(';'):
        words_list.append(word[:-1])
    else:
        words_list.append(word)

words_list = list(set(words_list))

max_length_word = max([len(word) for word in words_list])

for length in range(1, max_length_word + 1):
    for word in sorted(words_list):
        if len(word) == length:
            sorted_words_list.append(word)

print(sorted_words_list)


# 9. Create un dizionario che mappi ogni carattere (chiave) con la sua occorrenza nel testo (valore)
chars_dict = {}

for word in text.split():
    for char in word:
        if char in chars_dict:
            chars_dict[char] += 1
        else:
            chars_dict[char] = 1

print(chars_dict)


# 10. Create un dizionario come il precedente per le sole lettere (no caratteri speciali), ignorando maiuscole
# e minuscole
chars_dict2 = {}

for word in text.upper().split():
    for char in word:
        if char not in ['!', "'", ',', '-', '.', ':', ';']:
            if char in chars_dict2:
                chars_dict2[char] += 1
            else:
                chars_dict2[char] = 1

print(chars_dict2)
