# Modified RSA Cryptography


```python
from sympy import *
import math 
import random

#Generate p and q
p = randprime(100, 250)
q = randprime(100, 250)

#Generate n and l(n)
n = p*q
l = (p-1)*(q-1)

#Function to test Co-Primality for generation of list of Public Keys
def isCoPrime(x):
    if math.gcd(l,x)==1:
        return True
    else:
        return False

#Function to find mod Inverese of e with l(n) to generate d 
def modInverse(e, l) :
    e = e % l;
    for x in range(1, l) :
        if ((e * x) % l == 1) :
            return x
    return 1


#List for Co-Primes
listOfCP = []
for i in range(1, l):
    if isCoPrime(i) == True:
        listOfCP.append(i)

#Print values of P, Q, N, L        
print("Value of P = ", p)
print("Value of Q = ", q)
print("Value of N = ", n)
print("Value of L = ", l)

print(" ")

#Print List of Co-Primes for e
print("List of Available Public Keys")
#print(listOfCP)
print(random.sample(listOfCP, 50))

print(" ")

#select a Public Key from list of Co-Primes
e = int(input("Select Public Key from the Above List ONLY: "))
offset = int(input("Set the offset-key: "))

#Value of d
d = modInverse(e, l)

print(" ")

#Print Public and Private Keys
print("PUBLIC  KEY SET : { e , n } = {", e ,",", n , "}")
print("PRIVATE KEY SET : { key , n , offset } = {", d ,",", n ,",", offset, "}")

print(" ")

#Encryption Algorithm
def encrypt(plainText):
    plaintext = plainText.split()
    encodedStream = []
    cipherStream = []
    for i in plainText:
        encodedStream.append(ord(i))
    for i in encodedStream:
        cipherStream.append(((i^offset)**e)%n)
    return cipherStream

#Decryption Algorithm
def decrypt(cipherStream):
    pvtKey = int(input("Enter your Private Key: "))
    encodedStream = []
    plainStream = []
    for i in cipherStream:
        encodedStream.append(((int(i))**pvtKey)%n)
    for i in encodedStream:
        plainStream.append(chr(i^offset))
    return "".join(plainStream)
    
#Driver Code

#Message Input
pt = input('Enter the Plain Text: ')
print("CipherText: ", encrypt(pt))

print(" ")

#CipherText Input
ct = input('Enter the Cipher Text: ').split(", ")
print("PlainText: ", decrypt(ct))
```

    Value of P =  127
    Value of Q =  179
    Value of N =  22733
    Value of L =  22428
     
    List of Available Public Keys
    [5287, 20659, 1499, 14783, 6259, 8213, 13133, 4105, 16003, 5357, 7225, 15469, 16735, 7853, 3127, 355, 14269, 1531, 2125, 13549, 13099, 1315, 1865, 4805, 18931, 13121, 17191, 14747, 2293, 13457, 6095, 6715, 19643, 16853, 12685, 1373, 6409, 14975, 20719, 2789, 21709, 6071, 15913, 263, 20549, 20387, 1091, 19489, 4597, 11587]
     
    Select Public Key from the Above List ONLY: 19489
    Set the offset-key: 1999
     
    PUBLIC  KEY SET : { e , n } = { 19489 , 22733 }
    PRIVATE KEY SET : { key , n , offset } = { 9745 , 22733 , 1999 }
     
    Enter the Plain Text: tanmoy@123
    CipherText:  [16681, 696, 2055, 3973, 11731, 11320, 20382, 4711, 20186, 3149]
     
    Enter the Cipher Text: 16681, 696, 2055, 3973, 11731, 11320, 20382, 4711, 20186, 3149
    Enter your Private Key: 9745
    PlainText:  tanmoy@123
    

### Modification

I modified the RSA, by performing an XOR operation on the Plaintext while encryption. The Plaintext is XORed with an offset value to give us an extra layer of protection.

The user chooses an offset value, O which is XORed with the Plaintext and Ciphertext.

#### Encryption:

For each element of the plaintext T as, T<sub>i</sub> and offset value, O provided by the user, The Ciphertext element, C<sub>i</sub> corresponding to T<sub>i</sub> is, 

**C<sub>i</sub>   =   T<sub>i</sub>   XOR   O**

#### Decryption:

For each element of the ciphertext C as, C<sub>i</sub> and offset value, O provided by the user, The Plaintext element, T<sub>i</sub> corresponding to C<sub>i</sub> is, 

**T<sub>i</sub>   =   C<sub>i</sub>   XOR   O**

Tanmoy Sen Gupta | +91 9864809029 | [tanmoysg.com](tanmoysg.com)
