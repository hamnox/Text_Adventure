#import pudb #this is for debugging
 # import 
# THIS DOESN"T WORK WTF https://docs.python.org/2/tutorial/classes.html

def move():
    # get location
    # check location_exists
    # check walls
    # move location
    print "You have moved!"
    return

def take():
    return

def list():
    print locations.append[-1] # inventory
    return

"""def invertDict(dictionary):
    return dict([v,k] for k,v in mydict.iteritems())
    """
# add a parser!
class World(object):
    def __init__(self,name,map_size=(10,10),startLocation=(1,1)):
        # change this to a for loop to make dictionary, generate a room.
        self.Locations = {}
        #[row[i] for row in map_size[0]]
        #          for i in range(len(map_size[1]+1)):""}

        # print range(1,map_size[0]+1)
        for x in range(1,map_size[0]+1):
          for y in range(1,map_size[1]+1):
            self.Locations[(x,y)] = Room(self,(x,y),name="Room "+str(x)+"-"+str(y))

        self.Locations["Inventory"] = Room(self,"Inventory",name="Inventory",description="Where all your stuff is kept")
        self.Locations["Ether"] = Room(self,"Ether",name="Ether",description="The land of hidden things")

        # the last location is a list.
        print "Welcome to the wonderful world of {}!".format(name)
        self.maplinks()
        
    def maplinks(self): # add init=True):
        for coord, room in self.Locations.items():
            for direction,location_offset in [["North",(1,0)],["South",(-1,0)],["East",(1,0)],["West",(-1,0)]]:
                try:
                    room.addmap(direction,(coord[0]+location_offset[0],coord[1]+location_offset[1]))
                except:
                    pass
        #someday it would be fun to allow rooms inside of rooms. But not today, PLEASE.
#must next set up a function for getting a room from a location key.

class Room(object):
    #pudb.set_trace() #this is for debugging
    def __init__(self,world,location_key,items=[],name="The Void",description="Nothing here to see."):
        self.name = name # attribute name/description
        self.description = description
        self.items = [] # attribute items
        self.items.extend(items)
        self.world = world
        self.location = location_key
        self.doors = {}
        self.directions = {}
    
    def look(self):
        return self.description
    def relocate(location): #,swap=True):
        pass # add this later yo
    def addmap(self,direction,location): #hidden=False):
        self.doors[direction] = self.world.Locations[location] #make sure we test this against real locations first.
        #TODO actually, let's just add this into world later.
    def put(item):
        self.items.extend(item)
    def remove(item):
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

TextLand = World("TextLand")

print "Hi, Welcome to TextLand! Who are you?\n"
username = raw_input("Name: ")
print "Hi %s\n" % (username)
user = Character(username,(0,0),"This person looks lot like you, except more 8-bit.")
# try:
while True:
    user_input = raw_input("What do?\n\t").split()
    if user_input[0]=="Quit":
        print "byenow"
        break
    if user_input[0] in ("look","Look", "see","See"):
        if " ".join(user_input[1:]) in TextLand.Locations.keys() #fix this with a function latre)
            return Locations[" ".join(user_input[1:]].description



