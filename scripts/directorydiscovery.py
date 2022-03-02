#/usr/bin/python
# Written By: Sahar Hathiramani
# Date: 01/24/2021

import requests
import os
os.system("clear")
print("🄱🄰🄳 🄱🄾🅈 🄱🅄🅃 🄰 🅂🄰🄳 🄱🄾🅈")


def request(url):
    try:
        return requests.get("http://" + url)
    except requests.exceptions.ConnectionError:
        pass

targetURL = input("Enter Target URL: ")
file = open("common.txt", "r")
for line in file:
    line = line.strip('\n')
    fullURL = targetURL + "/" + line
    response = request(fullURL)
    if response:
        print('[+] Discovered Directory at Link: ' + fullURL)

n = str(input("Enter y to return back:"))
if n=="y":
  os.system("clear")
