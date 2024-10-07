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
