"""
break the first ciphering solution

Known-plaintext attack.
"""

from random import shuffle
import time

max_number_of_attempts = int(1e4)


def decipher_1(code: str, extract: str, max_number_of_attempts: int) -> str:
    """
    From the coded message, find the original one based on an extract
    We assume that we know that the word "COURSE" is in the original
    message.

    We assume the messages are uppercase letters only.
    See Ascii_sample.txt.

    :param code (str): code to decipher
    :param extract (str): know extract in the text
    :param max_number_of_attempts (int): we manually limit the number of attempts
    :returns decoded_message (str): a decoded message
    """
    print(f"code to decipher : {code}")
    key = [i for i in range(26)]
    attempt = 0
    decoded_message = ""
    while extract not in decoded_message and attempt < max_number_of_attempts:
        decoded_message = ""
        # try a new key
        shuffle(key)
        attempt += 1
        if attempt % 1e3 == 0:
            print(f"attempt {attempt}")
        for character in code:
            ascii_index = ord(character)
            if ascii_index > 64 and ascii_index < 91:
                """
                EDIT HERE
                """
                key_index = key[6] + 65
                decoded_message += "r"
            else:
                decoded_message += character
        if "COURSE" in decoded_message:
            print(f"attempt : {attempt}")
            print(decoded_message)
    return decoded_message


with open("crypted_messages/crypted_message_1.txt", "r") as text_file:
    code = text_file.read()


time_before = time.time()
decoded_message = decipher_1(code, "COURSE", max_number_of_attempts)
total_time = time.time() - time_before
time_per_key = total_time / max_number_of_attempts
print(f"---\ntotal time {1e3*total_time} ms")
print(f"time per key {1e3*time_per_key} ms")
# print(f"necessary time to have around 40% of chances of stopping the program {time_per_key*1e8/60} min")
