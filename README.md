# graduation
Simple tool to help live stream graduations. This tool compiles a sum of images into a single video clip, which is then to be used in editing software to show yearbook photos for example.

The idea is to have a folder of, say, 1200 images, and be able to make them into a .mp4 file. Then, someone creates a cool background, masks in the MP4 (it exports the same resolution as the images) in Adobe Premiere / Final Cut / Resolve, and then uses a subtitle tool to generate matching text (save time). Instead of having to edit for 72 hours, you can get it done in about an hour with this tool.

Usage:
Run `graduation.py` in the folder with the images. They can be any number from 0001 to 9999, anything else and you'll have to edit the file get params in the script. The script will render the video as `photos.mp4`, which you then import into your editing software.
