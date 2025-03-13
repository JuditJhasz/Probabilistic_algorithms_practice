import mmh3


def hash1(key):
    return 42


def hash2(key):
    return len(key)


def hash3(key):
    return sum(ord(char) for char in key)


def hash4(key, base=31, mod=1e9 + 9):
    hash_value = 0
    power = 1
    for char in key:
        hash_value = (hash_value + (ord(char) * power) % mod) % mod
        power = (power * base) % mod
    return int(hash_value)


def hash5(key, seed=42):
    return mmh3.hash(key, seed)



