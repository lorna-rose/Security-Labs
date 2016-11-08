from Crypto.Cipher import DES

myKey = '12345678'
originaltext = 'AAAABBBBAAAABBBB'
IV = '00000000'
encryptDes = DES.new(myKey, DES.MODE_CBC, IV)
decryptDes = DES.new(myKey, DES.MODE_CBC, IV)
c1 = encryptDes.encrypt(originaltext)
print('The plaintext is '+ originaltext)
print('The ciphertext is ' + c1.encode('hex'))
c2 = decryptDes.decrypt(c1)
print('Decrypted again!: ' + c2)
