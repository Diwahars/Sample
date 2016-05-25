import requests
import parse
import re
 
import subprocess #for running a bash command within the python script
 
import sys
import glob
import os
 
from mutagen.easyid3 import EasyID3 #for changing the tags
 
song= sys.argv[1] + sys.argv[2] + sys.argv[3] #storing the user entry
 
query_string = urllib.parse.urlencode({"search_query" : song}) #creating the youtube search query
 
html_content = urllib.request.urlopen("YouTube?" + query_string) 
search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
link_to_video= "http://www.youtube.com/watch?v=" + searc_results[0]
 
subprocess.call(["youtube-dl", "--extract-audio", "--audio-format", "mp3", "--output", "%(uploader)s%(title)s.%(ext)s", link_to_video])
#downloading it through youtube-dl
 
#I could not get any other way of getting the path of the downloaded  filename  to work properly, so I thought of grabbing the last created file using glob
newest = max(glob.iglob('*.[Mm][Pp]3'), key=os.path.getctime) #getting the newest file that was created
audio = EasyID3(newest) #changing the tags
audio["title"] = sys.argv[1]
audio["artist"] = sys.argv[2]
audio["album"] = sys.argv[3]
audio.save()
os.rename(newest, sys.argv[1]+".mp3") #changing the file name to a proper one
