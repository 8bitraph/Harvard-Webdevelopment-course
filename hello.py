"""
print("hello, world!")
name = input("Name: ")
# print("Hello," + name)
# -- formating string --
print(f"Hello, {name}" )
"""
"""
# -- CONDITIONS --
n = int (input("Number: "))

if n > 0:
    print("n is positive")
elif n < 0:
    print("n is negative")
else:
    print("n is zero")
"""

# DATA STRUCTURE
"""
# -- sequence --
#list: (sequence of mutable (changable) values)
# name = "Harry"
name = ["Harry", "Ron", "Hermione"]
print(name[0])

coordinateX = 10.0
coordinateY = 20.0
# tuple: (sequence of immutable (unchangeable) values)
coordinate = (10.0, 20.0)

# -- list --
name = ["Harry", "Ron", "Hermione", "Ginny"]
print(name[0])
names.append("Draco")
#.append is a method or function that adds a value to the end of a existing list
name.sort()
#.sort is a method or function that sorts the list alphabetically


# -- set --
# set: is a collection of unique values
s = set()

s.add(1)
s.add(4)
s.add(3)
s.add(2)
s.add(6)
s.add(3)
# set doesn't add another set of the same value/number
print(s)
s.remove(2)
print(s)

print(f"The set had {len(s)} elements.")

"""

# -- LOOPING --
"""
for i in [0,1,2,3,4,5]:
    print(i)
"""
for i in range(6):
