# 2. Display --> pregunta + opciones (true,false & repeat command)
# 3. TTS para leer
# 4. Grabar la respuesta de un jugador e implementar un timer

import question_reader as qr
import time 
import os
import signal

TIMEOUT = 60
total_points = 0

def interrupted (signum, frame):
    print ("\nTIME OUT!")
    #signal.signal(signal.SIGALRM, interrupted)
    os._exit(1)
def user_input():
    try:
        user_answer = input()
        return user_answer
    except:
        return
signal.alarm(TIMEOUT)
signal.signal(signal.SIGALRM, interrupted)

while(1):
    filename = qr.pick_category()
    correct_answer,possible_answers = qr.read_json(filename)
    options = {}
    available_options = ["a","b","c","d"]
    for i in range(len(available_options)):
        options[available_options[i]]=i
    #qr.speak("Pick and answer");
    print("Pick and answer: ", end="")

    user_answer = user_input()
    if(user_answer =="exit"):
        break
    qr.check_solution(correct_answer, possible_answers[options[user_answer]], total_points)
    print("\n")
    
