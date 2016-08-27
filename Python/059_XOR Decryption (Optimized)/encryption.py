def encrypt(text, password):
    encryptedMessage = []
    index = 0

    for char in text:
        encryptedMessage.append(ord(char) ^ ord(password[index]))
        if index == len(password) - 1:
            index = 0
        else:
            index += 1

    return encryptedMessage