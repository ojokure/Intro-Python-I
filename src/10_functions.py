# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE

# Read a number from the keyboard
num = input("Enter a number: ")


def checkType(n):
    if int(n) % 2 == 0:
        print('Even')
    else:
        print('Odd')


checkType(num)
# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE
