import nltk


def is_english(text):
    english_vocab = set(w.lower() for w in nltk.corpus.words.words())
    words = nltk.wordpunct_tokenize(text)
    word_count = sum(1 for word in words if word.lower() in english_vocab)
    return word_count / len(words) > 0.5  # Threshold for English detection


# Caesar Cipher Hacker
#message = 'guv6Jv6Jz!J6rp5r7Jzr66ntrM'
message = 'qeFIP?eGSeECNNS'

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'
# Loop through every possible key:

for key in range(len(SYMBOLS)):
    # It is important to set translated to the blank string so that the
    # previous iteration's value for translated is cleared:
    translated = ''

    # Loop through each symbol in message:
    for symbol in message:
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
    if is_english(translated):
        break



            