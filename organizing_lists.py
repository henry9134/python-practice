cars = ['bmw', 'audi', 'toyota', 'honda']
cars.sort()
print(cars)
# the 'sort' method sorts a list into alphabetical order, however doing this will permenantly change the list
cars = ['bmw', 'audi', 'toyota', 'honda']
cars.sort(reverse=True)
print(cars)
# the 'reverse=True' method sorts a list in reverse-alphabetical order

cars = ['bmw', 'audi', 'toyota', 'honda']
print('Here is the original list:')
print(cars)

cars = ['bmw', 'audi', 'toyota', 'honda']
print("/nHere is the sorted list:")
print(sorted(cars))
# if you want to sort a list but not permenantly change it, you can use the 'sorted' method

cars = ['bmw', 'audi', 'toyota', 'honda']
print(cars)

cars.reverse()
print(cars)
# the 'reverse' method sorts the list in reversse order (not reverse-alphabetically).

cars = ['bmw', 'audi', 'toyota', 'honda']
print(len(cars))
# the 'len' method will count the number of items in a list.
