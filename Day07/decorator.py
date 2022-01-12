# def outer_func(msg):
# 	def inner_func():
# 		print(msg)
# 	return inner_func
	
# hi_func=outer_func('helo')
# hi_func()		

'''def decorator_function(original_func):
	def wrapper_function():
		print("Hello world")
		return original_func()
	return wrapper_function

@decorator_function'''
def disp():
    print('This display functon is Running')	
disp()    

# decorated_disp= decorator_function(disp)#this line is rewritten in different way(@decorator_function)
# decorated_disp() 
# Hello world
# This display functon is Running

#disp()#This display functon is Running

	