# enumerate 

areas = [11.25, 18.0, 20.0, 10.75, 9.50]

for room, a in enumerate(areas) :		# enumerate used to concatinate two different variable values into each instance of a for loop 
    print("room " + str(room) + ": " + str(a))

# Will return 
room 0: 11.25
room 1: 18.0
room 2: 20.0
room 3: 10.75
room 4: 9.5