def owr(origlist):
    for i in range(len(origlist)//2):
        swap = origlist[i]
        origlist[i] = origlist[-i-1]
        origlist[-i-1] = swap
    return origlist
