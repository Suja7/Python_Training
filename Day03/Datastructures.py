#Summary####
'''A list is an ordered collection of items.
# Use square bracket notation [] to access a list element by its index. The first element has an index 0.
# Use a negative index to access a list element from the end of a list. The last element has an index -1.
# Use list[index] = new_value to modify an element from a list.
# Use append() to add a new element to the end of a list.
# Use insert() to add a new element at a position in a list.
# Use pop() to remove an element from a list and return that element.
# Use remove() to remove an element from a list.'''


##Lists
#message=['hello', 'hi','welcome','namaskar']
# print(message[0])#hello
# print(message[1])#hi
# print(message[0:3])#['hello', 'hi', 'welcome']
# message.append('vandanam')#['hello', 'hi', 'welcome', 'namaskar', 'vandanam']
# print(message)
#message.insert(1,'all')#['hello', 'all', 'hi', 'welcome', 'namaskar']--> first mention in which index 
# you want to insert.
# print(message)
# #message.extend('vanakkam')#['hello', 'all', 'hi', 'welcome', 'namaskar',
# # 'v', 'a', 'n', 'a', 'k', 'k', 'a', 'm']
# message.extend(message)#['hello', 'all', 'hi', 'welcome', 'namaskar', 'hello', 'all',
# # 'hi', 'welcome', 'namaskar']
# print(message)
# message.remove('namaskar')#['hello', 'hi', 'welcome']
# print(message)
# message.pop(1)
#message.pop()# it will remove the last index if we didnt specify any index. also it remembers 
#which one we removed
# removed=message.pop()
# print(removed)#welcome

# print(message)#['hello', 'welcome', 'namaskar']--> index value 1='hi' is removed
# #in pop method you cannot directly specify the string. we need to specify the index.

# List1=['welcome', 'to', 'python']
# List2=List1.pop(1)
# print(List1)#['welcome', 'python']
# print(List2)#to

#list1=['welcome', 'to', 'python']
#list1.sort()
#print(list1)#['python', 'to', 'welcome']-->sorts strings in alphabetical order

#guest=['James', 'Mary', 'John', 'Patricia', 'Robert', 'Jennifer']
# guest.sort()
# print(guest)#['James', 'Jennifer', 'John', 'Mary', 'Patricia', 'Robert']

#num1=[8,1,6,9,7]
#num1.sort()
# print(num1)#[1, 6, 7, 8, 9]
# num1.sort(reverse=True)[9, 8, 7, 6, 1]
# print(num1)

#Converting list to string and Vice versa#
#==========================================
#courses=['physics','maths','compsci']
#courses_str=','.join(courses) #physics,maths,compsci
#courses_str='-'.join(courses) #physics-maths-compsci
# courses_str=' '.join(courses) #physics maths compsci
# print(courses_str)
# new_list=courses_str.split(' ')
# print(new_list)#['physics', 'maths', 'compsci']  

# courses=['physics','maths','compsci']
# list1=['bio','Chem']
# courses.insert(0,'eng')
#courses.append(list1)#['eng', 'physics', 'maths', 'compsci', ['bio', 'Chem']]in which we will get whole bio,chem
#as 5th index 
# courses.extend(list1)#['eng', 'physics', 'maths', 'compsci', 'bio', 'Chem']

# print(courses)#['eng', 'physics', 'maths', 'compsci']

#courses=['physics','maths','compsci']
#print('maths' in courses)#True

#For going through the list to find all or any items in the list "for loop is used"####
#--------------------------------------------------------------------------------------
# for item in courses: #physics ##for each item it pick it will the items that many time
#                      # maths
#                      # compsci
# 	print(item)

#for course in courses: #['physics', 'maths', 'compsci']
                        #['physics', 'maths', 'compsci']
                        #['physics', 'maths', 'compsci']
# 	print(courses)

#courses=['maths', 'physics','compsci']

# for i in courses:
#     print('courses')#courses
#                     #courses
#                     #courses

#TO find the index value of list we have to use enumerate function#
#-------------------------------------------------------------------
# for index, value in enumerate(courses): 
#     print(index,value)   #0 maths
#                          # 1 physics
                         # 2 compsci

# for course in enumerate(courses):
#     print(course)
#(0, 'maths')
# (1, 'physics')
# (2, 'compsci')


## Lists are mutable means we can modify, add or change
#============================================
# list1=['physics','maths','compsci']
# list2=list1
# print(list2)#['physics', 'maths', 'compsci']
# list1[0]='bio'
# print(list2)#['bio', 'maths', 'compsci']

##Tuple are immutable means we cannot change or add anything
#===========================================================
# tuple1=('physics','maths','compsci')
# tuple2=tuple1
# print(tuple2)#('physics', 'maths', 'compsci')

######Sets which always returns unique items
#============================================
#Sets are used for performing the membership test whether the particular set is present in the sets
# courses={'maths', 'physics','compsci','maths', 'physics','compsci','maths','maths'}
# print(courses)#{'maths', 'physics', 'compsci'} -->It only prints unique items means it will not repeat

#Empty list
#============
# empty_list=[]
# empty_list=list()

#Empty Tuple
#============
# empty_tuple=()
# empty_tuple=tuple()

##Empty Sets
#=============
# empty_set={}#Dont use this method to create set this is used create dictionaries
# empty_set=set()

##Dictionaries: working with key to get the value pair///
#======================================================

# emp={'name':'John', 'age':26, 'prog-lang':['python','Java']}#keys can also be integer

# print(emp['age'])#26
# print(emp.get('name'))#John
# print(emp.get('email'))#None

##to add something in the dictionary
#emp['email']='John@company.com'
#print(emp)#{'name': 'John', 'age': 26, 'prog-lang': ['python', 'Java'], 'email': 'John@company.com'}

# emp.update({'name':'Jane', 'age':16})
# print(emp)#{'name': 'Jane', 'age': 16, 'prog-lang': ['python', 'Java'], 'email': 'John@company.com'}

# del emp['age']
# print(emp)#{'name': 'John', 'prog-lang': ['python', 'Java'], 'email': 'John@company.com'}

#emp.pop('age')
# print(emp)#{'name': 'John', 'prog-lang': ['python', 'Java'], 'email': 'John@company.com'}

# removed=emp.pop('age')
# print(removed)#26-->pop option remembers what it removed

emp={'name':'John', 'age':26, 'prog-lang':['python','Java']}
# print(emp.keys())#dict_keys(['name', 'age', 'prog-lang'])
# print(emp.values())#dict_values(['John', 26, ['python', 'Java']])
#If you want to get both keys and values then we have to print items
#print(emp.items())#dict_items([('name', 'John'), ('age', 26), ('prog-lang', ['python', 'Java'])])

# for item in emp:
# 	print(item)# it returns only keys
#name
# age
# prog-lang

#to get both keys and values we have to mention emp.items
#=========================================================
# for item in emp.items():
# 	print(item) 
#('name', 'John')
# ('age', 26)
# ('prog-lang', ['python', 'Java'])

#we can also write

for keys,value in emp.items():
	print(f"{keys}: {value}")
#name: John
# age: 26
# prog-lang: ['python', 'Java']	