"""
    Deciphering a crypted text when we know the private key.
"""
import os

from termcolor import colored

import rsa_functions

def main():
    # load the keys
    public_key_path = os.path.join(
            "rsa_keys",
            "generated_public_key.txt"
            )
    with open(public_key_path, "r") as text_file:
        public_key_str = text_file.read()

    private_key_path = os.path.join(
            "rsa_keys",
            "generated_private_key.txt"
            )
    with open(private_key_path, "r") as text_file:
        private_key_str = text_file.read()

    # convert to integers
    n = int(public_key_str.split(",")[0])
    a = int(public_key_str.split(",")[1])
    b = int(private_key_str)

    public_key = (n, a)
    private_key = b
    print(f"public key : {public_key}")
    print(f"private_key : {private_key}")

    encoded_text_path = os.path.join(
            "crypted_messages",
            "crypted_message_rsa.txt",
            )
    with open(encoded_text_path, "r") as code_txt:
        code = code_txt.read()

    print(f"code : {code}")

    deciphered_text = rsa_functions.decipher_rsa(
            code=code,
            public_key=public_key,
            private_key=private_key,
            )

    print(colored(f"deciphered text : {deciphered_text}", "blue", attrs=["bold"]))

if __name__ == "__main__":
    main()
