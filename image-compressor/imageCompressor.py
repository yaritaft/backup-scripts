from send2trash import send2trash
from PIL import Image, ExifTags
import os
import glob

def replace_dir_with_spaces_with_dashs(parent):
    for path, folders, files in os.walk(parent):
        for f in files:
            os.rename(os.path.join(path, f), os.path.join(path, f.replace(' ', '-')))
        for i in range(len(folders)):
            new_name = folders[i].replace(' ', '-')
            os.rename(os.path.join(path, folders[i]), os.path.join(path, new_name))
            folders[i] = new_name

def compressMe(file, extension, verbose = False):
    filepath = os.path.join(os.getcwd(), file)
      
    # open the image
    picture = Image.open(filepath)
      
    # Save the picture with desired quality
    # To change the quality of image,
    # set the quality variable at
    # your desired level, The more 
    # the value of quality variable 
    # and lesser the compression
    for orientation in ExifTags.TAGS.keys() : 
        if ExifTags.TAGS[orientation]=='Orientation' : break
    raw_exif = picture._getexif()
    if raw_exif and (raw_exif.items() is not None):
        exif=dict(raw_exif.items())
        
        if orientation in exif:
            print(exif[orientation])
            if exif[orientation] in [1,3]:
                picture=picture.rotate(0)
            elif exif[orientation] == 6 : 
                picture=picture.rotate(270, expand=True)
            elif exif[orientation] == 8 : 
                picture=picture.rotate(90, expand=True)
    quality = 75
    picture.save(file.split(".")[0]+"compressed-"+str(quality)+"."+extension, 
                 "JPEG" if extension in ["jpg", "jpeg"] else "PNG",
                 optimize = True, 
                 quality = quality)
    # Send to trash original
    send2trash(filepath)

JPG = ['jpeg','jpg']
PNG = ['png']
types = JPG + PNG
all_files = []
base_dir = os.getcwd()
replace_dir_with_spaces_with_dashs(base_dir)
with open("errors.txt", "a+") as file_object:
    for one_type in types:
        files_with_given_extension = glob.glob("**/*."+one_type, recursive=True)
        print(files_with_given_extension)
        for one_file in files_with_given_extension:
            try:
                compressMe(one_file, one_type)
            except Exception as Argument:
                file_object.write(f"ERROR: {one_file} Exception: {str(Argument)}")



print(all_files)
