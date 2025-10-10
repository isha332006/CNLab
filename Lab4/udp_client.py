import socket
import cv2
import numpy as np

IP='localhost'   
PORT=5001        # Port to listen on
CHUNK_SIZE=4096

# Create UDP socket
sock=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((IP, PORT))

print("Client listening for video stream...")
while True:
    frame_data=b''
    while True:
        packet,_=sock.recvfrom(CHUNK_SIZE + 1)  # Plus 1 for marker
        marker=packet[0]
        chunk=packet[1:]
        frame_data+=chunk
        if marker==1:
            break
    np_data=np.frombuffer(frame_data, np.uint8)
    frame=cv2.imdecode(np_data, cv2.IMREAD_COLOR)
    if frame is not None:
        cv2.imshow('UDP Video Stream', frame)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

cv2.destroyAllWindows()
sock.close()

