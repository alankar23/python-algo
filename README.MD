# This repo contains Python Algos and Problems.

## OOPS
    class Car:
        def __init__(self, name, make,color):
            self.name = name
            self.make = make
            self.color = color
        
        def descp(self):
            print(f"Car Details are \n Model: {self.name}\n Year: {self.make}\n Color:{self.color}")



    myCar = Car("ciaz","2015","red")

    myCar.descp()
    print(myCar)

OUTPUT

    Car Details are 
    Model: ciaz
    Year: 2015
    Color:red

## Fibonacci Series

    def fibb(n):
        n1,n2 =0,1
        sum=0
        series = []
        for x in range(n):
            if x == 0:
                series.append(x)
            else:
                n1,n2 = n2 , sum
                sum = n1+n2
                series.append(sum)

        return print(series)

    fibb(10)

OUTPUT 

    [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

## Bubble Sort


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

OUTPUT

    [3, 26, 60, 62, 65, 70, 79, 80, 97, 97]