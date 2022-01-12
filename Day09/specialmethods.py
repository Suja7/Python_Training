class Emp:
	def __init__(self,first,last,pay):
		self.first=first
		self.last=last
		self.pay=pay
		self.email=f"{first},{last}@company.com"

	def fullname(self):
	    return f"{self.first} {self.last}"

	def __repr__(self):
		return f"Emp('{self.first}', '{self.last}','{self.pay}')"

	def __str__(self):
		return f"{self.fullname()} - {self.email}" #It replaces the _rpr_ method
		
	    

emp1=Emp('John','K',50000)
emp2=Emp('Jane','M',60000)

# print(emp1.fullname())#John K
# print(emp2.fullname())	#Jane M
# print(Emp.fullname(emp2))#Jane M    

print(emp1) #John K - John,K@company.com-->we have to define either __rpr__ or _str_ method
#otherwise it will throw error. IF we have both it will execute __str__ methos


#To access methods
print(emp1.__repr__()) #Emp('John', 'K','50000')
print(emp1.__str__())#John K - John,K@company.com
print(repr(emp1))#Emp('John', 'K','50000')
print(str(emp1))#John K - self.John,K@company.com