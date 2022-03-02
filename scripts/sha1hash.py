#!/usr/bin/python
# Written By: Sahar Hathiramani
# Date: 01/13/2021
import os
import urllib.request
import hashlib
from colorama import Fore
os.system("clear")
print("🄱🄰🄳 🄱🄾🅈 🄱🅄🅃 🄰 🅂🄰🄳 🄱🄾🅈")


sha1hash = input('[*] Enter SHA1 Hash: ')

passwordList = str(urllib.request.urlopen('https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-10000.txt').read(), 'UTF-8')

for password in passwordList.split('\n'):
    hashGuess = hashlib.sha1(bytes(password, 'UTF-8')).hexdigest()
    if hashGuess == sha1hash:
        print(Fore.GREEN + "[+] Password Found: " + str(password))
        quit()
    else:
        print(Fore.RED + '[-] Password not found. Trying next password...')
        pass

print("Password Not Found in Password List")
n = str(input("Enter y to return back:"))
if n=="y":
  os.system("clear")
