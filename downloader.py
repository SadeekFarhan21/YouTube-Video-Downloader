import pytube
import os

p = pytube.Playlist('https://www.youtube.com/playlist?list=PL0-GT3co4r2y2YErbmuJw2L5tW4Ew2O5B')
os.mkdir('Linear Algebra')
os.chdir('Linear Algebra')

# Assume 'p.videos' is a list of YouTube objects
for video in p.videos:
    # Get the highest resolution stream available
    stream = video.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    if stream:
        #print(f"Downloading: {video.title}")
        old_name = stream.download()
        print(old_name)
        #print("Download completed.")
    else:
        print("No suitable stream found for this video.")