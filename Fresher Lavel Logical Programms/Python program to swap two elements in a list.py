def swaplist(newlist):
    newlist[0],newlist[-2]=newlist[-2],newlist[0]
    return newlist
newlist=[23,65,19,90]
print(swaplist(newlist))