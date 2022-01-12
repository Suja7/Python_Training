class Emp:
	raise_amount=1.04
	
	def __init__(self,first,last,pay):
		self.first=first
		self.last=last
		self.pay=int(pay)
		self.email=f"self.{first},{last}@company.com"

		
	def fullname(self):
	    return f"{self.first} {self.last}"
	def apply_raise(self):
	    self.pay=int(self.pay*self.raise_amount)


	@classmethod
	def set_raise_amount(cls,amount):
		cls.raise_amount=amount	  

	@classmethod
	def from_string(cls,emp_str):
		first,last,pay=str_emp_1.split('-')
		return cls(first,last,pay)


	@staticmethod
	
	def is_workday(day):
		if day.weekday()==5 or day.weekday()==6:
			return False
		return True
		


emp1=Emp('John','K',50000)
emp2=Emp('Jane','M',60000)

str_emp_1='John-k-50000'

new_emp_1=Emp.from_string(str_emp_1)

# first,last,pay=str_emp_1.split('-')
# new_emp_1=Emp(first,last,pay)

# print(Emp.raise_amount) #1.04
# Emp.set_raise_amount(1.08)
# print(Emp.raise_amount)#1.08

print(new_emp_1.first)

import datetime
my_date = datetime.date(2021,12,11)
print(my_date)

print(Emp.is_workday(my_date))

# print(datetime.__file__)




