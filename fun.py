# Print a message to prompt the user for input
def prompt():
 print("Please enter an integer value: ", end="")
# Start of program
print("This program adds together two integers.")
print("fun call")
prompt() # Call the function
value1 = int(input())
print("fun call")
prompt() # Call the function again
value2 = int(input())
sum = value1 + value2;
print(value1, "+", value2, "=", sum)

print("############  second call  ###################")
# Count to ten and print each number on its own line
def count_to_10():
 for i in range(1, 11):
  print(i , end=" ")
print()
print("Going to count to ten . . .")
count_to_10 ()
print()
print("Going to count to ten again. . .")
count_to_10()
print()
print("############  third call  ###################")
# Count to n and print each number on its own line
def count_to_n(n):
 for i in range(1, n + 1):
  print(i)

print("Going to count to ten . . .")
count_to_n(10)
print("Going to count to five . . .")
count_to_n(5)
#below are wrong way to all function
#count_to_n()
#count_to_n(3, 5)
#count_to_n(3.2)

print()
print("############  next call  ###################")
# Definition of the prompt function
def prompt():
 value = int(input("Please enter an integer value: "))
 return value

#print("This program adds together two integers.")
value1 = prompt() # Call the function
value2 = prompt() # Call the function again
sum = value1 + value2
print(value1, "+", value2, "=", sum)

print()
print("############  next call  ###################")
# Definition of the prompt function
def prompt(n):
 value = int(input("Please enter integer # "))
 print(n)
 value = value * -1
 print(value)
 return value

print("This program adds together two integers.")
value1 = prompt(1) # Call the function
value2 = prompt(2) # Call the function again
sum = value1 + value2
print(value1, "+", value2, "=", sum)

print()
print("############  next call  ###################")
def gcd(num1, num2):
# Determine the smaller of num1 and num2
	min = num1 if num1 < num2 else num2
# 1 is definitely a common factor to all ints
	largestFactor = 1
	for i in range(1, min + 1):
		if num1 % i == 0 and num2 % i == 0:
			largestFactor = i # Found larger factor
	return largestFactor
print(gcd(36, 24))
x=2
x = gcd(x - 2, 24)
print('x ki value ', x)
y=2
y = gcd(y - 2, gcd(10, 8))
print('y ki value ', y)