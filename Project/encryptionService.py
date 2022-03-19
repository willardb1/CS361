#!/usr/bin/python

import time, os
from operator import length_hint

def encrypt(input,key):
    length = len(input)
    keyLength = len(key) - 1

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

def decrypt(input, key):
    length = len(input)
    keyLength = len(key) - 1

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

def main():
    while True: #Run continuously
        time.sleep(0.25) #Check the file every .25 seconds
        f = open("service-comm.txt", "r+") #Open the file
        flag = f.readline().strip() #Read the flag line
        if flag == '1': #Only run if flag is 1
            message = f.readline().strip() #Collect message
            key = f.readline().strip() #Collect key
            mode = f.readline().strip() #Collect mode
            f.truncate(0) #Delete text in file
            f.seek(0) #Move to beginning of file

            if mode.startswith('e'): #Encryption
                newMessage = encrypt(message, key)
                f.write('0\n')
                f.write(newMessage)
                f.write('\n')
                f.write(key)
            elif mode.startswith('d'): #Decryption
                newMessage = decrypt(message, key)
                f.write('0\n')
                f.write(newMessage)
                f.write('\n')
                f.write(key)
            f.close()



if __name__ == '__main__':
    main()
