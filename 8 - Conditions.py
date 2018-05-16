name = "Saurabh"
age = 33
if name == "Saurabh" and age == 33:
    print("Your name is %s, and you are also %d years old."%(name, age))

if name == "John" or name == "Rick":
    print("Your name is either John or Rick.")
else:
    print("Who are you?")
##############################################
x = 2
if x == 2:
    print("x equals two!")
else:
    print("x does not equal to two.")
########################################

# is Operator : Unlike the double equals operator "==", the "is" operator does not match the values of the variables,
# but the instances themselves
x = [1,2,3]
y = [1,2,3]
print(x == y) # Prints out True
print(x is y) # Prints out False

if (x is not y) :
    print ("x is not equals to y")
