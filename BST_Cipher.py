#  File: BST_Cipher.py

#  Description: Encryption / Decryption with Binary Search Trees 

#  Student Name: Junaid K. Jumani

#  Student UT EID: jkj696

#  Partner Name:

#  Partner UT EID:

#  Course Name: CS 313E

#  Unique Number: 50945

#  Date Created: April 29th, 2016

#  Date Last Modified: April 30th, 2016

class Node(object):
  def __init__(self, data):
    self.data = data
    self.lChild = None
    self.rChild = None	
	
class Tree (object):
  # the init() function creates the binary search tree with the
  # encryption string. If the encryption string contains any
  # character other than the characters 'a' through 'z' or the
  # space character drop that character.
  def __init__ (self):
    self.root = None
  # the insert() function adds a node containing a character in
  # the binary search tree. If the character already exists, it
  # does not add that character. There are no duplicate characters
  # in the binary search tree.
  def insert (self, ch):
    newNode = Node (ch)	
    if (self.root == None):
      self.root = newNode
    else:
      current = self.root
      parent = self.root
      while (current != None):
        parent = current
        if (ord(ch) < ord(current.data)):
          current = current.lChild
        elif (ord(ch) == ord(current.data)):
          return    
        else:
          current = current.rChild

      if (ord(ch) < ord(parent.data)):
        parent.lChild = newNode
      else:
        parent.rChild = newNode   
  # the search() function will search for a character in the binary
  # search tree and return a string containing a series of lefts
  # (<) and rights (>) needed to reach that character. It will
  # return a blank string if the character does not exist in the tree.
  # It will return * if the character is the root of the tree.

  def search (self, ch): 
    s = ""
    current = self.root
    if (ord(current.data) == ord(ch)):
      return '*' + '!'	
    while ((current != None) and (ord(current.data) != ord(ch))):
      if (ord(ch) < ord(current.data)):
        current = current.lChild
        s += '<'
      else:
        current = current.rChild
        s += '>'		
    return s + '!'
  # the traverse() function will take string composed of a series of
  # lefts (<) and rights (>) and return the corresponding 
  # character in the binary search tree. It will return an empty string
  # if the input parameter does not lead to a valid character in the tree.
  def traverse (self, st):
    a = ''
    current = self.root
    if (current != None):
      for i in st:  
        if (i == '*'):
          return current.data
        if (i == '<'):
          current = current.lChild
        if (i == '>'):
      	  current = current.rChild
      a += current.data 
      return a	
  # the encrypt() function will take a string as input parameter, convert
  # it to lower case, and return the encrypted string. It will ignore
  # all digits, punctuation marks, and special characters.
  def encrypt (self, st):
    string = '' 
    for i in st:
      string += self.search(i)	  
    string = string[:-1] 
    print(string, end ="") 
  # the decrypt() function will take a string as input parameter, and
  # return the decrypted string.
  def decrypt (self, st):
    s = '' 
    st = st + '!'	
    for i in st:
      if (i != '!'):	
        s += i
      else:    
        print(self.traverse(s), end ="")
        s = '' 		

def main():
#User input the string to encrypt, key is provided
  key = 'the quick brown fox jumps over the lazy dog'
  encrypt_str = str(input('Enter string to be encrypted : '))
#Drop digits, punctuation marks and special characters from string that is to be encryoted  
  for i in range (0, 10):
    i = str(i)  
    if (i in encrypt_str):
      encrypt_str = encrypt_str.replace(i, '')
  for i in encrypt_str:
    a = i.lower()
    if (i in [',',"'", '!']):
      a = ''
    encrypt_str = encrypt_str.replace(i, a)	
#create Tree
  enr = Tree()
#Insert key into Binary Tree  
  for i in key:
    enr.insert(i)
#Print Encrypted String	
  print ('Encrypted string: ', end='')	
  enr.encrypt(encrypt_str)
  print()  
  print()
#User input the string to decrypt,  
  decrypt_str = str(input('Enter string to be decrypted : '))
#Print decrypted String  
  print ('Decrypted string: ', end='')  
  enr.decrypt (decrypt_str)  
main()    