

# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# '''
# Fill this in
# '''
class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * capacit


# '''
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


# Hint: Used the LL to handle collisions
# '''
def hash_table_insert(hash_table, key, value):
    # set the hash index
    index = hash(key, hash_table.capacity)
    # set the key value pair
    new_pair = LinkedPair(key, value)
    # get the current pair
    current_pair = hash_table.storage[index]
    # if the key/value exists and the key is different
    if current_pair is not None:
        if new_pair.key != current_pair.key:
            current_pair.next = new_pair
    else:
        current_pair = new_pair

# '''
# Fill this in.

# If you try to remove a value that isn't there, print a warning.
# '''


def hash_table_remove(hash_table, key):
     # set the hash index
    index = hash(key, hash_table.capacity)
    # get the current pair
    current_pair = hash_table.storage[index]
    # if no index exists
    if current_pair is None:
        # warning value doesnt exist
        print("warning, no value for this key")
    elif current_pair.key == key:
        # if  index exists
        current_pair = None


# '''
# Fill this in.

# Should return None if the key is not found.
# '''
def hash_table_retrieve(hash_table, key):
     # set the hash index
    index = hash(key, hash_table.capacity)
    # get the current pair
    current_pair = hash_table.storage[index]
    # if not found
    if current_pair is not None:
        # retrieve the key
        if current_pair.key == key:
            return current_pair.value


# '''
# Fill this in
# '''
def hash_table_resize(hash_table):
     # doubles the size of your hash table
    capacity = len(hash_table.storage) * 2
    new_table = HashTable(capacity)
    # copies all elements into the new data structure.
    for i in range(0, len(hash_table.storage) - 1):
        new_table.storage[i] = hash_table.storage[i]
    return new_table


ht = HashTable(2)


print("initial table", ht.capacity)

ht2 = hash_table_resize(ht)

print("resize table", ht2.capacity)


# def Testing():
#     ht = HashTable(2)

#     hash_table_insert(ht, "line_1", "Tiny hash table")
#     hash_table_insert(ht, "line_2", "Filled beyond capacity")
#     hash_table_insert(ht, "line_3", "Linked list saves the day!")

#     print(hash_table_retrieve(ht, "line_1"))
#     print(hash_table_retrieve(ht, "line_2"))
#     print(hash_table_retrieve(ht, "line_3"))

#     old_capacity = len(ht.storage)
#     ht = hash_table_resize(ht)
#     new_capacity = len(ht.storage)

#     print("Resized hash table from " + str(old_capacity)
#           + " to " + str(new_capacity) + ".")


# Testing()
