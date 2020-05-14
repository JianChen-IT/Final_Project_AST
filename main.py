# 1. Lectura de base de datos
# 2. Display --> pregunta + opciones (a,b,c,d || true,false & repeat command)
# 3. TTS para leer
# 4. Grabar la respuesta de un jugador e implementar un timer
# 5. Chequear pregunta

import question_reader as qr

while(1):
    filename = qr.pick_category()
    correct_answer,possible_answers = qr.read_json(filename)
    options = {}
    available_options = ["a","b","c","d"]
    for i in range(len(available_options)):
        options[available_options[i]]=i

    print("Pick and answer: ", end="")
    user_answer = input()
    if(user_answer =="exit"):
        break
    qr.check_solution(correct_answer, possible_answers[options[user_answer]])
    print("\n")
    
