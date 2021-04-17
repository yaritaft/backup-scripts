from send2trash import send2trash
import glob
import os
import json
AUDIO_BITRATE = 160
CODE_QUALITY = "26RF" ## 22 REALLY GOOD 26 VERY GOOD 28 GOOD ENOUGH
QUALITY_VALUES = {
    "22RF": 22.0,
    "26RF": 26.0,
    "28RF": 28.0,
}
base_dir = os.getcwd()

#command = ".\HandBrakeCLI.exe -i .\20171125_205539.mp4 -o 20171125_2055392221111.mp4 --preset-import-file .\22RF-1080p-30fps.json"

# STEPS listar files
# Rename to guiones
# Generar nuevo nombre con guiones
# Render videos
# Send to trash
def replace_dir_with_spaces_with_dashs(parent):
    for path, folders, files in os.walk(parent):
        for f in files:
            os.rename(os.path.join(path, f), os.path.join(path, f.replace(' ', '-')))
        for i in range(len(folders)):
            new_name = folders[i].replace(' ', '-')
            os.rename(os.path.join(path, folders[i]), os.path.join(path, new_name))
            folders[i] = new_name

replace_dir_with_spaces_with_dashs(base_dir)

videos_relative_paths = glob.glob("**/*.mp4", recursive=True)
with open("errors.txt", "a+") as file_object:
    for video_relative_path in videos_relative_paths:
        video_name = video_relative_path.split("\\")[-1]
        video_path_list = video_relative_path.split("\\")[:-1]
        video_relative_path_without_name = "\\".join(video_path_list)
        full_path = os.path.join(base_dir, video_relative_path_without_name, video_name)
        new_video_name = video_name.split(".mp4")[0] + f"-compressed-{CODE_QUALITY}" + ".mp4"
        new_full_path = os.path.join(base_dir, video_relative_path_without_name, new_video_name)
        command = f".\\HandBrakeCLI.exe -i {full_path} -o {new_full_path} --ab {AUDIO_BITRATE} -q {QUALITY_VALUES[CODE_QUALITY]}"
        # Generate compressed video
        process_result = os.system(command)
        if (process_result):
            message_error = json.dumps({"command": command, "full_path": full_path, "result": process_result})+",\n"
            print("==============ERROR===========")
            print(message_error)
            print("==============ERROR===========")
            file_object.write(message_error)
        if (process_result==0):
            # Send to trash old files
            send2trash(full_path)
        print(command)
        print(full_path)
        print(new_full_path)

