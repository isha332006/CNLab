class Packet:
    def __init__(self, source_ip, dest_ip, payload, priority):
        self.source_ip = source_ip
        self.dest_ip = dest_ip
        self.payload = payload
        self.priority = priority
def fifo_scheduler(packet_list: list) -> list:
    return packet_list
def priority_scheduler(packet_list: list) -> list:
    return sorted(packet_list, key=lambda pkt: pkt.priority)

if __name__ == "__main__":
    packets = [
        Packet('src1', 'dst1', 'Data Packet 1', 2),
        Packet('src2', 'dst2', 'Data Packet 2', 2),
        Packet('src3', 'dst3', 'VOIP Packet 1', 0),
        Packet('src4', 'dst4', 'Video Packet 1', 1),
        Packet('src5', 'dst5', 'VOIP Packet 2', 0)
    ]

    fifo_out = fifo_scheduler(packets)
    print([p.payload for p in fifo_out])

    priority_out = priority_scheduler(packets)
    print([p.payload for p in priority_out])
