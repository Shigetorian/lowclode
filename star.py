import random
import time 
import os
u = 4287
types = ['cs','py','js']
while True:
    u+=1
    i = random.randint(0,2)
    open('files/'+str(u)+'.'+str(types[i]),mode = 'w')
    print(u)