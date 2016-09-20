#  File: Graph.py

#  Description: Create Graph using information in graph.txt file

#  Student Name: Junaid K. Jumani

#  Student UT EID: jkj696

#  Course Name: CS 313E

#  Unique Number: 50945

#  Date Created: May 7th, 2016

#  Date Last Modified: May 9th, 2016

class Stack (object):
  def __init__ (self):
    self.stack = []

  # add an item to the top of the stack
  def push (self, item):
    self.stack.append ( item )

  # remove an item from the top of the stack
  def pop (self):
    return self.stack.pop()

  # check what item is on top of the stack without removing it
  def peek (self):
    return self.stack[len(self.stack) - 1]

  # check if a stack is empty
  def isEmpty (self):
    return (len(self.stack) == 0)

  # return the number of elements in the stack
  def size (self):
    return (len(self.stack))

class Queue (object):
  def __init__ (self):
    self.queue = []

  def enqueue (self, item):
    self.queue.append (item)

  def dequeue (self):
    return (self.queue.pop(0))

  def isEmpty (self):
    return (len (self.queue) == 0)

  def size (self):
    return len (self.queue)

class Vertex (object):
  def __init__ (self, label):
    self.label = label
    self.visited = False

  # determine if a vertex was visited
  def wasVisited (self):
    return self.visited

  # determine the label of the vertex
  def getLabel (self):
    return self.label

  # string representation of the Vertex
  def __str__ (self):
    return str(self.label)

class Graph (object):
  def __init__ (self):
    self.Vertices = []
    self.adjMat = []

  # check if a vertex already exists in the graph
  def hasVertex (self, label):
    nVert = len (self.Vertices)
    for i in range (nVert):
      if (label == (self.Vertices[i]).label):
        return True
    return False

  # given a label get the index of a Vertex
  def getIndex (self, label):
    nVert = len (self.Vertices)
    for i in range (nVert):
      if ((self.Vertices[i]).label == label):
        return i
    return -1

  # add a Vertex with a given label to the graph
  def addVertex (self, label):
    if not self.hasVertex (label):
      self.Vertices.append (Vertex (label))

      # add a new column in the adjacency matrix for the new Vertex
      nVert = len (self.Vertices)
      for i in range (nVert - 1):
        (self.adjMat[i]).append (0)

      # add a new row for the new Vertex in the adjacency matrix
      newRow = []
      for i in range (nVert):
        newRow.append (0)
      self.adjMat.append (newRow)

  # add weighted directed edge to graph
  def addDirectedEdge (self, start, finish, weight = 1):
    self.adjMat[start][finish] = weight

  # add weighted undirected edge to graph
  def addUndirectedEdge (self, start, finish, weight = 1):
    self.adjMat[start][finish] = weight
    self.adjMat[finish][start] = weight

  # return an unvisited vertex adjacent to vertex v
  def getAdjUnvisitedVertex (self, v):
    nVert = len (self.Vertices)
    for i in range (nVert):
      if (self.adjMat[v][i] > 0) and (not (self.Vertices[i]).wasVisited()):
        return i
    return -1

  # do depth first search in a graph
  def dfs (self, v):
    # create a stack
    theStack = Stack()

    # mark vertex as visited and push on the stack
    (self.Vertices[v]).visited = True
    print (self.Vertices[v])
    theStack.push (v)

    while (not theStack.isEmpty()):
      # get an adjacent unvisited vertex
      u = self.getAdjUnvisitedVertex(theStack.peek())
      if (u == -1): 
        u = theStack.pop()
      else:
        (self.Vertices[u]).visited = True
        print (self.Vertices[u])
        theStack.push(u)

    # the stack is empty, let us reset the flags
    nVert = len (self.Vertices)
    for i in range (nVert):
      (self.Vertices[i]).visited = False

  # do breadth first search in a graph
  def bfs (self, v):
    # create a Queue
    theQueue = Queue()

    # to be completed in a similar manner to dfs
    (self.Vertices[v]).visited = True
    print (self.Vertices[v])
    theQueue.enqueue (v)

    while (not theQueue.isEmpty()):
      # get an adjacent unvisited vertex
      u = self.getAdjUnvisitedVertex(theQueue.queue[0])
      if (u == -1): 
        u = theQueue.dequeue()
      else:
        (self.Vertices[u]).visited = True
        print (self.Vertices[u])
        theQueue.enqueue(u)
  def getVertices (self):
    Vertices_copy = []
    for i in range (len(self.Vertices)):
      Vertices_copy.append(self.Vertices[i])
    return Vertices_copy
  def getEdgeWeight (self, fromVertexLabel, toVertexLabel):
    start =  getIndex (fromVertexLabel) 
    finish = getIndex (toVertexLabel) 
    return self.adjMat[start][finish]
  def getNeighbors (self, vertexLabel):
    lab = self.getIndex (vertexLabel)
    neighbors = []
    for i in range (self.adjMat[lab]):	
      if (self.adjMat[lab][i] == 1):
        neighbors.append(self.adjMat[lab][i]) 
    return neighbors
  def hasCycle (self):
    theStack = Stack()
    return True
  def deleteEdge (self, fromVertexLabel, toVertexLabel):
    start =  self.getIndex (fromVertexLabel) 
    finish = self.getIndex (toVertexLabel) 
    self.adjMat[start][finish] = 0
