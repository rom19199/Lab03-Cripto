
from random import randint
import random

def WichmanHill(a,b):
    seed1 = randint(1, 30000)
    seed2 = randint(1, 30000)
    seed3 = randint(1, 30000)
    
    l = ''
    
    for i in range(b):
        seed1 = (171 * seed1) % 30269
        seed2 = (172 * seed2) % 30307
        seed3 = (170 * seed3) % 30323
        
        resp = ((float(seed1)/30269 + float(seed2)/30307 + float(seed3)/30323) % 1)
        l += str(round(resp))
        
    return (l)
                 