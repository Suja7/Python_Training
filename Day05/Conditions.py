'''if False:
	print('the condition is true')
else:
  print('the condition is false')

program='Java'

if program=='Python':
  print('the program is Python')
elif program== 'Java':
  print('the program is Java')
else:
  print('No Match')


lunch='yes'
hw=True
if lunch=='yes' and hw:
  print('you can play')
else:
 print('no play')    


a=[1,2,3]
b=[1,2,3]
print(id(a))#1666496679424
print(id(b))#1666496711872 

#False Values## If thr condition have the following values it will return as False 
 #false
 #None
 #0
 #'',[],()-->empty string, empty list, empty tuple
 #{} --> empty dictionary

condition=()
if condition:
 	print('The condition is True')
else:
  print('The condition is False')'''	

#nums = [1,2,6,5,3]

# for i in nums:
#     if i==5:
#        print('found!')
#        break
#     print(i)  
# 1
# 2
# 6
# found!   


# for i in nums:
#     if i==5:
#        print('found!')
#        continue
#     print(i) 
# 1
# 2
# 6
# found!
# 3        


# x=0

# while x<10:
# 	if x==5:
# 	   break
# 	x+=1
# 	print(x)# it will print 1 to 5 

####Just for practice##

# c=['comp,physics,maths']
# c_str='_'.join(c)
# print(c_str)
# nw_list=c_str.split(' ')
# print(nw_list)

'''s='Hello'
for i in s:
	#print(s,end='\n')#prints Hello five times one by one
	print(s,end=' ') #Hello Hello Hello Hello Hello'''

'''list1=[x for x in range(10)]
#print(list1)#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# list2=[x+1 for x in range(10)]
# print(list2)#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# list3=[x+1 for x in range(10) if x%2==0]
# print(list3)#odd numbers[1, 3, 5, 7, 9]
list4=[x for x in range(10) if x%2==0]
print(list4)#[0, 2, 4, 6, 8]'''

#friends={'a':'10', 'b':'20', 'c':'30'}
#for items in friends.items():
#	print(items)
#('a', '10')
#('b', '20')
#('c', '30')

# for keys,values in friends.items():
# 	print(f"{keys}:{values}")
# a:10
# b:20
# c:30
# for x in friends:
# 	print(x,":",friends[x])
# a:10
# b:20
# c:30	

# t1=()
# print(t1)#() creates empty tuple 

# x=['Python', 'is', 'cool']
# print(' '.join(x))# Python is cool--> now the list is converted to string

# x1=('Python is cool')
# list5=x1.split(' ')
# print(list5)#['Python', 'is', 'cool'] converted to list

# a1=('apple*is*sweet')
# a2=a1.split('*')
# print(a2)#['apple', 'is', 'sweet'] 

# s1='  Henry V  '
# print(s1)#{  Henry V  } before stripping  it types with space
# s1=s1.strip()
# print(s1)#Henry V after striping it returns without space

# s1='0000Henry V+++*'
# s1=s1.strip('0+*')
# print(s1)#Henry V it cuts whatever specific character we specify

'''x=0

while x<10:
    if x==5:
       break
    print(x)
    x=x+1'''    