import ex_25
sentence = "All good things come to those who wait."
words = ex_25.break_words(sentence)
words
sorted_words = ex_25.sort_words(words)
sorted_words
ex_25.print_first_word(words)
ex_25.print_last_word(words)
print(words)


ex_25.print_first_word(sorted_words)
ex_25.print_last_word(sorted_words)
print(sorted_words)

sorted_words = ex_25.sort_sentence(sentence)
print(sorted_words)

ex_25.print_first_and_last(sentence)
ex_25.print_first_and_last_sorted(sentence)

help(ex_25.break_words)
