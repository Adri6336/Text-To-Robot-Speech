# Text-To-Robot-Speech
Tool to convert text to speech, creating files for later use. TTRS uses Google's gTTS module to easily create robo text readin' on command.

# TTRS v0.3.2 Changelog:
- Made playing genrated audio more effecient. TTRS will no longer look like it's frozen whenever it plays audio. 
- Slightly updated code to look nicer

# Using TTRS
*Using as executable file*

To use easily, you can simply download the TTRS_v0.3.2 zip and run the .exe file within. It's already packed for you, so it should be as easy as double-clicking 
and getting to work. The exact steps are as follows:
1. Download TTRS_v-0.3.2.zip
2. Extract the zip file
3. Within the newly extracted folder, you'll find the executable (with all the other files). The executable is labeled TTRS_v-0.3.2.exe
4. Double click the .exe file to start the program

*Using as Python Script*

To use, you'll first need to get the gtts module and set up Python 3.9. To install using pip on Windows (comes with standard Python installations), do the following: 
1. Right click the windows icon
2. Press "Windows PowerShell (Admin)
3. Type "pip install gtts", then enter -- the computer will do the rest
4. Download the TTRS_v-0.3.2.py and icon2.ico files. Place them both in same directory.
5. Run the Python script

Full requirements: tkinter, tkinter.ttk ,os, time, playsound, and gtts

With gtts installed, you should be able to run the script. If something goes wrong, you can just use the executable I prepared instead; it will run the script without any effort on your end, though it will be a bit slower to start up. To find the executable, you'll need to download the TTRS_v-0.3.1 folder and its contents (mainly just the icon2 file),
then select the sole .exe file with the same name.

# Additional Notes:

- Generating audio can still make TTRS look like it has frozen. An update that'll fix this is in the works.
