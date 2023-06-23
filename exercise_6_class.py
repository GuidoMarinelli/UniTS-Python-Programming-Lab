#
# File: exercise_6_class.py
#
# Author: G.Marinelli
#
# Date: 2023/06/24
#
# Version: 1.0
#
# Description: Lezione 10 - Librerie: Soluzione Esercizio 6 come classe.
#

import numpy as np
import matplotlib.pyplot as plt


class CalculteIntegral:
    """
    Classe che compie operazioni di calcolo e visualizzazione di un integrale su una funzione gausiana 1D.
    """

    def __init__(self, min_int=0, max_int=0):
        self.min_int = min_int
        self.max_int = max_int
        self._integral = 0
        self._x = []
        self._y = []
        self._number_iterations = 0
        self.epsilon = None
        self._fig = None
        self._number_of_points = None

    def calculate_integral(self, number_of_points):
        """Metodo che ritorna il valore dell'integrale di una funzione dati il numero di punti di campionamento."""
        default = 1
        self._number_of_points = number_of_points
        self._x = np.linspace(self.min_int, self.max_int, self._number_of_points + default, dtype='int')
        self._y = [self._profilo_gaussiano(i, 10) for i in self._x]
        self._integral = np.trapz(self._profilo_gaussiano(self._x, 10), self._x)

        return self._integral

    @staticmethod
    def _profilo_gaussiano(v, sigma):
        # valore profilo gaussiano in posizione x, data apertura
        return np.exp(-0.5 * ((v / sigma) ** 2))

    def sampling_cycle(self, epsilon):
        """
        Metodo che incrementa ciclicamente il numero di punti di campionamento per migliorare la stima dell’intervallo
        e interrompe la stima dell’integrale quando la differenza tra valore precedente ed attuale è minore del valore
        di approssimazione massimo definito 'epsilon'.
        Stampa il valore finale dell’integrale ed il numero di iterazioni eseguito per ottenerlo.
        """
        actual_integral = 0
        num_points = 1
        diff = 1
        prev_integral = 1

        while diff >= epsilon:
            actual_integral = self.calculate_integral(num_points)
            diff = abs(actual_integral - prev_integral)

            prev_integral = actual_integral
            self._number_iterations += 1
            num_points += 1

        print(f"Value of the integral: {actual_integral}, number of iterations: {self._number_iterations - 1}")

    def print_charts(self):
        """Metodo che visualizza la funzione campionata in 3 momenti: default, metà corrispondente al risultato."""
        self._fig, (ax1, ax2, ax3) = plt.subplots(nrows=1, ncols=3, figsize=(15, 5))

        x_default = self._x[0]
        y_default = self._y[0]

        x_half_it = self._x[:(round(self._number_iterations / 2))]
        y_half_it = self._y[:(round(self._number_iterations / 2))]

        self._fig.suptitle('The function sampled in 3 moments:', size=17)

        ax1.set_title('At the first default estimate')
        ax1.set_xlim(xmin=-58.5, xmax=58.5)
        ax1.set_ylim(ymin=-0.05, ymax=1.05)
        ax1.plot(x_default, y_default, color='b', marker='x')

        ax2.set_title('Half of the total number of iterations')
        ax2.set_xlim(xmin=-58.5, xmax=58.5)
        ax2.set_ylim(ymin=-0.05, ymax=1.05)
        ax2.plot(x_half_it, y_half_it)

        ax3.set_title('Final curve corresponding to the result')
        ax3.set_xlim(xmin=-58.5, xmax=58.5)
        ax3.set_ylim(ymin=-0.05, ymax=1.05)
        ax3.plot(self._x, self._y, color='darkorange')

        plt.show()

    def graph_above_threshol_y(self, y):
        """Metodo che visualizza la funzione sopra una soglia 'y' data."""
        y_threshold = []

        for value in self._y:
            if value < y:
                y_threshold.append(None)
            else:
                y_threshold.append(value)

        self._fig, ax = plt.subplots()

        ax.plot(self._x, y_threshold)
        ax.set_xlim(xmin=-58.5, xmax=58.5)
        ax.set_ylim(ymin=-0.05, ymax=1.05)
        ax.set_title(f'Graph with only the portion of function above the threshold y = {y}')

        plt.show()

    def save_chart(self, name='untitled'):
        """Metodo che salva il grafico."""
        self._fig.savefig(name)

    def __repr__(self):
        """Metodo che ritorna la stringa del calcolo del valore dell'integrale per il numero di punti massimi."""
        return f"Given {self._number_of_points} sampling points, the value of the integral is {self._integral}"


def main():
    integral = CalculteIntegral(-50, 50)
    max_points = int(input('Please enter the number of points you want to sample the function with: '))
    integral.calculate_integral(max_points)
    print(integral)
    integral.sampling_cycle(1.0e-5)
    integral.print_charts()
    integral.save_chart('graph1')
    integral.graph_above_threshol_y(0.2)
    integral.save_chart('graph2')


# chiamo la funzione principale
main()
