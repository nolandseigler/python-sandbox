from nltk import RegexpParser, Tree
from pos_tagged_oz import pos_tagged_oz
from vp_chunk_counter import vp_chunk_counter
from np_chunk_counter import np_chunk_counter
# from pos_tagged_oz import pos_tagged_oz

# define adjective-noun chunk grammar here
chunk_grammar = "AN: {<JJ><NN>}"

# create RegexpParser object here
chunk_parser = RegexpParser(chunk_grammar)

# chunk the pos-tagged sentence at index 282 in pos_tagged_oz here
scaredy_cat = chunk_parser.parse(pos_tagged_oz[282])
print(scaredy_cat)

# pretty_print the chunked sentence here
Tree.fromstring(str(scaredy_cat)).pretty_print()

# STUFFS
# define noun-phrase chunk grammar here
chunk_grammar = "NP: {<DT>?<JJ>*<NN>}"

# create RegexpParser object here
chunk_parser = RegexpParser(chunk_grammar)

# create a for loop through each pos-tagged sentence in pos_tagged_oz here
np_chunked_oz = [chunk_parser.parse(word) for word in pos_tagged_oz]


# store and print the most common np-chunks here
most_common_np_chunks = np_chunk_counter(np_chunked_oz)

print(most_common_np_chunks)



# MO STUFFS
from nltk import RegexpParser
from pos_tagged_oz import pos_tagged_oz
from vp_chunk_counter import vp_chunk_counter

# define verb phrase chunk grammar here
chunk_grammar = "VP: {<VB.*><DT>?<JJ>*<NN><RB.?>?}"

# create RegexpParser object here
chunk_parser = RegexpParser(chunk_grammar)

vp_chunked_oz = [chunk_parser.parse(word) for word in pos_tagged_oz]


# store and print the most common vp-chunks here
most_common_vp_chunks = vp_chunk_counter(vp_chunked_oz)

print(most_common_vp_chunks)

#CHUNK FILTERING

# define chunk grammar to chunk an entire sentence together
grammar = "Chunk: {<.*>+}"
chunk_grammar = """NP: {<.*>+}
}<VB.?|IN>+{"""
# create RegexpParser object
parser = RegexpParser(grammar)
chunk_parser = RegexpParser(chunk_grammar)

# chunk the pos-tagged sentence at index 230 in pos_tagged_oz
chunked_dancers = parser.parse(pos_tagged_oz[230])
print(chunked_dancers)


# chunk and filter the pos-tagged sentence at index 230 in pos_tagged_oz here
filtered_dancers = chunk_parser.parse(pos_tagged_oz[230])
print(filtered_dancers)


# pretty_print the chunked and filtered sentence here
Tree.fromstring(str(filtered_dancers)).pretty_print()