#  def deleteVertex (self, vertexLabel):
  def toposort (self, startIndex):
    topsort_list = []
    a = self.dfs (startIndex)
    topsort_list.append(a)
    return topsort_list	
  def deleteVertex (self, vertexLabel):
    start =  self.getIndex (vertexLabel)  
    for i in range(len(self.Vertices)): 
      del self.adjMat[i][start]
    del self.adjMat[start]  
def main():
  # create a Graph object
  cities = Graph()

  # open file for reading 
  inFile = open ("./graph.txt", "r")

  # read the vertices
  numVertices = int ((inFile.readline()).strip())

  for i in range (numVertices):
    city = (inFile.readline()).strip()
    cities.addVertex (city)
 
  # read the edges
  numEdges = int ((inFile.readline()).strip())

  for i in range (numEdges):
    edge = ((inFile.readline()).strip())

    edge = edge.split()
    start = int (edge[0])
    finish = int (edge[1])
    weight = int (edge[2])

    cities.addDirectedEdge (start, finish, weight)
  print ()	
  print ("UnDirected graph")
  # print the adjacency matrix
  print ("\nAdjacency Matrix")
  for i in range (numVertices):
    for j in range (numVertices):
      print (cities.adjMat[i][j], end = ' ')
    print()
  print()

  # read the starting vertex for dfs and bfs
  startVertex = (inFile.readline()).strip()

  # get index of the start index
  startIndex = cities.getIndex (startVertex)

  # do depth first search
  print ("\nDepth First Search from " + startVertex)
  cities.dfs (startIndex)
  print()

  # do breadth first search
  print ("\nBreadth First Search from " + startVertex)
  cities.bfs (startIndex)
  print()
  print ()
  print ("Directed graph")
  
    # create a Graph object
  cities1 = Graph()
  # read the vertices
  numVertices = int ((inFile.readline()).strip())

  for i in range (numVertices):
    city = (inFile.readline()).strip()
    cities1.addVertex (city)
 
  # read the edges
  numEdges = int ((inFile.readline()).strip())

  for i in range (numEdges):
    edge = ((inFile.readline()).strip())

    edge = edge.split()
    start = int (edge[0])
    finish = int (edge[1])
    weight = int (edge[2])

    cities1.addDirectedEdge (start, finish, weight)
  print ()	
  # print the adjacency matrix
  print ("\nAdjacency Matrix")
  for i in range (numVertices):
    for j in range (numVertices):
      print (cities1.adjMat[i][j], end = ' ')
    print()
  print()
    # read the starting vertex for dfs and bfs
  startVertex = (inFile.readline()).strip()

  # get index of the start index
  startIndex = cities1.getIndex (startVertex)
  print ("\nDepth First Search from " + startVertex)
  cities1.dfs (startIndex)
  print()

  # do breadth first search
  print ("\nBreadth First Search from " + startVertex)
  cities1.bfs (startIndex)
  print()
  print ()
  print ("Removed edge from B to F")
  b = cities1.deleteEdge ('B', 'F')
  print ("\nAdjacency Matrix")
  for i in range (numVertices):
    for j in range (numVertices):
      print (cities1.adjMat[i][j], end = ' ')
    print()
  print()
  print ("Removed vertex A")  
  c = cities1.deleteVertex ('A')
  print ("\nAdjacency Matrix")
  for i in range (numVertices - 1):
    for j in range (numVertices - 1):
      print (cities1.adjMat[i][j], end = ' ')
    print()
  print()    
main()
