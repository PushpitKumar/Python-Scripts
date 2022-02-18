#The module keyword determines if a string is a keyword. e.g. keyword.iskeyword(s) where s is a string will return either True or False, depending on whether or not the string is a Python keyword. Import the keyword module and test to see whether each of the words in list test are keywords. Save the respective answers in a list, keyword_test.
import keyword
keyword_test = []
test = ["else", "integer", "except", "elif"]
for word in test:
        keyword_test.append(keyword.iskeyword(word))
print(keyword_test)
