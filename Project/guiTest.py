from asyncio.windows_events import NULL
from cgitb import text
from fileinput import filename
from http.client import FAILED_DEPENDENCY
from logging import NullHandler
from msilib.schema import File, Font
from telnetlib import ENCRYPT
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter.filedialog import askopenfile, asksaveasfile
from tkinter.tix import COLUMN
from turtle import left, title, width
import os

import encryption as enDe


fileText = NULL

inputData ={
    'text': NULL,
    'password': NULL,
    'cypher' : NULL
}

outputData = {
    'text': NULL,
    'password': NULL
}


#################### window ##########################
window = Tk()
window.title('Encrypt/Decrypt')
window.geometry("1200x900")

#######################################################



################ functions/button calls #######################

def pullText():
    global fileText

    valid = True
    message = []
    if opt1.get() == 1: #chose textbox
        print(opt1.get())
        try:
            inputData['text'] = inputText.get(1.0,END)

        except:
            valid = False
            message.append('no text')

    else: #chose text file
        if fileText != NULL:
            try:
                inputData['text']= fileText
            except:
                valid = False
                message.append('could not open')
        else:
            message.append('no text file selected')

    try: #check for password
        inputData['password'] = passwordInput.get(1.0,END)
    except:
        valid = False
        message.append('no password')

    if valid: #have a password and input
        print('sending to micro')
    else:
        print('did not send text')

    return valid, message



def serializeText():

    inputData['cypher'] = opt2.get()

    #post data to microservice in json format {cypher: (1 or 2), password:(text), input text: (text)}
    print(inputData)

    


def retrieveText():
    outputText.config(state='normal')
    outputText.delete(1.0, 'end')
    outputText.config(state='disabled')
    #global outputData

    ### get data from microservice
    outputText.config(state='normal')
    outputText.insert('end',outputData['text'])
    outputText.config(state='disabled')

    print('outputing text')



def downloadText():

    filetypesTup = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )

    try:
        file = asksaveasfile(filetypes= filetypesTup)
        filename = os.path.basename(file.name)
        file.write(outputData['text'])
        file.write('\nPassword: ' + outputData['password'])
        file.close()
        
        outputFileText.config(state='normal')
        outputFileText.config(text=filename)
        outputFileText.config(state='disabled')


    except:

        outputFileText.config(state='normal')
        outputFileText.config(text='output file')
        outputFileText.config(state='disabled')
        messagebox.showerror(title='Failed to Download', message = 'Failed to download text file')


def selectFile():
    global fileText

    filetypesTup = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )

    try:
        file = askopenfile(filetypes=filetypesTup)
        filename = os.path.basename(file.name)
        fileText= file.read()
        file.close()

        inputFileText.config(state='normal')
        inputFileText.config(text=filename)
        inputFileText.config(state='disabled')
    except:
        fileText = NULL 
        inputFileText.config(state='normal')
        inputFileText.config(text='select a file')
        inputFileText.config(state='disabled')
        messagebox.showerror(title='Failed to Open Text', message = 'Failed to load text file')


def run():
    
    valid, messageTxt = pullText()
    a = ''
    for x in messageTxt:
        a = a + x +'\n'

    messageTxt = a

    if valid:
        serializeText()
        testFunc()
        retrieveText()

    else:
        print(messageTxt)
        messagebox.showerror(title='Failed Inputs', message = messageTxt)
        

def testFunc():
    outputData['password'] = inputData['password']

    if inputData['cypher'] == 1:
        outputData['text'] = enDe.encrypt(inputData['text'], inputData['password'])
    else:
        outputData['text'] = enDe.decrypt(inputData['text'], inputData['password'])

    



############### GUI ############################

########## column 0 ##########

Frame(window, width= 10, height= 5).grid(row = 0, column=0)

#######  column 1 ###########

##input
inputLabel = Label(window, text = 'Input', justify='left', font= 'none 18 bold underline', pady = 5)
inputLabel.grid(row=1,column=1, sticky=W)

inputText = Text(window, width = 50, height= 10, bg = 'white', bd = 5, font = 'none 12')
inputText.grid(row = 2, column = 1, rowspan = 8,columnspan=3, sticky=W)

Frame(window, height= 10).grid(row = 10, column=1)

inputFileText = Label(window, width = 40, bg = 'white', bd = 5, font = 'none 12', fg = 'black',text ='select a file', state='disabled')
inputFileText.grid(row = 11, column = 1, columnspan=2, sticky=W)

