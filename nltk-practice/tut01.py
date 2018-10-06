from nltk.tokenize import sent_tokenize, word_tokenize

# tokenizing: work tokeinizers and sentece tokenizers.

# lexicon and corporas
# corpora: body of text, e.g. medical journals, speeches, English language
# lexicon: words and their meanings

# investor-speak and regular english-speak

example_text = "Hello Mr. Smith, how are you doing today? The weather is great and Python is awesome. It is raining, you should take an umbrella with you."
print(sent_tokenize(example_text))
# print(word_tokenize(example_text))

for i in word_tokenize(example_text):
    print(i)
