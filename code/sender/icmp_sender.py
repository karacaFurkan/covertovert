from scapy.all import *


def sendPackage(ip):
    send(IP(dst = ip, ttl = 1)/ICMP())


sendPackage("receiver")


# Implement your ICMP sender here
