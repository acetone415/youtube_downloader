from pytube import YouTube
import os

# Insert here link to video to download 
yt = YouTube('')

# Selecting and downoading audio track from video
video = yt.streams.filter(only_audio=True).first()
out_file = video.download(output_path=".")

# Reformating mp4 audio to mp3
base, ext = os.path.splitext(out_file)
new_file = base + '.mp3'
os.rename(out_file, new_file)
