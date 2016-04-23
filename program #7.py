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
##
## OTHER COMMENTS:
##      Any special comments
##
######################################################################
def user_input(answer):
    answer = input(question)
    return answer

file = open("movieReviews.txt","r")
for line in file.readlines():
    slc = line[0]#Prints out ratings only
    print(slc)

question = user_input("Please enter the file containing a list of words you would like to analyze.")