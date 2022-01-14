import convertor, checker

hashes = convertor.read_hash()
count = 1

f = open('results.txt', 'a')

for hash in hashes:
    a, h =  convertor.hash_to_addr(hash)
    
    result, addr, priv_key = checker.check_by_addr(a, h)
    if result == None:
        break
    else:
        f.writelines(f'{result}: {priv_key}: {addr}\n')
        print(f'{count} -> {result}: {addr}')
        print('===============================')
        count += 1
    
f.close

    

    
