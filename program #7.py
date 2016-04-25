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
##      Program 7 Algorithm
##•	Prompt user for what file they would like to read
##•	Open movie reviews file
##•	Close movie reviews file
##•	Open file that user chose
##•	Close file that user chose
##•	Iterate over movie reviews file and find the matching words from the list the user chose
##•	Count how many times each word is used
##•	Create a dictionary of the word as the key and the count as the value
##•	For each word, calculate the average and standard deviation
##o	Average = sum of numbers divided by the amount of numbers
##o	Standard deviation = (number minus the average squared) for each number, divided by the total amount of numbers
##•	Prompt user for how they would like their information displayed
##o	From highest average score to lowest
##o	Lowest to highest average
##o	Highest standard deviation to lowest
##o	Lowest standard deviation to highest
##•	Print the information in a table
##
##
##
## 
## ERROR HANDLING:
## If file user entered does not exist
## if movie review file does not exist
##  if user does not choose from the provided data layout options
##  if user enters a string instead of an int
##
## OTHER COMMENTS:
##      "I am your king"
##      "I didn't vote for you"
##                  -Monty Python and the Holy Grail
##
######################################################################
def open_file(correct):
   return open(correct)#opens file user chose

def get_user_input(question):
    """prints prompt to ask what file the user would like to use or if they want to quit the program"""
    while True:
        answer = input(question).lower()#gets input and converts it to lowercase
        if answer == "quit":
            return 0
        try:
            correct = open_file(answer)
        except FileNotFoundError:#Error handling if file not found
            print ("The file",answer,"was not found; Please try again.")
        except IOError:#Error handling for wrong file name format
            print("Please check the file name",answer,"for any incorrect special characters")
        except Exception:#catch all for any other errors
            print("Something went wrong; Please try again.")
        else:
            return correct#if no errors

def sort_order(question):
    """gets user input for what order they would like their data sorted in. Error handling for malicious input"""
    while True:
        user_answer = input(question)
        try:
            cnvrt = int(user_answer)#converts string to in to check if user entered a value in the expected range
            if cnvrt not in range(1,5):# if wrong number
                print("Your answer must be an integer from 1 to 4.")
                continue
            else:
                break
        except Exception:#if other error
            print("Please use a integer from 1 to 4.")
            continue
    return user_answer#returns value if no errors

def sort_ratings_stdeviation(order,words_list):
    """Sorts data depending on which type of sort the user chose."""
    if order == "1":
        return sorted(words_list,key=lambda x:x.avg_rating(),reverse=False)#average rating in ascending order
    elif order == "2":
        return sorted(words_list,key=lambda x:x.avg_rating(),reverse=True)#average rating in descending order
    elif order == "3":
        return sorted(words_list,key=lambda x:x.st_deviation(),reverse=False)#standard deviation in ascending order
    elif order == "4":
        return sorted(words_list,key=lambda x:x.st_deviation(),reverse=True)#standard deviation in descending order
    else:
        return words_list#will return list of words if no average rating or standard deviation


class Word(object):
    """create word class with attributes; word,raing_lst,rating. Functions to find average rating, total rating, standard deviation, and word count"""
    def __init__(self,word):
        self.word = word
        self.rating_lst = []
        self.rating = 0
    def avg_rating(self):
        """finds average rating"""
        if len(self.rating_lst) > 0:#makes sure function does divide by zero
            return self.total_rating()/len(self.rating_lst)
        else:
            return 0
    def total_rating(self):
        """finds total rating"""
        total_rating = 0
        for number in self.rating_lst:
            total_rating += number
        return total_rating

    def st_deviation(self):
        """finds standard deviation"""
        avg = self.avg_rating()
        sum_numerator = 0
        if len(self.rating_lst) == 0:#making sure not to divide by zero
            return 0
        for number in self.rating_lst:
            sum_numerator += ((number-avg)**2#finding numerator for standard deviation
        return sum_numerator/len(self.rating_lst)#sum of numerator divided by the length of the list
    def word_count(self):
        """finding the number of words"""
        return len(self.rating_lst)



class Review(object):
    """review class with attributes; rating and review. """
    def __init__(self,rating,review):
        self.rating = rating
        self.review = review



while True:
    try:
        movie_file = open("movieReviews.txt","r")#automatically opens file
        review_lst = []
        for line in movie_file.readlines():
            derp = Review(int(line[0]),(line [1:]).lower())#splits the list into ratings and reviews and converts reviews to all lowercase
            review_lst.append(derp)#appends the rating and the review to a new list
    except FileNotFoundError:
        print("movieReviews.txt was not found. Save it in the same location as the program and try again.")#if file not saved in the correct location
        break

    print("Word Sentiment Analyzer\n")#print title of program
    word_file = get_user_input("Please enter the file containing a list of words you would like to analyze or type quit to quit the program.")#ask user what file they want to analyze
    if word_file == 0:#quit the program if user enters quit
        break
    order_question = sort_order("In which order would you like your data displayed?\n1.)Avg ascending\n2.)Avg descending\n3.)Standard deviation ascending\n4.)Standard deviation descending\n")
    #asking user what order in which they want their data displayed
    word_lst = []
    for item in word_file:
        movie_word = Word((" "+(item.strip("\n"))+" ").lower())#strip line breaks and add spaces to either side of the word so that when searching the word is not part of a larger word
        word_lst.append(movie_word)
    for review in review_lst:
        for word in word_lst:#comparing two lists for a word in the wordlist files to see if they are in the movie review files
            if word.word in review.review:
                word.rating_lst.append(review.rating)#if the words are present in both files, make a new list of both the ratings and the reviews associated with the word

    print("{:<15}{:^15}{:>15}{:>30}".format("Word","Occurence","Avg","Std deviation"))#formating the headers of the table
    print("-"*75)#divides the headers with the rest of the table
    for word in sort_ratings_stdeviation(order_question,word_lst):#calls on a method to sort the standard deviation and the average ratings, given the parameters of which order the user chose
        #and the list created of the words that were found in the movie review files and their associated data
        print("{:<15}{:^15}{:>15.2f}{:>30.2f}".format(word.word,word.word_count(),word.avg_rating(),word.st_deviation()))#formating all the data found

