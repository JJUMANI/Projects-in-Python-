#  File: TestBinaryTree.py

#  Description: Creating and Testing Binary Tree

#  Student Name: Junaid K. Jumani

#  Student UT EID: jkj696

#  Course Name: CS 313E

#  Unique Number: 50945

#  Date Created: April 26th, 2016

#  Date Last Modified: April 28th, 2016

class Node (object):
  def __init__ (self, data):
    self.data = data
    self.lChild = None
    self.rChild = None

class Tree (object):
  def __init__ (self):
    self.root = None

  # Search for a node with the key
  
  def search (self, key):
    current = self.root
    while ((current != None) and (current.data != key)):
      if (key < current.data):
        current = current.lChild
      else:
        current = current.rChild
    return current

  # Insert a node in the tree
  def insert (self, val):
    newNode = Node (val)
    if (self.root == None):
      self.root = newNode
    else:
      current = self.root
      parent = self.root
      while (current != None):
        parent = current
        if (val < current.data):
          current = current.lChild
        else:
          current = current.rChild

      if (val < parent.data):
        parent.lChild = newNode
      else:
        parent.rChild = newNode
  
  def delete (self, key):
    deleteNode = self.root
    parent = self.root
    isLeft = False

    # If empty tree
    if (deleteNode == None):
      return False

    # Find the delete node
    while ((deleteNode != None ) and (deleteNode.data != key)):
      parent = deleteNode
      if (key < deleteNode.data):
        deleteNode = deleteNode.lChild
        isLeft = True
      else:
        deleteNode = deleteNode.rChild
        isLeft = False
      
    # If node not found
    if (deleteNode == None):
      return False

    # Delete node is a leaf node
    if ((deleteNode.lChild == None) and (deleteNode.rChild == None)):
      if (deleteNode == self.root):
        self.root = None
      elif (isLeft):
        parent.lChild = None
      else:
        parent.rChild = None

    # Delete node is a node with only left child
    elif (deleteNode.rChild == None):
      if (deleteNode == self.root):
        self.root = deleteNode.lChild
      elif (isLeft):
        parent.lChild = deleteNode.lChild
      else:
        parent.rChild = deleteNode.lChild

    # Delete node is a node with only right child
    elif (deleteNode.lChild == None):
      if (deleteNode == self.root):
        self.root = deleteNode.rChild
      elif (isLeft):
        parent.lChild = deleteNode.rChild
      else:
        parent.rChild = deleteNode.rChild

    # Delete node is a node with both left and right child
    else:
      # Find delete node's successor and successor's parent nodes
      successor = deleteNode.rChild
      successorParent = deleteNode

      while (successor.lChild != None):
        successorParent = successor
        successor = successor.lChild

      # Successor node right child of delete node
      if (deleteNode == self.root):
        self.root = successor
      elif (isLeft):
        parent.lChild = successor
      else:
        parent.rChild = successor

      # Connect delete node's left child to be successor's left child
      successor.lChild = deleteNode.lChild

      # Successor node left descendant of delete node
      if (successor != deleteNode.rChild):
        successorParent.lChild = successor.rChild
    successor.rChild = deleteNode.rChild

    return True  

  # In order traversal - left, center, right
  def inOrder (self, aNode):
    if (aNode != None):
      inOrder (aNode.lChild)
      print (aNode.data)
      inOrder (aNode.rChild)

  # Pre order traversal - center, left, right
  def preOrder (self, aNode):
    if (aNode != None):
      print (aNode.data)
      preOrder (aNode.lChild)
      preOrder (aNode.rChild)

  # Post order traversal - left, right, center
  def postOrder (self, aNode):
    if (aNode != None):
      postOrder (aNode.lChild)
      postOrder (aNode.rChild)
      print (aNode.data)

  # Find the node with the smallest value
  def minimum (self):
    current = self.root
    parent = current
    while (current != None):
      parent = current
      current = current.lChild
    return parent

  # Find the node with the largest value
  def maximum (self):
    current = self.root
    parent = current
    while (current != None):
      parent = current
      current = current.rChild
    return parent

  # Delete a node with a given key

  def recurse (self, current, current1):
    if (current == None and current1 == None):
      return True 
    elif ((current1 == None and current != None) or (current == None and current1 != None)):
      return False
    elif(current1.data != current.data):
      return False	
    else:
      return (self.recurse (current.lChild, current1.lChild) or self.recurse (current.rChild, current1.rChild))	
  # Returns true if two binary trees are similar
  def isSimilar (self, pNode):
    current = self.root
    current1 = pNode.root
    return self.recurse (current, current1)
	

  # Prints out all nodes at the given level
  def printLevel (self, level): 
    current = self.root
    if (level == 0):
      print (current.data) 	
      return 
    else:	
      self.print_Sub_Level(level - 1, current.lChild) 
      self.print_Sub_Level(level - 1, current.rChild)	
  def print_Sub_Level (self, level, current): 
    if (current == None):
      return	
    if (level == 0):
      print (current.data," ", end ="")	
      return
    else:	
      self.print_Sub_Level(level - 1, current.lChild)
      self.print_Sub_Level(level - 1, current.rChild)	  
  # Returns the height of the tree
  def getHeight (self): 
    current = self.root
    if (current == None):
      return 0
    else:
      return 1 + (self.get_Sub_Height(current.lChild) or self.get_Sub_Height(current.rChild))	
  def get_Sub_Height (self, current):
    if (current == None):
      return 0
    else:
      return 1 + (self.get_Sub_Height(current.lChild) or self.get_Sub_Height(current.rChild))  
  # Returns the number of nodes in the left subtree and
  # the number of nodes in the right subtree
  def numNodes (self):
    current = self.root
    if (current == None):
      return 0
    else:
      return 1 + (self.num_Sub_Nodes(current.lChild) + self.num_Sub_Nodes(current.rChild))
  def num_Sub_Nodes (self, current):
    if (current == None):
      return 0
    else:
      return 1 + (self.num_Sub_Nodes(current.lChild) + self.num_Sub_Nodes(current.rChild))	
