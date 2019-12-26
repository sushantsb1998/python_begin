# write if else statement
# if user input is less than 10 print less than 10 
# else print it is greater than 10



def if_else():
	print( "write a number" )
	num = int ( input())
	if ( num < 10 ):
		print( " It is less than 10" )
	elif ( num == 10):
		print("it is equal" )
	else:
		print(" It is greater than 10")

if_else()
