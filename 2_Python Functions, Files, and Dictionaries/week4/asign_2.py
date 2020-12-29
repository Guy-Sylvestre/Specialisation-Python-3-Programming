
# # -------------------------   1   -------------------------
# We have provided some synthetic (fake, semi-randomly generated) twitter data in a csv file named project_twitter_data.csv which has the text of a tweet, the number of retweets of that tweet, and the number of replies to that tweet. We have also words that express positive sentiment and negative sentiment, in the files positive_words.txt and negative_words.txt.
# Your task is to build a sentiment classifier, which will detect how positive or negative each tweet is. You will create a csv file, which contains columns for the Number of Retweets, Number of Replies, Positive Score (which is how many happy words are in the tweet), Negative Score (which is how many angry words are in the tweet), and the Net Score for each tweet. At the end, you upload the csv file to Excel or Google Sheets, and produce a graph of the Net Score vs Number of Retweets.
# To start, define a function called strip_punctuation which takes one parameter, a string which represents a word, and removes characters considered punctuation from everywhere in the word. (Hint: remember the .replace() method for strings.)

punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

def strip_punctuation(word):
    New_word=""  
    print("Word is: ",word)
    for w in word:
        if w not in punctuation_chars:
            New_word=New_word+w
    return New_word



# # -------------------------   2   -------------------------
# Next, copy in your strip_punctuation function and define a function called get_pos which takes one parameter, a string which represents one or more sentences, and calculates how many words in the string are considered positive words. Use the list, positive_words to determine what words will count as positive. The function should return a positive integer - how many occurrences there are of positive words in the text. Note that all of the words in positive_words are lower cased, so you’ll need to convert all the words in the input string to lower case as well.
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# list of positive words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())

def strip_punctuation(word):
    New_word=""  
    print("Word is: ",word)
    for w in word:
        if w not in punctuation_chars:
            New_word=New_word+w
    return  New_word


def get_pos(sentences):
    lower_string=sentences.lower()                    ## As the list of positive words are in lower case
    str_punc_removed=strip_punctuation(lower_string)  ##For Punctuation Removal
    print("str_punc_removed:",str_punc_removed)
    splitted_string=str_punc_removed.split()          ## For splitting the sentence into words
    print ("splitted_string:",splitted_string)
    
    
    pos_count=0
    for w in splitted_string:
        if w in positive_words:
            pos_count=pos_count+1
    return pos_count

# # -------------------------   3   -------------------------
# Next, copy in your strip_punctuation function and define a function called get_neg which takes one parameter, a string which represents one or more sentences, and calculates how many words in the string are considered negative words. Use the list, negative_words to determine what words will count as negative. The function should return a positive integer - how many occurrences there are of negative words in the text. Note that all of the words in negative_words are lower cased, so you’ll need to convert all the words in the input string to lower case as well.
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())
            

def strip_punctuation(word):
    New_word=""  
    print("Word is: ",word)
    for w in word:
        if w not in punctuation_chars:
            New_word=New_word+w
    return  New_word


def get_neg(sentences):
    lower_string=sentences.lower()                    ## As the list of positive words are in lower case
    str_punc_removed=strip_punctuation(lower_string)  ## For Punctuation Removal
    print("str_punc_removed:",str_punc_removed)
    splitted_string=str_punc_removed.split()          ## For splitting the sentence into words
    print ("splitted_string:",splitted_string)
    
    
    neg_count=0
    for w in splitted_string:
        if w in negative_words:
            neg_count=neg_count+1
    return neg_count
# # -------------------------   4   -------------------------





# # -------------------------   All   -------------------------
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

def strip_punctuation(oldS):
    for i in punctuation_chars:
        oldS = str(oldS).replace('%s' % i, '')
    return oldS

def strip_punctuation(oldS):
    for i in punctuation_chars:
        oldS = str(oldS).replace('%s' % i, '')
    return oldS

punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# list of positive words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())

def get_pos(str):
    str = strip_punctuation(str).split()
    j = 0
    for i in str:
        if i in positive_words:
            j += 1
    return j

def strip_punctuation(oldS):
    for i in punctuation_chars:
        oldS = str(oldS).replace('%s' % i, '')
    return oldS

punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())
            
def get_neg(str):
    str = strip_punctuation(str).split()
    k = 0
    for i in str:
        if i in negative_words:
            k += 1
    return k


def run(file):
    csvFile = open(file, 'r')
    lines = csvFile.readlines()
    
    lines = lines[1:]
    neg_count = []
    pos_count = []
    wordList = []
    for i in lines:
        i = i.strip()
        i = i.split(",")[0]
        wordList.append(i)
    for i in wordList:
        neg_count.append(get_neg(i))
        pos_count.append(get_pos(i))
    res = ['retweet_count,reply_count,pos_count,neg_count,score']
    
    res = []
    for i in lines:
        i = i.strip()
        i = i.split(",")[1:]
        res.append(i)
    temp = []
    for i in res:
        i = list(map(int, i))
        temp.append(i)
    res = temp
    for i in range(len(res)):
        res[i].append(pos_count[i])
        res[i].append(neg_count[i])
        res[i].append(pos_count[i] - neg_count[i])
        
    temp = []
    for i in res:
        temp.append(','.join('%s' %id for id in i))
    res = temp
    
    res.insert(0, "Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score")
    print(res)
    res = '\n'.join('%s' % id for id in res)
    with open("resulting_data.csv", 'w') as csvFile:
        write = csvFile.write(res)


if __name__ == '__main__':
    run('project_twitter_data.csv')