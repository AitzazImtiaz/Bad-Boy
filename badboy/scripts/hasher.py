#!/usr/bin/python
# Written By: Sahar Hathiramani
# Date: 01/13/2021
import os
import hashlib
os.system("clear")
print("π±π°π³ π±πΎπ π±ππ π° ππ°π³ π±πΎπ")

hashValue = input('Enter String to Hash: ')

hashmd5 = hashlib.md5()
hashmd5.update(hashValue.encode())
print('MD5 Hash: ' + hashmd5.hexdigest())

hashsha1 = hashlib.sha1();
hashsha1.update(hashValue.encode())
print('SHA1 Hash: ' + hashsha1.hexdigest())

hashsha224 = hashlib.sha224()
hashsha224.update(hashValue.encode())
print('SHA224 Hash: ' + hashsha224.hexdigest())

hashsha256 = hashlib.sha256()
hashsha256.update(hashValue.encode())
print('SHA256 Hash: ' + hashsha256.hexdigest())

hashsha512 = hashlib.sha512()
hashsha512.update(hashValue.encode())
print('SHA512 Hash: ' + hashsha512.hexdigest())
n = str(input("Enter y to return back:"))
if n=="y":
  os.system("clear")
