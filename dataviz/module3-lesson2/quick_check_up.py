# print hello user!
print ("hello user! ")

# take in user input
name = input("what is your name? ")

#respond back with user input
print(f"hello (name)")

#take in the user favorite number
fav_num = input("what is your favorite number? ")

#respond back with a statement based on your favorite number
x = 50
if int(fav_num) < 50:
    print(f'your fav number, {str(fav_num)}, is less than mine')
else:
    print(f'your fav number, {str(fav_num)}, is more than mine') 