Frame(window, height= 10).grid(row = 12, column=1)


##password
passwordLabel = Label(window, text = 'Password', justify='left', font= 'none 18 bold underline')
passwordLabel.grid(row=13,column=1, sticky=W)

passDescription = Label(window, text='Provide password for text processing',justify='left', font= 'none 12', pady = 2)
passDescription.grid(row =14, column = 1, sticky= W)

passwordInput = Text(window, width = 50, height= 1, bg = 'white', bd = 5, font = 'none 12')
passwordInput.grid(row = 15, column = 1,columnspan=3, sticky=W)

Frame(window, height= 20).grid(row = 16, column=1)

##execute
runLabel = Label(window, text = 'Run', justify='left', font= 'none 18 bold underline')
runLabel.grid(row=17,column=1, sticky=W)

runDescription = Label(window, text = 'Process input and generate text', justify='left', font= 'none 12')
runDescription.grid(row=18,column=1, sticky=W)

runButton = Button(window,text = 'Process Text', justify='left', font= 'none 14 bold', bg ='white', bd=5, padx=5, command=run )
runButton.grid(row=19,column=1, sticky=W)

Frame(window, height= 30).grid(row = 20, column=1)

##output
outputLabel = Label(window, text = 'Output', justify='left', font= 'none 18 bold underline', pady = 5)
outputLabel.grid(row=21,column=1, sticky=W)

outputText = Text(window, width = 50, height= 10, bg = 'white', bd = 5, font = 'none 12', state = 'disabled')
outputText.grid(row = 22, column = 1, columnspan=3, sticky=W)

Frame(window, height= 10).grid(row = 23, column=1)

outputFileText = Label(window, width = 40, bg = 'white', bd = 5, font = 'none 12', fg = 'black',text ='output file', state='disabled')
outputFileText.grid(row = 24, column = 1, columnspan=2, sticky=W)
# update output box
# text.configure(state='normal')
# text.insert('end', 'Some Text')
# text.configure(state='disabled')


##### column 2 #############


selectButton = Button(window,text = 'File Select', justify='left', font= 'none 12 bold', bg ='white', bd=5, padx=10, command=selectFile)
selectButton.grid(row = 11, column = 3, sticky='E')


selectButton = Button(window,text = 'Download', justify='left', font= 'none 12 bold', bg ='white', bd=5, padx=10, command=downloadText)
selectButton.grid(row = 24, column = 3, sticky='E')
#####  column 4 #############

Frame(window, width= 100, height= 5).grid(row = 0, column=4)
#####  columb 5 ##############
## input options
inputFormat = Label(window, text = 'Input Format', justify='left', font= 'none 18 bold underline', pady = 5)
inputFormat.grid(row=1,column=5, sticky=W)


inFormatDescription = Label(window, text = 'Select which input you would like to use', justify='left', font= 'none 12')
inFormatDescription.grid(row=2,column=5, sticky=NW)

opt1 = IntVar()
opt1.set(1)
inputOption1 = Radiobutton(window, text = 'Use TextBox', justify='left',font= 'none 12 bold', value=1, variable=opt1)
inputOption1.grid(row=3,column=5, sticky=NW)

inputOption2 = Radiobutton(window, text= 'Use Text File',justify='left',font= 'none 12 bold', value = 2, variable=opt1)
inputOption2.grid(row=4,column=5, sticky=NW)


## cypher option

cypherLabel = Label(window, text = 'Cypher Options', justify='left', font= 'none 18 bold underline', pady = 5)
cypherLabel.grid(row=11,column=5, sticky=W)

CypherDescription = Label(window, text = 'Select whether you would like to encrypt od decrypt the provided text', justify='left', font= 'none 12')
CypherDescription.grid(row=12,column=5, sticky=NW)

opt2 = IntVar()
opt2.set(1)
cypherOption1 = Radiobutton(window, text = 'Encrypt', justify='left',font= 'none 12 bold', value = 1, variable= opt2)
cypherOption1.grid(row=13,column=5, sticky=NW)

cypherOption2 = Radiobutton(window, text= 'Decrypt',justify='left',font= 'none 12 bold', value = 2, variable=opt2)
cypherOption2.grid(row=14,column=5, sticky=NW)



## output test button ###############
#remove later 

# outputTest = Button(window,text = 'OutputTest', justify='left', font= 'none 12 bold', bg ='white', bd=5, padx=10, command=retrieveText)
# outputTest.grid(row=22,column=5, sticky=NW)


###### Execute #######
window.mainloop()


