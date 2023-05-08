import socket
import requests

hostname=input("\r\nEnter the hostname to create a socket: ")
port=80

def create_socket(hostname):
    mysocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    print("[+] Trying to connect with the host")
    mysocket.connect((hostname,port))
    print("[+] Connected with the host")
    data="GET / HTTP/1.1\r\nHost: {}\r\n\r\n".format(hostname)
    print("[+] Sending data\r\n"+data)
    mysocket.send(data.encode())
    response=mysocket.recv(4096)
    print("{}\r\n".format(response))
    return response
response=create_socket(hostname)


def redirection(response):
    if (b'301') in response:
        redirect=input("Redirection Found! \r\n\r\nDo you want to redirect? (Y/N): " )
        if redirect.lower() == "y":
            print("\r\n[+] Your redirect request will be sent\r\n")
        elif redirect.lower() == "n":
            print("\r\n[+] Closing the socket\r\n")
        else:
            print("\r\n[!] Enter a valid response\r\n")
redirection(response)