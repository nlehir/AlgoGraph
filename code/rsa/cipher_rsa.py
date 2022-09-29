"""
    script that uses a simplification of rsa
    in order to generate keys from a couple of prime numbers
    and cipher a short text file.
"""
import rsa_functions
from termcolor import colored

# prime numbers used to generate the keys
# it is important to use prime numbers
p, q = 17, 11

a, b = rsa_functions.generate_rsa_keys(p, q)

n = p * q
phi = (p - 1) * (q - 1)

public_key = (n, a)
private_key = b
print(f"public key : {public_key}")
print(f"private key : {private_key}")

# check our keys
remainder = a * b % phi
if remainder == 1:
    print(
        colored(
            "keys are ok : b is the inverse of a modulo phi", "blue", attrs=["bold"]
        )
    )
else:
    print(
        colored(
            "probem with keys ! b is not the inverse of a modulo phi",
            "yellow",
            attrs=["bold"],
        )
    )

# save the keys
with open("rsa_keys/generated_public_key.txt", "w") as text_file:
    text = text_file.write(f"{public_key[0]}, {public_key[1]}")

with open("rsa_keys/generated_private_key.txt", "w") as text_file:
    text = text_file.write(str(b))

# # text to code
# with open("texts/example_text.txt", "r") as text_file:
#     text = text_file.read()
#
# code = rsa_functions.cipher_rsa(text, public_key)
#
# # save the code
# with open("crypted_messages/crypted_message_rsa.txt", "w") as text_file:
#     text_file.write(code)
# print(f"code : {code}")
