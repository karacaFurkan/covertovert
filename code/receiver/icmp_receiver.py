from scapy.all import *

def receivePacket():
    sniff(filter="icmp", prn=lambda x: x.show() if (x.ttl == 1 and x[ICMP].type == 8) else exit())

if __name__=="__main__":
    receivePacket()
# Implement your ICMP receiver here
