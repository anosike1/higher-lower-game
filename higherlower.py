# immport data from our game_data file (which contains our data)
from game_data import *
# import the art from our art file
from art import *
# import random
from random import *

# print out the introductory text
print ("Welcome to the higher lower game".upper())

# let the initial score be 0 (we'll change this later)
score = 0
# create a loop which will keep running until we say so
while True:
    # get a random data dictionary from our data list and assign it to the variable FIRST
    first = choice (data)
# get another random dictionary from the data list and assign it to the variable SECOND
    second = choice (data)
    # to avoid repetition, if the second data dicitonary is the same as the first...
    # another data dictionary will be created
    if second == first:
        second = choice (data)

# print our introdcutory message, by formatting the string using....
# ...the name, description, and country of the selected data
    print (f"Compare A: {first['name']}, a {first['description']}, from {first['country']}")
    print (vs)
    print (f"Against B: {second ['name']}, a {second['description']}, from {second['country']}")

# ask the user to guess who has the higher follower count and format this in lower case
    guess = input ("Who has a higher follower count? A or B? ").lower()

# if the follower count in our first data dictionary is more than the second, that will
#...become our answer
    if first ['follower_count']>second['follower_count']:
        answer = first ['follower_count']
# else the follower count in the second data dictionary is our answer
    else:
        answer = second ['follower_count']
# if the user types in 'a', then it means that he selected the first follower count
    if guess == 'a':
        user_guess = first ['follower_count']
# else if he typed in 'b', it means that he opted for the second follower count
    elif guess == 'b':
        user_guess = second ['follower_count']
# if he typed neither 'a' nor 'b', he gets a WRONG OPTION response and the program ends
    else:
        print ("Wrong option!")
        break
# if the user guess is the answer, he gets a CORRECT ANSWER, and the score increases
    if user_guess == answer:
        print ("Correct answer!")
        score+=1 
# if the user gets the wrong answer, he gets a YOU LOST RESPONSE,
# gets the total points
# and the program ends
    else:
        print ("Oh, You Lost!")
        print (f"You scored {score} points!")
        break