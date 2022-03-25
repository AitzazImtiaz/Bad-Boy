#!/usr/bin/python
# Written By: Sahar Hathiramani
# Date: 01/12/2021
import os
import ftplib
os.system("clear")
print("🄱🄰🄳 🄱🄾🅈 🄱🅄🅃 🄰 🅂🄰🄳 🄱🄾🅈")

def anonLogin(hostname):
    try:
        ftp = ftplib.FTP(hostname)
        ftp.login('anonymous', 'anonymous')
        print('[+] ' + hostname + ' FTP Anonymous Login Successfull')
        ftp.quit()
        return True
    except:
        print('[-] ' + hostname + ' FTP Anonymous Login Failed')
        return False

host = input("Enter IP Address to Target: ")
anonLogin(host)

n = str(input("Enter y to return back:"))
if n=="y":
  os.system("clear")
