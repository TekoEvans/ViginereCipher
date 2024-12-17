import string

alphabet = string.printable + "éèêàôëùïü"


def cesar_cipher(message, key):
    crypted_message = ""
    # find index of out message charaters in all alphabet (string.printable)
    for char in message:
        index_charater_in_printable = alphabet.index(char)
        index_crypted_charater = (
            index_charater_in_printable + key) % (len(alphabet))
        crypted_charater = alphabet[index_crypted_charater]
        crypted_message += crypted_charater

    return crypted_message

# Uncipher  fonction


def cesar_uncipher(message, key):
    return cesar_cipher(message, key*(-1))

# force brute


def force_brute_cesar(message):
    for possible_key in range(len(alphabet)):
        uncrypted_message = cesar_uncipher(message, possible_key)
        print(uncrypted_message)
        print("*"*15)


def password_convertor_to_list_of_keys(password):
    list_of_keys = []
    for char in password:
        list_of_keys.append(alphabet.index(char))
        return list_of_keys


def viginere_cipher(message, password, reverse=False):
    crypted_message = ""
    list_of_keys = password_convertor_to_list_of_keys(password)

    for index, char in enumerate(message):
        current_key = list_of_keys[index % (len(list_of_keys))]
        crypted_message += cesar_cipher(
            char, current_key) if reverse else cesar_uncipher(char, current_key)
    return crypted_message


print(viginere_cipher("Evans", "MOT"))


# crypted_message = cesar_cipher("Evans", 528)
# print(crypted_message)


# print(cesar_uncipher("'XCPU", 528))
# force_brute_cesar("'XCPU")
