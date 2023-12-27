import sys
import os

current_directory = os.getcwd()
steps_path = os.path.join(current_directory, 'steps')
#print(steps_path)
sys.path.append(steps_path)

import commonSteps


# Caesar Cipher Hacker
#message = 'guv6Jv6Jz!J6rp5r7Jzr66ntrM'
inputFilename = sys.argv[1]
outputFilename = sys.argv[2]
# Read in the message from the input file
fileObj = open(inputFilename)
content = fileObj.read()
fileObj.close()
#message = 'qeFIP?eGSeECNNS'

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'
# Loop through every possible key:

for key in range(len(SYMBOLS)):
    # It is important to set translated to the blank string so that the
    # previous iteration's value for translated is cleared:
    translated = ''

    # Loop through each symbol in message:
    for symbol in content:
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)
            translatedIndex = symbolIndex - key

            # Handle the wraparound:
            if translatedIndex < 0:
                translatedIndex = translatedIndex + len(SYMBOLS)

            # Append the decrypted symbol:
            translated = translated + SYMBOLS[translatedIndex]

        else:
            # Append the symbol without encrypting/decrypting:
            translated = translated + symbol

        
    # Display every possible decryption:
    print('Key #%s: %s' % (key, translated))
    if commonSteps.is_english(translated):
        # Write out the translated message to the output file:
        outputFileObj = open(outputFilename, 'w')
        outputFileObj.write(translated)
        outputFileObj.close()
        break

# poetry run python tests/caesarBruteForce/bruteForceCaesarFile.py tests/caesarBruteForce/input/encoded.txt tests/caesarBruteForce/input/file1.txt


            