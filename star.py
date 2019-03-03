import random
import time 
import os
u = 0
types = ['cs','py','js']
while True:
    u+=1
    i = random.randint(0,2)
    r = open('files/'+str(u)+'.'+str(types[i]),mode = 'w')
    r.write(str(random.randint(13,666)))
    r.close()
    print(u)