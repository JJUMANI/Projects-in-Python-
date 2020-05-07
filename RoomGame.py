class Room:
    def __init__(self,name,north,east,south,west,up,down, contents): #add code here
        self.name = name
        self.north = north
        self.east = east
        self.south = south
        self.west = west
        self.up = up
        self.down = down
        self.contents = contents

    def displayRoom(self): #add code here

        if self.name != "None":
            print("Room name: %s "  %(self.name))  
        if self.north != "None":
            print("   Room to the north: %s " %(self.north))  
        if self.east != "None":
            print("   Room to the east:  %s " %(self.east))  
        if self.south != "None":
            print("   Room to the south: %s " %(self.south)) 
        if self.west != "None":
            print("   Room to the west:  %s " %(self.west))
        if self.up != "None":
            print("   Room above:        %s " %(self.up))
        if self.down != "None":
            print("   Room below:        %s " %(self.down)) 
        if self.contents != "None": 
            print("   Room contents:        %s " %(self.contents)) 
        print("\n")

def createRoom(roomData): #add code here
    if(len(roomData) > 7):
        roomContents = []
        for i in range(7,len(roomData)):
            content = roomData[i]
            roomContents.append(content)
    else:
        roomContents = []        
    roomInst = Room (roomData[0], roomData[1], roomData[2], roomData[3], roomData[4], roomData[5], roomData[6], roomContents) 
    return roomInst

def look(): #add code here
    print("You are currently in the %s" %(current.name))
    print("Contents of the room:")
    if(current.contents != []):
        for i in current.contents:
            print(i)
    else:
        print("None")        


def getRoom(name): #add code here
    for rooms in floorPlan:
        if rooms.name == name:
            return rooms

def move(direction): #add code here
    directions=["north", "east", "south", "west", "up", "down"]
    directionValues=[current.north, current.east, current.south, current.west, current.up, current.down]
    directionIdx = 0
    flag = 0

    for idx in range(len(directions)):
        if direction == directions[idx]:
            directionIdx = idx
            flag = 1
            break

    foundDirectionvalue = directionValues[idx]

    if foundDirectionvalue != "None":
        roomObj = getRoom(foundDirectionvalue)
        print("You are now in the %s." % (roomObj.name))
        return roomObj
    else:
        print("You can't move in that direction.")
        return current


def displayAllRooms(): #add code here
    for room in floorPlan:
        room.displayRoom()




def loadMap():

    global floorPlan    # make the variable "floorPlan" a global variable

    inFile = open ("./RoomData.txt", "r")

    room1 = inFile.readline()
    room1 = room1.strip()
    room1 = room1.split(",")
    room2 = inFile.readline()
    room2 = room2.strip()
    room2 = room2.split(",")    
    room3 = inFile.readline()
    room3 = room3.strip()
    room3 = room3.split(",")    
    room4 = inFile.readline()
    room4 = room4.strip()
    room4 = room4.split(",")    
    room5 = inFile.readline()
    room5 = room5.strip()
    room5 = room5.split(",")    
    room6 = inFile.readline()
    room6 = room6.strip()
    room6 = room6.split(",")    
    room7 = inFile.readline()
    room7 = room7.strip()
    room7 = room7.split(",")    






    floorPlan = [createRoom(room1),createRoom(room2),createRoom(room3),createRoom(room4),createRoom(room5),createRoom(room6),createRoom(room7)]
def pickup(itemPick):
    if(itemPick in current.contents):
        current.contents.remove(itemPick)
        inventory.append(itemPick)
        print("You now have the",itemPick)
    else:
        print("That item is not in this room.")    

def drop(itemDrop):

    if(itemDrop in inventory):
        inventory.remove(itemDrop)
        current.Contents.append(itemDrop)
        print("You have dropped the ITEM.")
    else:
        print("You don't have that item.")   

def listInventory():

    if(inventory == []):
        print("You are currently carrying:")
        print("nothing.")
    else:
        print("You are currently carrying:")
        for i in inventory:
            print(i)            

def main ():

    global current       # make the variable "floorPlan" a global variable

    global inventory     

    inventory = []

 #   pickup()

 #   drop()

 #   listInventory()

    loadMap()

    displayAllRooms()

    # TEST CODE: walk around the house

    current = floorPlan[0] #start in the living room
    look() # Living Room
    item = ""
    txt = input("Enter a command: ") 
    while(txt != "exit"):
        if(txt == "help"):
            print("look:        display the name of the current room and its contents")
            print("north:       move north") 
            print("east:        move east ")
            print("south:       move south")
            print("west:        move west ")    
            print("up:          move up")
            print("down:        move down")
            print("inventory:   list what items you're currently carrying")
            print("get <item>:  pick up an item currently in the room")
            print("drop <item>: drop an item you're currently carrying")
            print("help:        print this list")
            print("exit:        quit the game")
            txt = input("Enter a command: ") 
        if(txt == "look"):
            look()
            txt = input("Enter a command: ")    
        if(txt == "north"):
            current = move("north")
            txt = input("Enter a command: ")
        if(txt == "east"):
            current = move("east")
            txt = input("Enter a command: ")
        if(txt == "south"):
            current = move("south")
            txt = input("Enter a command: ")
        if(txt == "west"):
            current = move("west")
            txt = input("Enter a command: ")
        if(txt == "up"):
            current = move("up")
            txt = input("Enter a command: ")
        if(txt == "down"):
            current = move("down")
            txt = input("Enter a command: ")
        if(txt == "inventory"):
            listInventory()
            txt = input("Enter a command: ")
        if(txt[0:3] == "get"):        
            item = txt[4:]
            item = '"'+str(item)+'"'
            pickup(item)
            txt = input("Enter a command: ")
        if(txt[0:4] == "drop"):
            item = txt[5:]
            item = '"'+str(item)+'"'
            drop(item)
            txt = input("Enter a command: ")

    print("Quitting  game") 
    exit()                                              
main()
