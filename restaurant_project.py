class Menu:
    def __init__(self, name, items, start_time, end_time):
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time

    def __repr__(self):
        return self.name.capitalize() + " Menu available from " + str(self.start_time) + " to " + str(self.end_time)

    def calculate_bill(self, purchased_items):
        price = 0
        for key, value in self.items.items():
            if key in purchased_items:
                price += value
        return price


brunch_items = {'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50,
                'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50, }
early_bird_items = {'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00,
                    'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50,
                    'coffee': 1.50, 'espresso': 3.00, }
dinner_items = {'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00,
                'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00, }
kids_items = {'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00, }

brunch = Menu("brunch", brunch_items, 1100, 1600)
early_bird = Menu("early bird", early_bird_items, 1500, 1800)
dinner = Menu("dinner", dinner_items, 1700, 2300)
kids = Menu("kids", kids_items, 1100, 2100)

menusList = [brunch, early_bird, dinner, kids]

print(brunch)
print(brunch.calculate_bill(['pancakes', 'home fries', 'coffee']))
print(early_bird.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)']))


class Franchise:
    def __init__(self, address, menus):
        self.address = address
        self.menus = menus

    def __repr__(self):
        return "Store at " + self.address

    def available_menus(self, time):
        return [menu for menu in self.menus if time >= menu.start_time and time <= menu.end_time]


flagship_store = Franchise("1232 West End Road", menusList)
new_installment = Franchise("12 East Mulberry Street", menusList)

print(flagship_store.available_menus(1200))
print(flagship_store.available_menus(1700))


class Business:
    def __init__(self, name, franchises):
        self.name = name
        self.franchises = franchises


arepas_menu = Menu("Take a' Arepa",
                   {'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50, }, 1000,
                   2000)

arepas_place = Franchise("189 Fitzgerald Avenue", arepas_menu)

take_a_arepa = Business("Take a' Arepa", arepas_place)
