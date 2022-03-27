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
d8888b.  .d8b.  d8888b. d8888b.  .d88b.  db    db 
88  `8D d8' `8b 88  `8D 88  `8D .8P  Y8. `8b  d8' 
88oooY' 88ooo88 88   88 88oooY' 88    88  `8bd8'  
88~~~b. 88~~~88 88   88 88~~~b. 88    88    88    
88   8D 88   88 88  .8D 88   8D `8b  d8'    88    
Y8888P' YP   YP Y8888D' Y8888P'  `Y88P'     YP    
""")
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
  print (Fore.MAGENTA+"10)Quit")
  option=int(input("Enter Your Option:"))
  if option==1:
    os.system("python3 badboy/scripts/macsniffer.py")
  elif option==2:
    os.system("python3 badboy/scripts/synflooder.py")
  elif option==3:
    os.system("python3 badboy/scripts/hasher.py")
  elif option==4:
    os.system("python3 badboy/scripts/sha1hash.py")
  elif option==5:
    os.system("python3 badboy/scripts/portscan.py")
  elif option==6:
    os.system("python3 badboy/scripts/ftpanonymouslogin.py")
  elif option==7:
    os.system("python3 badboy/scripts/sshlogin.py")
  elif option==8:
    os.system("python3 badboy/scripts/directorydiscovery.py")
  elif option==9:
    os.system("python3 badboy/scripts/aboutme.py")
  elif option=='10':
    exit()
  else:
    print(Fore.RED+"You think Bad Boy is dumb?")
    time.sleep(5)
    os.system("clear")
                                                                  
                                                                  
