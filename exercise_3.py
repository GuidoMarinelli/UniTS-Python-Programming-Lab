#
# File: exercise_3.py
#
# Author: G.Marinelli
#
# Date: 2023/06/22
#
# Version: 1.0
#
# Description: Lezione 5 - Regine: Soluzione Esercizio 3.
#

#  Il Problema delle 8 regine
# 
# Il rompicapo (o problema) delle otto regine** è un problema che consiste nel trovare il modo di posizionare
# otto donne (pezzo degli scacchi) su una scacchiera 8x8 tali che nessuna di esse possa catturarne un’altra,
# usando i movimenti standard della regina. Perciò, una soluzione dovrà prevedere che nessuna regina abbia una colonna,
# traversa o diagonale in comune con un’altra regina. […]” (Wikipedia)

# funzioni di utilità prese dal programma dei professori

#
# File: Otto_regine.py
#
# Author: E.Romelli, D.Tavagnacco
#
# Date: 2021/04/13
#
# Version: 1.0
#
# Description: Example program to solve 8 queen-like problem
#              using brute force + random approach
#

import random
import time


def stessa_diagonale(x0, y0, x1, y1):
    """
    Ritorna Vero se posizioni (x0, y0) e (x1, y1) sono sulla stessa "diagonale"
    """
    # distanza lungo y
    dy = abs(y1 - y0)

    # distanza lungo x
    dx = abs(x1 - x0)

    # se dx == dy , dx/dy == 1 e sono sulla stessa diagonale, boolean expression
    return dx == dy


def incrocia_colonne(posizioni, col):
    """
    Ritorna Vero se la colonna 'col', che indica la posizione della regina 
    (col, posizioni[col]) incrocia la diagonale di qualcuna 
    delle posizioni delle regine precedenti
    """
    # controllo tutte le precedenti fino a questa 'col'
    for c in range(col):
        # la coordinata X (la riga) è indice (c)
        # la coordinata Y,(la colonna) è valore lista nell'indice (c)
        if stessa_diagonale(c, posizioni[c], col, posizioni[col]):
            # stop se trovo problemi
            return True
            # nessun incrocio, la posizione va bene e NON incrocia altre colonne
    return False


def soluzione_ok(soluzione_posizioni):
    """
    Controlla tutte le posizioni della possibile soluzione 
    'soluzione_posizioni' per verificare se ognuna delle posizioni 
    (colonne dela permatazione) ogni colonna incrocia la diagonale 
    di qualche altra posizione
    """

    for col in range(1, len(soluzione_posizioni)):
        # verifica se incrocia
        # if incrocia_colonne(soluzione_posizioni, col) == True:
        if incrocia_colonne(soluzione_posizioni, col):
            # stop se trova incroci, la soluzione non è valida
            return False

            # Se non è ritornato prima,
    # allora nessun incrocio trvato: posizioni della soluzione valide
    return True


# 1. Trovate 7 soluzioni per il gioco delle regine con il metodo delle permutazioni: quanto è il tempo medio?
print('Tempo medio per trovare 7 soluzioni per il gioco delle regine con il metodo delle permutazioni.'.upper())

number_solutions = 7
solutions = 0
times_list = []

# inizializzo generatore permutazioni
random_generator = random.Random()

# preparo la "possibile soluzione" con posizoni da testare
scacchiera = list(range(8))

# misuro il tempo di partenza per la ricerca della soluzione
start_time = time.time()

while solutions < number_solutions:

    # permutazione casuale della soluzione 'mescolando' posizioni
    random_generator.shuffle(scacchiera)

    # verifica se la permutazione casuale e' soluzione
    # if soluzione_ok(scacchiera) == True:
    if soluzione_ok(scacchiera):
        
        time_solution = time.time() - start_time
        times_list.append(time_solution)

        # se la soluzione è buona, scrive
        print(f'Found solution {scacchiera} in {time_solution} s.')

        # incremento contatore soluzioni trovate (condizione stop loop)
        solutions += 1

        # reset timer ricerca soluzione
        start_time = time.time()

print(f"The average time is {sum(times_list) / number_solutions} s.")


# 2. Contate quanti tentativi fa il programma per trovare ogni soluzione del problema 8 regine
print('\nConta quanti tentativi fa il programma per trovare ogni soluzione del problema 8 regine.'.upper())

solutions = 0
attempts = 0

