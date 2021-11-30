import socket
results = open('results.txt', 'a')
def scanMe(ip,port):

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        s.connect((str(ip), port))
        return True
    except (TimeoutError, ConnectionRefusedError,OSError):
        return False
    except KeyboardInterrupt:
        results.write("Scan has been stopped")



def scanSystem(ip):
    startPort  = int(input("Starting port number: "))
    endPort = int(input("Ending port number: "))
    for port in range(startPort, endPort):
        print(port)
        if scanMe(ip ,port)== True:
            print(f"\n {port} is open")
            results.write(f"\n {port} is open ")








 #I know ports 53 80 and 443 are open