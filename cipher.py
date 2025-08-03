import os 
import requests
import socket 
from bs4 import BeautifulSoup
import time
import sys  
from urllib.parse import urljoin
class Colors:

    RESET = "\033[0m"
    # Bright Text Colors
    BRIGHT_BLACK = "\033[90m"
    BRIGHT_RED = "\033[91m"
    BRIGHT_GREEN = "\033[92m"
    BRIGHT_YELLOW = "\033[93m"
    BRIGHT_BLUE = "\033[94m"
    BRIGHT_MAGENTA = "\033[95m"
    BRIGHT_CYAN = "\033[96m"
    BRIGHT_WHITE = "\033[97m"
    # STYLE
    BOLD = "\033[1m"

    # Text colors
    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"





#funtion for my tools 
def banner():
    print(f"""{Colors.BRIGHT_RED}


                      __                              
                     /\ \                             
  ___   __  __  _____\ \ \___      __   _ __          
 /'___\/\ \/\ \/\ '__`\ \  _ `\  /'__`\/\`'__\        
/\ \__/\ \ \_\ \ \ \L\ \ \ \ \ \/\  __/\ \ \/         
\ \____\\/`____ \ \ ,__/\ \_\ \_\ \____\\ \_\         
 \/____/ `/___/> \ \ \/  \/_/\/_/\/____/ \/_/         
            /\___/\ \_\                               
            \/__/  \/_/                               

          created by </XENOPHOBIC-X> 



{Colors.RESET}""") 
def clear_screen():
    os.system("clear")
#user agent will be inputed here 

def attack_menu():
    clear_screen()
    banner()
    print(f"{Colors.BLUE}\n[1] subdomain scanner{Colors.RESET}")
    print(F"{Colors.BLUE}\n[2] ip resolution{Colors.RESET}")
    print(f"{Colors.BLUE}\n[3]portscanner{Colors.RESET}")
    print(f"{Colors.BLUE}\n[4]webcrawler{Colors.RESET}")
    print(f"{Colors.BLUE}\n[0]EXIT FROM TOOL......{Colors.RESET}")
def subdomain_banner():
    print(f"""{Colors.BRIGHT_BLUE}



 
            ___.                                                    
  ________ _\_ |__   ______ ____ _____    ____   ____   ___________ 
 /  ___/  |  \ __ \ /  ___// _____  \  /    \ /    \_/ __ \_  __ 
 \___ \|  |  / \_\ \___ \  \___ / __ \|   |  \   |  \  ___/|  | \/
/____  >____/|___  /____  >\___  >____  /___|  /___|  /\___  >__|   
     \/          \/     \/     \/     \/     \/     \/     \/       





{Colors.RESET}""")
def subdomain():

    subdomain_banner()
    print(f"{Colors.BRIGHT_GREEN}[!]welcome to subdomian_scanner\n{Colors.RESET}")
    print(60*'-')
    print("\toptions")
    print(60*'-')
    print(f"{Colors.BRIGHT_YELLOW}[1]full scan{Colors.RESET}")
    print(f"{Colors.BRIGHT_YELLOW}[0]EXIT FROM TOOL\n{Colors.RESET}")
    fat=f"{Colors.BRIGHT_RED}[subdomain_scanner]>{Colors.RESET}"
    print(f"[!] input an option.....")
    time.sleep(0.5)
    print("....")
    time.sleep(0.5)
    print(".....")
    time.sleep(0.5)
    print("......")
    time.sleep(0.5)
    stats=input(f"{fat}")
    if stats=="1":
        host=input("enter url target: ")
        headers={
            'useragent':'mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36'}
            
        try:
           

           response= requests.get(host, headers=headers)
           response.raise_for_status()
           soup= BeautifulSoup(response.text, 'html5lib')
           links = soup.find_all('a')
           for links in links:

            href = links.get('href')
            if href is not None:
                full = urljoin(host, href)
                print(full)
        except requests.exceptions.RequestException as e:
            print(f"{Colors.BRIGHT_RED}invaild url {Colors.RESET}")

        pass

    elif stats=="0":
        attack_menu()
    else:
        print(f"{Colors.BRIGHT_MAGENTA}invaild input{Colors.RESET}")

 
def ip_banner():
    pass
def ip_resolution():
    
    ip_banner()
    
    print("\toption")
    print("1 get ip address of your target")
    
    print("2 get info about ipaddress")
    print("0 exit from the back to main meanu\n")
    
    suboption=f"{Colors.BLUE}(ip resolution){Colors.RESET}"
    print("please enter an option\n")
    cmd=input(f"{suboption}")
    
    if cmd=="1":
        
        try:
            url= input("enter target domain: ")
            ip = socket.gethostbyname(url)
            print(f"{Colors.BRIGHT_MAGENTA} ipaddress for {url}: {ip}{Colors.RESET}")
        except socket.gaierror as e:
            print(f"failed to resolve {url}: {e}") 

    elif cmd=="2":
    

    
        
        print(f"{Colors.BRIGHT_GREEN}###### WELCOME TO IPADDRESS OSINT #####\t{Colors.RESET}")
        print(90*"-")
        
        ip_info=input(f"{Colors.BRIGHT_BLUE}enter your target ipaddress: {Colors.RESET}")
        
        API=f"https://ipinfo.io/{ip_info}/json"
        try:
            RESPONSE = requests.get(API)
            RESPONSE.raise_for_status() 
            data = RESPONSE.json()
            time.sleep(0.8)
            print("processing..........")
            time.sleep(0.6)
            
            print(f"ip address: {data['ip']}")
            print(f"city: {data['city']}")
            print(f"Region: {data['region']}")
            print(f"Country: {data['country']}")
            print(f"Location: {data['loc']}")
            print(f"Organizatoion: {data['org']}")
            
           #print(f"Timezone: {data['timezone']}")
            #print(f"status: {data[('status', 'N/A')]}")
            #print(f"postal: {data['postal']}")

        except requests.exceptions.RequestException as e:
            print(f"errors fetching ip info: {e}")
    elif cmd=="0":
        attack_menu()



def port_scanner():
    clear_screen()
    banner()
    host=input("enter domain of your host: ")
    port=int(input("enter port you want to scan: "))
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(6)
        if s.connect_ex((host, int(port)))==0:
            print(f"port: {port} is open")
        else:
            print(f"port: {port} is closed")

    
    time.sleep(10)
    print("exiting to main meanu")
    attack_menu()
    


        

           


def main():
    
    attack_menu()
    while True:
        chioce=input(f"{Colors.BRIGHT_GREEN}enter your command tool [cipher]:{Colors.RESET} ")
        if chioce=="1":
            subdomain()
        elif chioce=="2":
            ip_resolution()
        elif chioce=="3":
            port_scanner()
        elif chioce=="0":
            exit()
            break
        else:
            print("invaild....")   
if __name__=="__main__":
    main()