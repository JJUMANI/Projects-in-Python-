
#  File: Triangle.py

#  Description: the four different approaches to problem solving to find the greatest path sum
#  starting at the top of the triangle and moving only to adjacent numbers on the row below

#  Student Name: Junaid K. Jumani

#  Student UT EID: jkj696

#  Partner Name: Aya Seidemann 

#  Partner UT EID: ags2269

#  Course Name: CS 313E

#  Unique Number: 50945

#  Date Created: April 16, 2016

#  Date Last Modified: April 17, 2016

# returns the greatest path sum using exhaustive search
def Search(i, j, grid):
	if (len(grid) == i):
		return 0
	else:	
		return (grid[i][j] + max(Search(i+1, j+1, grid), Search(i+1, j, grid)))
def exhaustive_search (grid):
	i = 0
	j = 0
	b = Search(i, j, grid)
	return b

# returns the greatest path sum using greedy approach
def greedy (grid):
  a = 0
  sum = 0
  for i in range (len (grid)):
    for j in range(len(grid[i])):	
      if (len(grid[i]) <= 1):
        sum += grid[i][j]		  
      else: 
        if (grid[i][a+1] > grid[i][a]):
            a += j+1
            sum += max(grid[i][a-1], grid[i][a])
        else:
            a += j
            sum += max(grid[i][a], grid[i][a+1])
        break	  
  return (sum)	
# returns the greatest path sum using divide and conquer (recursive) approach
def rec(i, j, grid):
	if (len(grid) == i):
		return 0
	else:	
		return (grid[i][j] + max(rec(i+1, j+1, grid), rec(i+1, j, grid)))
def rec_search (list):
	i = 0
	j = 0
	sum = 0
	a = rec(i, j, list)
	return a

# returns the greatest path sum using dynamic programming
def dynamic_prog (grid):
  for i in range(len(grid)-1, 0, -1):
    for j in range(0, i):
        grid[i-1][j] += max(grid[i][j], grid[i][j+1])
  return grid[0][0]	

#Reading File  
def readFile (in_file):
  list = []
  line = in_file.readline().rstrip("\n").split()
  first_line = int (line[0])

  for i in range (first_line):
    List = []
    line = in_file.readline().rstrip("\n").split()
    for j in line:
      List.append(int(j))
    list.append(List)  
  return list
# Print in main function
def main():
	in_file = open('triangle.txt', 'r')	
	list = readFile (in_file)
	x = exhaustive_search (list)
	print ('The greatest path sum through exhaustive search is', x)
	y = greedy (list)
	print ('The greatest path sum through greedy search is',y)
	z = rec_search (list)
	print ('The greatest path sum through recursive search is',z)	
	q = dynamic_prog (list)
	print ('The greatest path sum through dynamic programming is',q)
	
main()	