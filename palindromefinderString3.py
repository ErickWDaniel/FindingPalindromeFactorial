# Using String checker
word_to_be_checked = input("Enter the word to be checked if it Palindrome\n")
# change all letter into same case so it can be easy if the caps are mixed
word_to_be_checked_case_convetor = word_to_be_checked.casefold()
# using reversed for the string library
reversed_word = reversed(word_to_be_checked_case_convetor)
if list(word_to_be_checked_case_convetor) == list(reversed_word):
    print(word_to_be_checked, "is palindrome")
else:
    print(word_to_be_checked, "is not palindrome")
