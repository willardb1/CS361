

###########################
from operator import length_hint

#####################################################
def encrypt(input,key):
    length = len(input) - 1
    keyLength = len(key) -1
    output = ''
    for x in range(0,length):

        ival = ord(input[x])
        if ival == 32:
            ival = 91

        if x > keyLength:
            k = x % keyLength
        else:
            k = x
        kval = ord(key[k])

        oval = ival - kval + 65

        output = output + chr((oval))

    output = output + '\0'

    return output




#############################################################
def decrypt(input, key):
    length = len(input) - 1
    keyLength = len(key) - 1

    print('length: ', length)
    print('keyLength: ', keyLength)

    output = ''

    for x in range(0,length):

        ival = ord(input[x])

        if x > keyLength:
            k = x % keyLength
        else:
            k = x 
        kval = ord(key[k])

        oval = ival + kval - 65

        if oval == 91:
            oval = 32

        output = output + chr(oval)

    output = output + '\0'
    return output

############################################################################