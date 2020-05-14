import os
import random
import json
import html

os.chdir(os.path.dirname(os.path.abspath(__file__)) + "/Database/")
def pick_category():
    #categories_file = os.path.dirname(os.path.abspath(__file__)) + "/Database/"
    all_categories = os.listdir()
    filename = random.choice(all_categories)
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
    options = ["a","b","c","d"]
    for i in range(len(possible_answers)):
            print("\t"+options[i] + "." + " " + possible_answers[i] + "\t")
    
    json_file.close()
    return correct_answer,possible_answers

def check_solution(correct_answer, given_answer):
    if correct_answer == given_answer:
        print("Correct!")
        return True
    else:
        print("Incorrect! The correct answer is: " + correct_answer)
        return False

