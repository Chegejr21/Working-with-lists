#lists and tuples
#lists
#NOTE THAT THE MAIN DIFFERENCE BETWEEN TUPLES N LIST IS THAT TUPLES ARE IMMUTABLE THUS THE DATA IN IT ONCE IS ENTERED CANT BE CHANGED....USED MAINLY TO STORE DATA THAT DOES NOT CHANGE THE REVERSE IS TRUE FOR LISTS

friends = ["chege", "dave", "dee", "altone", "mercy"]
print(friends)

#".append" function is used to add an item to the list

friends.append("higgins")
print(friends)

#".extend" function is used to combine two list together and be one

enemies = ["chris", "you", "I am X", "bruno"]
friends.extend(enemies)
print(friends)

#"pop" function is used to remove the last item on the list

friends.pop()
print(friends)

# ". insert" function is used to insert an item to an already existing list at a given index

friends.insert(2, "fred")
print(friends)

# "remove" function removes an item in the list

friends.remove("chege")
print(friends)

# ".clear" function is used to clear the entire contents in the list

friends.reverse()
print(friends)
print(friends[::-1])

friends.clear()
print(friends)
