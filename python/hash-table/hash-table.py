def hashing_by_division(key, value):
    return key % value

# Create a empty hashtable
hash_table = {}

# Add elements to hashtable
hash_table[hashing_by_division(42, 13)] = 'Brazil'
hash_table[hashing_by_division(50, 13)] = 'Germany'
hash_table[hashing_by_division(23, 13)] = 'Italy'

print(hashing_by_division(42, 13)) # 3
print(hashing_by_division(50, 13)) # 10
print(hashing_by_division(23, 13)) # 11

# Get the hashtable values
value1 = hash_table[hashing_by_division(42, 13)]
value2 = hash_table[hashing_by_division(50, 13)]
value3 = hash_table[hashing_by_division(23, 13)]

print(value1)  # 'Brazil'
print(value2)  # 'Germany'
print(value3)  # 'Italy'