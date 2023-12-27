import sys
import os

current_directory = os.getcwd()
steps_path = os.path.join(current_directory, 'steps')
#print(steps_path)
sys.path.append(steps_path)

import transposition


def main():
    myMessage = 'Cenoonommstmme oo snnio. s s c'
    myKey = 8

    plaintext = transposition.decryptMessage(myKey, myMessage)

    # Print with a | (called "pipe" character) after it in case
    # there are spaces at the end of the decrypted message:
    print(plaintext + '|')


# If transpositionDecrypt.py is run (instead of imported as a module),
# call the main() function:
if __name__ == '__main__':
    main()