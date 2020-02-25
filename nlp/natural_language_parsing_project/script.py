from nltk import pos_tag, RegexpParser
from tokenize_words import word_sentence_tokenize
from chunk_counters import np_chunk_counter, vp_chunk_counter

# import text of choice here
text = open("the_iliad.txt",encoding='utf-8').read().lower()

# tokenize sentences then tokenize words from sentences
word_tokenized_text = word_sentence_tokenize(text)

# # test
# single_word_tokenized_sentence = word_tokenized_text[100]
# print(single_word_tokenized_sentence)


# pos_tagged_sentences
pos_tagged_text = [pos_tag(sentence) for sentence in word_tokenized_text]

# # test
# single_pos_sentence = pos_tagged_text[100]
# print(single_pos_sentence)

# define chunk grammar and make the chunk parsers
np_chunk_grammar = "NP: {<DT>?<JJ>+<NN>}"
vp_chunk_grammar = "VP: {<DT>?<JJ>+<NN><VB.*><RB.?>?}"

np_chunk_parser = RegexpParser(np_chunk_grammar)
vp_chunk_parser = RegexpParser(vp_chunk_grammar)


# chunk parse phrases to lists
np_chunked_text = [np_chunk_parser.parse(pos_sentence) for pos_sentence in pos_tagged_text]
vp_chunked_text = [vp_chunk_parser.parse(pos_sentence) for pos_sentence in pos_tagged_text]

# # test
# print(np_chunked_text[100])
# print(vp_chunked_text[100])



# print most common np and vp chunks
most_common_np_chunks = np_chunk_counter(np_chunked_text)
print(most_common_np_chunks)
most_common_vp_chunks = vp_chunk_counter(vp_chunked_text)
print(most_common_vp_chunks)



