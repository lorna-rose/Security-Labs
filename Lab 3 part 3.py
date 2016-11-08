from Crypto.Cipher import DES

def addPadding(data):
    length =  8 - (len(data) % 8)
    data += "\x00"*(length)
    return data

def chunks(longdata, n):
    for i in range(8, len(longdata),n):
        yield longdata[i:i +n]

myKey ='12345678'
des = DES.new(myKey, DES.MODE_ECB)
originaltext = 'AAAABBBBAAAABBBB'
plain_text_padding = addPadding(originaltext)
datasource = dict(enumerate(list(chunks(plain_text_padding, 32)), start = 0))
c1 = des.encrypt(originaltext)
c3 = des.encrypt(plain_text_padding)
print('The orginal text is: ' + originaltext)
print('The orginal text with padding: ' + plain_text_padding)
print('Encrypted text is: '+c1.encode('hex'))
print('Encrypted text is: '+c3.encode('hex'))
print str(datasource)
c2 = des.decrypt(c1)
print('Decrypted: ' + c2)




