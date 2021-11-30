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
    results.write('\nThe IP address is either invalid or not responding')

results.write("\nScan completed in %s seconds" % (time.time() - startTime)  )
results.write(f"\non {dateOfScan}" )
print('Scan is complete. Please open result.txt to see what occured')
