import socket
import cv2
import numpy as np
import time

# Configuration
IP = 'localhost'         
PORT=5001              # Port to send to
CHUNK_SIZE=4096        

# Create UDP socket
sock=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Open video file
cap=cv2.VideoCapture(r"C:\Users\HP\Downloads\Lab4\video.mp4")  

if not cap.isOpened():
    print("Error: Unable to open video file")
    exit()

FPS=cap.get(cv2.CAP_PROP_FPS)
frame_interval=1.0/FPS if FPS else 0.04   # Use default if unable to read FPS

while cap.isOpened():
    ret,frame=cap.read()
    if not ret:
        break
    # (a) Resize frame (optional for lower bandwidth)
    frame=cv2.resize(frame, (640, 480))
    # (b) Encode frame as JPG
    encoded,buffer=cv2.imencode('.jpg', frame)
    byte_data=buffer.tobytes()
    # (c) Split frame into chunks and send each with marker bit
    for i in range(0, len(byte_data), CHUNK_SIZE):
        chunk=byte_data[i:i+CHUNK_SIZE]
        marker=1 if i + CHUNK_SIZE>=len(byte_data) else 0
        # Header: first byte is marker (1=last, 0=not last)
        data=marker.to_bytes(1,'big')+chunk
        sock.sendto(data,(IP, PORT))
    # (d) Sleep to maintain frame rate
    time.sleep(frame_interval)

cap.release()
sock.close()
print("Video streaming complete.")