def main():
  # Create three trees - two are the same and the third is different  
  Tree1 = Tree()
  Tree2 = Tree()
  Tree3 = Tree()
  Tree1.insert(50)
  Tree1.insert(30)
  Tree1.insert(70)
  Tree1.insert(10)
  Tree1.insert(40)
  Tree1.insert(60)
  Tree1.insert(80)
  Tree1.insert(7)
  Tree1.insert(25)
  Tree1.insert(38)
  Tree1.insert(47)
  Tree1.insert(58)
  Tree1.insert(65)
  Tree1.insert(77)
  Tree1.insert(96)
  
  Tree2.insert(50)
  Tree2.insert(30)
  Tree2.insert(70)
  Tree2.insert(10)
  Tree2.insert(40)
  Tree2.insert(60)
  Tree2.insert(80)
  Tree2.insert(7)
  Tree2.insert(25)
  Tree2.insert(38)
  Tree2.insert(47)
  Tree2.insert(58)
  Tree2.insert(65)
  Tree2.insert(77)
  Tree2.insert(96)
  
  Tree3.insert(50)
  Tree3.insert(60)
  Tree3.insert(74)
  Tree3.insert(28)
  Tree3.insert(86)
  Tree3.insert(5)
  Tree3.insert(15)
  Tree3.insert(14)
  Tree3.insert(56)
  Tree3.insert(25)
  Tree3.insert(8)
  Tree3.insert(87)
  Tree3.insert(44)
  Tree3.insert(67)
  Tree3.insert(34)  
    # Test your method isSimilar()
  a = Tree1.isSimilar (Tree2)
  print ("Is Tree1 Similiar to Tree2 =", a)
  a1 = Tree1.isSimilar (Tree3)
  print ("Is Tree1 Similiar to Tree3 =", a1)
    # Print the various levels of two of the trees that are different
  print ("Tree1 Nodes on Level 2")	
  b = Tree1.printLevel (2)
  print (" ")
  print ("Tree3 Nodes on Level 3")
  c = Tree3.printLevel (3)
    # Get the height of the two trees that are different
  print (" ")	
  d = Tree1.getHeight ()
  print ("Height of Tree 1 =", d)
  e = Tree3.getHeight ()
  print ("Height of Tree 3 =", e)
    # Get the number of nodes in the left and right subtree
  f = Tree1.numNodes ()
  print ('Number of nodes in Tree1 =', f)
main()  