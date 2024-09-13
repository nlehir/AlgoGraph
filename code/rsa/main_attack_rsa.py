"""
    Deciphering a crypted text without knowing the private key.
    This time, we need to find the private key.
"""
import os

from termcolor import colored

import rsa_functions

def main():
    # we have several public keys and private keys,
    # that involve larger prime numbers.
    index = 2

    # load the public key
    public_key_path = os.path.join(
            "rsa_keys",
            f"public_key_{index}.txt"
            )
    with open(public_key_path, "r") as text_file:
        public_key_str = text_file.read()

    # convert to integers
    n = int(public_key_str.split(",")[0])
    a = int(public_key_str.split(",")[1])
    public_key = (n, a)
    print(f"public key file : public_key_{index}.txt")
    print(f"public key : {public_key}\n")

    # find the private key
    private_key, phi, p, q = rsa_functions.find_private_key(public_key)
    if not p == 0:
        print(colored(f"found private key : b={private_key}", "blue", attrs=["bold"]))
        print(f"p : {p}")
        print(f"q : {q}")
        print(f"phi : {phi}")
    else:
        print("did not find primary decomposition")


    encoded_text_path = os.path.join(
            "crypted_messages",
            f"crypted_message_rsa_{index}.txt",
            )
    with open(encoded_text_path, "r") as code_txt:
        code = code_txt.read()

    print(f"\ncode : {code}")

    decoded_text = rsa_functions.decipher_rsa(
            code=code,
            public_key=public_key,
            private_key=private_key,
            )
    print(f"decoded text : {decoded_text}")

if __name__ == "__main__":
    main()
