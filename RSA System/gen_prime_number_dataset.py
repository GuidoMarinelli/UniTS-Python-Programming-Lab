#
# File: gen_prime_number_dataset.py
#
# Author: G.Marinelli
#
# Date: 2023/07/13
#
# Version: 1.0
#
# Description: Program that creates a list of prime numbers.
#

import sympy

primes_ds = []

for i in range(800, 2000):
    if sympy.isprime(i) and len(primes_ds) < 100:
        primes_ds.append(i)

print("Check the number of items in 'primes_ds':")
print(len(primes_ds))
print('\nDisplay the first ten prime numbers in the list:')
print(primes_ds[:10])
print('\nDisplay the last ten prime numbers in the list:')
print(primes_ds[-10:])

filename = 'prime_number_ds.txt'
primes_str = ', '.join([str(value) for value in primes_ds])

# Save the list to a txt file
with open(filename, 'w') as f:
    f.write(primes_str)