# inizializzo generatore permutazioni
random_generator = random.Random()

# preparo la "possibile soluzione" con posizoni da testare
scacchiera = list(range(8))

# misuro il tempo di partenza per la ricerca della soluzione
start_time = time.time()

while solutions < 1:

    # permutazione casuale della soluzione 'mescolando' posizioni
    random_generator.shuffle(scacchiera)

    # verifica se la permutazione casuale e' soluzione
    # if soluzione_ok(scacchiera) == True:
    if soluzione_ok(scacchiera):
        # se la soluzione è buona, scrive
        print(f'Found solution {scacchiera} in {time.time() - start_time} s.')

        # incremento contatore soluzioni trovate (condizione stop loop)
        solutions += 1

        # reset timer ricerca soluzione
        start_time = time.time()
    else:
        attempts += 1

print(f'The number of attempts is {attempts}')


# 3. Alcune soluzioni possono essere ripetute: fate in modo che le soluzioni siano “uniche”
print('\nTrova solo soluzioni uniche.'.upper())

unique_solution = []
solutions = 0
number_solutions = 7

# inizializzo generatore permutazioni
random_generator = random.Random()

# preparo la "possibile soluzione" con posizoni da testare
scacchiera = list(range(8))

# misuro il tempo di partenza per la ricerca della soluzione
start_time = time.time()

while solutions < number_solutions:

    # permutazione casuale della soluzione 'mescolando' posizioni
    random_generator.shuffle(scacchiera)
    
    # verifica se la permutazione casuale e' soluzione
    # if soluzione_ok(scacchiera) == True:
    if soluzione_ok(scacchiera):
        
        if scacchiera not in unique_solution:
            unique_solution.append(scacchiera.copy())

            # se la soluzione è buona, scrive
            print(f'Found solution {scacchiera} in {time.time() - start_time} s.')

            # incremento contatore soluzioni trovate (condizione stop loop)
            solutions += 1
    
            # reset timer ricerca soluzione
            start_time = time.time()
        
print(f'Number of unique solutions: {len(unique_solution)} ')


# 4. Se ci sono soluzioni ripetute, contate quante volte ogni soluzione è ripetuta
print('\nSe ci sono soluzioni ripetute, conta quante volte ogni soluzione è ripetuta.'.upper())

solutions_list = []
unique_solution = []
solutions = 0
number_solutions = 7

# inizializzo generatore permutazioni
random_generator = random.Random()

# preparo la "possibile soluzione" con posizoni da testare
scacchiera = list(range(8))

# misuro il tempo di partenza per la ricerca della soluzione
start_time = time.time()

while solutions < number_solutions:

    # permutazione casuale della soluzione 'mescolando' posizioni
    random_generator.shuffle(scacchiera)
    
    # verifica se la permutazione casuale e' soluzione
    # if soluzione_ok(scacchiera) == True:
    if soluzione_ok(scacchiera):
        # se la soluzione è buona, scrive
        print(f'Found solution {scacchiera} in {time.time() - start_time} s.')
        solutions_list.append(scacchiera.copy())

        if scacchiera not in unique_solution:
            unique_solution.append(scacchiera.copy())

            # se la soluzione è buona, scrive
            #print(f'Found solution {scacchiera} in {time.time() - start_time} s.')

            # incremento contatore soluzioni trovate (condizione stop loop)
            solutions += 1
    
            # reset timer ricerca soluzione
            start_time = time.time()

if len(solutions_list) != number_solutions:
    print('\n      TIMES THAT A SOLUTION APPEARS ')
    
    for solution in unique_solution:
       print(f'Solution {solution} appears {solutions_list.count(solution)} times.')


# 5. Generalizzate il programma per risolvere una scacchiera di qualunque dimensione NxN
def main(dim_scacchiera = 8):
    if dim_scacchiera < 4:
        print('The size of the chessboard must be at least 4x4 for the queens problem to be resolved.')
    else:
        # inizializzo generatore permutazioni
        random_generator = random.Random()
    
        # preparo la "possibile soluzione" con posizoni da testare
        scacchiera = list(range(dim_scacchiera))
    
        # conto le soluzioni trovate, inizio da 0
        solutions = 0
    
        # misuro il tempo di partenza per la ricerca della soluzione
        start_time = time.time()
    
        # loop finchè non trovo una soluzione
        while solutions < 1:
    
            # permutazione casuale della soluzione 'mescolando' posizioni
            random_generator.shuffle(scacchiera)
    
            # verifica se la permutazione casuale e' soluzione
            # if soluzione_ok(scacchiera) == True:
            if soluzione_ok(scacchiera):
                # se la soluzione è buona, scrive
                print(f'Found solution {scacchiera} in {time.time() - start_time} s.')
    
                # incremento contatore soluzioni trovate (condizione stop loop)
                solutions += 1
    
                # reset timer ricerca soluzione
                start_time = time.time()


