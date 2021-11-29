
import os

results = open('results.txt', 'w')
def pingME(ipAdd):
    try:
        ipToTest = str(ipAdd)
        response = os.system('ping -n 1 ' + ipToTest)
        if response == 0:
          return True
        else:
            return False

    except ValueError:
        results.write("Something went wrong.Sorry")

