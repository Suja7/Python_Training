#LEGB-->Local..Enclosing..Global..Builtins
#=========================================
#when we call a function first it looks for local variable, then enclosing, then Global and finally 
#looks for builtins if it finds nothing in all these variables then only it throws error.


'''x='Global x'

def demo_func():
	y='local y'
	print(y)

demo_func()
print(x)	
#local y
#Global x '''

#if you want to change local variable to global variable just chanege it by adding global to 
#local variable ex: global y. 
#Otherwise you cannot acces the local variable globaly(means from outside)

# x='Global x'

# def demo_func():
# 	global y
# 	y='local y'
# 	print(y)

# demo_func()
# print(y)	
#local y
#local y

# x='Global x'

# def demo_func(z):
# 	y='local y'
# 	print(z)

# demo_func('hello')
# print(x)
# hello
# Global x

#Builtins#
#==========
# nums=[4,1,2,3,5]
# print(max(nums))#5 

#There are lot of builtins which already defined in python to see all those type
#import builtins

'''def outer():
	x='outer x'
	print(x)
	def inner():
		y='inner y'
		print(y)
	inner()
outer()
#inner y
#outer x'''

'''x='global x'
def outer():
	#x='outer x'
	print(x)
	def inner():
		# x='inner x'
		print(x)
	inner()
outer()
print(x)'''
#outer x --> if all the three variables available
# inner x
# global x

#if there is no local variable it will look for outer(enclosing)variable, then the output is:
# outer x
# outer x
# global x

##if there is no local and outer variable it will look for global variable, then the output is:
#global x
# global x
# global x
##if there is no local,outer and global variable it will look for builtin, then if there is nothing 
#it will throw error :NameError: name 'x' is not defined

x='global x'
def outer():
	x='outer x'
	
	def inner():
		nonlocal x
		x='inner x'
		print(x)
	inner()
	print(x)
outer()
print(x)

#to change the (inner)local variable and acces the outer variable print nonlocal x in 
#inner function it will from enclosing as local variable and the output is
# inner x
# inner x
# global x