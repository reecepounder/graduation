from moviepy.editor import *
import srt


images = []
for i in range(1,12):
    images.append(f"{i:04d}")

duration = input("How long should each image be on-screen (s) > ")
transition = input("How long should the crossfade transition take? > ")

duration = int(duration)
transition = int(transition)

clips = []
for j in images:
    clips.append(ImageClip(j + '.jpg').set_duration(duration).crossfadein(transition))
    print("Loading " + j + ".jpg")
video = concatenate(clips, method="compose", padding=-transition)
video.write_videofile('graduation.mp4', fps=24)

