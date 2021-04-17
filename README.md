# Backup script

# Overview

The idea behind these script are to compress video and images to make a softer gdrive backup.

## Settings
- Video compressed with Handbrake-CLI with 26 RF and 160 Kbps audio quality. This only changes bitrate not FPS or Resolution. This compression it is almost invisible to human eye.
- Images compressed with Pilow library applying 75% quality. Same as above.

## Warning

Today these scripts works better with windows because it has a case insensitive filesystem, so there's no difference between a.jpg and a.JPG.

## How to use them

0. Using windows and powershell create a virtualenv and do pip install -r requirements.txt then ./venv/Scripts/activate.ps1
1. Copy (NOT MOVE) your desired folder into Video Compressor folder.
2. Do python videoCompressor.py this will compress the video and erase original file.
3. Then move your folder to image compressor and the same as above, create a virtualenv and inside it.
4. Do python imageCompressor.py this will compress your images and erase original ones.
5. Do whatever you want with your compressed files.

## Errors

They will be logged in errors.txt.

## Modify settings

Inside video compressor and image compressor scripts you can edit quality. In video compressor the more RF you choose the lesser quality you get. And audio bitrate works the other way around.
Inside image compressor you have the quality parameter that can be switched, more quality means less compression. Until 75% it is almost invisible to human eye.

## Compression Ratio

It depends on the file, a compressed file wont be compressed more.