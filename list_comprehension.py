heights = [161, 164, 156, 144, 158, 170, 163, 163, 157]

# List comprehension. short hand of making a list using a loop and an optional conditional
can_ride_coaster = [height for height in heights if height > 161]

print(can_ride_coaster)

celsius = [0, 10, 15, 32, -5, 27, 3]

# convert celsius to fahrenheit using list comprehension
fahrenheit = [cel * (9 / 5) + 32 for cel in celsius]

print(fahrenheit)

single_digits = range(10)
squares = []
for digit in single_digits:
    print(digit)
    squares.append(digit ** 2)
print(squares)
cubes = [digit ** 3 for digit in single_digits]
print(cubes)
