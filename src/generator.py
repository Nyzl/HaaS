import random
from src.hex import hex_codes


def generate_hex(n):
    hexs = []
    hexagrams = []
    
    for col in range(n):
        gram = []
        for row in range(6):
            bar = random.randint(0, 1)
            gram.append(bar)
        hexs.append(gram)

    for h in hexs:
        bin = ''.join(str(x) for x in h)
        hexagrams.append(hex_codes[bin])

    return (hexagrams)


def generate_reading(x):
    return "not implemented yet"
