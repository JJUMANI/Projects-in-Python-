#  File: TestCipher.py

#  Description: This program reads through a text file called "cipher.txt". The first line is encoded using the substitution cipher.
#				The second line is decoded also using the substitution cipher. The third and fourth lines are encoded and decoded 
#				using the Vigenere cipher. The program returns the correct encoded and decoded lines. 

#  Student Name: Junaid K. Jumani

#  Student UT EID: jkj696

#  Partner Name: Justin Lyan

#  Partner UT EID: jl38965

#  Course Name: CS 313E

#  Unique Number: 50945

#  Date Created: March 27, 2016

#  Date Last Modified: March 30, 2016

def substitution_encode ( strng ):
#Create list 'words'
  words = []
  cipher = ['q', 'a', 'z', 'w', 's', 'x', 'e', 'd', 'c', 'r', 'f', 'v', 't', 'g', 'b', 'y', 'h', 'n', 'u', 'j', 'm', 'i', 'k', 'o', 'l', 'p']
#Using for loop to append encrypted text into 'words' list and joining all elements in list 
  for i in strng:
    if (i == ' ' or i == '!' or i == '.' or i.isdigit() or i == ','):
      words.append(i)
    else:  
      idx = ord (i.lower()) - ord ('a')
      words.append(cipher[idx])
  words = ''.join(words)	
  return words	
def substitution_decode ( strng ):
#Create list 'words'
  words = []
  plain = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',  's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
  cipher = ['q', 'a', 'z', 'w', 's', 'x', 'e', 'd', 'c', 'r', 'f', 'v', 't', 'g', 'b', 'y', 'h', 'n', 'u', 'j', 'm', 'i', 'k', 'o', 'l', 'p']
#Using for loop to append encrypted text into 'words' list and joining all elements in list 
  for i in strng: 
    if (i == ' ' or i == '!' or i == '.' or i.isdigit() or i == ','):
      words.append(i)
    else:  
      for n in range (len(cipher)):	
        if (i == cipher[n]):  
          words.append(plain[n])
  words = ''.join(words)	
  return words

def vigenere_encode ( strng, passwd ):
  q = 0    
  first = 0      
  words = []
  plain = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',  's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# Using for loop to append the encrypted letter in a list and then converting or joining into strings  
  for i in strng:  
    if (i == ' ' or i == '!' or i == '.' or i.isdigit() or i == ','):
      words.append(i)
    else:  
      if (q == passwd[-1]):
        first = 0
        q = passwd[first]
        idx_strng = ord(i.lower()) - ord('a')
        idx = ord(q.lower()) - ord('a') + idx_strng
        if (idx >= 26):
          idx = idx - 26    
          first += 1  
          words.append(plain[idx])
        else:  
          first += 1  
          words.append(plain[idx])    
      else:    
        q = passwd[first]
        idx_strng = ord(i.lower()) - ord('a')
        idx = ord(q.lower()) - ord('a') + idx_strng
        if (idx >= 26):
          idx = idx - 26    
          first += 1  
          words.append(plain[idx])
        else:  
          first += 1  
          words.append(plain[idx])    
  words = ''.join(words)
  return words

def vigenere_decode ( strng, passwd ):
  q = 0    
  first = 0      
  words = []
  plain = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',  's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# Using for loop to append the non-encrypted letter in a list and then converting or joining into strings    
  for i in strng:  
    if (i == ' ' or i == '!' or i == '.' or i.isdigit() or i == ','):
      words.append(i)
    else:  
      if (q == passwd[-1]):
        first = 0
        q = passwd[first]
        idx = ord(i.lower()) - ord(q.lower())  
        first += 1  
        words.append(plain[idx]) 
      else:    
        q = passwd[first]
        idx = ord(i.lower()) - ord(q.lower())
        first += 1  
        words.append(plain[idx])    
  words = ''.join(words)
  return words

def main():
  # open file for reading
  in_file = open ("./cipher.txt", "r")

  # print header for substitution cipher
  print ("Substitution Cipher")
  print ()

  # read line to be encoded
  line = in_file.readline()
  line = line.strip()

  # encode using substitution cipher
  encoded_str = substitution_encode (line)

  # print result
  print ("Plain Text to be Encoded: " + line)
  print ("Encoded Text: " + encoded_str)
  print ()

  # read line to be decoded
  line = in_file.readline()
  line = line.strip()

  # decode using substitution cipher
  decoded_str = substitution_decode (line)

  # print result
  print ("Encoded Text to be Decoded: " + line)
  print ("Decoded Plain Text: " + decoded_str)
  print ()

  # print header for vigenere cipher
  print ("Vigenere Cipher")
  print ()

  # read line to be encoded and pass phrase
  line = in_file.readline()
  line = line.strip()
  passwd = in_file.readline()
  passwd = passwd.strip()

  # encode using vigenere cipher
  encoded_str = vigenere_encode (line, passwd)

  # print result
  print ("Plain Text to be Encoded: " + line)
  print ("Pass Phrase (no spaces allowed): " + passwd)
  print ("Encoded Text: " + encoded_str)
  print ()

  # read line to be decoded and pass phrase
  line = in_file.readline()
  line = line.strip()
  passwd = in_file.readline()
  passwd = passwd.strip()

  # decode using vigenere cipher
  decoded_str = vigenere_decode (line, passwd)

  # print result
  print ("Encoded Text to be Decoded: " + line)
  print ("Pass Phrase (no spaces allowed): " + passwd)
  print ("Decoded Plain Text: " + decoded_str)
  print ()

  # close file
  in_file.close()

main()