# Transposition Cipher Hacker
import sys
import os

current_directory = os.getcwd()
steps_path = os.path.join(current_directory, 'steps')
#print(steps_path)
sys.path.append(steps_path)

import detectEnglish, transposition


def main():
    inputFilename = sys.argv[1]
    # BE CAREFUL! If a file with the outputFilename name already exists,
    # this program will overwrite that file:
    outputFilename = sys.argv[2]
    myKey = 8
    myMode = 'encrypt' # Set to 'encrypt' or 'decrypt'.

    # If the input file does not exist, the program terminates early:
    if not os.path.exists(inputFilename):
        print('The file %s does not exist. Quitting...' % (inputFilename))
        sys.exit()

    # If the output file already exists, give the user a chance to quit:
    if os.path.exists(outputFilename):
        print('This will overwrite the file %s. (C)ontinue or (Q)uit?' % (outputFilename))
        response = input('> ')
        if not response.lower().startswith('c'):
            sys.exit()

    # Read in the message from the input file
    fileObj = open(inputFilename)
    content = fileObj.read()
    fileObj.close()
    myMessage = content

    hackedMessage = hackTransposition(myMessage)

    if hackedMessage == None:
        print('Failed to hack encryption.')
    else:
        print('Copying hacked message to clipboard:')
        print(hackedMessage)
        # Write out the translated message to the output file:
        outputFileObj = open(outputFilename, 'w')
        outputFileObj.write(hackedMessage)
        outputFileObj.close()
        #pyperclip.copy(hackedMessage)


def hackTransposition(message):
    print('Hacking...')

    # Python programs can be stopped at any time by pressing Ctrl-C (on
    # Windows) or Ctrl-D (on Mac and Linux)
    print('(Press Ctrl-C or Ctrl-D to quit at any time.)')

    # Brute-force by looping through every possible key.
    for key in range(1, len(message)):
        print('Trying key #%s...' % (key))

        decryptedText = transposition.decryptMessage(key, message)

        if detectEnglish.isEnglish(decryptedText):
            # Ask user if this is the correct decryption.
            print()
            print('Possible encryption hack:')
            print('Key %s: %s' % (key, decryptedText[:100]))
            print()
            print('Enter D if done, anything else to continue hacking:')
            response = input('> ')

            if response.strip().upper().startswith('D'):
                return decryptedText

    return None

if __name__ == '__main__':
    main()

# poetry run python tests/transpositionBruteForce/transpositionFileHacking.py tests/transpositionBruteForce/file.txt tests/transpositionBruteForce/file1.txt