import turtle
my_turtle=turtle.Turtle()
my_turtle.speed(0)


def rect(width,length,angle):
    for i in range(2):
	    my_turtle.forward(width)
	    my_turtle.right(angle)
	    my_turtle.forward(length)
	    my_turtle.right(angle)
for i in range(200):
    rect(100,200,90)
    my_turtle.right(11)

turtle.done()	

#practice for loop

# nlist=('apple', 'orange', 'banana', 'strawberry')
# for items in nlist:
# 	if items=='banana':
# 	    print('gotit')
# 	    continue
# 	print(items)
# apple
# orange
# gotit
# strawberry	

##while loop

#x=0
# while x<10:
#  x=x+1
#  print(x) 

# while x<10:
#    if x==7:
#    	break
#    x+=1
#    print(x)

