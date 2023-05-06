import math
#from datetime 
import datetime

powerPi = pow(math.pi,2)
squareRoot = math.sqrt(powerPi)

i = 0
timeBefore = datetime.datetime.now()
while i < 10000:
    dowerPi = pow(squareRoot+i,2)
    squareRoot = math.sqrt(powerPi)
    print(i, powerPi, squareRoot)
    i +=1


timeAfter = datetime.datetime.now()

print(timeAfter - timeBefore)
timeAfter
print(timeAfter - timeBefore)

