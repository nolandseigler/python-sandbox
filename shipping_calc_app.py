# Functions to calculate shipping prices
def get_ground_price(weight):
    if (weight >= 10):
        return 4.75 * weight + 20
    elif (weight >= 6):
        return 4.00 * weight + 20
    elif weight >= 2:
        return 3.00 * weight + 20
    elif weight > 0:
        return 1.50 * weight + 20


def get_drone_price(weight):
    if weight >= 10:
        return 14.75 * weight
    elif weight >= 6:
        return 12.00 * weight
    elif weight >= 2:
        return 9.00 * weight
    elif weight > 0:
        return 4.50 * weight


premium_ground_price = 125.00


# End calc shipping functions
# Calculate cheapest shipping option
def best_shipping(weight):
    ground = get_ground_price(weight)
    drone = get_drone_price(weight)
    if (ground < drone) and (ground < premium_ground_price):
        return "The ground shipping method is the best value for a package that weighs " + str(
            weight) + "lbs. Your total " \
                      "shipping price " \
                      "is $" + str(ground) + \
               ". "
    elif (drone < ground) and (drone < premium_ground_price):
        return "The drone shipping method is the best value for a package that weighs " + str(
            weight) + "lbs. Your total " \
                      "shipping price is " \
                      "$" + str(drone) + ". "
    else:
        return "The premium ground shipping method is the best value for a package that weighs " + str(weight) + "lbs. " \
                                                                                                                 "Your " \
                                                                                                                 "total " \
                                                                                                                 "shipping " \
                                                                                                                 "price is " \
                                                                                                                 "$" + \
               str(premium_ground_price) + ". "


# End calculate cheapest shipping option
print("Welcome to Sal's Shipping.")

while True:
    user_input = input("Input your package weight to see the cheapest shipping option.")
    print(best_shipping(float(user_input)))
    user_input = input("Would you like to calculate another weight? [Yes/No]")
    if user_input.lower() != "yes":
        break
