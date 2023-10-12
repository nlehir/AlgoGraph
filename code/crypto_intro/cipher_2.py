"""
    second ciphering method
"""
from random import randrange

from termcolor import colored


def cipher_2(message, key_size):
    """
    the key size is a parameter of this method.
    How many subkeys do we want to use ?

    We assume the messages are uppercase letters only.
    See Ascii_sample.txt.

    :param message (str): message to cipher
    :param key_size (int): size of the ciphering key
    :returns crypted_message (str): ciphered message
    """
    key = [randrange(1, 27) for _ in range(key_size)]
    print(f"key : {key}")
    crypted_message = ""
    subkey = 0
    for character in message:
        # convert to ascii unicode code point
        ascii_index = ord(character)
        if ascii_index > 64 and ascii_index < 91:
            # change the unicode code point
            """
            EDIT HERE
            """
            new_index = 1
            # change the subkey
            subkey = 1
            # convert back to string
            crypted_message += chr(new_index)
        else:
            crypted_message += character
    with open("crypted_messages/crypted_message_2.txt", "w") as text_file:
        text_file.write(crypted_message)
    return crypted_message


print(
    "coded message : "
    + colored(cipher_2("ALGORITHM COURSE", 3), "green", attrs=["bold"])
)
