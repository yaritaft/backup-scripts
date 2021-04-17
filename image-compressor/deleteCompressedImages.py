import os
import glob
from send2trash import send2trash

def replace_dir_with_spaces_with_dashs(parent):
    for path, folders, files in os.walk(parent):
        for f in files:
            os.rename(os.path.join(path, f), os.path.join(path, f.replace(' ', '-')))
        for i in range(len(folders)):
            new_name = folders[i].replace(' ', '-')
            os.rename(os.path.join(path, folders[i]), os.path.join(path, new_name))
            folders[i] = new_name

videos_relative_paths = glob.glob("**/*compressed-75*", recursive=True)
for one_video in videos_relative_paths:
    full_path = os.path.join(os.getcwd(), one_video)
    send2trash(full_path)
print(videos_relative_paths)