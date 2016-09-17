#  File: Josephus.py

#  Description: Create a circular linked list having the number of soldier specified.
#               This program will print out the order in which the soldiers get eliminated and the one who survived.

#  Student Name: Junaid K. Jumani

#  Student UT EID: jkj696

#  Course Name: CS 313E

#  Unique Number: 50945

#  Date Created: April 8, 2016

#  Date Last Modified: April 10, 2016
# Create Class Link
class Link(object):
  def __init__ (self, item, next = None):
    self.item = item
    self.next = next
class CircularList(object):
  # Constructor
  def __init__ ( self ):   
    self.first = Link(None)
    self.first.next = self.first   
    self.numLinks = 1
    self.Elimination_list = []
  # Insert an element in the list
  def insert ( self, item ):
    newLink = Link (item)
    current = self.first
    previous = self.first

    if (current == None):
        self.first = newLink
        newLink.next = newLink
        self.numLinks += 1
        return

    while (current.next != previous):
        current = current.next

    current.next = newLink
    newLink.next = previous
    self.numLinks += 1

    
  # Find the link with the given key
  def find ( self, item ):
    current = self.first.next

    if (current == None):
      return None

    while (current.item != item):
      if (current.item == None):
        return None
      else:
        current = current.next
 
    return current	
  # Delete a link with a given key
  def delete ( self, item ):
    current = self.first
    previous = self.first.next
    while (previous.next != self.first):
        previous = previous.next

    if (current.item == item):
        previous.next = current.next
        self.numLinks -= 1

    current = current.next
    previous = previous.next
    while (current.item != item and current != self.first):
        current = current.next
        previous = previous.next

    if (current.item == item):
        previous.next = current.next
        self.numLinks -= 1

  # Delete the nth link starting from the Link start 
  # Return the next link from the deleted Link
  def deleteAfter ( self, start, n ):  
    numLinks = 1
    After_start = 0
    current = self.first.next
    while (current != self.first):
        current = current.next
    while (current.item != start):
        current = current.next
    while (numLinks == 1):    
        if (current.item == start or After_start == 1): 
            while (numLinks != n):
                if (current.item == None):
                    current = current.next
                numLinks += 1
                current = current.next   
            if (numLinks == n):
                if (current.item == None):
                    current = current.next			
                self.Elimination_list.append(current.item)
                CircularList.delete(self, current.item)
                current = current.next
                numLinks = 1
                After_start = 1
            if (self.numLinks == 2):
                return
        else:
            current = current.next
            
            
  # Return a string representation of a Circular List
  def __str__ ( self ):
    s = ''  
    current = self.first.next
    for i in range(len(self.Elimination_list)):
        s += str (self.Elimination_list[i]) + ' '
    if (current.item != None):
        r = '\n' + str (current.item)
    else:
        current = current.next
    return s + r
	
def main():
#Open File and storing values
    in_file = open('josephus.txt', 'r')
    first = in_file.readline()
    first = first.strip()
    first = first.split()
    soldiers = int(first[0])
    second = in_file.readline()
    second = second.strip()
    second = second.split()
    start = int(second[0])
    third = in_file.readline()
    third = third.strip()
    third = third.split()
    n = int(third[0])
#Close File	
    in_file.close()
#Create a CircularList object and using deleteAfter function to print out required solution	
    list = CircularList()
    for i in range(1, soldiers+1):
        list.insert(i)   
    list.deleteAfter(start, n)
    print (list)
main()