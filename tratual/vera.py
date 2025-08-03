import requests
import json
import socket
import threading
import os
from urllib.parse import urljoin
from bs4 import BeautifulSoup  # Import BeautifulSoup

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

def banner():
    print(71 * f"{Colors.RED}*{Colors.RESET}")
    print(f"""{Colors.BOLD}{Colors.BRIGHT_RED}
 ______  ____    ____  ______  __ __   ____  _
|      ||    \  /    ||      ||  |  | /    || |
|      ||  D  )|  o  ||      ||  |  ||  o  || |
||  |||    / |     |||  |||  |  ||     || |___
  |  |  |    \ |  _  |  |  |  |  :  ||  _  ||     |
  |  |  |  .  \|  |  |  |  |  |     ||  |  ||     |
  ||  ||\||||  ||   \,|||||_|
                AUTHOR:GHOST
           TEAM:NETHUNTERS
         \nTHANK YOU FOR INSTALLING, PLEASE USE FOR EDUCATIONAL PURPOSE ONLY!\n
      {Colors.RESET}""")

def menu():
    print(71 * f"{Colors.RED}-{Colors.RESET}")
    print(f"{Colors.RED}\n<<<<MENU>>>>\n{Colors.RESET}")
    print(71 * f"{Colors.RED}-{Colors.RESET}")

    print(f"{Colors.BOLD}{Colors.BRIGHT_BLUE}[1] port scanner {Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.BRIGHT_BLUE}[2] web scraping{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.BRIGHT_BLUE}[3] IP Resolution{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.BRIGHT_BLUE}[4] DDOS attack{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.BRIGHT_BLUE}[5] ABOUT NETHUNTERS{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.BRIGHT_BLUE}[6] ABOUT TOOL!{Colors.RESET}")

def clear_screen():
    os.system('clear')

def go_again():
    while True:
        go_again = input("Exit/continue [e/c]: ")
        if go_again.lower() == "c":
            return True
        elif go_again.lower() == "e":
            return False
        else:
            print("Invalid input")

def port_scanner():
    print(71 * f"{Colors.RED}*{Colors.RESET}")
    print(f"{Colors.GREEN}PORT SCANNER\n{Colors.RESET}")
    print(71 * f"{Colors.RED}*{Colors.RESET}")
    target_ip = input(f"{Colors.BLUE}Enter target ip: {Colors.RESET} ")
    # Display menu
    print(f"{Colors.BLUE}[OPTIONS]\n{Colors.RESET}")
    print(f"{Colors.YELLOW}1. SCAN CUSTOM PORTS")
    print(f"{Colors.YELLOW}2. SCAN DEFAULT PORT{Colors.RESET}")
    print(f"{Colors.YELLOW}3. SCAN RANGE OF PORT{Colors.RESET}")
    print(f"{Colors.YELLOW}4. RETURN TO MAIN MENU\n{Colors.RESET}")

    sub_menu = f"{Colors.RED}PORT SCANNER{Colors.RESET}"
    cmd = int(input(f"[{sub_menu}]/> "))

    if cmd == 1:
        host =int(input("[+] INPUT TARGET IP: "))
        port = int(input("[+] ENTER PORT YOU WANT TO SCAN: "))
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(6)
            if s.connect_ex((host, port)) == 0:
                print(f"[!] Scanning port {port}")
                print(f"{port} is open")
            else:
                print(f"{port} is closed")
    elif cmd == 2:
        # Implement default port scanning logic here
        pass
    elif cmd == 3:
        # Implement range port scanning logic here
        pass
    elif cmd == 4:
        return
    else:
        print("Invalid option")

