key_table = [["M","F","H","I/J","K"],["U","N","O","P","Q"],["Z","V","W","X","Y"],["E","L","A","R","G"],["D","S","T","B","C"]]
"""  I/J  --> 0,3 """
encryptText = ""
decryptText = "Must see you over Cadogan West. Coming at once."

def initMatrix(x,y,init):
    return [[init] * y for i in range(x)]

def replacer(s, newstring, index, nofail=False):
    # raise an error if index is outside of the string
    if not nofail and index not in range(len(s)):
        raise ValueError("index outside given string")

    # if not erroring, but the index is still not in the correct range..
    if index < 0:  # add it to the beginning
        return newstring + s
    if index > len(s):  # add it to the end
        return s + newstring

    # insert the new string between "slices" of the original
    return s[:index] + newstring + s[index + 1:]

def createKeyMatrix(key, x, y):
    matrix = initMatrix(x,y,'')
    idx = 0
    Alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    Alphabet = Alphabet.upper()
    Alphabet = Alphabet.replace('J','')
    key = key.replace('J','')
    for i in range(0, x):
        for j in range(0, y):
            if key != '':
                temp = key[0]
                key = key.replace(temp,'')
                Alphabet = Alphabet.replace(temp,'')
                # if temp == 'I':
                #     temp = "I/J"
                matrix[i][j] = temp
            else:
                temp = Alphabet[0]
                Alphabet = Alphabet.replace(temp,'')
                # if temp == 'I':
                #     temp = "I/J"
                matrix[i][j] = temp
    return matrix

def checkRow(chr, matrix, x, y):
    row = -1
    col = -1
    for i in range(0,x):
        for j in range(0,y):
            if matrix[i][j] in chr:
                row = i
                col = j
                break
        if row != -1:
            break
    for i in range(0,y):
        if matrix[row][i] in chr and i != col:
            return True
    return False

def replaceRow(chr, matrix, x, y):
    col = -1
    row = -1
    for i in range(0, x):
        for j in range(0, y):
            if matrix[i][j] == chr:
                row = i
                col = j
                break
        if row != -1:
            break
    if col == y - 1:
        col = 0
    else:
        col += 1
    newChr = matrix[row][col]
    return newChr

def replaceCol(chr, matrix, x, y):
    col = -1
    row = -1
    for i in range(0, x):
        for j in range(0, y):
            if matrix[i][j] == chr:
                row = i
                col = j
                break
        if row != -1:
            break
    if row == x - 1:
        row = 0
    else:
        row += 1
    newChr = matrix[row][col]
    return newChr

def replaceRowCol(chr, matrix, x, y):
    col = [-1,-1]
    row = [-1,-1]
    for i in range(0, x):
        for j in range(0, y):
            if chr[0] == matrix[i][j]:
                row[0] = i
                col[0] = j
            if chr[1] == matrix[i][j]:
                row[1] = i
                col[1] = j
    return [matrix[row[0]][col[1]], matrix[row[1]][col[0]]]

def checkCol(chr, matrix, x, y):
    row = -1
    col = -1
    for i in range(0,x):
        for j in range(0,y):
            if matrix[i][j] in chr:
                row = i
                col = j
                break
        if col != -1:
            break
    for i in range(0,x):
        if matrix[i][col] in chr and i != row:
            return True
    return False

def PlayfairEncrypt(txt, key):
    x = 5
    y = 5
    txt = txt.replace(' ','')
    txt = txt.upper()
    cipherText = ''
    matrix = createKeyMatrix(key,5,5)
    lastChr = ''
    print("Length: ", len(txt))
    if len(txt) % 2 != 0:
        print("Length % 2 = 1 --> add X")
        txt = txt + 'X'
    print(txt)
    for i in range(0,len(txt),2):
        plaintext = [txt[i],txt[i+1]]
        if txt[i] == 'J':
            txt = replacer(txt,'I',i)
        if txt[i+1] == 'J':
            txt = replacer(txt,'I',i+1)
        chrs = [txt[i],txt[i+1]]
        if str(txt[i]) == str(txt[i+1]):
            newChr = [txt[i], 'X']
            cipherText += newChr[0] + newChr[1]
            print(plaintext, "-->", newChr)
        elif checkRow(chrs,matrix,x,y):
            newChr = [replaceRow(chrs[0], matrix, x, y), replaceRow(chrs[1], matrix, x, y)]
            cipherText += newChr[0] + newChr[1]
            print(plaintext, "-->", newChr)
        elif checkCol(chrs,matrix,x,y):
            newChr = [replaceCol(chrs[0], matrix, x, y), replaceCol(chrs[1], matrix, x, y)]
            cipherText += newChr[0] + newChr[1]
            print(plaintext, "-->", newChr)
        else:
            newChr = replaceRowCol(chrs, matrix, x, y)
            cipherText += newChr[0] + newChr[1]
            print(plaintext, "-->", newChr)
        cipherText += " "
    print(cipherText)
    return None

def PlayfairDecrypt(text, key):
    return None

def main():
    # key = "MONARCHY"
    key = "MFHIKUNOPQZVWXYELARGDSTBC"
    plaintext = "Must see youover Cadogan West Coming at once"
    key = key.upper()
    PlayfairEncrypt(plaintext,key)
    return None

if __name__ == '__main__':
    main()
#MU ST SE EY OU OV ER CA DO GA NW ES TC OM IN GA TO NC EX
#UZ TB DL GZ PN NW LG TG TU ER OV LD BD UH FP ER HW QS RZ 
#UZ TB DL GZ PN NW LG TG TU ER OV LD BD UH FP ER HW SQ RZ
