import streamlit as st

placeholder = st.empty()

# video_file = open("source/snapdouyin.app-watermark-1751427338536.mp4", "rb")
video_file = open("source/v15044gf0000d5sgjsvog65lr9jsenrg.mov", "rb")
video_bytes = video_file.read()

with st.container(border=None, horizontal_alignment="center", width=360, height=640):
    st.video(video_bytes)