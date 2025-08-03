import requests 
import time 
import threading 

done = False

def work():
    while not done:
        count = 0
        threading.Thread(target= work).start()
        count += 0
        print(f"counting {count}")
work()