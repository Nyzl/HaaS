"""Generate Hexagrams."""
import itertools
import json
import random

ALL_HEXAGRAMS = ["".join(hexagram) for hexagram in itertools.product("01", repeat=6)]
HEX_CODES = json.load(open("haas/hex.json"))


def generate_hex(n):
    """Get n random hexagrams for a reading."""
    return [HEX_CODES[hexagram] for hexagram in random.choices(ALL_HEXAGRAMS, k=n)]


def generate_reading(x):
    """Generate a reading."""
    return "not implemented yet"
