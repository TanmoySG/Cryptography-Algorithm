# RSA Cryptography Algorithm

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

![RSA-block-diagram-image.png](https://github.com/TanmoySG/Cryptography-Algorithm/blob/master/RSA-Algorithm/RSA-block-diagram-image.png)
