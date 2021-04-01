Alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
cipherText = "KNXMNSLKWJXMBFYJWGJSIXFIRNYXBTWIKNXMWFSITAJWMJQRNSLFSDIFD"

# M = (C-K) mod 26

def indexAlphabet(value):
    for i,x in enumerate(Alphabet):
        if x == value.upper():
            return i
    return 0

def tansuat(key, txt):
    f = 0
    for x in txt:
        if str(x) == str(key.upper()):
            f = f + 1
    return 100.0 * f / len(txt)

def caecar(key, cipherText):
    txt = ""
    for x in cipherText:
        m = (indexAlphabet(x) - key) % 26
        txt = txt + Alphabet[m]
    print("Key = ", key)
    print(" | Cipher = ", cipherText)
    print(" | PlainText = ", txt)
    for x in Alphabet:
        print("F[",x,"] = ", tansuat(x, txt), "%")

def main():
    k = 5
    #for k in range(1,10):
    caecar(k, cipherText)

if __name__ == '__main__':
    main()

    
