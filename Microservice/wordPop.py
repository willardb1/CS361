

from random import randint
import time


dicText = []

def populateDic():
    global dicText
    with open('words.txt') as file:
            dicText = file.readlines()
            file.close()

    print('dictionary Populated')



def textGenerator(wordCount):
    print('generating text with: ', wordCount, ' words')
    text = ''
    listLength = len(dicText)


    for x in range(int(wordCount)):
        
        number = randint(0,listLength)
        
        word = dicText[number]
        
        text = text + word.strip() + ' '
        

    #print(text)
    return text




def main():
    print("starting service")
    run = True
    while (run):
        try:
            with open("wordCount.txt") as file:
                lines = file.readlines()
                print(lines)
                file.close()
                if int(lines[0]) == 1: #check txt file communication from UI
                    if lines[1] == "quit":
                        print("closing word service")
                        with open("wordCount.txt","w") as file: #write random text to wordCount.txt
                            file.write("0\n")
                            file.write("waiting") 
                            file.close()
                        run = False #exit loop and end program
                    else:
                        wordCount = lines[1]
                        #print(wordCount)
                        text = textGenerator(wordCount)
                        #print(text)
                        with open("wordCount.txt","w") as file: #write random text to wordCount.txt
                            file.write("0\n")
                            file.write(text) 
                            file.close()
                else:
                    file.close()
                    pass
        except:
            pass

        time.sleep(0.25) #check txt file every 0.25secs


if __name__ == "__main__":
    populateDic()
    main()
