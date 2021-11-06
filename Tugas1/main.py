import sdes
import random
from sdes import *

# key bebas 10 bit
# inputnya 8 bit (1 char)

def encrypt3des2key(key1, key2, plaintext):
    """Encrypt plaintext with given key"""
    a = encrypt(key1, ord(plaintext))
    b = decrypt(key2, a)
    c = encrypt(key1, b)    
    
    return chr(c)

def decrypt3des2key(key1, key2, ciphertext):
    """Decrypt ciphertext with given key"""
    a = decrypt(key1, ord(ciphertext))
    b = encrypt(key2, a)
    c = decrypt(key1, b)    
    
    return chr(c)

def tripleDES2key(key1, key2, plaintext):
    print("-----tripleDES2key-----")
    for i in plaintext:
      a = encrypt3des2key(key1, key2, i)
      b = decrypt3des2key(key1, key2, a)
      print(i, " - ", b)
# ---------------------------------------------------------
def encrypt3des3key(key1, key2, key3, plaintext):
    """Encrypt plaintext with given key"""
    a = encrypt(key1, ord(plaintext))
    b = decrypt(key2, a)
    c = encrypt(key3, b)    
    
    return chr(c)

def decrypt3des3key(key1, key2, key3, plaintext):
    """Decrypt ciphertext with given key"""
    a = decrypt(key3, ord(plaintext))
    b = encrypt(key2, a)
    c = decrypt(key1, b)    
    
    return chr(c)

def tripleDES3key(key1, key2, key3, plaintext):
    print("-----tripleDES3key-----")
    for i in plaintext:
      a = encrypt3des3key(key1, key2, key3, i)
      b = decrypt3des3key(key1, key2, key3, a)
      print(i, " - ", b)
# ------------------------------------------------------------
def cbc_encrypt(k, iv, plaintext):
    ctr = 0
    index = 0
    textToProcess = ""
    for i in plaintext:
        if (ctr == 0):
            i = ord(i) ^ iv
            i = i ^ k
            i = i << 1
            ctr = 1
            textToProcess += chr(i)

        else:
            i = ord(i) ^ ord(plaintext[index-1])
            i = i ^ k
            i = i << 1
            textToProcess += chr(i)
        index += 1
    
    for i in textToProcess: 
        if (not isinstance(i, str)):
            i = chr(i)

    return textToProcess

def cbc_decrypt(k, iv, ciphertext):
    ctr = 0
    index = 0
    textToProcess = ""
    for i in ciphertext:
        if (ctr == 0):
            i = ord(i) >> 1
            i = i ^ k
            i = i ^ iv
            ctr = 1
            textToProcess += chr(i)

        else:
            i = ord(i) >> 1
            i = i ^ k
            i = i ^ ord(plaintext[index-1])
            textToProcess += chr(i)
        index += 1
            
    for i in textToProcess: 
        if (not isinstance(i, str)):
            i = chr(i)

    return textToProcess

def cbc_impl(k, iv, plaintext):
    a = cbc_encrypt(k, iv, plaintext)
    b = cbc_decrypt(k, iv, a)
    print("-----CBC-----")
    print(plaintext, ' - ', a, ' - ', b)

# ------------------------------------------------------------
def ctr_encrypt(k, ctr, plaintext):
    textToProcess = ""
    for i in plaintext:
        a = encrypt(k, ctr)
        i = ord(i) ^ a
        ctr += 1
        ctr %= 256
        textToProcess += chr(i)
    
    for i in textToProcess: 
        if (not isinstance(i, str)):
            i = chr(i)

    return textToProcess

def ctr_decrypt(k, ctr, ciphertext):
    textToProcess = ""
    for i in ciphertext:
        a = encrypt(k, ctr)
        i = ord(i) ^ a
        ctr += 1
        ctr %= 256
        textToProcess += chr(i)
    
    for i in textToProcess: 
        if (not isinstance(i, str)):
            i = chr(i)

    return textToProcess

def ctr_implementation(k, ctr, plaintext):
    a = ctr_encrypt(k, ctr, plaintext)
    b = ctr_decrypt(k, ctr, a)
    print("-----CTR-----")
    print(plaintext, ' - ', a, ' - ', b)
    

if __name__ == '__main__':
    plaintext = "WAHYU"
    key1 = 0b1110001110
    key2 = 0b1110011111
    key3 = 0b1100111100
    tripleDES2key(key1, key2, plaintext)
    tripleDES3key(key1, key2, key3, plaintext)

    k  = 0b11100011
    iv = 0b11101100
    cbc_impl(k, iv, plaintext)

    ctr = random.randrange(99999)
    ctr_implementation(k, ctr, plaintext)