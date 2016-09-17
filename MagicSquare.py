#  File: Nim.py

#  Description: Create Magic Square for odd numbers of rows and colums

#  Student's Name:Junaid K. Jumani

#  Student's UT EID: jkj696
 
#  Partner's Name: Justin Lyan

#  Partner's UT EID: JL38965

#  Course Name: CS 313E 

#  Unique Number: 50945

#  Date Created: February 6th 2016

#  Date Last Modified: February 7th 2016

# Populate a 2-D list with numbers from 1 to n2 and create magic square
def makeSquare ( n ):
	square = []
	count = 1
	for i in range(n):
		square.append([0]*(n)) 
	
	X = n-1 
	Y = n//2 
	square[int(X)][int(Y)] = 1 
	while count < n**2:
		X = X+1
		Y = Y+1
		if (X > n-1): 
			X = 0
		if (Y > n-1):
			Y = 0
		if (square[int(X)][int(Y)] != 0):
			if (X == 0):
			    X = n-2
			if (Y == 0):
				Y = n-1	
			else:
			    X = X-2
			    Y = Y-1
		square[int(X)][(Y)] = count + 1
		count = count + 1
	return square
		

# Print the magic square in a neat format where the numbers
# are right justified
def printSquare(magic):
    for row in magic:
        for val in row:
            print('{:2d} '.format(val), end='')
        print()
    return ""   
# Check that the 2-D list generated is indeed a magic square
def checkSquare ( magicSquare ):
	sumRow = 0
	sumCol = 0
#Check Sum of row from every angle
	for j in range(len(magicSquare[0])):
		sumRow = sumRow + magicSquare[0][j]
	for i in range(len(magicSquare)):
		row = 0
		for j in range(len(magicSquare[i])):
			row = row + magicSquare[i][j]
		if (row != sumRow):
			print ("Not a magic square!")	
	print ("Sum of row = ", sumRow)
#Check Sum of column from every angle	
	for i in range(len(magicSquare)):
		sumCol = sumCol + magicSquare[i][0]
	for j in range(len(magicSquare[j])):
		col = 0
		for i in range(len(magicSquare)):
			col = col + magicSquare[i][j]
		if (col != sumCol):
			print ("Not a magic square!")
	print ("Sum of column = ", sumCol)		
#Check Sum of diagonal from every angle	 
	count = 0
	sumDia_LR = 0
	while count < len(magicSquare):
		sumDia_LR = sumDia_LR + magicSquare[count][count]
		count = count + 1
	print ("Sum of diagonal (UL to LR) = ", sumDia_LR)
	
	X = len(magicSquare) - 1
	Y = 0
	counter = 0
	sumDia_RL = 0
	while counter < len(magicSquare):
		sumDia_RL = sumDia_RL + magicSquare[X-counter][counter]
		counter = counter + 1 
	print ("Sum of diagonal (UR to LL) = ",  sumDia_RL)

def main():
  # Prompt the user to enter an odd number 3 or greater
  x = int(input("Enter an odd number 3 or greater: "))
  # Check the user input
  if(x%2 == 0 or x < 3):
  	print ("Cannot make a magic square")
  # Create the magic square
  result = makeSquare(x)
  # Print the magic square
  print ("Here is a", x, "x", x, "magic square:")
  print ()
  print (printSquare(result))
  # Verify that it is a magic square
  checkSquare (result)
  
main()