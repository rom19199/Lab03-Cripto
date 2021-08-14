import random as ran

def randomNumber():
    num = randint(0, 1)
    return num   

def lfsr(semillas, taps, k):
    res = semillas
    sr, xor = semillas, 0
    while len(res) < k:
        for x in taps:
            xor += int(sr[x-1])
        xor = 0 if xor %2 == 0.0 else 1
        sr, xor = str(xor) + sr[:-1], 0
        res += sr
    return res