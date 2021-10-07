
# # person_tuple = ('Bob', 'Smith')

# # print(person_tuple[0])


# person = {
#     "first_name": "Bob",
#     "last_name": "Smith"
# }

# person["age"] = 23

# # print(person)

# for key in person:
#     print(f"{key}={person[key]}")
#     # print(key + "=" + str(person[key]))

car1 = ('Ford', 'Fusion Hybrid', 2021)

car2 = {
    "make": "Ford",
    "model": "Fusion Hybrid",
    "year": 2021
}

class Car:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def __repr__(self):
        return f"Car - make: {self.make}, model: {self.model}, year: {self.year}"

car3 = Car('Ford', 'Fusion Hybrid', 2021)

print(car1)
print(car2)
print(car3)
