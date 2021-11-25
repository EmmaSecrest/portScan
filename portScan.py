import socket

def scanMe(port,ip):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:

        s.connect(ip,port)
        return True
    except:
        return False
    else:
        return True

def scanSystem(ip):
  # not printing anything
  for port in range(1, 1025):
      if scanMe(port,ip):
          print(f" {port} is open ")
      else:
         pass


