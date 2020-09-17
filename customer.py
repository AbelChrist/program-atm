class Customer:
	# deklarasi variabel awal id, pin, dan saldo
	def __init__(self, id, defaultPin, defaultBalance):
		self.defaultPin = defaultPin
		self.defaultBalance = defaultBalance
		self.id = id
		self.pin = defaultPin
		self.balance = defaultBalance

	# fungsi cek pin awal
	def cekPinAwal(self):
		return self.defaultPin

	# fungsi cek saldo awal
	def cekSaldoAwal(self):
		return self.defaultBalance

	def checkId(self):
		return self.id

	def checkPin(self):
		return self.pin

	def checkBalance(self):
		return self.balance

	def withdrawBalance(self, nominal):
		self.balance -= nominal

	def depositBalance(self, nominal):
		self.balance += nominal

	def changePin(self, newPin):
		self.pin = newPin
