import scapy.all as scapy


def build_packet(ip, port):
    ip_layer = scapy.IP(dst=ip)
    tcp_layer = scapy.TCP(dport=port, flags="S", seq=1000)
    packet = ip_layer/tcp_layer
    return packet



























