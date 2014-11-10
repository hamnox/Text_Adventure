# import 

map_size = [10,10]

# change this to a for loop to make dictionary, generate a room.
Locations = {[row[i] for row in myArray] 
          for i in range(len(myArray))}

locations["Inventory"] = []
# the last location is a list.
print "Welcome to my world :) "
input()

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

class Room:
	def __init__(self,name,items,location):
		self.name = name # attribute name/description
		self.items = [] # attribute items
		self.items.extend(items)
		self.location = location # init assign_location
	def self.look(item) # THIS DOESN"T WORK WTF https://docs.python.org/2/tutorial/classes.html
		if item in self.items
			return "ITEM DESCRIPTION" # TO BE CHANGED WHEN I MAKE AN ITEM
		else:
			return "FAIL"
	
	# function look
	# function move
	# function put
	# function get_location


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
	#function inventory
	