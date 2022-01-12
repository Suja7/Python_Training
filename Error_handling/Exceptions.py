# try:
# 	pass
# except:
# 	pass
# else:
# 	pass
# finally:
# 	pass

# f = open('test_file.txt')
# print(f.read())
# f.close()
# print(f.closed)

# try:
# 	f = open('testfile.txt')
# except Exception:
# 	print('File does not exist')

# try:
# 	f = open('test_file.txt')
# 	new_var = old_var
# except Exception:#it is only for (file not found error) open, should not display for variable error
# 	print('File does not exist')

# try:
# 	f = open('test_file.txt')
# 	new_var = old_var
# except FileNotFoundError:# this will display (if there is error in line 27 	
# 	print('File does not exist')
# except Exception:
# 	print('something went wrong')# this will display if error in line 28 and line 27 is correct

#new_var = old_var #NameError: name 'old_var' is not defined

# try:
# 	f = open('test_file.txt')
# 	new_var = old_var
# except FileNotFoundError as e:#No such file or directory: 'testfile.txt' 	
# 	print(e)
# except Exception as e:
# 	print(e)# name 'old_var' is not defined

try:
	f = open('test_file.txt')
	#new_var = old_var
except FileNotFoundError as e:#No such file or directory: 'testfile.txt' 	
	print(e)
except NameError as e:
	print(e)# name 'old_var' is not defined
except Exception as e:
 	print(e)
else:
	print(f.read())
	f.close()
finally:
	print('Executing...')









