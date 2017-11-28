''' 
This application writes to the hosts file and blocks a user from being able to access sites which are listed
in the website_list section during normal business hours. 
'''

import time
from datetime import datetime as dt

'''This is the host_path used for a mac computer
   For a Windows computer change the hosts_path to:
   hosts_path =r"C:\Windows\System32\drivers\etc\hosts" 

'''
hosts_path="/etc/hosts"
redirect="127.0.0.1"
website_list=["www.facebook.com","facebook.com","www.twitter.com","twitter.com"]

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,16):
        print("Working hours...")
        with open(hosts_path,'r+') as file:
            content=file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+ website+"\n")
    else:	
        print("Fun hours...")
    time.sleep(5)
