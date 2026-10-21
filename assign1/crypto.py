#!/usr/bin/env python3 -tt
"""
File: crypto.py
---------------
Assignment 1: Cryptography
Course: CS 41
Name: <YOUR NAME>
SUNet: <SUNet ID>

Replace this with a description of the program.
"""
import utils
import string

# Caesar Cipher

def encrypt_caesar(plaintext):
    result = ""
    for s in plaintext:
        if s.isalpha():
            result+= chr((ord(s) - ord('A') + 3) % 26 + ord('A'))
        else:
            result+= s
    return result


def decrypt_caesar(ciphertext):
    result = ""
    for s in ciphertext:
        if s.isalpha():
            result+= chr((ord(s) - ord('A') - 3) % 26 + ord('A'))
        else:
            result+= s   
    return result


# Vigenere Cipher

def encrypt_vigenere(plaintext, keyword):
    result=""
    for i in range(len(plaintext)):
        shift=keyword[i%len(keyword)]
        result+= chr((ord(plaintext[i]) - 2 * ord('A') + ord(shift)) % 26 + ord('A'))
    return result


def decrypt_vigenere(ciphertext, keyword):
    result=""
    ind=0;
    for i in range(len(ciphertext)): 
        if(ciphertext[i].isalpha() and ciphertext[i].isupper()):
            shift=keyword[ind]
            result+= chr((ord(ciphertext[i]) - ord(shift)) % 26 + ord('A'))
            ind=(ind+1)%len(keyword)
        else:
            result+=ciphertext[i]
    return result


# Merkle-Hellman Knapsack Cryptosystem

def generate_private_key(n=8):
    """Generate a private key for use in the Merkle-Hellman Knapsack Cryptosystem.

    Following the instructions in the handout, construct the private key components
    of the MH Cryptosystem. This consistutes 3 tasks:

    1. Build a superincreasing sequence `w` of length n
        (Note: you can check if a sequence is superincreasing with `utils.is_superincreasing(seq)`)
    2. Choose some integer `q` greater than the sum of all elements in `w`
    3. Discover an integer `r` between 2 and q that is coprime to `q` (you can use utils.coprime)

    You'll need to use the random module for this function, which has been imported already

    Somehow, you'll have to return all of these values out of this function! Can we do that in Python?!

    @param n bitsize of message to send (default 8)
    @type n int

    @return 3-tuple `(w, q, r)`, with `w` a n-tuple, and q and r ints.
    """
    raise NotImplementedError  # Your implementation here

def create_public_key(private_key):
    """Create a public key corresponding to the given private key.

    To accomplish this, you only need to build and return `beta` as described in the handout.

        beta = (b_1, b_2, ..., b_n) where b_i = r × w_i mod q

    Hint: this can be written in one line using a list comprehension

    @param private_key The private key
    @type private_key 3-tuple `(w, q, r)`, with `w` a n-tuple, and q and r ints.

    @return n-tuple public key
    """
    raise NotImplementedError  # Your implementation here


def encrypt_mh(message, public_key):
    """Encrypt an outgoing message using a public key.

    1. Separate the message into chunks the size of the public key (in our case, fixed at 8)
    2. For each byte, determine the 8 bits (the `a_i`s) using `utils.byte_to_bits`
    3. Encrypt the 8 message bits by computing
         c = sum of a_i * b_i for i = 1 to n
    4. Return a list of the encrypted ciphertexts for each chunk in the message

    Hint: think about using `zip` at some point

    @param message The message to be encrypted
    @type message bytes
    @param public_key The public key of the desired recipient
    @type public_key n-tuple of ints

    @return list of ints representing encrypted bytes
    """
    raise NotImplementedError  # Your implementation here

