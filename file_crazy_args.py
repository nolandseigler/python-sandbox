def remove(filename, *args, **kwargs):
    with open(filename) as file_obj:
        text = file_obj.read()
    for arg in args:
        text = text.replace(arg, "")
    for kwarg, replacement in kwargs.items():
        text = text.replace(kwarg, replacement)
    return text


print(remove("text.txt", "generous", "gallant", fond="amused by", Robin="Mr. Robin"))


# destructure dictionary with ** when passing in or unpack list or tuple with * when passing in
def create_product(name, price):
    print("{} created, being sold for ${}".format(name, price))


def create_products(**products_dict):
    for name, price in products_dict.items():
        create_product(name, price)


new_product_dict = {
    'Apple': 1,
    'Ice Cream': 3,
    'Chocolate': 5,
}

create_products(**new_product_dict)
