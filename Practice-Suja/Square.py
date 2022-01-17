# import turtle
# my_turtle=turtle.Turtle()

# my_turtle.forward(100)
# my_turtle.right(90)
# my_turtle.forward(100)
# my_turtle.right(90)
# my_turtle.forward(100)
# my_turtle.right(90)
# my_turtle.forward(100)
# my_turtle.right(90)
# turtle.done()

#Always follow this method DRY--> Dont repeat yourself

#For single square
#=================
# def square():
# 	my_turtle.forward(100)
# 	my_turtle.right(90)
# 	my_turtle.forward(100)
# 	my_turtle.right(90)
# 	my_turtle.forward(100)
# 	my_turtle.right(90)
# 	my_turtle.forward(100)
# 	my_turtle.right(90)
	    
  
# for i in range(10):
# 	square ()
	
# turtle.done()

# def square(length,angle):
# 	my_turtle.forward(length)
# 	my_turtle.right(angle)
# 	my_turtle.forward(length)
# 	my_turtle.right(angle)
# 	my_turtle.forward(length)
# 	my_turtle.right(angle)
# 	my_turtle.forward(length)
# 	my_turtle.right(angle)
	    
# square(100,90)    
# turtle.done()

###to make circle with square 
# import turtle
# my_turtle=turtle.Turtle()
# my_turtle.speed(0)


# def square():
# 	my_turtle.forward(100)
# 	my_turtle.right(90)
# 	my_turtle.forward(100)
# 	my_turtle.right(90)
# 	my_turtle.forward(100)
# 	my_turtle.right(90)
# 	my_turtle.forward(100)
# 	my_turtle.right(90)

##or square angle is 90 and for circle angle is 360. to make circle with square is 36 times 
#move forward with angle 10	    
  
# for i in range(36):# to make circle with 36 squares 
# 	square ()
# 	my_turtle.right(10)
# turtle.done()


import turtle
my_turtle=turtle.Turtle()
my_turtle.speed(0)


# def square():

# 	for i in range(4):
# 	    my_turtle.forward(100)
# 	    my_turtle.right(90)
# for i in range(36):
#     square()
#     my_turtle.right(10)

# turtle.done()    	    

#To make uniqe squares# Give the angle in prime number 
#======================

# def square():

# 	for i in range(4):
# 	    my_turtle.forward(200)
# 	    my_turtle.right(90)
# for i in range(200):
#     square()
#     my_turtle.right(11)

# turtle.done()    	   

#To make diferent length and angle 

def square(length,angle):

	for i in range(4):
	    my_turtle.forward(length)
	    my_turtle.right(angle)


for i in range(100):
    square(80,90)
    my_turtle.right(11)	    


turtle.done() 



