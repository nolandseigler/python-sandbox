# this is so coooollll. list comprehension

# Write your word_length_dictionary function here:
def word_length_dictionary(words):
    return {word: len(word) for word in words}


# Uncomment these function calls to test your  function:
# print(word_length_dictionary(["apple", "dog", "cat"]))
# should print {"apple":5, "dog": 3, "cat":3}
# print(word_length_dictionary(["a", ""]))
# should print {"a": 1, "": 0}
user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931,
            "keysmithKeith": 129384}
tc_id = user_ids.get("teraCoder", 100000)
print(tc_id)
stack_id = user_ids.get("superStackSmash", 100000)
print(stack_id)
available_items = {"health potion": 10, "cake of the cure": 5, "green elixir": 20, "strength sandwich": 25,
                   "stamina grains": 15, "power stew": 30}
health_points = 20
health_points += available_items.pop("stamina grains", 0)
health_points += available_items.pop("power stew", 0)
health_points += available_items.pop("mystic bread", 0)
print(available_items)
print(health_points)

user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931,
            "keysmithKeith": 129384}
num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18,
                 "dictionaries": 18}

users = user_ids.keys()
lessons = list(num_exercises)

print(users)
print(lessons)

num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18,
                 "dictionaries": 18}
total_exercises = 0
for num in num_exercises:
    total_exercises += num_exercises.get(num)

print(total_exercises)

pct_women_in_occupation = {"CEO": 28, "Engineering Manager": 9, "Pharmacist": 58, "Physician": 40, "Lawyer": 37,
                           "Aerospace Engineer": 9}

for occupation, qty in pct_women_in_occupation.items():
    print("Women make up " + str(qty) + " percent of " + occupation + "s.")

tarot = {1: "The Magician", 2: "The High Priestess", 3: "The Empress", 4: "The Emperor", 5: "The Hierophant",
         6: "The Lovers", 7: "The Chariot", 8: "Strength", 9: "The Hermit", 10: "Wheel of Fortune", 11: "Justice",
         12: "The Hanged Man", 13: "Death", 14: "Temperance", 15: "The Devil", 16: "The Tower", 17: "The Star",
         18: "The Moon", 19: "The Sun", 20: "Judgement", 21: "The World", 22: "The Fool"}

spread = {}
spread["past"] = tarot.pop(13)
spread["present"] = tarot.pop(22)
spread["future"] = tarot.pop(10)

for time, card in spread.items():
    print("Your " + time + " is the " + card + " card.")
