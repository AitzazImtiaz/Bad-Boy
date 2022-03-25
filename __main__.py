# Copyright ©️ Aitzaz Imtiaz
# Without Royalty, use MIT license to do anything here
# Do not delete this text from the file if you publish it anywhere
from colorama import Fore
import os
import time
os.system("clear")
infinity = 1
while infinity == 1:
  print(Fore.RED+"""
 /$$$$$$$   /$$$$$$  /$$$$$$$        /$$$$$$$                     
| $$__  $$ /$$__  $$| $$__  $$      | $$__  $$                    
| $$  \ $$| $$  \ $$| $$  \ $$      | $$  \ $$  /$$$$$$  /$$   /$$
| $$$$$$$ | $$$$$$$$| $$  | $$      | $$$$$$$  /$$__  $$| $$  | $$
| $$__  $$| $$__  $$| $$  | $$      | $$__  $$| $$  \ $$| $$  | $$
| $$  \ $$| $$  | $$| $$  | $$      | $$  \ $$| $$  | $$| $$  | $$
| $$$$$$$/| $$  | $$| $$$$$$$/      | $$$$$$$/|  $$$$$$/|  $$$$$$$
|_______/ |__/  |__/|_______/       |_______/  \______/  \____  $$
                                                         /$$  | $$
                                                        |  $$$$$$/
                                                         \______/ """)
  print(Fore.BLUE+"Designed by Aitzaz Imtiaz")
  print(Fore.WHITE+"A little sad but a Bad Boy")
  print(Fore.RED+"Bad Boy Framework + Bad Boy = System Crash")
  print("I am sort of bad and your friend until  you go jail. Use ethically or you become evil boy!")
  print("")
  print(Fore.YELLOW+"Options to Choose:")
  print(Fore.BLUE+"1)MAC Sniffer")
  print(Fore.YELLOW+"2)Syn Flooder")
  print(Fore.WHITE+"3)Text Hasher")
  print(Fore.YELLOW+"4)SHA1Hash Decoder(Brute Force)")
  print(Fore.CYAN+"5)Port Scanner")
  print(Fore.WHITE+"6)FTP Anonymous Login")
  print(Fore.MAGENTA+"7)SSH Login")
  print(Fore.GREEN+"8)Website Secret Directories")
  print(Fore.WHITE+"9)About me")
  option=int(input("Enter Your Option:"))
  if option==1:
    os.system("python3 scripts/macsniffer.py")
  elif option==2:
    os.system("python3 scripts/synflooder.py")
  elif option==3:
    os.system("python3 scripts/hasher.py")
  elif option==4:
    os.system("python3 scripts/sha1hash.py")
  elif option==5:
    os.system("python3 scripts/portscan.py")
  elif option==6:
    os.system("python3 scripts/ftpanonymouslogin.py")
  elif option==7:
    os.system("python3 scripts/sshlogin.py")
  elif option==8:
    os.system("python3 scripts/directorydiscovery.py")
  elif option==9:
    os.system("python3 scripts/aboutme.py")
  else:
    print(Fore.RED+"You think Bad Boy is dumb?")
    time.sleep(10)
    os.system("clear")                                                                
                                                                  
