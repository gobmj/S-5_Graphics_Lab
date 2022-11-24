x=raw_input("Enter a String: ")
y=raw_input("Enter a Character: ")
if x.find(y)>0:
	print("Character Present at the Location: ",x.find(y))
	print("Count of Character in String: ",x.count(y))
else:
	print("Character Not Present")
print("Length of the String is: ",len(x))
z=raw_input("Enter a String to Concatenate: ")
print("Concatenated String is: "+x+z)
