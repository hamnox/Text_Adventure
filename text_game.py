#import pudb #this is for debugging
 # import 

import hams_parser as parsy
def move():
    # get location
    # check location_exists
    # check walls
    # move location
    print "You have moved!"
    return

def take():
    return

def list_inventory():
    print locations.append[-1] # inventory
    return

"""def invert_Dict(dictionary):
    return dict([v,k] for k,v in mydict.iteritems())
    """

class World(object):
    def __init__(self,name,map_size=(10,10),startLocation=(1,1)):
        # change this to a for loop to make dictionary, generate a room.
        self.Locations = {}
        #[row[i] for row in map_size[0]]
        #          for i in range(len(map_size[1]+1)):""}

        # print range(1,map_size[0]+1)
        for x in range(1,map_size[0]+1):
          for y in range(1,map_size[1]+1):
            self.Locations[(x,y)] = Room(self,(x,y),"Room "+str(x)+"-"+str(y),"Nothing to see here.")

        self.Locations["Inventory"] = Room(self,"Inventory",name="Inventory",description="Where all your stuff is kept")
        self.Locations["Ether"] = Room(self,"Ether",name="Ether",description="The land of hidden things")

        # the last location is a list.
        print "Welcome to the wonderful world of {}!".format(name)
        self.maplinks()
        
    def maplinks(self): # add init=True):
        for coord, room in self.Locations.items():
            for direction,location_offset in [["North",(1,0)],["South",(-1,0)],["East",(1,0)],["West",(-1,0)]]:
                if isinstance(coord,tuple):
                    new_coords = (coord[0]+location_offset[0],coord[1]+location_offset[1])
                    try:
                        room.addmap(direction,new_coords)
                    except KeyError:
                        pass
        #someday it would be fun to allow rooms inside of rooms. But not today, PLEASE. 
        #http://pygame.org/wiki/2DVectorClass for offset?
    def getRoom(self,locationkey):
        return self.Locations[locationkey] #worried there is some funky behavior in passing a direct link...

class Room(object):
    #pudb.set_trace() #this is for debugging
    def __init__(self,world,location_key,name,description,items=[]):
        self.name = name # attribute name/description
        self.description = description
        self.items = [] # attribute items
        self.items.extend(items)
        self.world = world
        self.location = location_key
        self.doors = {}
        self.directions = {}
    #woah, woah woah woah woah--I should actually make Items generateable from the Room
    # instead of merely passing a list of pre-made references like I planned.
    
    def look(self):
        return self.description
    def relocate(location): #,swap=True):
        pass # add this later yo
    def addmap(self,direction,location): #hidden=False):
        self.doors[direction] = self.world.Locations[location] #make sure we test this against real locations first.
        #TODO actually, let's just add this into world later.
    def put(self,item):
        self.items.extend(item)
    def remove(self,item):
        self.items.remove(item)
        Map.Locations["Ether"].extend(item)

class Item(object):
    def __init__(self,name="Thing",location="Ether",description="A Thingy Thing"):
        self.name = name
        self.aliases = []
        self.location = location
        self.description = description
    # add match names to dictionary
    # attribute name/description
    # attribute hidden?
    # attribute interactable
    # attribute moveable
    # attribute location
    # function interact (look up dictionary list of terms)
    # function look
    # function use
    # function grok
    pass

class Character(Item):
    pass

import sys
thismodule = sys.modules[__name__]

TextLand = World("TextLand")

print "Hi, Welcome to TextLand! Who are you?\n"
username = raw_input("Name: ")
print "Hi %s" % (username)
user = Character(username,(0,0),"This person looks lot like you, except more 8-bit.")
# try:

while True:
    user_text = raw_input("\nWhat do?\n")
    cmd_pairs = parsy.x(user_text.lower()).toplevel()
    if cmd_pairs == "quit":
        print "byenow"
        exit()
    for pair in cmd_pairs:
        methodToCall = getattr(thismodule, pair[0])
        methodToCall(pair[1])
    
    """
    command = command.lower()
    if command=="quit":
        print "byenow"
        break
    if command in ("look", "see"):
        if eval(remaining) in TextLand.Locations: #fix this into something non-hackable and not assuming tuple
            print "\t" + TextLand.Locations[eval(remaining)].description,
        else:
            print remaining
    """