# This will be where I run the entire python code
import time
from datetime import date
from checkingValidIP import pingME
from portScan import scanSystem
import ipaddress as ip

dateOfScan = date.today()
startTime = time.time()
ipAdd = ip.ip_address(input("Please enter an ip address: "))

if pingME(ipAdd) == True :
     scanSystem(ipAdd)
else:
    print("Scan could not be completed")

print("scan completed in %s seconds" % (time.time() - startTime) , end = ' ' )
print("on", dateOfScan)

# I know ports 53,80,111,and 443 are open