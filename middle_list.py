# middle if odd. average of middle two if even
def middle_element(lst):
    length = len(lst)
    if length % 2 == 0:
        return (lst[int((length / 2) - .5)] + lst[int((length / 2) + .5)]) / 2
    else:
        return lst[int(length / 2)]
