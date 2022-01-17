#Defining empty Function
#=========================

# def hello():
# 	pass

# def hello():
#     print('Welcome')#Welcome. We can define it one place and we can call 
#     #that function to do the sme task
# hello()    	

#print(list(range(10)))#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# for i in range(10):
#      print("hello")# it prints hello ten time

# def hello():
#     return('Welcome')
# hello()    	#when you run this it wil not give any results. because when you say return 
# #it will run and keep the results 

# print(hello())# Welcome
#==========================================================================================
# def func(message, name):
# 	return f"{message} {name}"

# print(func('hello', 'Kate'))	#hello Kate

#For passing multiple args need to give before * otherwise it will throw error
#=================================================
def emp_info(*args):
    print(args)
emp_info('language', 'python','java')#('language', 'python', 'java')

#TO mention key words in dictionary arguments use **kwargs
#=========================================================

def emp_info(*args,**kwargs):
    print(args)
    print(kwargs)
emp_info('language', 'python','java',name='John', age='25',city='troy')
#('language', 'python', 'java')
#{'name': 'John', 'age': '25', 'city': 'troy'}

