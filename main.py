# This will be where I run the entire python code
import time
from datetime import date
from checkingValidIP import pingME
dateOfScan = date.today()
startTime = time.time()
pingME()
print("scan completed in %s seconds" % (time.time() - startTime) , end = ' ' )
print("on", dateOfScan)

