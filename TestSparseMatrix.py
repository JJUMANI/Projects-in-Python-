
#  File: TestSparseMatrix.py

#  Description: Testing Sparse Matrix

#  Student Name: Junaid K. Jumani

#  Student UT EID: jkj696

#  Partner Name: Aya Seidemann 

#  Partner UT EID: ags2269

#  Course Name: CS 313E

#  Unique Number: 50945

#  Date Created: April 12, 2016

#  Date Last Modified: April 14, 2016

class Link (object):
  def __init__ (self, row, col, data, next = None):
    self.row = row
    self.col = col
    self.data = data
    self.next = None

  def __str__ (self):
    s = ''
    return s

class SparseMatrix (object):
  def __init__ (self, row = 0, col = 0):
    self.num_rows = row		# number of rows
    self.num_cols = col		# number of columns
    self.matrix = None

  # setElement() perform an assignment operation a[i][j] = value
  # if value is 0 the link if it exists is deleted
  # if value is non zero then the current value is updated if a
  # link already exists or a new link is added
  def setElement (self, row, col, data):
    if (data == 0):
      self.deleteLink (row, col)
    else:
      self.insertLink (row, col, data)

  def insertLink (self, row, col, data):
    # do nothing if data = 0
    if (data == 0):
      return

    # create a new link
    newLink = Link (row, col, data)

    # if matrix is empty then the newLink is the first link
    if (self.matrix == None):
      self.matrix = newLink
      return

    # find position to insert
    previous = self.matrix
    current = self.matrix

    while ((current != None) and (current.row < row)):
      previous = current
      current = current.next

    # if the row is missing
    if ((current != None) and (current.row > row)):
      previous.next = newLink
      newLink.next = current
      return
  
    # on the row, search by column
    while ((current != None) and (current.col < col)):
      previous = current
      current = current.next

    # if link already there do not insert but reset data
    if ((current != None) and (current.row == row) and (current.col == col)):
      current.data = data
      return

    # now insert newLink
    previous.next = newLink
    newLink.next = current

  # deletes and returns a Link if it is there or None otherwise
  def deleteLink (self, row, col):
    current = self.matrix
    previous = self.matrix
    while (current != None):
      if (current.col == col and current.row == row):
        if (current == self.matrix):
          self.matrix = self.matrix.next
        else:
          previous.next = current.next
        return current
      else:
        previous = current
        current = current.next
    return None
      

  # return a row of the sparse matrix
  def getRow (self, row_num):
    # create a blank list
    a = []

    # search for the row
    current = self.matrix
    if (current == None):
      return a

    while ((current != None) and (current.row < row_num)):
      current = current.next

    if ((current != None) and (current.row > row_num)):
      for i in range (self.num_cols):
        a.append (0)
      return a

    if ((current != None) and (current.row == row_num)):
      for j in range (self.num_cols):
        if (current.col == j):
          a.append (current.data)
          current = current.next
        else:
          a.append (0)
      return a
        
  # return a column of the sparse matrix
  def getCol (self, col_num):
    a = []

    # search for the row
    current = self.matrix
    if (current == None):
      return a

    while ((current != None) and (current.col < col_num)):
      current = current.next

    if ((current != None) and (current.col > col_num)):
      for i in range (self.num_rows):
        a.append (0)
      return a

    if ((current != None) and (current.col == col_num)):
      for j in range (self.num_rows):
        if (current.col == j):
          a.append (current.data)
          current = current.next
        else:
          a.append (0)
      return a

  # add two sparse matrix
  def __add__ (self, other):
    if (self.num_rows != other.num_rows) or (self.num_cols != other.num_cols):
      return None

    mat = SparseMatrix (self.num_rows, self.num_cols)
    current = self.matrix
    current1 = other.matrix
	
    while (current != None and current1 != None):		
        if (current.row == current1.row):
          if (current.col == current1.col):
            sum = current.data + current1.data 
            mat.insertLink (current.row, current.col, sum)
            current = current.next
            current1 = current1.next
          elif (current.col < current1.col):
            sum = current.data 
            mat.insertLink (current.row, current.col, sum) 
            current = current.next			
          elif (current.col > current1.col):
            sum = current1.data 
            mat.insertLink (current1.row, current1.col, sum)
            current1 = current1.next	
        elif (current.row > current1.row):
          sum = current1.data 
          mat.insertLink (current1.row, current1.col, sum)
          current1 = current1.next			
        elif (current.row < current1.row):
          sum = current.data 
          mat.insertLink (current.row, current.col, sum)
          current = current.next			  
    if (current == None and current1 == None):
      return mat		  
    if (current == None):
      sum = current1.data 
      mat.insertLink (current1.row, current1.col, sum)
    if (current1 == None):
      sum = current.data 
      mat.insertLink (current.row, current.col, sum)
	  
    return mat
  def Search (self, row, col):
    current = self.matrix
    while (current != None):
      if (current.col == col and current.row == row):
        return current
      current = current.next
    return None
  # multiply two sparse matrices
  def __mul__ (self, other):
    if (self.num_cols != other.num_rows):
      return None
    mat = SparseMatrix (self.num_rows, other.num_cols)
    for i in range (self.num_rows):
      for j in range (other.num_cols):
        sum_n = 0
        for k in range(other.num_rows):
          first = self.Search(i,k)
          second = other.Search(k,j)		  
          if (first != None and second != None):	 		
            sum_n += first.data * second.data
        mat.setElement(i,j,sum_n)
    return mat
  # return a string representation of the matrix
  def __str__ (self):
    s = ''
    current = self.matrix

    # if the matrix is empty return blank string
    if (current == None):
      return s

    for i in range (self.num_rows):
      for j in range (self.num_cols):
        if ((current != None) and (current.row == i) and (current.col == j)):
          s = s + str (current.data).rjust(4)
          current = current.next
        else:
          s = s + "0".rjust(4)
      s = s + "\n"
    return s

def readMatrix (inFile):
  line = inFile.readline().rstrip("\n").split()
  row = int (line[0])
  col = int (line[1])
  mat = SparseMatrix (row, col)

  for i in range (row):
    line = inFile.readline().rstrip("\n").split()
    for j in range (col):
      elt = int(line[j])
      if (elt != 0):
        mat.insertLink (i, j, elt)
  line = inFile.readline()

  return mat
def main():  
  inFile = open ("matrix.txt", "r")

  print ("\nTest Matrix Addition")
  matA = readMatrix (inFile)
  print (matA)
  matB = readMatrix (inFile)
  print (matB)

  matC = matA + matB
  print (matC)

  print ("\nTest Matrix Multiplication")
  matP = readMatrix (inFile)
  print (matP)
  matQ = readMatrix (inFile)
  print (matQ)
  
  matR = matP * matQ
  print (matR)

  print ("\nTest Setting a Zero Element to a Non-Zero Value")
  matA.setElement (1, 1, 5)
  print (matA)

  print ("\nTest Setting a Non-Zero Element to Zero")
  matA.setElement (1, 1, 0)
  print (matA)

  print ("\nTest Getting a Row")
  row = matP.getRow(1)
  print (row)

  print ("\nTest Getting a Column")
  col = matQ.getCol(0)
  print (col)

  inFile.close()
main()