def web_scrapping():
    print(71 * f"{Colors.RED}*{Colors.RESET}")
    print(f"{Colors.BLUE}[OPTION]\n{Colors.RESET}")
    print(f"{Colors.YELLOW}1. scrap all links{Colors.RESET}")
    print(f"{Colors.YELLOW}2. scrap with user agent{Colors.RESET}")
    print(f"{Colors.YELLOW}3. Advance scrap{Colors.RESET}")
    print(f"{Colors.YELLOW}4. exit\n {Colors.RESET}")
    
    sub_menu = f"{Colors.RED}WEB_SCRAPPER{Colors.RESET}"
    cmd = input(f"[{sub_menu}]/>")
    
    if cmd == "1":
        host = input("Enter url target: ")
        try:
            response = requests.get(host)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, "html5lib")
            links = soup.find_all("a")
            for link in links:
                href = link.get("href")
                if href is not None:
                    print(href)
        except requests.exceptions.RequestException as e:
            print('Invalid URL or network error:', e)
    
    elif cmd == 2:
        url = input("Enter url of target: ")
        try:
            # Adding a User-Agent header to mimic a real browser request
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
            
            response = requests.get(url, headers=headers)
            response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
            
            soup = BeautifulSoup(response.text, 'html5lib')
            links = soup.find_all('a')
            
            for link in links:
                href = link.get('href')
                if href is not None:
                    # Convert relative URLs to absolute URLs
                    full_url = urljoin(url, href)
                    print(full_url)
                    
        except requests.exceptions.RequestException as e:
            print('Invalid URL or network error:', e)
def ip_resoluton():
    (f"{Colors.BRIGHT_YELLOW}#####\n Welcome to ip resolution #####\n{Colors.RESET}")
    print(f"{Colors.BRIGHT_GREEN}1. get ip address of TARGET Site{Colors.RESET}")
    print(f"{Colors.BRIGHT_GREEN}2. get info about target ip address {Colors.BRIGHT_GREEN}")
    print(f"{Colors.BRIGHT_GREEN}3. quit from section tool\n{Colors.BRIGHT_GREEN}")
    
    sub_menu=f"{Colors.BRIGHT_GREEN}ip resolution{Colors.RESET}"


    cmd=input(f"[{sub_menu}]/> ")
    if cmd == "1":

        try:
            url=input("Enter target domain: ")
            ip=socket.gethostbyname(url)
        except:
            print(f"{url}faild to resolve ")

    elif cmd == "2":
        
             
         

        print(f"{Colors.BRIGHT_RED}#### welcome to ip info ####\n{Colors.RESET}")
        
        print(60*"_")
        print(f"{Colors.BRIGHT_MAGENTA}{Colors.BOLD}##### WELCOME TO WEB INFO, GETTING A TARGET IP INFO #####{Colors.RESET}")

        ip_address = input(f"{Colors.BRIGHT_RED}{Colors.BOLD} INPUT YOUR TARGET IP: {Colors.RESET}")

        url = f"https://ipinfo.io/{ip_address}/json"
        response = requests.get(url)
        response.raise_for_status()  # Raises an HTTPError for bad responses (4xx and 5xx)
    
        data = response.json()
        print(f"{Colors.  BRIGHT_YELLOW }_{Colors.RESET}")
    
        print(f"IP Address: {data['ip']}")
    
        print(f"City: {data['city']}")
    
        print(f"Region: {data['region']}")
    
        print(f"Country: {data['country']}")
    
        print(f"Location: {data['loc']}")
    
        print(f"Organization: {data['org']}")
    
        print(f"Postal: {data['postal']}")
    
        print(f"Timezone: {data['timezone']}")
   
        print(f"ZIP: {data['zip']}")
    
        print(f"STATUS: {data['status']}")
    
        print(f"PROXY: {data['proxy']}")

    elif cmd == "3":
        menu()
    




    


def main():

    banner()
    while True:
        menu()
        choice = input(f"{Colors.BLUE}Enter your choice: {Colors.RESET}")
        if choice == "1":
            port_scanner()
        elif choice == "2":
            web_scrapping()
        elif choice == "3":
            ip_resoluton()
             
            pass
        elif choice == "4":
            # ddos()
            pass
        elif choice == "5":
            # Implement about NETHUNTERS logic here
            pass
        elif choice == "6":
            # Implement about tool logic here
            pass
        else:
            print("Invalid choice")

        if not go_again():
            break

if __name__ == "__main__":
    main()