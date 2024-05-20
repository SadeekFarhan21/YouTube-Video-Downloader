import streamlit as st
import os
import pytube

st.title("YouTube Playlist Downloader")
url = st.text_input("Enter the URL of the YouTube playlist:")

p = pytube.Playlist(url)
try:
    folder_name = "/"
    folder_name = st.text_input("Enter the folder name:")
    os.mkdir(folder_name)
    os.chdir(folder_name)
except Exception as e:
    st.write(f"Error occurred: {str(e)}")

for video in p.videos:
    stream = video.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    if stream:
        old_name = stream.download()
        st.write(old_name)
    else:
        st.write("No suitable stream found for this video.")