

# '''
# Basic hash table key/value pair
# '''
class Pair:
    def __init__(self, key, value):
        self.key = key
        self.value = value


# '''
# Basic hash table
# Fill this in.  All storage values should be initialized to None
# '''
class BasicHashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * capacity


# '''
# Fill this in.
# Research and implement the djb2 hash function
# '''
def hash(string, max):
    hash = 5381
    for x in string:
        # hash << 5 is the same thing as multiplying hash by 2**5
        # returns hash with the bits shifted to the left by 5 places
        hash = ((hash << 5) + hash) + ord(x)
    return hash % max


# '''
# Fill this in.

# If you are overwriting a value with a different key, print a warning.
# '''
def hash_table_insert(hash_table, key, value):
    # set the hash index
    # key is "string", hash table capacity is "max"
    # int index = hash_function(key) % array.length
    index = hash(key, hash_table.capacity)
    # create the key value pair
    new_pair = Pair(key, value)

    # create warning if the index exists
    if hash_table.storage[index] is not None:
        if hash_table.storage[index].key != key:
            print(
                "Warning! Overwriting key: {hash_table.storage[index].key}.")
            hash_table.storage[index].key = key
        hash_table.storage[index].value = value
    else:
        # add to hash table
        # array[index] = value
        hash_table.storage[index] = new_pair


# '''
# Fill this in.

# If you try to remove a value that isn't there, print a warning.
# '''
def hash_table_remove(hash_table, key):
     # hash the key, max is hash table capacity
    index = hash(key, hash_table.capacity)
    # if index exists
    if hash_table.storage[index]:
        # remove the index by setting to none
        hash_table.storage[index] = None
    else:
        # if key value doesnt exist
        print("warning, no value for this key")


# '''
# Fill this in.

# Should return None if the key is not found.
# '''
def hash_table_retrieve(hash_table, key):
    # set the hash index
    index = hash(key, hash_table.capacity)
    # if not found
    if not hash_table.storage[index]:
        return None
    # retrieve the key
    return hash_table.storage[index].value


def Testing():
    ht = BasicHashTable(16)

    hash_table_insert(ht, "line", "Here today...\n")

    hash_table_remove(ht, "line")

    if hash_table_retrieve(ht, "line") is None:
        print("...gone tomorrow (success!)")
    else:
        print("ERROR:  STILL HERE")


Testing()

ht = BasicHashTable(16)
print(ht.storage)
print(ht.capacity)
