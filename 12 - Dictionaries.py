phonebook = {
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}

# write your code here
phonebook["Jake"] = 938273443
del phonebook["Jill"]

# testing code
if "Jake" in phonebook:
    print("Jake is listed in the phonebook.")
if "Jill" not in phonebook:
    print("Jill is not listed in the phonebook.")


    phonebook2 = {"John" : 938477566,"Jack" : 938377264,"Jill" : 947662781}
for name, number in phonebook2.items():
    print("Phone number of %s is %d" % (name, number))
