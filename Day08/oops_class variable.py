class Emp:
	raise_amount=1.04
	nums_of_emp = 0
	def __init__(self,first,last,pay):
		self.first=first
		self.last=last
		self.pay=int(pay)
		self.email=f"{first},{last}@company.com"

		Emp.nums_of_emp +=1

	def fullname(self):
	    return f"{self.first} {self.last}"
	def apply_raise(self):
	    self.pay=int(self.pay*self.raise_amount)
print(Emp.nums_of_emp) #0	      


emp1=Emp('John','K',50000)
emp2=Emp('Jane','M',60000)

print(Emp.nums_of_emp)#2

# print(emp1.fullname())#John K
# print(emp2.fullname())	#Jane M
# print(Emp.fullname(emp2))#Jane M       

print(emp1.raise_amount)#1.04 

print(Emp.raise_amount)
emp1.apply_raise()
print(emp1.pay)#52000

emp2.raise_amount=1.05

emp2.apply_raise()
print(emp2.pay)#63000 


