''' 
This application writes to the hosts file and blocks a user from being able to access sites which are listed
in the website_list section during normal business hours or during the hours you decide.
'''

import time
from datetime import datetime as dt

'''This is the host_path used for a mac computer
   For a Windows computer change the hosts_path to:
   hosts_path =r"C:\Windows\System32\drivers\etc\hosts" 
'''
hosts_path="/etc/hosts"
redirect="127.0.0.1"
# Add the list of websites to this list that you want to block a user from accessing
website_list=["www.facebook.com","facebook.com","www.twitter.com","twitter.com"]

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,16):
        print("Normal Business Hours...")
        with open(hosts_path,'r+') as file:
            content=file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+ website+"\n")
    else:
        with open(hosts_path,'r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
        print("After Work Hours...")
    time.sleep(5)
