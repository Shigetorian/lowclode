import random
import time 
import os
u = 5515
types = ['cs','py','js','kt','html','css','vbs','php']
while True:
    u+=1
    i = random.randint(0,7)
    r = open('files/'+str(u)+'.'+str(types[i]),mode = 'w')
    r.write(str(random.randint(13,666)))
    r.close()
    print(u)