########################################################################
##
## CS 101
## Program # 7
## Name Brooke McFarland
## Email blmz99@mail.umkc.edu
##
## PROBLEM : Given a list of words, determine the context in which the word is used on average using movie reviews and the
## associated ratings. This will show if the words is used negitively or positively.
##
## ALGORITHM : 
##      1. Write out the algorithm
## 
## ERROR HANDLING:
##      Any Special Error handling to be noted.  Wager not less than 0. etc
## OTHER COMMENTS:
##      Any special comments
##
######################################################################
def open_file(correct):
   return open(correct)

def get_user_input(question):
    while True:
        answer = input(question).lower()
        try:
            correct = open_file(answer)
        except FileNotFoundError:
            print ("The file",answer,"was not found. Please try again.")
        except IOError:
            print("Please check the file name",answer,"for any incorrect special characters")
        else:
            return correct

class Word(object):
    def __init__(self,word):
        self.word = word
        self.word_count = 0
        self.review_total = 0

class Review(object):
    def __init__(self,rating,review):
        self.rating = rating
        self.review = review




while True:
    movie_file = open("movieReviews.txt","r")
    review_lst = []
    for line in movie_file.readlines():
        derp = Review(line[0],line [1:])
        review_lst.append(derp)


    word_file = get_user_input("Please enter the file containing a list of words you would like to analyze.")
    lst = []
    for item in word_file:
        movie_word = Word(item)
        lst.append(movie_word)
        #for line in reviews:
            #if movie_word in reviews:
                #movie_word.word_count += 1

