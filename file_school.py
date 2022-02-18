#Assign the first 30 characters of school_prompt.txt as a string to the variable beginning_chars.
with open('school_prompt2.txt','r') as infile:
    beginning_chars = infile.read()[:30]
print(beginning_chars)
