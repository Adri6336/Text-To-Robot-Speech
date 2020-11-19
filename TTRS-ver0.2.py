from gtts import gTTS # Google's module: allows for speech generation
import os # os module: allows for console screen clearing


# PROGRAM FUNCTIONS ========================================================================
# ========================================================================

def clear(): #This will clear the screen if the user wishes to make another file
    os.system('cls')

def getFileType():# This will determine which file extention should be added to the save file
    escape = False
    while escape == False:

        print('\nSelect File Type: \n')
        print('1. WAV\n2. MP3\n3. OGG')
        type = input('\nFILETYPE: ')
        
        if type == '1' or type == '1.' or type == 'WAV' or type == 'wav':
            escape = True
            return '.wav'
            
        elif type == '2' or type == '2.' or type == 'MP3' or type == 'mp3':
            escape = True
            return '.mp3'
            
        elif type == '3' or type == '3.' or type == 'OGG' or type == 'ogg':
            escape = True
            return '.ogg'
            
        else:
            clear()

def makeIt(fileName, text, accent, fileType): #This is called to send the info to Google and have them generate a sound file
    output = gTTS(text = text, lang = accent, slow = False)
    output.save(fileName + fileType) 

def whatLang(): # This will determine which accent to use
    exit = False
    while exit == False:
    
        print('Select Accent: \n')
        print('1. English\n2. Spanish\n3. German\n4. French')
        selection = input('\nACCENT: ')
        
        if selection == '1' or selection == '1.' or selection == 'en' or selection == 'EN' or selection == 'English' or selection == 'english' or selection == 'One' or selection == 'one':
            exit = True
            return 'en' # It returns language codes that will be sent to Google in the makeIt function
            
        elif selection == '2' or selection == '2.' or selection == 'es' or selection == 'ES' or selection == 'Spanish' or selection == 'spanish' or selection == 'Two' or selection == 'two':
            exit = True
            return 'es'
            
        elif selection == '3' or selection == '3.' or selection == 'de' or selection == 'DE' or selection == 'German' or selection == 'german' or selection == 'Three' or selection == 'three':
            exit = True
            return 'de'
            
        elif selection == '4' or selection == '4.' or selection == 'fr' or selection == 'FR' or selection == 'French' or selection == 'french' or selection == 'Four' or selection == 'four':
            exit = True
            return 'fr'
            
        #elif selection == '5' or selection == '5.' or selection == 'zh' or selection == 'ZH' or selection == 'Chinese' or selection == 'chinese' or selection == 'Five' or selection == 'five':
        #    exit = True
        #    return 'zh' ----> Option scrapped due to Google not supporting the language
        
        else:
            clear() # If incorrect input is entered, clear the response and try again

def menu():
    accent = whatLang() # Function returns a language code refrenced by the variable 'accent'

    print('\nEnter What You Want to Be Read')
    myText = input('TEXT: ')

    fileType = getFileType()
    
    print('\nWhat do you want to name the file?')
    fileName = input('NAME: ')
    
    makeIt(fileName, myText, accent, fileType) # Procede to create sound. The first input determines the name of the file where the sound will be saved at, the second sends a text request to Google for processing, and the third tells Google which language accent to use 



#START PROGRAM ========================================================================
# ========================================================================

quit = False # Establish loop exit condition
while quit == False: # If quit is not desired, run the loop again

    print('Text-To-Robot-Speech Generator\n=============================')
    menu() # Get info needed for process
    
    print('\n\nWould you like to make another file?')
    resp = input('Answer: ') # If not an explicit "NO", the program will run again
    if resp == 'no' or resp == 'No' or resp == 'N' or resp == 'n' or resp == '0' or resp == 'Nein' or resp == 'nein':
        quit = True
    else:
        clear()
    

