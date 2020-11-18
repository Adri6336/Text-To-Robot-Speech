from gtts import gTTS
import os

def clear(): #This will clear the screen if the user wishes to make another file
    os.system('cls')

def makeIt(fileName, text): #This is called to send the info to Google and have them generate a sound file
    language = 'en' # Sets accent
    output = gTTS(text = text, lang = language, slow = False)
    output.save(fileName + '.wav')

def menu():
    print('Enter What You Want to Be Read')
    myText = input('TEXT: ')

    print('\n\nWhat do you want to name the file?')
    fileName = input('NAME: ')
    
    makeIt(fileName, myText) # Procede to create sound



#Start Program
quit = False

while quit == False:
    print('Text-To-Robot-Speech Generator\n=============================')
    menu()
    
    print('\n\nWould you like to make another file?')
    resp = input('Answer: ')
    if resp == 'no' or resp == 'No' or resp == 'N' or resp == 'n' or resp == '0' or resp == 'Nein' or resp == 'nein':
        quit = True
    else:
        clear()
    

#os.system('start ' + fileName + '.wav')