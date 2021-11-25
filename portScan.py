import socket
# now just need to change open port print to write to a file
def scanMe(ip,port):

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        s.connect((str(ip), port))
        return True
    except (TimeoutError, ConnectionRefusedError,OSError):
        return False
    except KeyboardInterrupt:
        print("Scan has been stopped")



def scanSystem(ip):

    for port in range(1, 1025):
        print(port)
        if scanMe(ip ,port)== True:
           print(f" {port} is open ")
        else:
            continue




 #I know ports 53 80 111 and 443 are open