def read_hash():
    f = open('hash.txt', 'r')
    lines = f.readlines()
    
    for line in lines:
        trimmed_line = str(line).rstrip()
        print(trimmed_line)
    
def hash_to_addr(hash):
    pass