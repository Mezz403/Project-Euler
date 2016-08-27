import encryption

def brute_force_encrypt(chrText, firstChr, lastChr):
    output = open('bruteforceoutput.txt', 'w')

    for letter1 in range(firstChr, lastChr):
        for letter2 in range(firstChr, lastChr):
            for letter3 in range(firstChr, lastChr):
                password = str(chr(letter1) + chr(letter2) + chr(letter3))
                message = encryption.encrypt(chrText, password)
                output.write('\n')
                output.write('Password: %s' % password)
                output.write('\n')
                output.write('Decrypted Message')
                output.write('\n')
                output.write(''.join(chr(e) for e in message))

    output.close()