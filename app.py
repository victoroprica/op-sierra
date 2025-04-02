import av
import cv2
import streamlit as st
from streamlit_webrtc import webrtc_streamer, VideoProcessorBase, RTCConfiguration

st.title("📷 Live Webcam Feed with OpenCV")

class VideoProcessor(VideoProcessorBase):
    def recv(self, frame):
        img = frame.to_ndarray(format="bgr24")

        return av.VideoFrame.from_ndarray(img, format="bgr24")

rtc_configuration = RTCConfiguration(
    {"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]}
)

webrtc_streamer(
    key="webcam",
    video_processor_factory=VideoProcessor,
    rtc_configuration=rtc_configuration
)
