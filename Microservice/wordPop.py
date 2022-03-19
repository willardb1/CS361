# Author: Brody Willard
# Class: CS361
# DATE: 3/18/2022
# Description: mircoservice that generates random text based on a users request for X number of words

from random import randint
import time


dicText = []


def populateDic(): #populates program dictionary from txt file
    global dicText
    with open('words.txt') as file:
        dicText = file.readlines()
        file.close()



def textGenerator(wordCount): #generates random text for user 
    print('generating text with: ', wordCount, ' words')
    text = ''
    listLength = len(dicText)

    for x in range(int(wordCount)):
        number = randint(0,listLength)
        word = dicText[number]
        text = text + word.strip() + ' '
    return text



def quitProg():  #reset txt and set condition to shutdown service
    with open("wordCount.txt","w") as file: 
        file.write("0\n")
        file.write("waiting") 
        file.close()
    return False



def textToText(text): #pass random text to communication pipeline
    with open("wordCount.txt","w") as file: 
        file.write("0\n")
        file.write(text) 
        file.close()



def execute(): 
    with open("wordCount.txt") as file:
        lines = file.readlines()
        file.close()
        if int(lines[0]) == 1: #check txt file for communication from UI
            if lines[1] == "quit":
                run = quitProg() #exit loop and end program
            else:
                text = textGenerator(lines[1]) #get random text for user
                textToText(text)
        else:
            pass
    return run



def main():
    run = True
    while (run):
        try:
            run = execute()
        except:
            pass

        time.sleep(0.25) #check txt file every 0.25secs



if __name__ == "__main__":
    populateDic()
    main()
