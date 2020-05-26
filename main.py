'''
Group Members: Irene Cantero Bandera (207525), Joan Garcia Marty (205331), Jian Chen (206064)
Final Project - Advanced Speech Technologies
TITLE:  

'''

import question_reader as qr
import time 
import os
import signal
import ASR
import sys

#---------------------------------VARIABLES------------------------------
#Variables used
TIMEOUT = 120           #2 min of game
total_points = 0        #Accumulated points
correct_answers = 0     #Number of correctly answered questions
total_questions = 0     #Number of total questions asked

#-----------------------AUXILIARY FUNCTIONS------------------------------
# Function that interrupts the program after 2 minutes
def interrupted (signum, frame):
    print ("\nTIME OUT!")
    os._exit(1)

# Setting the game to be interrupted after the TIMEOUT
signal.alarm(TIMEOUT)
signal.signal(signal.SIGALRM, interrupted)

#--------------------CORE PART OF THE GAME-------------------------------
while(1):
    filename = qr.pick_category()                                   # Picking a category to be displayed
    correct_answer,possible_answers = qr.read_json(filename)        # Choosing one question and collecting the correct answer and possible answers

    # Creating a dictionary to map each question to a,b,c or d. 
    # In this way, the computer can map the answer of the player with the different possible answers
    options = {}
    available_options = ["a","b","c","d"]
    for i in range(len(available_options)):
        options[available_options[i]]=i

    user_answer=ASR.asr()       #Getting the user answer

    # While loop to prevent any other possible solution. In this case is not necessary, but if we add more functionalities
    # it would be interesting to have it.
    while(user_answer!="a" and user_answer!="b" and user_answer!="c" and user_answer!="d" and user_answer!="exit"):
        print("\n")
        print("Your answer is not valid! Try Again!")
        sys.stdout.write("Pick an answer: ")
        sys.stdout.flush()
        user_answer=ASR.asr()

    print(user_answer)
    # If the user wants to end the game before the 2 minutes
    if(user_answer =="exit"):
        print("YOUR FINAL SCORE IS: " + str(total_points) + " " + str(correct_answers) + "/" + str(total_questions))
        break
    # Function that gives feedback to the user about the chosen question and updates the score.
    total_points, correct_answers, total_questions=qr.check_solution(correct_answer, possible_answers[options[user_answer]], total_points, correct_answers, total_questions)
    print("\n")
    
