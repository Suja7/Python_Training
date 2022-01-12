'''class Emp:
	raise_amount=1.04
	
	def __init__(self,first,last,pay):
		self.first=first
		self.last=last
		self.pay=int(pay)
		self.email=f"{first},{last}@company.com"

		

	def fullname(self):
	    return f"{self.first} {self.last}"
	      


emp1=Emp('John','K',50000)
emp2=Emp('Jane','M',60000)

emp1.first='kate'

print(emp1.first)#kate
print(emp1.email)#John,K@company.com-->first name not updated in email to update the email
#we need to create function'''


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
	      


emp1=Emp('John','K',50000)
emp2=Emp('Jane','M',60000)

emp1.first='kate'

print(emp1.first)#kate
print(emp1.email)
#print(emp1.fullname()) #kate K if you dont want to (call)add paranthesis next to fullname nee to add 
#property before the fullname method

print(emp1.fullname)#kate K
