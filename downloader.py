import os
import argparse

from pytube import YouTube

parser = argparse.ArgumentParser(
    description='This script downloads mp3 audio from Youtube video')
parser.add_argument('link', help='Link to Youtube video')
args = parser.parse_args()

yt = YouTube(args.link)

# Selecting and downoading audio track from video
video = yt.streams.filter(only_audio=True).first()
out_file = video.download(output_path=".")

# Reformating mp4 audio to mp3
base, ext = os.path.splitext(out_file)
new_file = base + '.mp3'
os.rename(out_file, new_file)
