# simple hashing
def simple_hash(key):
    total = 0
    for ch in key:
        total += ord(ch)
    return total

# Multiplicative hashing
def multiplicative_hash(key):
    h = 1
    for ch in key:
        h = (h * 31) + ord(ch)
    return h

# DJB2
def djb2(key):
    h = 5381
    for ch in key:
        h = (h<<5) + ord(ch)

    return h

# built-in hash function
def built_in(key):
    return hash(key)

key = "987"
print(f"simple hash : {simple_hash(key)}")
print(f"multiplicative hash : {multiplicative_hash(key)}")
print(f"djb2 : {djb2(key)}")
print(f"built-in function : {built_in(key)}")
