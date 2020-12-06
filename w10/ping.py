if __name__ == "__main__":
    import os
    import threading

    def ping(host):
        print(host)
        print()
        ping_out = os.popen("ping " + host, "r")  # bufsize = 10 bytes
        while True:
            line = ping_out.readline()
            if not line:
                break
            print(line)

    servers = ["google.com",  "instagram.com", "vk.com"]

    threads = [threading.Thread(target = ping, args = (ip,)) for ip in servers]

    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
