class Emp:
	raise_amount=1.04
	
	def __init__(self,first,last,pay):
		self.first=first
		self.last=last
		self.pay=int(pay)
		self.email=f"{first}.{last}@company.com"

		
	def fullname(self):
	    return f"{self.first} {self.last}"
	def apply_raise(self):
	    self.pay=int(self.pay*self.raise_amount)
      

class Developer(Emp):
	raise_amount=1.08

	def __init__(self,first,last,pay,prog_lang):
		super().__init__(first,last,pay)
		#Emp.__init__(first,last,pay) we can also mention like this but if we want change super class here
		#also need to make change better use the first one
		self.prog_lang=prog_lang 

class Manager(Emp):
	def __init__(self,first,last,pay,employees=None):
		super().__init__(first,last,pay)
		if employees is None:
			self.employees=[]
		else:
			self.employees=employees

	
	def add_emp(self,emp):
		if emp not in self.employees:
			self.employees.append(emp)

	def remove_emp(self,emp):
		if emp in self.employees:
			self.employees.remove(emp)

	def print_emps(self):
		for emp in self.employees:
			print(emp.fullname())		

        	
Dev1=Developer('John','K',50000,'Python')
emp2=Emp('Jane','M',60000)
Mngr=Manager('Tom','H',90000,[Dev1])

#print(Mngr.email)
Mngr.add_emp(emp2)
# Mngr.print_emps()

Mngr.remove_emp(Dev1)
Mngr.print_emps()

print(isinstance(Mngr,Developer)) #false Instance(object) or subclass also we can use
print(issubclass(Manager,Manager))#true

# print(emp1.fullname())#John K
# print(emp2.fullname())	#Jane M
# print(Emp.fullname(emp2))#Jane M    

#print(help(Developer))   #this will show the method which it inherited.

# print(Dev1.first)
# Dev1.apply_raise()
# print(Dev1.pay)

# print(emp2.pay)
# emp2.apply_raise()
# print(emp2.pay)

# print(Dev1.prog_lang)#Python

