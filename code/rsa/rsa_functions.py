"""
    Functions used to implement the simplification of RSA.

    RSA : Rivest, Shamir, Adleman (1977)
    in this case, the public key is used to cipher the text and the
    private key is used to decipher the text. However this can
    depend on the situation.
"""

import math
from random import randrange
from termcolor import colored
from itertools import count, islice


def generate_rsa_keys(p: int, q: int) -> tuple[int, int]:
    """
    Using two primary numbers p and q, generate the keys

    :param p (int): prime number
    :param q (int): prime number
    :returns (a, b) (tuple of ints): elements of private and public key
    """
    # find the number a
    phi = (p - 1) * (q - 1)
    # find a such that a and phi are coprime
    # les entiers a et phi doivent etre premiers entre eux.
    """
        EDIT HERE
    """
    a = randrange(1, phi)
    while not a % 2 == 0:
        a += 1

    # find b such that ab=1[phi]
    # b is the inverse of a modulo phi
    r, b, v, r2, b2, v2 = a, 1, 0, phi, 0, 1
    # we use the extended euclid algorithm
    while not (r2 == 0):
        q = r // r2
        r, b, v, r2, b2, v2 = r2, b2, v2, r - q * r2, b - q * b2, v - q * v2
    while b < 0:
        b += phi
    return (a, b)


def cipher_rsa(text: str, public_key: tuple[int, int]) -> str:
    """
    Ciphers a text with RSA algorithm.

    :param text (str): message to cipher
    :param public_key (tuple): key used to cipher
    :returns code (str): message ciphered (string containing integers)
    """
    print("cipher rsa")
    n = public_key[0]
    a = public_key[1]
    code = ""
    for character in text:
        ascii_index = ord(character)
        """
            EDIT HERE
        """
        coded_index = 1
        print(colored(character + f" ({ascii_index})", "blue", attrs=["bold"]), end="")
        print(" becomes ", end="")
        print(colored(coded_index, "blue", attrs=["bold"]))
        # we use a comma as a separator
        code += str(coded_index) + ","
    # remove the last comma
    code = code[:-1]
    return code


def decipher_rsa(code, public_key, private_key):
    """
    Deciphers the code.

    :param text (str): message to cipher
    :param public_key (tuple): key used to cipher
    :param private_key (tuple): key used to decipher
    :returns decoded_text (str): decoded message
    """
    print("decipher")
    n = public_key[0]
    b = private_key
    # separate the commas
    code_str = code.split(",")
    # convert to integers
    code_list = [int(x) for x in code_str]
    decoded_text = ""
    for coded_index in code_list:
        print(colored(coded_index, "blue", attrs=["bold"]), end="")
        """
        EDIT HERE
        """
        decoded_index = 73
        decoded_letter = "y"
        print(" becomes ", end="")
        print(colored(decoded_letter, "blue", attrs=["bold"]))
        decoded_text += decoded_letter
    return decoded_text


def find_private_key(public_key):
    """
    Finds the private key as a function
    of the public key (n,a) to break the RSA.
    It is sufficient to decompose n as a product of 2 prime numbers.
    n is known to be a composite number (not prime).

    :param public_key (tuple of ints): public key to use in order to
    find the private key
    :returns private_key (tuple): if found, returns the private key
    """
    n = public_key[0]
    a = public_key[1]
    # crucial step : find if n is a product of primary numbers
    p, q = primary_decomposition(n)
    # if yes, continue
    if not p == 0:
        # find b as before
        phi = (p - 1) * (q - 1)
        # b is the inverse of a modulo phi
        # extended euclid algorithm (as before)
        r, b, v, r2, b2, v2 = a, 1, 0, phi, 0, 1
        while not (r2 == 0):
            q1 = r // r2
            r, b, v, r2, b2, v2 = r2, b2, v2, r - q1 * r2, b - q1 * b2, v - q1 * v2
        while b < 0:
            b += phi
        return b, phi, p, q
    else:
        print("no primary decomposition found for n")
        # return for convenience
        return 0, 0, 0, 0


def primary_decomposition(n):
    """
    Decompose n in a product of prime numbers.
    Very importantly, there is a unique decomposition
    possible with prime numbers, with respect to the order
    of the product (pq=qp). This comes from the Gauss lemma.

    :param n (int): integer to decompose
    """
    # there is no need for testing all the values below n
    # (see course)
    # print('searching primary decomposition of ' + str(n))
    """
        EDIT THE LOOP
    """
    for p_test in range(2, 8):
        # check the remainder of
        # n/p_test to see if p_test divides n
        r_test = n % p_test
        if r_test == 0:
            # check if p_test is a primary number
            if isPrime(p_test):
                # print(str(p_test) + ' divides ' + str(n) + ' and is prime')
                q_test = n // p_test
                # check if q_test is a primary number
                if isPrime(q_test):
                    print(
                        f"decomposition in prime factors of {n} : {p_test} , {q_test}"
                    )
                    return p_test, q_test
    print("no decomposition in primary numbers found")
    # return 0 for convenience
    return 0, 0


def isPrime(n):
    if n < 2:
        return False

    # we use a genertor to save memory
    for number in islice(count(2), int(math.sqrt(n) - 1)):
        if n % number == 0:
            return False

    return True
