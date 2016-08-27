import brute_force
import encryption
import letter_frequency
import text_analyzer

def main(filename):
    with open(filename) as text:
        intText = list(map(int, text.read().split(',')))
        chrText = list(map(chr, intText))
        frequencies = text_analyzer.text_analyzer(filename)

        print('\nCreating brute force encryption file...')
        brute_force.brute_force_encrypt(chrText, 97, 123)
        print('Please review the created file to obtain the password')

        password = input('\nWhat is the determined password: ')

        message = encryption.encrypt(chrText, password)

        return print('\nThe sum of the encrypted message is %d' % sum(message))

if __name__ == '__main__':
    main('p059_cipher.txt')