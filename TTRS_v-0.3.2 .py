# TTRS ver 0.3.2 : Thread update
# Note: make a thread class for the generate audio function. Prevent playing audio if still generating

import tkinter as tk
import tkinter.ttk as ttk
from gtts import gTTS # Google's module: allows for speech generation
import os # Needed to make directory 
from playsound import playsound #Needed to play generated audio
import threading #Needed to play generated audio without stopping program






#====================================================================
# GUI CODE & FUNCTION ATTACHMENT ====================================
#====================================================================
#====================================================================


        
        
class Gui4App: #The GUI was made with pygubu-designer
     
    playing = False
    generating = False
        
    class ThreadPlay(threading.Thread): #This class will handle the playAudio thread
        path = '' #The audio file will be stored here
    
        def __init__(self): #Constructor initiates the thread
            threading.Thread.__init__(self)
        
        
        def run(self):
            Gui4App.playing = True
            playsound(self.path) #Play the audio
            #print('Thread ended')
            Gui4App.playing = False
            



        
    def __init__(self, master=None):
        
       
        
    
        # build ui
        self.frame_1 = tk.Frame(master)
        self.canvas_1 = tk.Canvas(self.frame_1)
        self.canvas_1.config(confine='false', cursor='arrow', height='500', relief='flat')
        self.canvas_1.config(state='normal', takefocus=False, width='600')
        self.canvas_1.pack(side='top')
        
        #TEXT ENTER ====== This will contain the message to be spoken
        self.txtEnter = tk.Text(self.frame_1)
        self.txtEnter.config(blockcursor='false', exportselection='true', height='1', setgrid='true')
        self.txtEnter.config(width='60')
        _text_ = '''Enter Text Here!'''
        self.txtEnter.insert('0.0', _text_)
        self.txtEnter.place(bordermode='outside', relheight='0.42', relwidth='0.87', relx='0.07', rely='0.53', x='0', y='0')
        
        #Button TEXT ENTER ====== This will collect the text info from txtEnter and do things with it
        self.btEnter = tk.Button(self.frame_1)
        self.btEnter.config(anchor='n', text='Generate Speech')
        self.btEnter.place(anchor='nw', relwidth='0.41', relx='0.07', rely='0.45', x='0', y='0')
        self.btEnter.configure(command=self.makeAudio) #Attaches button to makeAudio function
        
        #SET ACCENT ====== This will send info to function to modify string
        self.accent = tk.Message(self.frame_1)
        self.accent.config(text='Set Accent', width='100')
        self.accent.place(relx='0.09', rely='0.01', x='0', y='0')
        
        self.langEn = tk.Button(self.frame_1)
        self.langEn.config(default='normal', height='1', overrelief='flat', state='normal')
        self.langEn.config(text='English', width='12', wraplength='0')
        self.langEn.place(relx='0.07', rely='0.07', x='0', y='0')
        self.langEn.configure(command=lambda: self.setAcc('en')) #The lambda allows me to pass arguments into function
        
        self.langEs = tk.Button(self.frame_1)
        self.langEs.config(height='1', text='Spanish', width='12')
        self.langEs.place(anchor='nw', relx='.07', rely='0.14', x='0', y='0')
        self.langEs.configure(command=lambda: self.setAcc('es'))
        
        self.langDe = tk.Button(self.frame_1)
        self.langDe.config(height='1', text='German', width='12')
        self.langDe.place(anchor='nw', relx='.07', rely='.21', x='0', y='0')
        self.langDe.configure(command=lambda: self.setAcc('de'))
        
        self.langFr = tk.Button(self.frame_1)
        self.langFr.config(height='1', text='French', width='12')
        self.langFr.place(anchor='nw', relx='.07', rely='.28', x='0', y='0')
        self.langFr.configure(command=lambda: self.setAcc('fr'))
        
        #SET FILE TYPE ====== This will send info to function to modify string
        self.fileType = tk.Message(self.frame_1)
        self.fileType.config(text='Set File Type', width='100')
        self.fileType.place(anchor='nw', relx='.27', rely='0.01', x='0', y='0')
        
        self.mp3Typ = tk.Button(self.frame_1)
        self.mp3Typ.config(height='1', text='MP3', width='12')
        self.mp3Typ.place(anchor='nw', relx='.26', rely='.07', x='0', y='0')
        self.mp3Typ.configure(command=lambda: self.setType(typ='.mp3'))
        
        self.wavTyp = tk.Button(self.frame_1)
        self.wavTyp.config(height='1', text='WAV', width='12')
        self.wavTyp.place(anchor='nw', relx='.26', rely='.14', x='0', y='0')
        self.wavTyp.configure(command=lambda: self.setType(typ='.wav'))
        
        self.oggTyp = tk.Button(self.frame_1)
        self.oggTyp.config(height='1', text='OGG', width='12')
        self.oggTyp.place(anchor='nw', relx='.26', rely='.21', x='0', y='0')
        self.oggTyp.configure(command=lambda: self.setType(typ='.ogg'))
        
        #TEXT NAME ENTER ====== This will get the info for what user wants to name the file
        self.name = tk.Message(self.frame_1)
        self.name.config(text='Set File Name', width='100')
        self.name.place(anchor='nw', relx='0.78', rely='.01', x='0', y='0')
        self.enterName = tk.Entry(self.frame_1)
        _text_ = '''File Name'''
        self.enterName.delete('0', 'end')
        self.enterName.insert('0', _text_)
        self.enterName.place(anchor='nw', relx='.75', rely='0.06', x='0', y='0')
        
        #Warning ====== Modify this with setMessage function
        self.warning = tk.Message(self.frame_1)
        self.warning.config(foreground='#ff0000', highlightbackground='#ff0000', highlightthickness='1', text='   ')
        self.warning.config(width='500')
        self.warning.place(anchor='nw', relx='0.53', rely='0.45', x='0', y='0')
        
        #Option and temp strings  ====== Tells Google how to make it, functions will modify and use these strings
                                        #If any one of these values is NULL, the program will return an error
        self.accent = 'NULL'
        self.fileTyp = 'NULL'
        self.content = ''
        self.fileName = 'NULL'
        
        self.tempPath = '' 
        self.tempAc = ''
        
        self.settingChanged = False # This will be a marker to indicate if any settings have been changed after speech generation
        
        #Play Generated Audio ====== This will play the robotTalk you generated.
                                    #If no audio has yet been generated, will return error.
        self.playSound = tk.Button(self.frame_1)
        self.playSound.config(text='Play Audio')
        self.playSound.place(anchor='nw', relx='0.07', rely='0.4', x='0', y='0')
        self.playSound.configure(command=self.playAudio) #Attaches playAudio function to button
        
        self.note = ttk.Label(self.frame_1)
        self.note.config(text='Note: Must Generate Speech\nTo Update Spoken Content')
        self.note.place(anchor='nw', relx='0.72', rely='0.1', x='0', y='0')
        
        
        self.frame_1.config(height='600', relief='flat', width='600')
        self.frame_1.pack(side='top')

        # Main widget
        self.mainwindow = self.frame_1
        
        
    
    #====================================================================
    # FUNCTIONS NEEDED TO MAKE AUDIO ====================================
    #====================================================================
    #====================================================================
    
    
    def cleanUp(self): #Clears the temporary audio files made when playing from app
        #Set up roboVoice file if it does not exist
        if not os.path.exists('robotVoice'): #Check if folder exists. If not, make it
            os.makedirs('robotVoice')
        
    
        #Create a readme file in robotVoice
        if os.path.exists('robotVoice\\ReadMe.txt') == False: #If there's not a readme file, make one
            readme = open('robotVoice\\ReadMe.txt', 'w')
            readme.write('Please ignore the files with "play" attached to them.' + 
                         '\nThese files are needed for the "Play Audio" button to work and are only temporary.')
        
        #Create a log or open a log, then delete its targets 
        if os.path.exists('robotVoice\\log.TTRS'): #If there's a log
            file = open('robotVoice\\log.TTRS', 'r') #Open the log
            toDel = file.readline() #Fill toDel with the information contained within the log
            delList = toDel.split(',') #Create a list with toDel's info by filling each element 
                                       #with the text that procedes a comma (commas omitted from element except the last)
            
            #Eliminate empty tail
            size = len(delList) #Determine the size of the list
            del delList[size - 1] #The last element gets filled with a single comma, so lets remove that from the deletion list
            
            #Procede to deletion    
            for speech in delList: #Going through the elements in the list called delList
                os.remove(speech) #Delete the files located at the pathway specified within the list's current element

            file.close() #End deletion process
            
            #The log is now impotent, containing pathways to non-existent files. When this function is called again next start up,
            #an error will be generated that kills the program. To circumvent this issue, I must wipe all the recorded pathways.
            file = open('robotVoice\\log.TTRS', 'w') #Opens the file to wipe it. By using the 'w', we're telling python to
                                                     #prep the file for being written in
            file.write('') #Writing anything will tell Python to overrite the file. So to wipe the file, I'll just write an empty string to it
            file.close()   #End file-wiping process
    
    
    
    def playAudio(self): #When button pressed, the audio plays within app
        if self.playing == False:
            #print('Looks like I\'m not playing')
            if (os.path.exists(self.tempPath) == True and 
                self.settingChanged == False):
                
                self.setMessage(' ')
                self.mainAudio = self.ThreadPlay()
                self.mainAudio.path = self.tempPath
                self.mainAudio.start() #Starts the thread
                #print('Thread Started')
                del self.mainAudio
            
            else:
                self.setMessage(msg='Please Generate Audio First')
                
        elif self.playing == True:
            self.setMessage(msg='Currently Playing')
        
        elif self.generating == True:
            self.setMessage(msg='Please Wait for Audio to Generate')
            
        else:
            self.setMessage(msg='Something went wrong...')
        
        
        
    def makeIt(self, fileName, text, accent, fileType): #This is called to send the info to Google and have them generate a sound file
        output = gTTS(text = text, lang = accent, slow = False)
        output.save('robotVoice\\' + fileName + fileType) #Save the audio file into the robotVoice folder
        



    def makeAudio(self): #This will send the data to Google and produce a file
        self.setMessage(msg="Something went wrong ...") #if attempt fails, preventing a message below from printing
        self.getText() #Get the entered text and store into appropriate variables
        
        if (self.accent != 'NULL' and self.fileTyp != 'NULL' 
            and self.fileName != '' and self.content != ''): #Every variable has inputs
        
            #1. Make permenant file
            self.makeIt(fileName = self.fileName, text = self.content, accent = self.accent, fileType = self.fileTyp) #send info to makeit fn
            self.setMessage("Successfully created audio file!") #Display message indicating success
            
            #2. Create temp file for playback; must be .mp3 for playsound to work. If path is new, enter it into log
            if os.path.exists('robotVoice\\play' + self.fileName + '.mp3'): 
                os.remove('robotVoice\\play' + self.fileName + '.mp3')
            else:
                if os.path.exists('robotVoice\\log.TTRS'): #Add pathway to log
                    file = open('robotVoice\\log.TTRS', 'a') #If log exists, append to it
                else:
                    file = open('robotVoice\\log.TTRS', 'w') #If file does not exist, create it
                
                file.write('robotVoice\\play' + self.fileName + '.mp3,')
                file.close() #End file logging
            
            self.makeIt(fileName = 'play' + self.fileName, text = self.content, accent = self.accent, fileType = '.mp3')
            self.tempPath = 'robotVoice\\play' + self.fileName + '.mp3'
            
            #3. Report success
            self.settingChanged = False #If creation succesful, reset bool to false
            #print('Changes set to FALSE')
            #print("Success!")
            
        elif (self.accent == 'NULL' and self.fileTyp != 'NULL'): #FileType is selected, but accent is not
            self.setMessage(msg="Please select an accent")
            
        elif (self.accent != 'NULL' and self.fileTyp == 'NULL'): #Accent is selected, but fileType is not
            self.setMessage(msg="Please select a file type")
            
        elif (self.fileName == '' and self.content == '' 
              and self.accent == 'NULL' and self.fileTyp == 'NULL'):
              
            #User has gone out of their way to ensure all settings are invalid
            self.setMessage(msg="Aw fuck, I can't believe you've done this") 
            
        elif (self.accent == 'NULL' and self.fileTyp == 'NULL'): #Neither fileType nor accent is selected
            self.setMessage(msg="Please select an accent and file type")
            
        elif (self.accent != 'NULL' and self.fileTyp != 'NULL' 
              and self.fileName == '' and self.content != ''):
              
            #User has made appropriate selections, but has voided both text entries
            self.setMessage(msg="Please enter a file name")
            
        elif (self.accent != 'NULL' and self.fileTyp != 'NULL' 
              and self.fileName != '' and self.content == ''):
              
            #User has completed all other steps, but has left out what they want the robot to speak
            self.setMessage(msg="Please enter something to speak")
            
        elif (self.accent != 'NULL' and self.fileTyp != 'NULL' 
              and self.fileName == '' and self.content == ''):
              
            #user has voided both text entries, but has selected an accent and fileType
            self.setMessage(msg="Please enter a file name\n and what you want spoken")
            
        else: #Something else has happened that I've not thought of 
            self.setMessage(msg="Aw fuck, I can't believe you've done this")
            #print('Something went wrong ...') 
        
    
    
    def setMessage(self, msg): #This will modify the red box message, displaying a message
        self.warning.config(text=msg)
        self.warning.place(anchor='nw', relx='0.53', rely='0.45', x='0', y='0')
    
    
    
    def setAcc(self, selAc):
        self.accent = selAc
        
        #selAc is converted from gTTS compatible language codes to the full name so that the 
        #full name can be presented to the user
        
        if selAc == 'en':
            selAc = 'English'
        elif selAc == 'es':
            selAc = 'Spanish'
        elif selAc == 'de':
            selAc = 'German'
        elif selAc == 'fr':
            selAc = 'French'
            
        self.setMessage('Selected ' + selAc + ' accent') #Print the user friendly accent selection
        self.settingChanged = True #Report the change in settings 
        #print(self.accent + ' setting changed')



    def setType(self, typ):
        self.fileTyp = typ
        self.setMessage('Selected ' + typ + ' format')
        self.settingChanged = True #Report the change in settings 
        #print(self.fileTyp + ' setting changed')

        
        
    def getText(self):
        self.content = self.txtEnter.get("1.0", "end-1c") #read the line, but omit the newline indicator that's added
        self.fileName = self.enterName.get() #Yoink the text from the name box
        self.settingChanged = True #Report the change in settings 
        #print('setting changed')



    def run(self):
        self.mainwindow.mainloop()



if __name__ == '__main__':
    import tkinter as tk
    playing = False # Switch. If True, no threads may be activated.
    generating = False # Switch. If True, no threads may be activated.
    
    root = tk.Tk()
    root.resizable(height=False, width=False) #Prohibit resizing the height or width of window
    root.wm_title("TTRS v0.3.1") # Sets the title of the window to the string included as an argument
    root.iconbitmap('icon2.ico') # Sets window icon to the icon I made (quite shite if I do say so myself)
    
    
    app = Gui4App(root)
    Gui4App.cleanUp(Gui4App) #Delete temporary play files on startup, as a way to make the folder less cluttered
                             #I'm probably just going to put the play files into another folder to make it cleaner
    app.run()

