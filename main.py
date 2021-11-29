# This will be where I run the entire python code
import time
from datetime import date
from checkingValidIP import pingME
from portScan import scanSystem
import ipaddress as ip

results = open('results.txt', 'a')
dateOfScan = date.today()
startTime = time.time()
try:
    ipAdd = ip.ip_address(input("Please enter an ip address: "))

    if pingME(ipAdd) == True :
        scanSystem(ipAdd)
    else:
        results.write("Scan could not be completed")
except:
    pass

results.write("Scan completed in %s seconds" % (time.time() - startTime)  )
results.write("on " + dateOfScan)

# I know ports 53,80,111,and 443 are open