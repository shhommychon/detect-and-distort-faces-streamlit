import streamlit as st
from streamlit_webrtc import webrtc_streamer
import av
import cv2

st.title("MOSAIC")
st.write("demo by CV-11 CanVas")

col1, col2, col3 = st.columns(3)
target_type = None
button1 = col1.button("IMG")
button2 = col2.button("VID")
button3 = col3.button("CAM")

if button1:
    target_type = "img"
if button2:
    target_type = "vid"
if button3:
    target_type = "cam"

if target_type == "img":
    uploaded_img = st.file_uploader("Choose a target image", type=["png", "jpg", "jpeg"])
elif target_type == "vid":
    uploaded_vid = st.file_uploader("Choose a target video", type=["mp4", "mov", "avi", "wmv"])
elif target_type == "cam":
    class VideoProcessor:
        def __init__(self):
            pass
        
        def recv(self, frame):
            return frame
    
    c = webrtc_streamer(
        key="webcam", video_processor_factory=VideoProcessor,
        rtc_configuration={ # Add this line
            "iceServers": [{
                "url": "stun:stun2.l.google.com:19302"
            }]
        })