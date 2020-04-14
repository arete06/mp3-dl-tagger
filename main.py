from __future__ import unicode_literals
import youtube_dl
import sys
from mutagen.easyid3 import EasyID3
import os
import glob
from tkinter import *
from tkinter.filedialog import askopenfilename

# customize tags
def c_tags(): 
	global artist
	global title
	global album	
	artist = input("Song artist: ")
	title = input("Song name: ")
	album = input("Song album: ")
	audio["artist"] = artist
	audio["title"] = title
	audio["album"] = album

# download audio
if len(sys.argv) > 1:
	# get song title
	with youtube_dl.YoutubeDL() as ydl:
		info_dict = ydl.extract_info(sys.argv[1], download=False)	
		song_title = info_dict.get("title", None)

	# youtube-dl options
	ydl_opts = {
		"outtmpl": "%(title)s.%(ext)s",
		"format": "bestaudio/best",
		"postprocessors": [{
			"key": "FFmpegExtractAudio",
			"preferredcodec": "mp3",
			"preferredquality": "192",
		}],
	}

	with youtube_dl.YoutubeDL(ydl_opts) as ydl:		
		ydl.download([sys.argv[1]])

	# open file
	audio = EasyID3(song_title + ".mp3")

	c_tags()

	# save tags	
	audio.save()

	# rename file	
	for f in glob.glob(song_title + ".mp3"):
		os.rename(f, artist + " - " + title)

else:
	try:	
		# window to open file		
		root = Tk()
		root.withdraw()
		root.update()
		filename = askopenfilename()

	except:
		exit()

	audio = EasyID3(filename)
	filename = filename.rsplit("/", 1)[-1]
	print(filename)

	c_tags()

	# save tags
	audio.save()

	# rename file	
	for f in glob.glob(filename):
		os.rename(f, artist + " - " + title)
