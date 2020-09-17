from customer import Customer
class ATMCard1(Customer):
	def __init__(self, id, defaultPin = 1234, defaultBalance = 10000):
		super().__init__(id, defaultPin, defaultBalance)

class ATMCard2(Customer):
	def __init__(self, id, defaultPin = 123321, defaultBalance = 5000000):
		super().__init__(id, defaultPin, defaultBalance)