import socket
results = open('results.txt', 'w')
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

    for port in range(50, 81):
        print(port)
        if scanMe(ip ,port)== True:
           results.write(f"\n {port} is open ")
        else:
            continue





 #I know ports 53 80 and 443 are open