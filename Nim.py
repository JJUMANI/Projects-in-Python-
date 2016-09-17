#  File: Nim.py

#  Description: Strategy to win the nim Game by removing counters from specific Heap or Confirming if Losing the game

#  Student's Name:Junaid K. Jumani

#  Student's UT EID: jkj696
 
#  Partner's Name: Justin Lyan

#  Partner's UT EID: JL38965

#  Course Name: CS 313E 

#  Unique Number: 50945

#  Date Created: February 2nd 2016

#  Date Last Modified: February 2nd 2016

def main():
#Using "no_first_line" as False to make python to not consider first line
  no_first_line = False
#Reading the Data from the text given
  file = open("nim.txt", "r")
#Using for loops to read words from line and append it to lists "a" and "b"
  for line in file:
    X = 0
    a = []
    b = []
    line = line.split()
    if (no_first_line == True):
      for word in line:
         a.append(word)
         b.append(word)
#Using for loop to find nim-sum which is "X" in this case
      for n in range (len(a)):
        X = X ^ int(a[n]) 
#Using for loop to fine individual nim-sum which is "b[i]" in this case
      for i in range (len(b)):
        b[i] = X ^ int(b[i])
#Using "f" to stop for loop to get into if statement after first time
      f = 0
      for n in range (len(a)):
#Print Results
        if (X==0 and f==0):
          f += 1
          print ("Lose Game")
        if (b[n] < int(a[n]) and f == 0):
          f += 1
          print ("Remove", int(a[n])-b[n], "counters from Heap", n+1)
    no_first_line = True         
main()