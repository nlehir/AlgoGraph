"""
    script that uses a simplification of rsa
    in order to generate keys from a couple of prime numbers
    and cipher a short text file.
"""
import os

from termcolor import colored

import rsa_functions

def main():
    # prime numbers used to generate the keys
    # it is necessary to use prime numbers,
    # instead of general integers
    p, q = 17, 11

    a, b = rsa_functions.generate_rsa_keys(p=p, q=q)

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
    public_key_path = os.path.join(
            "rsa_keys",
            "generated_public_key.txt"
            )
    with open(public_key_path, "w") as text_file:
        text_file.write(f"{public_key[0]}, {public_key[1]}")

    private_key_path = os.path.join(
            "rsa_keys",
            "generated_private_key.txt"
            )
    with open(private_key_path, "w") as text_file:
        text_file.write(str(b))

    """
    Encode a text
    and save it to a file.
    """
    # text to code
    input_text_path = os.path.join(
            "texts",
            "example_text.txt",
            )
    with open(input_text_path, "r") as text_file:
        text = text_file.read()
    
    code = rsa_functions.cipher_rsa(text=text, public_key=public_key)
    
    # save the encoded text
    encoded_text_path = os.path.join(
            "crypted_messages",
            "crypted_message_rsa.txt",
            )
    with open(encoded_text_path, "w") as text_file:
        text_file.write(code)
    print(f"code : {code}")

if __name__ == "__main__":
    main()
