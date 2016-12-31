import sys
count = 1 # Initialize counter
while count <= 5: # Should we continue?
  print(count) # Display counter, then
  count += 1 # Increment counter
print("2nd ")    
for count in range(1, 11):
  print(count, end ="---")
print()

print("Third ")  
sum = ':)' # Initialize sum
for i in range(1, 9, 3):
  sum = sum + ':)'
  print(sum, end ='----> \n')
  
print ("forth")
# Print a multiplication table to 10 x 10
# Print column heading
print("       1   2   3   4   5   6   7   8   9  10")
print(" +-------------------------------------------")
for row in range(1, 11): # 1 <= row <= 10, table has 10 rows
 if row < 10: # Need to add space?
  print(" ", end="")
 print(row, "| ", end="") # Print heading for this row.
 for column in range(1, 11): # Table has 10 columns.
    product = row*column; # Compute product
    if product < 100: # Need to add space?
     print(end=" ")
    if product < 10: # Need to add another space?
       print(end=" ")
    print(product,end=" ") # Display product
 print()
 
print ('five')
 
# File computesquareroot.py
# Get value from the user
val = eval(input('Enter number: '))

# Compute a provisional square root
root = 1.0;

# How far off is our provisional root?
diff = root*root - val

# Loop until the provisional root
# is close enough to the actual root
while diff > 0.00000001 or diff < -0.00000001:
      root = (root + val/root) / 2 # Compute new provisional root
      print(root, 'squared is', root*root) # Report how we are doing
      # How bad is our current approximation?
      diff = root*root - val
# Report approximate square root
print('Square root of', val, "=", root)

print ('six')

from time import clock
print("Enter your name: ", end="")
start_time = clock()
name = input()
elapsed = clock() - start_time
print(name, "it took you", elapsed, "seconds to respond")

print ('seven')

from random import randrange, seed

seed(23) # Set random number seed
for i in range(0, 100): # Print 100 random numbers
 print(randrange(1, 1000), end=' ') # Range 1...1,000
print()

print('eight')

from random import randrange
# Roll the die three times
for i in range(0, 3):
 # Generate random number in the range 1...6
 value = randrange(1, 6)
 # Show the die
 print("+-------+")
 if value == 1:
	 print("| |")
	 print("| * |")
	 print("| |")
 elif value == 2:
	 print("| * |")
	 print("|   |")
	 print("| * |")
 elif value == 3:
	 print("| * |")
	 print("| * |")
	 print("| * |")
 elif value == 4:
	 print("| * * |")
	 print("|     |")
	 print("| * * |")
 elif value == 5:
	 print("| * * |")
	 print("| *   |")
	 print("| * * |")
 elif value == 6:
	 print("| * * * |")
	 print("|       |")
	 print("| * * * |")
 else:
	 print(" *** Error: illegal die value ***")
	 print("+-------+")