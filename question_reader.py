'''
Group Members: Irene Cantero Bandera (207525), Joan Garcia Marty (205331), Jian Chen (206064)
Final Project - Advanced Speech Technologies

TITLE: Trivial
Date: 26/05/2020
'''

import os
import random
import json
import html
from gtts import gTTS
import playsound
import glob
import sys
from pydub import AudioSegment


os.chdir(os.path.dirname(os.path.abspath(__file__)) + "/Database/")

# Function that chooses between the different jsons
def pick_category():
    all_categories = glob.glob("*.json")

    filename = random.choice(all_categories)
    return filename

# Core function needed to read and choose a question and get all the possible answers
def read_json(my_json):
    # Opening the json file
    json_file = open(os.getcwd() + "/" + my_json, 'r')
    data = json.load(json_file)
    # Selecting a random question, getting the correct answer and all possible answers
    choice = random.randint(0, len(data["results"]))
    # The html.unescape() is to interpret correctly the non-alphanumeric characters
    output_scaped = html.unescape(data["results"][choice]["question"])          
    correct_answer = html.unescape(data["results"][choice]["correct_answer"])
    possible_answers = data["results"][choice]["incorrect_answers"]
    possible_answers.append(correct_answer)
    # Applying html.unescape() to each possible answer and shuffling them
    for i in range(len(possible_answers)):
        possible_answers[i] = html.unescape(possible_answers[i])       
    random.shuffle(possible_answers)
    # Saying the question out loud
    print(output_scaped)
    speak(output_scaped)
    # Displaying the different possible answers and saying them out loud.
    options = ["a","b","c","d"]
    for i in range(len(possible_answers)):
            print("\t"+options[i] + "." + " " + possible_answers[i] + "\t")
            speak(options[i] + "." + " " + possible_answers[i])
    sys.stdout.write("Pick an answer: ")
    sys.stdout.flush()
    json_file.close()
    return correct_answer,possible_answers  # Returning the all possible answers to the main function

# Solution checker, which also gives feedback and updates the score.
def check_solution(correct_answer, given_answer, total_points, total_answers, total_questions):
    if correct_answer == given_answer:
        print("Correct!")
        print("TOTAL SCORE: " + str(total_points + 100) + " " + str(total_answers + 1) + "/" + str(total_questions + 1))
        return (total_points + 100), (total_answers + 1), (total_questions + 1)
    else:
        print("Incorrect! The correct answer is: " + correct_answer)
        print("TOTAL SCORE: " + str(total_points - 20) + " " + str(total_answers) + "/" + str(total_questions + 1))
        return (total_points - 20), (total_answers), (total_questions + 1)

# Function that makes faster the voice to make the game more dynamic.
# The pitch is also modified
def speed_change(sound, speed=1.0):
    sound_with_altered_frame_rate = sound._spawn(sound.raw_data, overrides={
         "frame_rate": int(sound.frame_rate * speed)
      })
    return sound_with_altered_frame_rate.set_frame_rate(44100)

# Core function of the TTS to make the program speak.
def speak(text):
    sound = "voices/voice.wav"
    tts = gTTS(text = text,lang ='en')
    tts.save(sound)
    test = AudioSegment.from_file(sound)
    fast_sound = speed_change(test,1.15)
    fast_sound.export(sound, format="wav")
    playsound.playsound("voices/voice.wav")