Orig Address: 1NiNja1bUmhSoTXozBRBEtR8LeF9TGbZBN
Orig Address SHA256: cf38da039b1bdd3ccc0d22174d58cc7e7bb798c98c14366f75ae8bf4df3752f6 # the same as Private Key HEX

Private Key HEX: cf38da039b1bdd3ccc0d22174d58cc7e7bb798c98c14366f75ae8bf4df3752f6 # the same as Orig Address SHA256
Private Key WIF: 5KPYnrJgFEFYkzUnFiMzWEmhrLAoBaCMpHmbUMuo5PpWx6BfqYz
Private Key WIF compressed: L4AXKNd2DoVDBAhcjwZep3nKJjcEqfX8sj1q9mJ2NPijBkHBctK2

Public Key: 0454e6d2d2bed3fb3f3ea2cfa64c9b9febbb8bcb7b5cbbecc2d68e28c80e602c0514a53b80155f248d6580eeefb6ca2aff4828917b41097b9927ec40f31329084e 
Public Key compressed: 0254e6d2d2bed3fb3f3ea2cfa64c9b9febbb8bcb7b5cbbecc2d68e28c80e602c05

Public Address 1: 1Ns55SngRhshA8kEnyuQ9ELZZPN7ubYfQJ   
Public Address 1 compressed: 1GFw2UnczLkhDjRQD69r5GHuFRuwAs6GZE

Public Address 3: 3QFEiPKyCqQ5WtXxGtZwdW57RzcVhitGsC  
Public Address bc1 P2WPKH: bc1q5awvaawa4xqna4hg0eaxp56cn88uj8phhtmn89    
Public Address bc1 P2WSH: bc1qw3fa45prwq9mvxzzupydh5r03hskax5wskgxntxujk0x4efvn2ksm8xkng

Ideas:
1. Get ALL addresses
2. Add few extra check:
    - 5 iterations of priv_key generation
        a. generate sha256 using orig_addr > use as priv_key for pub_addr (pub_addrc, etc ...) - priv_key_1
        b. generate sha256 using priv_key_1 > use as priv_key for pub_addr (pub_addrc, etc ...) - priv_key_2
        c. generate sha256 using priv_key_2 > use as priv_key for pub_addr (pub_addrc, etc ...) - priv_key_3
        d. generate sha256 using priv_key_3 > use as priv_key for pub_addr (pub_addrc, etc ...) - priv_key_4
        e. generate sha256 using priv_key_4 > use as priv_key for pub_addr (pub_addrc, etc ...) - priv_key_5
        f. generate sha256 using priv_key_5 > use as priv_key for pub_addr (pub_addrc, etc ...)

bs4
requests
base58
ecdsa
bitcoinaddress