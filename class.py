class Circle:
    pi = 3.14

    def __init__(self, diameter):
        self.radius = diameter / 2

    # use __repr__ to define what the string representation of the object should be so it doesnt just print memory
    # address
    def __repr__(self):
        return "Circle with radius {radius}".format(radius=self.radius)

    def area(self):
        return self.pi * self.radius ** 2

    def circumference(self):
        return self.pi * 2 * self.radius


medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)

# now prints what __repr__ returns
print(medium_pizza)
print(teaching_table)
print(round_room)

# functions can have instance vars added after init
# use dir to see all
# dunders __ are usually built in
print(dir(5))


def this_function_is_an_object(param):
    return "Anything you'd like."


print(dir(this_function_is_an_object))


class Student:
    def __init__(self, name, year):
        self.name = name
        self.year = year
        self.grades = []

    def add_grade(self, grade):
        if type(grade) is Grade:
            self.grades.append(grade)


roger = Student("Roger van der Weyden", 10)
sandro = Student("Sandro Botticelli", 12)
pieter = Student("Pieter Bruegel the Elder", 8)


class Grade:
    minimum_passing = 65

    def __init__(self, score):
        self.score = score


pieter.add_grade(Grade(100))
