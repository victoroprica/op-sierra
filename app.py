import av
import cv2
import streamlit as st
from streamlit_webrtc import webrtc_streamer, VideoTransformerBase

st.title("📷 Live Webcam Feed with OpenCV")

# Define a video transformer class
class VideoTransformer(VideoTransformerBase):
    def recv(self, frame):
        img = frame.to_ndarray(format="bgr24")  # Convert frame to numpy array
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Convert BGR to RGB
        return img  # Return the processed frame

# Initialize WebRTC streamer
webrtc_streamer(key="webcam", video_processor_factory=VideoTransformer)
