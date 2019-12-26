''' Ask users First and Last name, address, Qualification, and desired salary and print them at the end '''


def first():
	print('enter  your first name:-')
	firstname = input()
	print('enter your last name:-')
	lastname = input()
	print("enter ypour address")
	address = input()
	print("enter your qualification")
	qualification = input()
	print("enter your desired salary")
	salary = input()

# your name is first name + last name. with address. Your desire salary is.
	print(firstname + " " + lastname  +   " Your address is " +  address + " . Your desire salary is " + salary) 
	
first()


