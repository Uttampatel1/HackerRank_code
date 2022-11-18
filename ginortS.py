# creating lists
l = []
u = []
o = []
e = []

# using for loop in sorted string from user
for i in sorted(input()):
    
    # checking is the character is alphabet
    if i.isalpha():
        
        # Checking is the alphabet is upper letter or not
        x = u if i.isupper() else l
    
    # if the character is not alphabet, this code will execute
    else:
        
        # assigning accordingly
        x = o if int(i)%2 else e
        
    # apending and joining all characters.
    x.append(i)
print("".join(l+u+o+e))