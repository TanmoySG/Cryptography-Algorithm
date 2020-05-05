# RSA Cryptography Algorithm

## About RSA Algorithm
RSA (Rivest–Shamir–Adleman) is one of the first public-key cryptosystems and is widely used for secure data transmission. In such a cryptosystem, the encryption key is public and distinct from the decryption key which is kept secret (private).

## Algorithm

1. Select 2 Prime Numbers - **p & q**
2. Calculate **n = p x q**
3. Calculate Euler's Totient Function of n,  **φ(n) = (p-1) x (q-1)**
4. Select PUBLIC KEY, **e** such that **e & φ(n) are Co-primes**  i.e, **gcd(e , φ(n))=1**
5. Calculate PRIVATE KEY, **d** such that **(d x e) mod φ(n) = 1**

## Public and Private Keys

1. The Public  key is { e , n }, which is known to all in the network.
2. The Private key is { d , n }, which is known ONLY to the User to whom message is to be sent.

## Encryption & Decryption

#### Encryption Algorithm

The Cipher Text, C is generated from the plaintext, M using the public key, e as:

**C = M<sup>e</sup> mod n**

#### Decryption Algorithm

The Plain Text, M is generated from the ciphertext, C using the private key, d as:

**M = C<sup>d</sup> mod n**

![RSA-block-diagram%20%281%29.png](attachment:RSA-block-diagram%20%281%29.png)

## Implementation of RSA using Python


```python
from sympy import *
import math 

#Generate p and q
p = randprime(1, 10)
q = randprime(11, 20)

#Generate n and l(n)
n = p*q
l = (p-1)*(q-1)

#Function to test Co-Primality for generation of list of Public Keys
def isCoPrime(x):
    if math.gcd(l,x)==1:
        return True
    else:
        return False

#Function to find mod Inverese of e withl(n) to generate d     
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
print(listOfCP)

print(" ")

#select a Public Key from list of Co-Primes
e = int(input("Select Public Key from the Above List ONLY: "))

#Value of d
d = modInverse(e, l)

print(" ")

#Print Public and Private Keys
print("PUBLIC KEY  : { e , n } = {", e ,",", n , "}")
print("PRIVATE KEY : { d , n } = {", d ,",", n , "}")

print(" ")

#Encryption Algorithm
def encrypt(plainText):
    return (plainText**e)%n

#Decryption Algorithm
def decrypt(cipherText):
    pvtKey = int(input("Enter your Private Key: "))
    return (cipherText**pvtKey)%n

#Driver Code

#Message Input
pt = int(input('Enter the Plain Text: '))
print("CipherText: ", encrypt(pt))

print(" ")

#CipherText Input
ct = int(input('Enter the Cipher Text: '))
print("PlainText: ", decrypt(ct))
```

    Value of P =  7
    Value of Q =  19
    Value of N =  133
    Value of L =  108
     
    List of Available Public Keys
    [1, 5, 7, 11, 13, 17, 19, 23, 25, 29, 31, 35, 37, 41, 43, 47, 49, 53, 55, 59, 61, 65, 67, 71, 73, 77, 79, 83, 85, 89, 91, 95, 97, 101, 103, 107]
     
    Select Public Key from the Above List ONLY: 47
     
    PUBLIC KEY  : { e , n } = { 47 , 133 }
    PRIVATE KEY : { d , n } = { 23 , 133 }
     
    Enter the Plain Text: 51
    CipherText:  116
     
    Enter the Cipher Text: 116
    Enter your Private Key: 23
    PlainText:  51
    

## Encryption & Decryption Mechanism

The Encryption and Decryption mechanishm block diagram is shown below

![RSA-Encryption-Decryption-block-diagram.png](https://github.com/TanmoySG/Cryptography-Algorithm/blob/master/RSA-Algorithm/diagrams/RSA-Encryption-Decryption-block-diagram.png)

## Explanation

The explanation for the above example is shown below

![RSA-Example-maths-only-diagram.png](https://github.com/TanmoySG/Cryptography-Algorithm/blob/master/RSA-Algorithm/diagrams/RSA-Example-maths-only-diagram.png)

#### Tanmoy Sen Gupta
[tanmoysg.com](http://tanmoysg.com) | +91 9864809029 | tanmoysps@gmail.com
