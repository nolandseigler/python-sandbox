drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]
# zip obj list of list
zipped_drinks = zip(drinks, caffeine)
# then to dictionary
drinks_to_caffeine = {key: value for key, value in zipped_drinks}
# or jump straight to it
zip_to_the_chase = {key: value for key, value in zip(drinks, caffeine)}
