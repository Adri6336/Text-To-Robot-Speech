import tkinter as tk
import tkinter.ttk as ttk
from gtts import gTTS # Google's module: allows for speech generation
import os # Needed to make directory 
from time import sleep


# GUI CODE & FUNCTION ATTACHMENT
class Gui4App: #The GUI was made with pygubu-designer
    def __init__(self, master=None):
        # build ui
        self.frame_1 = tk.Frame(master)
        self.canvas_1 = tk.Canvas(self.frame_1)
        self.canvas_1.config(confine='false', cursor='based_arrow_down', height='500', relief='flat')
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
        self.btEnter.configure(command=self.makeAudio)
        
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
        
        #Warning ====== Modify this with function
        self.warning = tk.Message(self.frame_1)
        self.warning.config(foreground='#ff0000', highlightbackground='#ff0000', highlightthickness='1', text='   ')
        self.warning.config(width='500')
        self.warning.place(anchor='nw', relx='0.53', rely='0.45', x='0', y='0')
        
        #Option Strings  ====== Tell Google how to make it, functions will modify and use these strings
        #While any one of these values is NULL, the program will return an error
        self.accent = 'NULL'
        self.fileTyp = 'NULL'
        self.content = 'NULL'
        self.fileName = 'NULL'
        
        
        self.frame_1.config(height='600', relief='flat', width='600')
        self.frame_1.pack(side='top')

        # Main widget
        self.mainwindow = self.frame_1
        
        
    # FUNCTIONS NEEDED TO MAKE AUDIO ====================================

    def makeIt(self, fileName, text, accent, fileType): #This is called to send the info to Google and have them generate a sound file
        output = gTTS(text = text, lang = accent, slow = False)
        if not os.path.exists('robotVoice'): #check if folder exists. If not, make it
            os.makedirs('robotVoice')
        output.save('robotVoice\\' + fileName + fileType) 


    def makeAudio(self): #This will send the data to Google and produce a file
        self.setMessage(msg="Something went wrong ...") #if attempt fails
        self.getText() #Get the entered text
        
        if self.accent != 'NULL' and self.fileTyp != 'NULL' and self.fileName != '' and self.content != '': #Everything's good
            #Fill in with operations
            self.makeIt(fileName = self.fileName, text = self.content, accent = self.accent, fileType = self.fileTyp)
            self.setMessage("Successfully created audio file!")
            print("Success!")
        elif self.accent == 'NULL' and self.fileTyp != 'NULL': #FileType is selected, but accent is not
            self.setMessage(msg="Please select an accent")
        elif self.accent != 'NULL' and self.fileTyp == 'NULL': #Accent is selected, but fileType is not
            self.setMessage(msg="Please select a file type")
        elif self.fileName == '' and self.content == '' and self.accent == 'NULL' and self.fileTyp == 'NULL':
            #User has gone out of their way to ensure all settings are invalid
            self.setMessage(msg="Aw fuck, I can't believe you've done this") 
        elif self.accent == 'NULL' and self.fileTyp == 'NULL': #Neither fileType nor accent is selected
            self.setMessage(msg="Please select an accent and file type")
        elif self.accent != 'NULL' and self.fileTyp != 'NULL' and self.fileName == '' and self.content != '':
            #User has made appropriate selections, but has voided both text entries
            self.setMessage(msg="Please enter a file name")
        elif self.accent != 'NULL' and self.fileTyp != 'NULL' and self.fileName != '' and self.content == '':
            #User has completed all other steps, but has left out what they want the robot to speak
            self.setMessage(msg="Please enter something to speak")
        elif self.accent != 'NULL' and self.fileTyp != 'NULL' and self.fileName == '' and self.content == '':
            #user has voided both text entries, but has selected an accent and fileType
            self.setMessage(msg="Please enter a file name\n and what you want spoken")
        else: #Something else has happened that I've not thought of 
            self.setMessage(msg="Aw fuck, I can't believe you've done this")
            print('Something went wrong') #Create Failure code
        
    
    def setMessage(self, msg): #This will modify the red box message
        self.warning.config(text=msg)
        self.warning.place(anchor='nw', relx='0.53', rely='0.45', x='0', y='0')
    
    
    def setAcc(self, selAc):
        self.accent = selAc
        
        if selAc == 'en':
            selAc = 'English'
        elif selAc == 'es':
            selAc = 'Spanish'
        elif selAc == 'de':
            selAc = 'German'
        elif selAc == 'fr':
            selAc = 'French'
            
        self.setMessage('Selected ' + selAc + ' accent')
        print(self.accent)


    def setType(self, typ):
        self.fileTyp = typ
        self.setMessage('Selected ' + typ + ' format')
        print(self.fileTyp)
        
        
    def getText(self):
        self.content = self.txtEnter.get("1.0", "end-1c") #read the line, but omit the newline that's added
        self.fileName = self.enterName.get()


    def run(self):
        self.mainwindow.mainloop()


if __name__ == '__main__':
    import tkinter as tk
    root = tk.Tk()
    root.resizable(height=False, width=False) #Prohibit resizing the height or width of window
    root.wm_title("TTRS v0.3") # Sets the title of the window to the string included as an argument
    root.iconbitmap('icon.ico') # Sets window icon to the icon I made (quite shite if I do say so myself)
    
    
    app = Gui4App(root)
    app.run()

