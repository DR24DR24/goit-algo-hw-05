import random
import math



def bin_search(data,ref):
    left=0
    right=len(data)
    i=0
    while right-left>1:
        midle=(right+left)//2
        if ref<=data[midle]:
            right=midle
        else:
            left=midle
        i+=1
    return (right,i)

if __name__=="__main__":
    length=100
    data=[random.uniform(0,length) for _ in range(0,length)]
    data.sort()
    #print(data)
    print(f"length: {length}, value of step numbers: {math.log2(length)}, bin_search result: {bin_search(data,length//2)}")
