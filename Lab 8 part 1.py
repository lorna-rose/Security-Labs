prime = 23
base = 5
a = 6
b = 15

print('Prime: ' + str(prime))
print('Base:  '+ str(base))
# Alice chooses a secret int a, then sends Bob A = g^a mod p
A = (base**a) % prime
print('\nAlice Sends Over Public Chanel: '+ str(A))
# Bob chooses a secret int b, then sends Alice B = g^b mod p
B = (base ** b) % prime
print('Bob Sends Over Public Chanel: '+ str(B))
# Alice Computes  s = B^a mod p
aliceSharedSecret = (B ** a) % prime
print('\nAlice Shared Secret: ' + str(aliceSharedSecret))
# Bob Computes s = A^b mod p
bobSharedSecret = (A**b) % prime
print('Bob Shared Secret: '+ str(bobSharedSecret))
