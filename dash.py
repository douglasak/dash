#!/usr/bin/env python

from config import ip_addr, mac_addr
import requests
from scapy.all import *

def toggle_light():
	requests.get("http://"+ip_addr+":8080/CMD?MBR_Lamp=TOGGLE")

def arp_display(pkt):
	if ARP in pkt and pkt[ARP].op in (1,2):
		print("ARP Probe from: " + pkt[ARP].hwsrc + "/" + pkt[ARP].psrc)
		if pkt[ARP].hwsrc == mac_addr and pkt[ARP].psrc == "0.0.0.0":
			toggle_light()

sniff(prn=arp_display, filter="arp", store=0)
