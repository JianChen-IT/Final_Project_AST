import os
import random
import json
import html
from gtts import gTTS
import playsound
import glob
import sys
import ffmpy
from pydub import AudioSegment
os.chdir(os.path.dirname(os.path.abspath(__file__)) + "/Database/")
def pick_category():
    #categories_file = os.path.dirname(os.path.abspath(__file__)) + "/Database/"
    all_categories = glob.glob("*.json")
    #print(all_categories)
    filename = random.choice(all_categories)
    #print(filename)
    #print(all_categories)
    return filename

def read_json(my_json):
    json_file = open(os.getcwd() + "/" + my_json, 'r')
    data = json.load(json_file)
    choice = random.randint(0, len(data["results"]))
    output_scaped = html.unescape(data["results"][choice]["question"])
    correct_answer = html.unescape(data["results"][choice]["correct_answer"])

    possible_answers = data["results"][choice]["incorrect_answers"]
    possible_answers.append(correct_answer)
    for i in range(len(possible_answers)):
        possible_answers[i] = html.unescape(possible_answers[i])       
    random.shuffle(possible_answers)
    print(output_scaped)
    speak(output_scaped)
    options = ["a","b","c","d"]
    for i in range(len(possible_answers)):
            print("\t"+options[i] + "." + " " + possible_answers[i] + "\t")
            speak(options[i] + "." + " " + possible_answers[i])
    sys.stdout.write("Pick an answer: ")
    sys.stdout.flush()
    json_file.close()
    return correct_answer,possible_answers

def check_solution(correct_answer, given_answer, total_points, total_answers, total_questions):
    if correct_answer == given_answer:
        print("Correct!")
        print("TOTAL SCORE: " + str(total_points + 100) + " " + str(total_answers + 1) + "/" + str(total_questions + 1))
        return (total_points + 100), (total_answers + 1), (total_questions + 1)
    else:
        print("Incorrect! The correct answer is: " + correct_answer)
        print("TOTAL SCORE: " + str(total_points - 20) + " " + str(total_answers) + "/" + str(total_questions + 1))
        return (total_points - 20), (total_answers), (total_questions + 1)


def speed_change(sound, speed=1.0):
    # Manually override the frame_rate. This tells the computer how many
    # samples to play per second
    sound_with_altered_frame_rate = sound._spawn(sound.raw_data, overrides={
         "frame_rate": int(sound.frame_rate * speed)
      })
     # convert the sound with altered frame rate to a standard frame rate
     # so that regular playback programs will work right. They often only
     # know how to play audio at standard frame rate (like 44.1k)
    return sound_with_altered_frame_rate.set_frame_rate(44100)

def speak(text):
    sound = "voices/voice.wav"
    tts = gTTS(text = text,lang ='en')
    tts.save(sound)
    test = AudioSegment.from_file(sound)
    fast_sound = speed_change(test,1.15)
    fast_sound.export(sound, format="wav")
    playsound.playsound("voices/voice.wav")