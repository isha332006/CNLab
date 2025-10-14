import random
import time

total_frames=int(input("Enter total number of frames to send: "))
loss_prob=float(input("Enter frame loss probability (0 to 1): "))
timeout=int(input("Enter timeout interval in seconds: "))

for frame in range(total_frames):
    sent=False
    while not sent:
        print(f"Sending Frame {frame}")
        if random.random()<loss_prob:
            print(f"Frame {frame} lost. Waiting for timeout...")
            time.sleep(timeout)
            print(f"Retransmitting Frame {frame}...")
        else:
            print(f"ACK {frame} received")
            sent=True

