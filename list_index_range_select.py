suitcase = ['shirt', 'shirt', 'pants', 'pants', 'pajamas', 'books']

beginning = suitcase[0:4]
print(beginning)
middle_index = len(suitcase) / 2

# select middle two
middle = suitcase[int(middle_index - .5):int(1 + middle_index + .5)]
