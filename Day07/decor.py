#Decorators-->First class functions-->Closures

#Decorator helps you to add functonality 
#A decorator in Python is a function that takes another function
# as its argument, and returns yet another function .
# Decorators can be extremely useful as they allow the extension of an
# existing function, without any modification to the original function 
#source code.

'''First class function-->A programming language is said to have First-class
functions when functions in that language are treated like any other variable.
For example, in such a language, a function can be passed as an argument to 
other functions, can be returned by another function and can be assigned 
as a value to a variable.'''

'''def square(x):
	return x*x
result=square(4)
print(result)#16'''

'''def square(x): #now we are assigning the function as variable
	return x*x
result=square #the function sqaure itself is varible now 
print(result(4))#16

def my_result(func,my_lst):# we are using the function square in another function to do with list 
                              #of numbers 
    for i in my_lst:       # to go through the list we are using for loop and to use square fuction 
    	print(func(i))            # we are printing the function 
my_result(square,[1,2,3,4])
#1
# 4
# 9
# 16 '''

#To get ouput as list we need to append the list to the function

'''def square(x): 
	return x*x
result=square 
#print(result(4))
def cube(x):
	return x*x*x
result=cube	

def my_result(func,my_lst):
	res=[]
	for i in my_lst:
		res.append(func(i))
	print(res)
my_result(square,[1,2,3,4])		#[1, 4, 9, 16]
my_result(cube,[1,2,3,4])  #[1, 8, 27, 64]'''

'''def outer(msg):
	def inner():
		print(f'hello:{msg}')
	return inner
new_var=outer('song')
#new_var()
print(new_var.__name__)		#inner(to find which function is used we have use this)'''

def decorator_function(original_function):
	def wrapper_function(*args,**kwargs):
		print('Hello World')
		return original_function(*args,*kwargs)
	return wrapper_function
	
@decorator_function
def display_info(name,age):
    print(f"display_info ran with args:'{name}','{age}'")	

display_info('john',26)    	






