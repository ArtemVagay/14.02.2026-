rus_letters = "КАМОНВЕРХСТорухаес"
eng_letters = "KAMOHBEPXCTopyxaec"

def start():
    while True:
        choice = int(input("Enter 1 - encode, 2 - decode, 3 - quit"))

        if choice == 1:
            encode()
        elif choice == 2:
            decode()
        elif choice == 3:
            break

def encode():
    text = open('text.txt', 'r')
    to_encode = open('to_encode.txt')
    encoded = open('encoded.txt', 'w')

    letter = 0
    encoded_bits = 0

    letter = to_encode.read(1)
    if letter:
        letter = ord(letter)
    while True:
        _symbol = text.read(1)
        if not _symbol:
            break

        if _symbol in eng_letters:
            if encoded_bits == 8:
                letter = to_encode.read(1)
                if not letter:
                    encoded.write(_symbol)
                    break

                letter = ord(letter)
                encoded_bits = 0

            bit_from_letter = (letter & 0b10000000) >> 7

            print(f"Read {_symbol}, bit {bit_from_letter}")

            if bit_from_letter:
                _symbol = rus_letters[eng_letters.index(_symbol)]

            letter <<= 1
            letter %= 256
            encoded_bits += 1

        encoded.write(_symbol)
    encoded.write(text.read())
    text.close()
    to_encode.close()
    encoded.close()

def decode():
    encoded = open('encoded.txt', 'r')
    decoded = open('decoded.txt', 'w')

    with open('to_encode.txt', 'r') as text:
        to_read = len(text.read())

    read = 0
    bits_read = 0
    byte = 0

    while read < to_read:
        symbol = encoded.read(1)
        if not symbol:
            break

        if symbol in eng_letters:
            byte <<= 1
            bits_read += 1
            print(symbol, byte)
        elif symbol in rus_letters:
            byte <<= 1
            byte |= 1
            bits_read += 1
            print(symbol, byte)

        if bits_read == 8:
            print(byte)
            decoded.write(chr(byte))
            read += 1
            bits_read = byte = 0

    encoded.close()
    decoded.close()

start()