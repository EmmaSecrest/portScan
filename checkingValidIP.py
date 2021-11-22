import ipaddress as ip
import os
def pingME():
    try:
        ipAdd = ip.ip_address(input("Please enter an ip address: "))
        ipToTest = str(ipAdd)
        response = os.system('ping -n 1 ' + ipToTest)
        if response == 0:
            return True

        else:
            return False

    except ValueError:
        print("Something went wrong.Sorry")


