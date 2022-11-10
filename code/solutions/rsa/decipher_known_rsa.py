"""
    Deciphering a crypted text when we know the private key.
"""
import rsa_functions
from termcolor import colored

# load the keys
with open("rsa_keys/generated_public_key.txt", "r") as text_file:
    public_key_str = text_file.read()

with open("rsa_keys/generated_private_key.txt", "r") as text_file:
    private_key_str = text_file.read()

# convert to integers
n = int(public_key_str.split(",")[0])
a = int(public_key_str.split(",")[1])
b = int(private_key_str)

public_key = (n, a)
private_key = b
print(f"public key : {public_key}")
print(f"private_key : {private_key}")

with open("crypted_messages/crypted_message_rsa.txt", "r") as code_txt:
    code = code_txt.read()

print("code : " + code)

deciphered_text = rsa_functions.decipher_rsa(code, public_key, private_key)
with open("decrypted_messages/decrypted_message_rsa.txt", "w") as text_file:
    text_file.write(deciphered_text)
print(colored("deciphered text : " + deciphered_text, "blue", attrs=["bold"]))
