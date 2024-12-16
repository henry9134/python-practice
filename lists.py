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
