import random
from src.hex import hex_codes

def generate_hex(n):
    symbol = ["■■■■■■■■■■  ", "■■■■  ■■■■  "]
    gram = {0:[],1:[],2:[],3:[],4:[],5:[]}
    hexs = []
    for row in range(6):
        line = ""
        for col in range(n):
            bar = random.randint(0, 1)
            line += symbol[bar]
            gram[col] += [bar]

    for g in gram:
        bin = ''.join(str(x) for x in gram[g])
        hexs.append(hex_codes[bin])
    
    return (hexs)

def generate_reading(x):
    return "not implemented yet"