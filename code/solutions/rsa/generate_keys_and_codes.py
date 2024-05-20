"""
    not for students
"""

import rsa_functions

primes_couples = [(11, 17), (13, 23), (29, 97), (97, 127), (8191, 127)]


def generate_key_code(p, q, index):
    """
    for a single value
    """
    phi = (p - 1) * (q - 1)
    print(f"p, q: {p}, {q}")
    n = p * q
    a, b = rsa_functions.generate_rsa_keys(p, q)
    remainder = a * b % phi
    if remainder == 1:
        print("keys are ok : b is the inverse of a modulo phi")
    else:
        print("probem with keys ! b is not the inverse of a modulo phi")

    public_key = (n, a)
    private_key = b
    print(f"public key: {public_key}")
    print(f"private_key: {private_key}")

    # save the keys
    with open(f"rsa_keys/public_key_{index}.txt", "w") as text_file:
        text = text_file.write(f"{public_key[0]}, {public_key[1]}")

    with open(f"rsa_keys/private_key_{index}.txt", "w") as text_file:
        text = text_file.write(str(b))

    # text to code
    with open("texts/lorem.txt", "r") as text_file:
        text = text_file.read()

    code = rsa_functions.cipher_rsa(text, public_key)

    # save the code
    with open(f"crypted_messages/crypted_message_rsa_{index}.txt", "w") as text_file:
        text_file.write(code)
    print(f"code: {code}")


# generate_keys_codes(primes_couples)
# use Mersene numbers
# generate_key_code(2**607 - 1, 2**1  279 - 1, 6)
# generate_key_code(4409, 2003, 6)
# https://fr.wikipedia.org/wiki/Mersenne_Twister
# https://fr.wikipedia.org/wiki/Nombre_de_Mersenne_premier
# https://www.nombres-premiers.fr/liste.html
# https://fr.wikipedia.org/wiki/2_147_483_647_(nombre)
# https://fr.wikipedia.org/wiki/Test_de_primalit%C3%A9_de_Lucas-Lehmer_pour_les_nombres_de_Mersenne
generate_key_code(2147483647, 2305843009213693951, 7)
