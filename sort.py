
import random

hello = [random.randint(1,100) for x in range(10)]
print(hello)

def bubble(lest):
    length = len(lest)-1
    sorted = False

    while not sorted:
        sorted = True
        for x in range(0,length):
            if lest[x] > lest[x+1]:
                lest[x], lest[x+1] = lest[x+1], lest[x]
                sorted=False
    return print(lest)


bubble(hello)
