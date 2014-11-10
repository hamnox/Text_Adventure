# import 

map_size = (10,10)

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

# add a parser!
class Room:
	def __init__(self,name,items=[]):
		self.name = name # attribute name/description
		self.items = [] # attribute items
		self.items.extend(items)
	def look(self,item): # THIS DOESN"T WORK WTF https://docs.python.org/2/tutorial/classes.html
		if item in self.items:
			return "ITEM DESCRIPTION" # TO BE CHANGED WHEN I MAKE AN ITEM
		else:
			return "FAIL"
	
	# function look
	# function move
	# function put
	# function get_location

"""
class Item:
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
	

class Character:
	# attribute status
	# attribute location
	def drop():
		#match item by name list
		try:
			locations[-1].remove(item)
			room.put(item)
		except:
			print "That didn't work dummy!"
	#function inventory"""
	
	
# change this to a for loop to make dictionary, generate a room.
Locations = {}
#[row[i] for row in map_size[0]]
#          for i in range(len(map_size[1]+1)):""}

print range(1,map_size[0]+1)
for x in range(1,map_size[0]+1):
  for y in range(1,map_size[1]+1):
    Locations[(x,y)] = Room("Room"+str(x)+"-"+str(y))

Locations["Inventory"] = []
# the last location is a list.
print "Welcome to my world :) "
input()