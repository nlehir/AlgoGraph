"""
    Deciphering a crypted text without knowing the private key.
    This time, we need to find the private key.
"""
import rsa_functions
from termcolor import colored

# we have several public keys and private keys, 
# that involve larger prime numbers.
index = 5

# load the public key
with open('rsa_keys/public_key_' + str(index) + '.txt', 'r') as text_file:
    public_key_str = text_file.read()


# convert to integers
n = int(public_key_str.split(',')[0])
a = int(public_key_str.split(',')[1])
public_key = (n, a)
print(f"public key file : public_key_{index}.txt")
print(f"public key : {public_key}\n")

# find the private key
private_key, phi, p, q = rsa_functions.find_private_key(public_key)
if not p == 0	:
    print(colored(f"found private key : b={private_key}",
                  "blue",
                  attrs=["bold"]))
    print(f"p : {p}")
    print(f"q : {q}")
    print(f"phi : {phi}")
else:
    print("did not find primary decomposition")


with open(f"crypted_messages/crypted_message_rsa_{index}.txt", "r") as code_txt:
    code = code_txt.read()

print("\ncode : " + code)

decoded_text = rsa_functions.decipher_rsa(code, public_key, private_key)
print('decoded text : ' + decoded_text)
