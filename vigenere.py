from cesar import cesar_cipher ,cesar_uncipher, alphabet

def viginere_cipher(message, password, reverse=False):
    crypted_message = ""
    list_of_keys =[alphabet.index(char) for char in password]

    for index, char in enumerate(message):
        current_key = list_of_keys[index % (len(list_of_keys))]
        crypted_message += cesar_cipher(char, current_key) if reverse else cesar_uncipher(char, current_key)
    return crypted_message