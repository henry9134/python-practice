# when creating a list, its good practice to give the list a plural name.
bicycles = ['trek', 'cannondale', 'redline', 'specialized' ]
print(bicycles)

print(bicycles[0])
# the square brackets help print a specified item in an array, arrays start from 0.

print(bicycles[0].title())

print(bicycles[-1])
# to print the last item of an array, you can use[-1]. [-1] refers to the last item in an array.

message = f"my first bicycle was a {bicycles[0].title()}"
print(message)

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)
# you can modify a list but changing the value of the item in an array

motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.append('ducati')
print(motorcycles)
# appending adds a new item to the end of a list

motorcycles =[]

motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)
# here you start with an empty array, and by appending you can add new items in that empty array

motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')
print(motorcycles)
# you can insert an item into the list by choosing the position of where to insert it.

motorcycles = ['honda', 'yamaha', 'suzuki']
del motorcycles[0]
print(motorcycles)
# you can remove an item in a list using the 'del' mehtod. This method is used to delete a specified item in an array.

motorcycles = ['honda', 'yamaha', 'suzuki']
popped_motorcycle = motorcycles.pop()
print(popped_motorcycle)
last_owned = motorcycles.pop(0)
print(f" The last motorcycle I owned was a {last_owned.title()}.")
# the 'pop' method is used to remove an item from an array but still have it saved so that it can be used in the future

motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.remove('yamaha')
print(motorcycles)

too_expensive = 'honda'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me." )
# the 'remove' method is used when removing an item from a list using the name. This is useful when you dont know the position of an item in an array
# you can assign a variable too the item that you remove
