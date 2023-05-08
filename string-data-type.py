"""
Working with the String Data Type
"""
myString = "This is a string."
print(myString)
print(type(myString))
print(str(myString) + " is of the data type " + str(type(myString)))
firstString = "water"
secondString = "fall"
thirdString = firstString + secondString
print(thirdString)
name = input("Siapa nama anda? ")
print(name)
warna = input("Apa warna favorit kamu? ")
hewan = input("Apa binatang favorit kamu? ")
print("{}, kamu suka {} {}!".format(name,hewan,warna))
