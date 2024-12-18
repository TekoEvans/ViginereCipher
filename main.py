from vigenere import *
from cesar import *

print(viginere_cipher("Evans", "MOT"))
print(viginere_cipher("è{#[^", "MOT", reverse=True))

crypted_message = cesar_cipher("Evans", 528)
print(crypted_message)


print(cesar_uncipher("'XCPU", 528))
force_brute_cesar("'XCPU")
