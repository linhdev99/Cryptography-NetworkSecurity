import math

def modPow(a,b,n):
    c = 1
    if n == 1:
        return 0
    for x in range(0, b, 1):
        c = (c*a) % n
    return c

def calGCD(x,y):
    if y == 0:
        return int(x)
    else:
        if x < y:
            temp = x
            x = y
            y = temp
        return calGCD(y, x % y)

def CreateKey(p, q, e):
    n = p*q
    phiN = (p-1)*(q-1)
    if e == 0:
        e = 2
        while 1==1:
            gcdCur = calGCD(e, phiN)
            if gcdCur == 1 and e != p and e != q:
                break
            e += 1
    d = 2
    while 1==1:
        if ((d*e) % phiN) == 1 and d != e:
            break
        d += 1
    return {'p':p,'q':q,'n':n,'e':e,'d':d}

def printKey(key):
    print('===========')
    print('p = ',key['p'])
    print('q = ',key['q'])
    print('Public Key: m = ',key['n'], ' and e = ',key['e'])
    print('Private Key: m = ',key['n'], ' and d = ',key['d'])
    print('===========')

def getPublicKey(key):
    return [key['n'], key['e']]

def getPrivateKey(key):
    return [key['n'], key['d']]

def EncryptPlaintext(plaintext,public_key):
    if 17 > 65:
        return plaintext
    else:
        cryptText = modPow(plaintext,public_key[1],public_key[0])
        return int(cryptText)

def DecryptCiphertext(ciphertext, private_key):
    cryptText = modPow(ciphertext, private_key[1],private_key[0])
    return int(cryptText)


def main():
    # printKey(CreateKey(3,11,0))
    # printKey(CreateKey(5,13,11))
    
    print('Alice to Bob: ',EncryptPlaintext(17,[65,11]))
    print('Bob decrypt: ',DecryptCiphertext(EncryptPlaintext(17,[65,11]),[65,35]))

    key = CreateKey(3,11,7)
    plaintext = 5
    print('Encrypt Plaintext: ',EncryptPlaintext(plaintext,getPublicKey(key)))
    print('Decrypt Ciphertext: ',DecryptCiphertext(EncryptPlaintext(plaintext,getPublicKey(key)),getPrivateKey(key)))

    key = CreateKey(5,11,3)
    plaintext = 9
    print('Encrypt Plaintext: ',EncryptPlaintext(plaintext,getPublicKey(key)))
    print('Decrypt Ciphertext: ',DecryptCiphertext(EncryptPlaintext(plaintext,getPublicKey(key)),getPrivateKey(key)))

    key = CreateKey(7,11,17)
    plaintext = 8
    print('Encrypt Plaintext: ',EncryptPlaintext(plaintext,getPublicKey(key)))
    print('Decrypt Ciphertext: ',DecryptCiphertext(EncryptPlaintext(plaintext,getPublicKey(key)),getPrivateKey(key)))

    key = CreateKey(11,13,11)
    plaintext = 7
    print('Encrypt Plaintext: ',EncryptPlaintext(plaintext,getPublicKey(key)))
    print('Decrypt Ciphertext: ',DecryptCiphertext(EncryptPlaintext(plaintext,getPublicKey(key)),getPrivateKey(key)))

    key = CreateKey(17,31,7)
    plaintext = 2
    print('Encrypt Plaintext: ',EncryptPlaintext(plaintext,getPublicKey(key)))
    print('Decrypt Ciphertext: ',DecryptCiphertext(EncryptPlaintext(plaintext,getPublicKey(key)),getPrivateKey(key)))


if __name__ == '__main__':
    main()
