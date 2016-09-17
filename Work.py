#  File: Work.py 

#  Description: figure out the minimum allowable value of v for a given productivity factor that will allow him to write at least n lines of code before he falls asleep

#  Student Name: Junaid K. Jumani

#  Student UT EID: jkj696

#  Course Name: CS 313E

#  Unique Number: 50945

#  Date Created: March 25, 2016

#  Date Last Modified: March 26, 2016

#Using Recursion to get total Recusrsive function value
def binaryRecursion (l, u):
    if (l//u == 0):
        return l 
    else:
        return l + binaryRecursion (l//u, u)
#Searching the value of "v" by binary seach	
def binarySearch (a, x):
  RecursiveValue = 0   
  lo = 0
  hi = len(a) - 1
  while (lo <= hi):
    mid = (lo + hi) // 2
    RecursiveValue = binaryRecursion (mid, x)    
    if (RecursiveValue > a[-1]):
      hi = mid - 1
    elif (RecursiveValue < a[-1]):
      lo = mid + 1
    else:
      return mid
  return mid



def main():
#Create empty list
  work = []
#Reading the file to get values of n and k  
  in_file = open('work.txt', 'r')
  line1 = in_file.readline()
  for line in in_file:
    line = line.split()
    n = int(line[0])
    k = int(line[1])
    for i in range (1, n+1):
      work.append(i)	
    v = binarySearch (work, k)
#Print "v"	
    print (v)
main()