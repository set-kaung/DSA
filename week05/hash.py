# Name: Set Kaung Lwin
# ID: 6632017
# Sec: 543
from sys import stdin
from math import ceil

# Read the sequence of operations to be operated on the hash table
operations = []
for line in stdin:
    line = line.split()
    if len(line) > 2:
        line[2] = int(line[2])
    operations.append(line)

# count keys
keyc = 0
for op in operations:
    if op[0] == "insert":
        keyc += 1


table_size = int(ceil((keyc)*1.3))    # set table size here
hash_table = [[] for i in range(table_size)]

def show_hash_table():
    print('-------------------')
    for item_list in hash_table:
        print(item_list)
    print('-------------------')

def hash_func(s):
    total = 0
    for i in range(len(s)): 
        total += ((37**i)*ord(s[i]))
    
    return total % table_size

    # return the hash value

def insert(s, v):
    key = hash_func(s)
    exist = False
    for i in hash_table[key]:
        if i[0] == s:
            exist = True
    if not exist:
        hash_table[key].insert(0,(s,v))
        return 0
    return -1
    # return 0 on successful insertion
    # return -1 if s has already been in the hash table

def search(s):
    key = hash_func(s)

    for i in hash_table[key]:
        if i[0] == s:
            return i[1]
    return -1 
    # return value of the key or
    # return -1 if s does not exist in hash table

def delete(s):
    key = hash_func(s)
    idx = -1
    for i in range(len(hash_table[key])):
        if hash_table[key][i][0] == s:
            idx = i
            break
    if idx != -1:
        hash_table[key] = hash_table[key][:idx] + hash_table[key][idx+1:]
        return 0
    return -1
    # return 0 on successful deletion
    # return -1 if s does not exist in hash table


# The main program to execute the sequence of operations
for op in operations:
    if op[0] == "insert":
        insert(op[1], int(op[2]))
        show_hash_table()
    elif op[0] == "search":
        v = search(op[1])
        print(v)
    elif op[0] == "delete":
        delete(op[1])
        show_hash_table()


    

