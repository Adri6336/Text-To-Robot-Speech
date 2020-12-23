# Text-To-Robot-Speech
Tool to convert text to speech, creating files for later use. TTRS uses Google's gTTS module to easily create robo text readin' on command.

# TTRS v0.3 Changelog:
- Added GUI for easier use

- Used a different .exe method, as the previous single-file method uses a technique similar to malware and consequentially tripped up Windows Defender a lot.
  I think it had to do with something called a "self-extracting binary" or something, so I'll just avoid the issue (and will retroactively delete all my 
  previous onefile executables). Plus the new method will allow a faster start-up.

- Added user guidance prompts for the tool

- Added easter egg

- Made it so that created files will be placed in a folder called robotVoice


# Using TTRS
To use, you'll first need to get the gtts module and set up Python 3.9. To install using pip on Windows (comes with standard Python installations), do the following: 
1. Right click the windows icon
2. Press "Windows PowerShell (Admin)
3. Type "pip install gtts", then enter -- the computer will do the rest

Full requirements: tkinter, tkinter.ttk ,os, time, and gtts

With gtts installed, you should be able to run the script. If something goes wrong, you can just use the executable I prepared instead; it will run the script without any effort on your end, though it will be a bit slower to start up. To find the executable, you'll need to download the TTRS_v-0.3 folder and its contents, then select the sole
.exe file with the same name. 
