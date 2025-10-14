import matplotlib.pyplot as plt
import random

rounds=int(input("Enter number of transmission rounds: "))
start_cwnd=int(input("Enter initial congestion window (cwnd): "))
start_ssthresh=int(input("Enter initial slow start threshold (ssthresh): "))
loss_prob=float(input("Enter packet loss probability (0 to 1): "))

cwnd=start_cwnd
ssthresh=start_ssthresh
cwnd_values=[]

for i in range(rounds):
    cwnd_values.append(cwnd)
    if random.random()<loss_prob:
        print(f"Packet loss in round{i + 1}. Timeout triggered.")
        ssthresh=max(cwnd//2,1)
        cwnd=start_cwnd
    else:
        if cwnd<ssthresh:
            cwnd*=2  # Slow Start
        else:
            cwnd+=1  # Congestion Avoidance

plt.plot(range(1,rounds+1),cwnd_values,marker='o')
plt.title('TCP Congestion Control Simulation')
plt.xlabel('Transmission Rounds')
plt.ylabel('cwnd (in segments)')
plt.grid()
plt.show()
