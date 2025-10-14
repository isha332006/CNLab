import random

total_frames=int(input("Enter total number of frames to send: "))
window_size=int(input("Enter window size N: "))
loss_prob=float(input("Enter frame loss probability (0 to 1): "))

next_frame=0
ack=0

while ack<total_frames:
    window_end=min(next_frame+window_size,total_frames)
    print(f"Sending frames {next_frame} to {window_end-1}")
    loss_occurred=False
    for i in range(next_frame,window_end):
        if random.random()<loss_prob:
            print(f"Frame {i} lost. Retransmitting from {i}...")
            next_frame=i
            loss_occurred=True
            break
        else:
            print(f"ACK {i} received")
            ack=i+1

    if not loss_occurred:
        next_frame=ack
