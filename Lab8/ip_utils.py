def ip_to_binary(ip_address: str) -> str:
    octets = ip_address.split('.')
    binary_str = ''.join(f'{int(octet):08b}' for octet in octets)
    return binary_str

def get_network_prefix(ip_cidr: str) -> str:
    address, mask_length = ip_cidr.split('/')
    binary_ip = ip_to_binary(address)
    prefix = binary_ip[:int(mask_length)]
    return prefix

if __name__ == "__main__":
    print("Binary of 192.168.1.1:", ip_to_binary("192.168.1.1"))
    print("Network prefix of 200.23.16.0/23:", get_network_prefix("200.23.16.0/23"))