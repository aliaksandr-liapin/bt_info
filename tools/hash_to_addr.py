import hashlib
import base58
import codecs
import ecdsa

def read_hash():
    f = open('hashes.txt', 'r')
    lines = f.readlines()
    hashes = []
    
    for line in lines:
        trimmed_line = str(line).rstrip()
        hashes.append(trimmed_line)
        
    return hashes

    
def hash_to_addr(hash):
    
    # Hex decoding the private key to bytes using codecs library
    private_key_bytes = codecs.decode(hash, 'hex')
    
    # Generating a public key in bytes using SECP256k1 & ecdsa library
    public_key_raw = ecdsa.SigningKey.from_string(private_key_bytes, curve=ecdsa.SECP256k1).verifying_key
    public_key_bytes = public_key_raw.to_string()
    
    # Hex encoding the public key from bytes
    public_key_hex = codecs.encode(public_key_bytes, 'hex')
    
    # Bitcoin public key begins with bytes 0x04 so we have to add the bytes at the start
    public_key = (b'04' + public_key_hex).decode("utf-8")
    
    # Checking if the last byte is odd or even
    if (ord(bytearray.fromhex(public_key[-2:])) % 2 == 0):
        public_key_compressed = '02'
    else:
        public_key_compressed = '03'
        
    # Add bytes 0x02 to the X of the key if even or 0x03 if odd
    public_key_compressed += public_key[2:66]
    
    # Converting to bytearray for SHA-256 hashing
    hex_str = bytearray.fromhex(public_key_compressed)
    sha = hashlib.sha256()
    sha.update(hex_str)
    sha.hexdigest() # .hexdigest() is hex ASCII
    
    rip = hashlib.new('ripemd160')
    rip.update(sha.digest())
    key_hash = rip.hexdigest()
    
    modified_key_hash = "00" + key_hash
    
    sha = hashlib.sha256()
    hex_str = bytearray.fromhex(modified_key_hash)
    sha.update(hex_str)
    
    sha_2 = hashlib.sha256()
    sha_2.update(sha.digest())
    sha_2.hexdigest()
    
    checksum = sha_2.hexdigest()[:8]
    
    byte_25_address = modified_key_hash + checksum
    address = base58.b58encode(bytes(bytearray.fromhex(byte_25_address))).decode('utf-8')
    
    return address, hash