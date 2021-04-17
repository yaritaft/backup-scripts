# Process

# WARNING: DO THIS PROCESS WITH A COPY OF YOUR INFO, NOT THE ONLY COPY YOU HAVE.
# WARNING: I highly recommend to use this script on windows because it is case sensitive and that helps taking files with upper case extensions just giving a
lower case extension.

# First always place the original folder inside video script.
# Select desired quality ( 22 RF (better) or 26 RF and 160 kbps audio)
# Then the script will remove spaces for - and will create new files and erase the original ones BE VERY CAREFULL WITH THIS, (from 2 to 4X of compression here)
The idea is to have a copy with original quality in PC and HDD and a softer version in cloud providers.
# Then once you have your folder with compressed videos drag and drop it in image compressor folder.
# Execute the script and this will do the same as video script, it will create a compressed version and erase original one. ( More than 3 X of compression here )
# Quality 75% gives extremely good results in terms of quality.
# Some rotation issues may appear depending of the exif (photo info). For examplo Samsung s9 pictures after being compressed where being rotate. There is
a workaround for that in the code in case that rotation is value 1 for that phone. Maybe with a new one this process should be done again with the help of a 
debugger. (Because exifs are handled differently from one camera to the other)


# FOR NEW FILES TO BE ADDED
# WARNING DO NOT RE APPLY THE SCRIPT TWICE IN A FOLDER THAT WAS ALREADY COMPRESSED, BECAUSE IT WILL COMPRESS THE COMPRESSED VIDEO.

# Just add the desired folders to add to your cloud copy inside every folder as above, and then once you have them compressed add them to the cloud backup.


# How to debug in windows
Step 1) Control + shift + p and select interpreter
Step 2) Copy and paste absolute route of python.exe from your virtualenv folder (maybe venv\Scripts\python.exe)
Step 3) Press F5 and that's it. You dont need any launch.json or settings.json.