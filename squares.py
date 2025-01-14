# Use a list comprehension to create a list of squared numbers (n*n). 
# The function receives the variables start and end, and returns a 
# list of squares of consecutive numbers between start and end inclusively. For example, squares(2, 3) should return [4, 9].
listOfSquares = []
def squares(start, end):
	for Number in range(start,end+1):
		squares1 = Number*Number
		listOfSquares.append(squares1)		
	return listOfSquares

print(squares(2, 3)) # Should be [4, 9]
print(squares(1, 5)) # Should be [1, 4, 9, 16, 25]
print(squares(0, 10)) # Should be [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]