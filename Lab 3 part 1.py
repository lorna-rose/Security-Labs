from Crypto.Cipher import DES

myKey ='12345678'
des = DES.new(myKey, DES.MODE_ECB)
originaltext = 'AAAABBBBAAAABBBB'
c1 = des.encrypt(originaltext)
print('The orginal text is: ' + originaltext)
print('Encrypted text is: '+c1.encode('hex'))
c2 = des.decrypt(c1)
print('Decrypted: ' + c2)
