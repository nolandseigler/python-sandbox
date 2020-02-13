drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]
# zip obj list of list
zipped_drinks = zip(drinks, caffeine)
# then to dictionary
drinks_to_caffeine = {key: value for key, value in zipped_drinks}
# or jump straight to it
zip_to_the_chase = {key: value for key, value in zip(drinks, caffeine)}

songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]
plays = {song:playcount for song, playcount in zip(songs, playcounts)}
print(plays)
plays["Purple Haze"] = 1
plays["Respect"] = 94
library = {"The Best Songs": plays, "Sunday Feelings": {}}
print (library)