def decrypt_mh(message, private_key):
    """Decrypt an incoming message using a private key

    1. Extract w, q, and r from the private key
    2. Compute s, the modular inverse of r mod q, using the
        Extended Euclidean algorithm (implemented at `utils.modinv(r, q)`)
    3. For each byte-sized chunk, compute
         c' = cs (mod q)
    4. Solve the superincreasing subset sum using c' and w to recover the original byte
    5. Reconsitite the encrypted bytes to get the original message back

    @param message Encrypted message chunks
    @type message list of ints
    @param private_key The private key of the recipient
    @type private_key 3-tuple of w, q, and r

    @return bytearray or str of decrypted characters
    """ 
    raise NotImplementedError  # Your implementation here

def encrypt_scytale(plaintext, circumference):
    result = [""]*circumference
    ind=0
    for s in plaintext:
        result[ind]+=s
        ind=(ind+1)%circumference
    final_result=""
    for st in result:
        final_result+=st
    return final_result

def decrypt_scytale(ciphertext, circumference):
    lc=len(ciphertext)
    resultl = [""]*lc
    ind=0
    ind2=1
    for s in ciphertext:
        resultl[ind]=s
        ind+=circumference
        if(ind>=lc):
            ind=ind2
            ind2+=1
    return "".join(resultl)

def encrypt_railfence(plaintext, num_rails):
    railfence=[""]*num_rails
    high=0
    direction=1
    for s in plaintext:
        railfence[high]+=s
        if high==0:
            direction=1
        elif high==num_rails-1:
            direction=-1
        high+=direction
    result=""
    for st in railfence:
        result+=st
    return result

def decrypt_railexitfence(ciphertext, num_rails):
    key = [[] for _ in range(num_rails)] #ez az egy syntax ai
    high=0
    direction=1
    for i in range(len(ciphertext)):
        key[high].append(i);
        if high==0:
            direction=1
        elif high==num_rails-1:
            direction=-1
        high+=direction
    
    result=[""]*len(ciphertext)
    ind=0;
    for i in range(num_rails):
        for j in range(len(key[i])):
            result[key[i][j]]=ciphertext[ind]
            ind+=1
    resultxt="".join(result)
    return resultxt

hosszuszoveg="WCR FCH! VJTK MBJ'PX PBITQMPUNIGGN HUXQ TZGVVLFLBG PQ FBQU PQ IVGFXZEL. VBCCLAZL, X'K CBGG PBWPBT P JHA CS ICQA GB IFTA WG'H Y EPHGAC XHGVTP YVF LDS MV RRRPRWH GWGL. HDCPPXUHYN GM DCEZQ ULHGTP BM W ETNXHH ETNXHH ETNXHH ETNXHH ZNQXST JXRA DCESQ MOOG PPX AVR HYFL ZRCEMO OF IFX RSL! QSM DVNI YKL HUT MWKG LDS CBGG VSXZGRS RAL YRN YGFKNN? UXSZ, FXLVL MBJ KTKS VI RAPG SPP, POM QDL'M FCH BYDL O CGGOHHR EMLA CA EGTGNN LGMO HUT QXJFRI UHYR CXLXHDCAC TUR V'AJ ZLH LDS T UWPT 10 CQAFN QMGBG CDGGAG. LDS PVB'G WYOL HB GCILOG GCILOG GCILOG GCILOG IFBZ QBJPLL!"

words=set()
with open("american-english-small", "r") as f:
    for line in f:
        words.add(line.strip().upper())


def decrypt_vigenere2(ciphertext, possible_keys):
    igazikey="AIDS"
    maxpont=0
    for key in possible_keys:
        ##print(key)##
        pontszam=0
        tipp=decrypt_vigenere(ciphertext, key)
        tipplista=tipp.split();
        for szo in tipplista:
            tiszta_szo = szo.strip(string.punctuation)
            if tiszta_szo in possible_keys:
                pontszam+=1
        if pontszam>maxpont:
            #print(tipplista)
            #print(key, pontszam)
            maxpont=pontszam
            igazikey=key
    return (igazikey, decrypt_vigenere(ciphertext, igazikey))



