#Class and instances

'''
Classes allows to logically group the data and functions in a which is easy to reuse '''


class Emp:
	def __init__(self,first,last,pay):
		self.first=first
		self.last=last
		self.pay=pay
		self.email=f"self.{first},{last}@company.com"

	def fullname(self):
	    return f"{self.first} {self.last}"

emp1=Emp('John','K',50000)
emp2=Emp('Jane','M',60000)

print(emp1.fullname())#John K
print(emp2.fullname())	#Jane M
print(Emp.fullname(emp2))#Jane M       
