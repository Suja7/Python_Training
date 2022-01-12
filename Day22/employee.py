class Emp:
	raise_amount=1.04
	def __init__(self,first,last,pay):
		self.first=first
		self.last=last
		self.pay=int(pay)
	@property	
	def email(self):
		return f"{self.first}.{self.last}@company.com"
	@property		
	def fullname(self):
	    return f"{self.first} {self.last}"
	def apply_raise(self):
	    self.pay=int(self.pay*self.raise_amount)
	      


emp1=Emp('John','K',50000)
emp2=Emp('Jane','M',60000)

print(emp1.email)



