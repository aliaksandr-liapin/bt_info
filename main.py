import tools.hash_to_addr as hash_to_addr, tools.caddr_hecker as caddr_hecker

hashes = hash_to_addr.read_hash()
count = 1

f = open('results.txt', 'a')

for hash in hashes:
    a, h =  hash_to_addr.hash_to_addr(hash)
    
    result, addr, priv_key = caddr_hecker.check_by_addr(a, h)
    if result == None:
        break
    else:
        f.writelines(f'{result}: {priv_key}: {addr}\n')
        print(f'{count} -> {result}: {addr}')
        print('===============================')
        count += 1
    
f.close

    

    
