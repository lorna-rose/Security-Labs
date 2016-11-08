from Crypto.Cipher import ARC4
from Crypto import Random

originaltext = 'Real Madrid will loose tonight vs Legia 2-1'
key = Random.new().read(16)
enc = ARC4.new(key)
dec = ARC4.new(key)
c1 = enc.encrypt(originaltext)
c2 = dec.decrypt(c1)
print('Plaintext ' + originaltext)
print('Encrypted: ' + c1)
print('Decrypted: ' + c2)
print('key: ' + key)



