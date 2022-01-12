import unittest
from employee import Emp

class Test_Emp(unittest.TestCase):

	def test_email(self):
		emp1 = Emp('John', 'K', 50000)
		emp2=Emp('Jane','M',60000)

	    self.assertEqual(emp1.email, 'John.K@company.com')
	    self.assertEqual(emp2.email, 'Jane.M@company.com')
	    
	    emp1.first = 'Kate'
	    emp2.first = 'Mike'

	    self.assertEqual(emp1.email, 'Kate.K@company.com')
	    self.assertEqual(emp2.email, 'Mike.M@company.com')

def test_fullname(self):
		emp1 = Emp('John', 'K', 50000)
		emp2= Emp('Jane','M',60000)
	    self.assertEqual(emp1.fullname, 'John K')
	    self.assertEqual(emp2.fullname, 'Jane M')

	    emp1.first = 'Kate'
	    emp2.first = 'Mike'

	    self.assertEqual(emp1.fullname, 'Kate K')
	    self.assertEqual(emp2.fullname, 'Mike M')


def test_apply_raise(self):
	emp1 = Emp('John', 'K', 50000)
	emp2= Emp('Jane','M',60000)

	emp1.apply_raise()
	emp2.apply_raise()

	self.assertEqual(emp1.pay, 52000)
	self.assertEqual(emp2.pay, 62400)