# chiamo la funzione principale
print('\nProgramma generallizato per risolvere una scacchiera di qualunque dimensione NxN.'.upper())

main(10)


# 6. Trovate quale è la scacchiera più grande di cui si riesce a trovare 1 soluzione in meno di 40s
def main(dim_scacchiera = 8):
    if dim_scacchiera < 4:
        print('The size of the chessboard must be at least 4x4 for the queens problem to be resolved.')
    else:
        # inizializzo generatore permutazioni
        random_generator = random.Random()
    
        # preparo la "possibile soluzione" con posizoni da testare
        scacchiera = list(range(dim_scacchiera))
    
        # conto le soluzioni trovate, inizio da 0
        solutions = 0
    
        # misuro il tempo di partenza per la ricerca della soluzione
        start_time = time.time()
    
        # loop finchè non trovo una soluzione
        while solutions < 1:
    
            # permutazione casuale della soluzione 'mescolando' posizioni
            random_generator.shuffle(scacchiera)
    
            # verifica se la permutazione casuale e' soluzione
            # if soluzione_ok(scacchiera) == True:
            if soluzione_ok(scacchiera):
                processing_time = time.time() - start_time
                
                # se la soluzione è buona, scrive
                # print(f'Found solution {scacchiera} in {time.time() - start_time} s.')
    
                # incremento contatore soluzioni trovate (condizione stop loop)
                solutions += 1
    
                # reset timer ricerca soluzione
                start_time = time.time()
    
        return processing_time


# chiamo la funzione principale
print('\nTrova la scacchiera più grande di cui si riesce a trovare 1 soluzione in meno di 40s.'.upper())

proces_time = 0
dimension = 4

while proces_time < 40:
    proces_time = main(dimension)
    
    if proces_time < 40:
        print(f'Found solution for the {dimension}x{dimension} size chessboard in {proces_time} s.')
    
    dimension += 1

print('\nEND')


# 7. Ogni soluzione è ‘simmetrica’ per rotazioni della scacchiera 8x8 di 90, 180 e 270 gradi.
# Trovata una soluzione, costruite le 4 simmetriche per rotazione prima di cercarne un’altra
def rotation_90(values_list):
    """Funzione che data la lista di soluzioni trova le soluzioni per simmetria di 90°."""
    turned_list = [0 for i in range(8)]
    col_reversed = 7
    
    for value in values_list:
        turned_list[value] = col_reversed
        col_reversed -= 1

    return turned_list


print('\nTrovata una soluzione, costruisce le 4 simmetriche per rotazione prima di cercarne un’altra.'.upper())

# inizializzo generatore permutazioni
random_generator = random.Random()

# preparo la "possibile soluzione" con posizoni da testare
scacchiera = list(range(8))

# conto le soluzioni trovate, inizio da 0           
solutions = 0     

# misuro il tempo di partenza per la ricerca della soluzione
start_time = time.time()

while solutions < 1:

    # permutazione casuale della soluzione 'mescolando' posizioni
    random_generator.shuffle(scacchiera)
    
    # verifica se la permutazione casuale e' soluzione
    # if soluzione_ok(scacchiera) == True:
    if soluzione_ok(scacchiera):
        # soluzioni simmetriche per rotazione di 90°, 180° 270°
        solution_90 = rotation_90(scacchiera)
        solution_180 = rotation_90(solution_90)
        solution_270 = rotation_90(solution_180)
        
        # se la soluzione è buona, scrive
        print(f'Found solution {scacchiera} in {time.time() - start_time} s.')
        print(f'\nFound solution for rotation of 90° is {solution_90}')
        print(f'Found solution for rotation of 180° is {solution_180}')
        print(f'Found solution for rotation of 270° is {solution_270}')

        # incremento contatore soluzioni trovate (condizione stop loop)
        solutions += 1

        # reset timer ricerca soluzione
        start_time = time.time()

