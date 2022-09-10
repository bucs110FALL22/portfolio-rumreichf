import random
#Part A
weeks = 16
print(weeks, type(weeks))
classes = 5
print(classes, type(classes))
tuition = 6000
print(tuition, type(tuition))
classes_per_week = 3
print(classes_per_week, type(classes_per_week))
cost_per_week = ((tuition / classes) / weeks)
cost_per_class = (cost_per_week / classes_per_week)
print("Cost per week:", cost_per_week)
print("Your cost per individual class is: ", cost_per_class)

#Part B
fruits = ["apple", "banana", "orange", "lemon", "strawberry"]
random_fruit = random.choice(fruits)
print(random_fruit)