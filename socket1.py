import socket
import http.client
from typing import Counter

def getWebData():
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect(('data.pr4e.org', 80))
    cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
    mysock.send(cmd)
    count = 0
    while True:
        data = mysock.recv(512)
        if len(data) < 1:
            break
        data_string = data.decode()
        data_lines = data_string.splitlines()
        #count = count + 1
        print(data.decode(),end='')
        #print(data_string)
        #print(data_lines)

    mysock.close()
    
    """
    conn = http.client.HTTPConnection("data.pr4e.org", 80)
    conn.request("GET", "/intro-short.txt")
    reply1 = conn.getresponse()
    header_dict = reply1.getheaders()
    print ('Why should you learn to write programs?')
    """
getWebData()