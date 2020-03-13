import time
from datetime import datetime as dt

hosts_file = open("C:\Windows\System32\drivers\etc\hosts")
redirects = "127.0.0.1"
website_list = [
    "www.facebook.com",
    "www.gmail.com",
    "www.hotmail.com",
    "www.twitter.com",
    "www.instagram.com",
]

while True:
    file = open(hosts_file, "r+")
    content = file.read()
    now = dt.now()
    if dt(now.year, now.month, now.day, 8) < now < dt(now.year, now.month, now.day, 16):
        print("Work Hours...")
        for site in website_list:
            if site not in content:
                file.write(redirects + "\t" + site + "\n")
    else:
        content = file.readlines()
        file.seek(0)
        for line in content:
            if not any(site in line for site in website_list):
                file.write(line)
        file.truncate()
        print("Let the fun times begin!")
        break
    time.sleep(10)
