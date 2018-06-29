import time
from datetime import datetime as dt
#About Host file: Host file contains the mappings of IP addresses to host names. Each
# entry should be kept on an individual line. The IP address should
# be placed in the first column followed by the corresponding host name.
# The IP address and the host name should be separated by at least one
# space.
#This Script modifies the host file by adding local host along with the websites to the
#host file between the working hours and it removes those websites if the current time doesn't lie
#in between the working hours as per user requirements
localhost="127.0.0.1"
hosts_path=r"C:\Windows\System32\drivers\etc\hosts" #host_file location
block_list=["www.facebook.com","www.instagram.com"]   #Website list to Block, Just add to it the site you want to block
while True:

    if dt(dt.now().year,dt.now().month,dt.now().day,9)< dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,17): #dt(year,month,day,hour) Change the hour as per your choice
         #if current time is between my working Hours, just block the list of sites contained in block_list
         with open(hosts_path,'r+') as file:
             content=file.read()
             for websites in block_list:
                 if websites not in content:
                     file.write(localhost+" " +websites + "\n")
    else:
        #Free or fun hours

        with open(hosts_path,'r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in block_list):
                    file.write(line)
            file.truncate()



    time.sleep(5)
