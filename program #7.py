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
            print ("The file",answer,"was not found; Please try again.")
        except IOError:
            print("Please check the file name",answer,"for any incorrect special characters")
        except Exception:
            print("Something went wrong; Please try again.")
        else:
            return correct

def table_input(question):
    user_answer = input(question)

#def make_table():
    #answer = input(order)




class Word(object):
    def __init__(self,word):
        self.word = word
        self.rating_lst = []
        self.rating = 0
        self. word_count = 0
    def avg_rating(self):
        if len(self.rating_lst) > 0:
            return self.total_rating()/len(self.rating_lst)
        else:
            return 0
    def total_rating(self):
        total_rating = 0
        for number in self.rating_lst:
            total_rating += number
        return total_rating

    def st_deviation(self):
        avg = self.avg_rating()
        sum_numerator = 0
        for number in self.rating_lst:
            sum_numerator += ((number-avg)**2)
        return sum_numerator/len(self.rating_lst)



class Review(object):
    def __init__(self,rating,review):
        self.rating = rating
        self.review = review



while True:
    movie_file = open("movieReviews.txt","r")
    review_lst = []
    for line in movie_file.readlines():
        derp = Review(int(line[0]),(line [1:]).lower())
        review_lst.append(derp)


    word_file = get_user_input("Please enter the file containing a list of words you would like to analyze.")
    order_question = table_input("In which order would you like your data displayed?\n1.)Avg ascending\n2.)Avg descending\n3.)Standard deviation ascending\n4.)Standard deviation descending\n")
    word_lst = []
    for item in word_file:
        movie_word = Word((" "+(item.strip("\n"))+" ").lower())
        word_lst.append(movie_word)
    for review in review_lst:
        for word in word_lst:
            if word.word in review.review:
                word.rating_lst.append(review.rating)

    print("-"*75)
