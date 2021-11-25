
import os
def pingME(ipAdd):
    try:
        ipToTest = str(ipAdd)
        response = os.system('ping -n 1 ' + ipToTest)
        if response == 0:
          return True
        else:
            return False

    except ValueError:
        print("Something went wrong.Sorry")


