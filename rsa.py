#! /usr/bin/env python

import random


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def multiplicative_inverse(e, phi):
    d = 0
    x1 = 0
    x2 = 1
    y1 = 1
    temp_phi = phi

    while e > 0:
        temp1 = temp_phi / e
        temp2 = temp_phi - temp1 * e
        temp_phi = e
        e = temp2

        x = x2 - temp1 * x1
        y = d - temp1 * y1

        x2 = x1
        x1 = x
        d = y1
        y1 = y

    if temp_phi == 1:
        return d + phi


def rand_prime():
    while True:
        p = random.randrange(101, 1000, 2)
        if all(p % n != 0 for n in range(3, int((p ** 0.5) + 1), 2)):
            return p


def generate_keypair(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)
    e = random.randrange(1, phi)
    g = gcd(e, phi)

    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)

    d = multiplicative_inverse(e, phi)
    return (e, n), (d, n)


# usage: encrypt(private_key, message)
def encrypt(pk, plaintext):
    key, n = pk
    cipher = [(ord(char) ** key) % n for char in plaintext]
    return cipher


# usage: decrypt(public_key, encrypted_msg)
def decrypt(pk, ciphertext):
    key, n = pk
    plain = [chr((char ** key) % n) for char in ciphertext]
    return ''.join(plain)


def rsa():
    p = rand_prime()
    q = rand_prime()
    pu, pr = generate_keypair(p, q)
    return pu, pr


if __name__ == '__main__':
    public, private = rsa()
    print 'public key: ', public
    print 'private key: ', private
    # use these for checking:
    public = (163789, 275801)
    privat = (207397, 275801)
    encrypted = encrypt(private, '192.168.116.132')
    print 'encrypted: ', encrypted
    print 'decrypted: ', decrypt(public, encrypted)


