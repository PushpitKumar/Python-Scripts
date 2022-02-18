#Once you have a file “object”, the thing returned by the open function, Python provides three methods to read data from that object. The read() method returns the entire contents of the file as a single string (or just some characters if you provide a number as an input parameter. The readlines method returns the entire contents of the entire file as a list of strings, where each item in the list is one line of the file. The readline method reads one line from the file and returns it as a string. The strings returned by readlines or readline will contain the newline character at the end.

#Using the file school_prompt2.txt, find the number of characters in the file and assign that value to the variable num_char.
file = open('school_prompt2.txt','r')
chars = file.read()
num_char = len(chars)
print(num_char)
file.close()

#Find the number of lines in the file, travel_plans2.txt, and assign it to the variable num_lines.
file = open('travel_plans2.txt','r')
lines = file.readlines()
num_lines = len(lines)
print(num_lines)
file.close()

#Create a string called first_forty that is comprised of the first 40 characters of emotion_words2.txt.
file = open('emotion_words2.txt','r')
first_forty = file.read(40)
print(first_forty)
file.close()
