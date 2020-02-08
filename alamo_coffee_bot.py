def coffee_bot():
    print("Welcome to Alamo Coffee!")
    size = get_size()
    drink_type = get_drink_type()
    if drink_type == "latte":
        latte = order_latte()
        print("Alright so that's a " + size + " " + latte + ".")
    else:
        print("Alright so that's a " + size + " " + drink_type + ".")
    name = input("Can I get your name please?")
    print("Ok, " + name + "! Your drink will be out shortly.")
    print("A few moments later.....")
    if drink_type == "latte":
        print(latte.capitalize() + " for " + name + "!")
    else:
        print(drink_type.capitalize() + " for " + name + "!")


# get drink size
def get_size():
    while True:
        user_response = input("What size drink can I get for you? \n[a] Small \n[b] Medium \n[c] Large \n>").lower()
        switch = {
            "a": "small",
            "b": "medium",
            "c": "large"
        }
        if switch.get(user_response, "Invalid size") != "Invalid size":
            break
        else:
            print("Please select a size by inputting 'a', 'b' or 'c'.")
    return switch.get(user_response, "Invalid size")


# end get drink size
# get drink type
def get_drink_type():
    while True:
        user_response = input(
            "What type of drink would you like? \n[a] Brewed Coffee \n[b] Mocha \n[c] Latte \n>").lower()
        switch = {
            "a": "brewed coffee",
            "b": "mocha",
            "c": "latte"
        }
        if switch.get(user_response, "Invalid size") != "Invalid size":
            break
        else:
            print("Please select a drink type by inputting 'a', 'b' or 'c'.")
    return switch.get(user_response, "Invalid size")


# end get drink type
# if latte is selected. order latter
def order_latte():
    while True:
        user_response = input("And what kind of milk for your latte? \n[a] 2% Milk \n[b] Non-fat Milk \n[c] Soy Milk "
                              "\n>").lower()
        switch = {
            "a": "latte",
            "b": "non-fat latte",
            "c": "soy latte"
        }
        if switch.get(user_response, "Invalid size") != "Invalid size":
            break
        else:
            print("Please select a milk type by inputting 'a', 'b' or 'c'.")
    return switch.get(user_response, "Invalid size")


# call main function
coffee_bot()
print("Thanks for coming to Alamo Coffee!!")
