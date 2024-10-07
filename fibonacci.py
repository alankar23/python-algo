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