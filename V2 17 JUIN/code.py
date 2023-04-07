import scapy
from scapy.all import *

pck = IP()

pck.dst = "8.8.8.8"

pck.show()
send(pck,iface="Ethernet")



