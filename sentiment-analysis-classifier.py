#We have provided some synthetic (fake, semi-randomly generated) twitter data in a csv file named project_twitter_data.csv which has the text of a tweet, the number of retweets of that tweet, and the number of replies to that tweet. We have also words that express positive sentiment and negative sentiment, in the files positive_words.txt and negative_words.txt.
#Your task is to build a sentiment classifier, which will detect how positive or negative each tweet is. You will create a csv file, which contains columns for the Number of Retweets, Number of Replies, Positive Score (which is how many happy words are in the tweet), Negative Score (which is how many angry words are in the tweet), and the Net Score for each tweet. At the end, you upload the csv file to Excel or Google Sheets, and produce a graph of the Net Score vs Number of Retweets.

#Part1 - To start, define a function called strip_punctuation which takes one parameter, a string which represents a word, and removes characters considered punctuation from everywhere in the word.
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
def strip_punctuation(string):
    for char in string:
        if char in punctuation_chars:
            string = string.replace(char,'')
    return string

#Part2 - Next, define a function called get_pos which takes one parameter, a string which represents one or more sentences, and calculates how many words in the string are considered positive words. Use the list, positive_words to determine what words will count as positive. The function should return a positive integer - how many occurrences there are of positive words in the text. Note that all of the words in positive_words are lower cased, so you’ll need to convert all the words in the input string to lower case as well.
def get_pos(string):
    positive_count = 0
    string = string.lower()
    string = strip_punctuation(string)
    words = string.split()
    for word in words:
        for positive_word in positive_words:
            if word == positive_word:
                positive_count+=1
    return positive_count

positive_words = list()
with open('positive_words.txt','r') as positive_infile:
    for line in positive_infile:
        if line[0]!=';' and line[0]!='\n':
            positive_words.append(line.strip())

#Part3 - Next, define a function called get_neg which takes one parameter, a string which represents one or more sentences, and calculates how many words in the string are considered negative words. Use the list, negative_words to determine what words will count as negative. The function should return a positive integer - how many occurrences there are of negative words in the text. Note that all of the words in negative_words are lower cased, so you’ll need to convert all the words in the input string to lower case as well.
def get_neg(string):
    negative_count = 0
    string = string.lower()
    string = strip_punctuation(string)
    words = string.split()
    for word in words:
        for negative_word in negative_words:
            if word == negative_word:
                negative_count+=1
    return negative_count

negative_words = list()
with open('negative_words.txt','r') as negative_infile:
    for line in negative_infile:
        if line[0]!=';' and line[0]!='\n':
            negative_words.append(line.strip())

#Finally, write code that opens the file project_twitter_data.csv which has the fake generated twitter data (the text of a tweet, the number of retweets of that tweet, and the number of replies to that tweet). Your task is to build a sentiment classifier, which will detect how positive or negative each tweet is. Now, you will write code to create a csv file called resulting_data.csv, which contains the Number of Retweets, Number of Replies, Positive Score (which is how many happy words are in the tweet), Negative Score (which is how many angry words are in the tweet), and the Net Score (how positive or negative the text is overall) for each tweet. The file should have those headers in that order. Remember that there is another component to this project. You will upload the csv file to Excel or Google Sheets and produce a graph of the Net Score vs Number of Retweets.
write_file = open('resulting_data.csv','w')
read_file = open('project_twitter_data.csv','r')

def write(write_file):
    write_file.write('Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score')
    write_file.write('\n')
    lines = read_file.readlines()
    header_not_use = lines.pop(0)
    for line in lines:
        words = line.strip().split(',')
        write_file.write('{}, {}, {}, {}, {}'.format(words[1],words[2],get_pos(words[0]),get_neg(words[0]),get_pos(words[0])-get_neg(words[0])))
        write_file.write('\n')

write(write_file)
read_file.close()
write_file.close()
