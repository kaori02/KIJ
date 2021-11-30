'''
Created on 07.09.2016

@author: Marius

url : https://raw.githubusercontent.com/mx0c/RSA-Implementation-in-Python/master/main.py
'''

import random
import hashlib

max_PrimLength = 1000000000000

'''
calculates the modular inverse from e and phi
'''
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

'''
calculates the gcd of two ints
'''
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

'''
checks if a number is a prime
'''
def is_prime(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for n in range(3, int(num**0.5)+2, 2):
        if num % n == 0:
            return False
    return True

def generateRandomPrim():
    while(1):
        ranPrime = random.randint(0,max_PrimLength)
        if is_prime(ranPrime):
            return ranPrime

def generate_keyPairs():
    p = generateRandomPrim()
    q = generateRandomPrim()
    
    n = p*q
    print("n ",n)
    '''phi(n) = phi(p)*phi(q)'''
    phi = (p-1) * (q-1) 
    print("phi ",phi)
    
    '''choose e coprime to n and 1 > e > phi'''    
    e = random.randint(1, phi)
    g = gcd(e,phi)
    while g != 1:
        e = random.randint(1, phi)
        g = gcd(e, phi)
        
    print("e=",e," ","phi=",phi)
    '''d[1] = modular inverse of e and phi'''
    d = egcd(e, phi)[1]
    
    '''make sure d is positive'''
    d = d % phi
    if(d < 0):
        d += phi
        
    #print("KEYS: ", ((e,n),(d,n)))
    return ((e,n),(d,n))
        
def decrypt(ctext,private_key):
    try:
        key,n = private_key
        text = [chr(pow(char,key,n)) for char in ctext]
        return "".join(text)
    except TypeError as e:
        print("[DECRYPT_ERROR] " + str(e))

def encrypt(text,public_key):
    key,n = public_key
    ctext = [pow(ord(char),key,n) for char in text]
    return ctext

def hash(data):
    # hash
    h = hashlib.sha3_256()
    h.update(data)
    st = ""
    for i in h.digest():
        st += str(hex(i)) + "/"
    return st    

if __name__ == '__main__':
    message = b"teknik informatika ITS"

    # generate private key and public key
    public_key,private_key = generate_keyPairs() 
    print("Public: ",public_key)
    print("Private: ",private_key)

    st = hash(message)
    
    ctext = encrypt(st, private_key)

    padding = bytes("||", encoding='UTF-8')
    result = [message, padding, ctext]
    print("\nTo send :")
    print(result)

    # diterima
    to_hash = result[0]
    to_decrypt = result[2]

    st2 = hash(to_hash)
    resulttext = decrypt(to_decrypt, public_key)
    print("\nhashed message\t: " + st)
    print("result text\t: " + resulttext, end="\n\n")

    if (resulttext == st2) : print("VALID")
