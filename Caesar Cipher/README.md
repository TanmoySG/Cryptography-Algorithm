# Caesar Cipher

## About RSA Algorithm
Caesar cipher, also known as Caesar's cipher, the shift cipher, Caesar's code or Caesar shift, is one of the simplest and most widely known encryption techniques. It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet. For example, with a left shift of 3, D would be replaced by A, E would become B, and so on.

## Algorithm

1. Input Plain Text, P from user.
2. Input Key, K from user.
3. During Encryption, each alphabet in the plaintext is Shifted to the right by K characters, in a cyclic order.
4. During Decryption, each alphabet in the plaintext is Shifted to the left by K characters, in a cyclic order.

**Example:**

Key = 2 and Plaintext = A 

  Encryption : **A -> B -> C** , therefore, Ciphertext = C
  
  Decryption : **A <- B <- C** , therefore, Plaintext = A

## Encryption

The Alphabets A ... Z are represented as 0 ... 25 with A = 0 , B = 1 , ... , Z = 25

1. Each alphabet in P, is represented in its numeric form as mentioned above. 
2. Modulus 26 is applied on the key, so that the key is within 0 to 26. 
3. The output value is added to the numeric representation, 
4. The resulting value if converted to its corresponding alphabet. 

Mathematically,
 
**C<sub>n</sub> = P<sub>n</sub> + ( k mod 26 )**     OR     **C<sub>n</sub> = ( P<sub>n</sub> + k ) mod 26**

where,

**P<sub>n</sub>** is the *numeric representation* of the n<sup>th</sup> Charcter of the plaintext, P

**C<sub>n</sub>** is the *numeric representation* of the n<sup>th</sup> Charcter of the Ciphertext, C

**k** is the *key*

![CaesarsEnc.jpg](https://github.com/TanmoySG/Cryptography-Algorithm/blob/master/Caesar%20Cipher/CaesarsEnc.jpg)

## Decryption

The Alphabets A ... Z are represented as 0 ... 25 with A = 0 , B = 1 , ... , Z = 25

1. Each alphabet in C, is represented in its numeric form as mentioned above. 
2. Modulus 26 is applied on the key, so that the key is within 0 to 26. 
3. The output value is subtracted from the the numeric representation, 
4. The resulting value if converted to its corresponding alphabet. 

Mathematically,
 
**P<sub>n</sub> = C<sub>n</sub> - ( k mod 26 )**     OR     **P<sub>n</sub> = ( C<sub>n</sub> - k ) mod 26**

where,

**P<sub>n</sub>** is the *numeric representation* of the n<sup>th</sup> Charcter of the plaintext, P

**C<sub>n</sub>** is the *numeric representation* of the n<sup>th</sup> Charcter of the Ciphertext, C

**k** is the *key*

![CaesarDec.jpg](https://github.com/TanmoySG/Cryptography-Algorithm/blob/master/Caesar%20Cipher/CaesarDec.jpg)

## Implementation of Caesar Cipher using Python


```python
def encrypt(plaintext, key):
    ciphertext = []
    for i in plaintext:
        if i.isupper() :
            ciphertext.append(chr((ord(i)+key-65)%26+65))
        elif i.islower():
            ciphertext.append(chr((ord(i)+key-97)%26+97))
        else:
            ciphertext.append(i)
    return "".join(ciphertext)

def decrypt(ciphertext, key):
    plaintext = []
    for i in ciphertext:
        if i.isupper() :
            plaintext.append(chr((ord(i)-key-65)%26+65))
        elif i.islower():
            plaintext.append(chr((ord(i)-key-97)%26+97))
        else:
            plaintext.append(i)
    return "".join(plaintext)

print("Welcome! This is Caesar Cipher's implementation in Python.")
print("----------------------------------------------------------")
print() 
print("Caesar Cipher Encryption")
plaintext = input("  Enter Plaintext: ")
print("  Ciphertext: ",  encrypt(plaintext, int(input("  Enter the Key: "))))
print()
print("Caesar Cipher Decryption")
ciphertext = input("  Enter Ciphertext: ")
print("  Plaintext: ", decrypt(ciphertext, int(input("  Enter the Key: "))))
```

    Welcome! This is Caesar Cipher's implementation in Python.
    ----------------------------------------------------------
    
    Caesar Cipher Encryption
      Enter Plaintext: Caesar Cipher is not Secure
      Enter the Key: 56
      Ciphertext:  Geiwev Gmtliv mw rsx Wigyvi
    
    Caesar Cipher Decryption
      Enter Ciphertext: Geiwev Gmtliv mw rsx Wigyvi
      Enter the Key: 56
      Plaintext:  Caesar Cipher is not Secure
    

### Disadvantages
1. If key is 0 , 26 or any multiple of 26 there will me no shift hence no encryption. For Example, if key is 135798, the shift is zero as 135798 mod 26 = 0 , hence the Message is not encrypted.
2. There will be more than one key that will correspond to the shift value, i.e if a message is to be shifted by 3, keys 3, 29, 56, etc will yield the same shift value 3 and hence the same ciphertext, this makes the encryption process vulnerable.
3. Using brute force attack, trying just 26 keys from 0 to 25 can give us the plaintext.
4. If one can identify patterns in the ciphertext, he/she can easily determine the shift value, hence the key.

#### Tanmoy Sen Gupta
[tanmoysg.com](http://tanmoysg.com) | +91 9864809029 | tanmoysps@gmail.com
