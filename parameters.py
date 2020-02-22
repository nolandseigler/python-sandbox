# some of this is example code i did but it will not execute just. I am using this for examples

import os
from os.path import join
# KEYWWORD ARGUMENT UNPACKING. **YIELDS A DICT OF ARGS
print("My name is {name} and I'm feeling {feeling}.".format(name="Bob Saget", feeling="hungry"))

from products import create_product


def create_products(**products_dict):
    for name, price in products_dict.items():
        create_product(name, price)


create_products(baseball=3, shirt=14, guitar=70)
# ARBITRARY POSITIONAL ARGUMENTS!!!! **YIELDS A TUPLE OF ARGS


path_segment_1 = "/Home/User"
path_segment_2 = "Codecademy/videos"
path_segment_3 = "cat_videos/surprised_cat.mp4"

# join all three of the paths here!
joined = join(path_segment_1, path_segment_2, path_segment_3)
print(joined)


def myjoin(*args):
    concat = ""
    for arg in args:
        concat += arg + "/"
    return concat


myjoined = myjoin(path_segment_1, path_segment_2, path_segment_3)
print(myjoined)


# DEFAULT ARGUMENTS
def make_folders(folders_list, nest=False):
    if nest:
        """
        Nest all the folders, like
        ./Music/fun/parliament
        """
        path_to_new_folder = ""
        for folder in folders_list:
            path_to_new_folder += "/{}".format(folder)
            try:
                os.makedirs(path_to_new_folder)
            except FileExistsError:
                continue
    else:
        """
        Makes all different folders, like
        ./Music/ ./fun/ and ./parliament/
        """
        for folder in folders_list:
            try:
                os.makedirs(folder)

            except FileExistsError:
                continue


# KEYWORD ARGUMENTS
import shapes


def draw_shape(shape_name="box", character="x", line_breaks=True):
    shape = shapes.draw_shape(shape_name, character)
    if not line_breaks:
        print(shape[1:-1])
    else:
        print(shape)


# call draw_shape() with keyword arguments here:
draw_shape(character="m", line_breaks=False)

make_folders(['./Music', './fun', './parliament'])


# HANDLE DEFAULT ARGS WITH MUTABLES USING NONE
def update_order(new_item, current_order=None):
    if current_order is None:
        current_order = []
    current_order.append(new_item)
    return current_order


order1 = update_order({'item': 'burger', 'cost': '3.50'})
order1 = update_order({'item': 'soda', 'cost': '1.50'}, order1)

order2 = update_order({'item': 'soda', 'cost': '1.50'})

print(order2)


# MULTIPLE RETURNS AND UNPACK
def scream_and_whisper(text):
    scream = text.upper()
    whisper = text.lower()
    return scream, whisper


result = scream_and_whisper("Words.")
the_scream = result[0]
the_whisper = result[1]
print(the_scream)
print(the_whisper)
