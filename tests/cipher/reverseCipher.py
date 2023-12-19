import sys

def reverseCipher(message: str):
    translated = ''
    i = len(message) - 1
    while i >= 0:
        translated = translated + message[i]
        i = i - 1

    return translated

    
message = open(sys.argv[1]).read().strip()
L = message.split('\n')
for line in L:
    print(reverseCipher(line))



