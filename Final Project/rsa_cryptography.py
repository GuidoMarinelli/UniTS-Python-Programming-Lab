#
# File: rsa_cryptography.py
#
# Author: G.Marinelli
#
# Date: 2023/07/13
#
# Version: 1.0
#
# Description: Implementing the RSA Public Key Encryption Algorithm.
#

import math
import random
import time


# ## Utility function
def load_message():
    """Takes a file as input, displays it and return it."""
    file_extension = '.txt'

    while True:
        try:
            filename = input('Enter the name of file to be encoded: ')
            file = filename + file_extension
            
            with open(file, mode='r') as f:
                text = f.read()
                
        except FileNotFoundError:
            print('No such files in the directory.\n')
            
        else:
            return text


def generate_key_e(z):
    """Determines the exponent e of the public key."""
    e = 0

    # find the first uncommon and smaller factor than z
    for i in range(2, z):
        if math.gcd(z, i) == 1:
            e = i
            break

    return e


def generate_key_d(z, e):
    """Determines the exponent d of the private key."""
    d = 0

    for i in range(z):

        if ((e * i) % z) == 1:
            d = i
            break

    return d


def int_to_binary(int_char):
    """Converts integer to binary by applying a padding."""
    unicode32_length = 32
    pad = '0'

    bin_char = str(bin(int_char))[2:]
    bin_char_length = len(bin_char)

    return pad * (unicode32_length - bin_char_length) + bin_char


def rsa_encode(m):
    return (m ** e) % n


def rsa_decode(c):
    return (c ** d) % n


def encode(message):
    message_list = [ord(char) for char in list(message)]
    code = [rsa_encode(m) for m in message_list]
    # print('encode int:', c_list)
    return ''.join([int_to_binary(c) for c in code])


def decode(code):
    unicode32_length = 32
    base = 2
    k = int(len(code) / unicode32_length)

    split_code = [code[unicode32_length * i: unicode32_length * (i + 1)] for i in range(k)]
    code_int = [int(c, base) for c in split_code]
    return ''.join([chr(rsa_decode(c)) for c in code_int])


def export_encrypted_file(encrypted_text, filename='file'):
    """Save the encrypted file as 'encrypted_filename.txt'."""
    file_extension = '.txt'

    encrypted_file = 'encrypted_' + filename + file_extension
    
    with open(encrypted_file, mode='w') as f:
        f.write(encrypted_text)


# Main Program

# Generation of public and private keys
# import a list of prime number values from a txt file
filename_ds = 'prime_number_ds.txt'

with open(filename_ds, 'r') as f:
    data = f.readline()

prime_number_ds = [int(p) for p in data.split(',')]

# randomly select two prime numbers from the dataset
p = random.choice(prime_number_ds)
q = random.choice(prime_number_ds)

print('Prime number p =', p)
print('Prime number q =', q)

# calculate the modulus
n = p * q

# calculate the tozient function
z = (p - 1) * (q - 1)

# determines the exponent e of the public key
e = generate_key_e(z)  
# determines the exponent d of the private key
d = generate_key_d(z, e)

# view the keys
print('\nKEYS:')
print(f'Public key: {n, e}')
print(f'Private key: {n, d}\n')


# Performs the encryption process
# load a message from a txt file
my_message = load_message()  

print('\nTEXT PRESENT IN THE FILE:')
print(my_message)

# encryption of the message
encrypted_message = encode(my_message)

# view the contents of the encrypted file
print('\nENCRYPTED FILE:')
print(encrypted_message)

# save the encrypted message
export_encrypted_file(encrypted_message)


# Performs the decryption process

start = time.time()

# decryption of the encrypted message
decrypted_message = decode(encrypted_message)

# view the contents of the dencrypted file
print('\nCHECK THE PROCESS (decrypted file):\n')
print(decrypted_message)

end = time.time()

print(f'\nTime for decryption of the message: {end - start:.1f}s')
