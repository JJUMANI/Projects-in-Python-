
#  File: Boxes.py

#  Description: Create Largest Nested Boxes

#  Student's Name:Junaid K. Jumani

#  Student's UT EID: jkj696
 
#  Course Name: CS 313E 

#  Unique Number: 50945

#  Date Created: March 2nd 2016

#  Date Last Modified: March 3rd 2016

def sub_sets (a, b, idx, box):
  if (idx == len(a)):
    box.append(b)
    return 
  else:
    c = b[:]
    b.append (a[idx])
    sub_sets (a, c, idx + 1, box)
    sub_sets (a, b, idx + 1, box)

def main():
# Create an empty list of boxes
  list = []
  boxes = []
  box = []
# Open and read the file boxes.txt
  in_file = open('boxes.txt', 'r')
  line1 = in_file.readline()
# Read each line of input and store in a list and sort
#  and add to the list of boxes
  for i in in_file:	
    line = i.split()
    line.sort()
    line[0] = int(line[0])
    line[1] = int(line[1])
    line[2] = int(line[2])
    boxes.append(line) 
  boxes.sort()  
# Close the file boxes.txt
  in_file.close()
# Get all of the subsets of boxes
  a = boxes
  b = []
  sub_sets (a, b, 0, box)
  
# With each subset check if they all fit inside each other
  hi = 0
  li = True
  for s in range (len(box)):
        temp = 0
        check = True
        li = True
        for a in range (len(box[s])-1):	
            hi = 0
            for n in range (len(box[s][a])):
                    if(li == True):
                      if (box[s][a][n] < box[s][a+1][n]):
                          hi = hi + 1 						  
                      else :
                          li = False
                          check = False	
        if(check == True):
          list.append(box[s])	 
# Go through the set of nesting boxes and find the maximum	
  print ('Largest Subset of Nesting Boxes')	  
  max = 0 
  for fi in range(len(list)-1):
    if (max < len(list[fi+1])):
      max = len(list[fi+1])
  for ki in range(len(list)):
    if(max == len(list[ki])):
# Print the largest set of nesting boxes	
      print(list[ki])	
  if (max == 0):
    print('No Nesting Boxes')  	
main()