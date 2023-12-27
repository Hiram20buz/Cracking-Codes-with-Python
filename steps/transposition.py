import math


# Transposition Cipher Encryption
def encryptMessage(key: int, message: str) -> str:
    # Each string in ciphertext represents a column in the grid:
    ciphertext = [''] * key

    # Loop through each column in ciphertext:
    for column in range(key):
        currentIndex = column

        # Keep looping until currentIndex goes past the message length:
        while currentIndex < len(message):
            # Place the character at currentIndex in message at the
            # end of the current column in the ciphertext list:
            ciphertext[column] += message[currentIndex]

            # Move currentIndex over:
            currentIndex += key

    # Convert the ciphertext list into a single string value and return it:
    return ''.join(ciphertext)


# Transposition Cipher Decryption
def decryptMessage(key: int, message: str) -> str:
    # The transposition decrypt function will simulate the "columns" and
    # "rows" of the grid that the plaintext is written on by using a list
    # of strings. First, we need to calculate a few values.

    # The number of "columns" in our transposition grid:
    numOfColumns = int(math.ceil(len(message) / float(key)))
    # The number of "rows" in our grid:
    numOfRows = key
    # The number of "shaded boxes" in the last "column" of the grid:
    numOfShadedBoxes = (numOfColumns * numOfRows) - len(message)

    # Each string in plaintext represents a column in the grid:
    plaintext = [''] * numOfColumns

    # The column and row variables point to where in the grid the next
    # character in the encrypted message will go:
    column = 0
    row = 0

    for symbol in message:
        plaintext[column] += symbol
        column += 1 # Point to the next column.

        # If there are no more columns OR we're at a shaded box, go back
        # to the first column and the next row:
        if (column == numOfColumns) or (column == numOfColumns - 1 and row >= numOfRows - numOfShadedBoxes):
            column = 0
            row += 1

    return ''.join(plaintext)
    
