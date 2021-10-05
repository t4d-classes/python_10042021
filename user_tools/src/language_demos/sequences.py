


# colors = ['red', 'green', 'blue'] # list

# point = (12, 5) # tuple


# print(colors)
# print(point)

# for item in colors:
#     print(item)

# for item2 in point:
#     print(item2)

# print(colors[0])
# print(point[0])

# print(len(colors))
# print(len(point))

# colors.append('yellow')
# point.append(23)

car1 = (1, "Ford", "Fusion Hybrid", "blue", 45000)
car2 = (2, "Tesla", "S", "red", 125000)

cars = [car1, car2]


def createPoint(x: int, y: int, z: int):

    return (x,y,z)

point = createPoint(1,4,7)

item = ('a', 1, False, lambda x: x * 2)

for item_element in item:
    print(item_element)


