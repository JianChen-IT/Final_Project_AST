'''
Group Members: Irene Cantero Bandera (207525), Joan Garcia Marty (205331), Jian Chen (206064)
Final Project - Advanced Speech Technologies

TITLE: Trivial
Date: 26/05/2020
'''


from pocketsphinx import get_model_path
from pocketsphinx import LiveSpeech
import os

# This function calls the ASR to listen to the user input.
def asr():
    # Getting the directory where the dictionary, language, and other features of the ASR is located
    model_path = get_model_path()
    # Setting the parameters of the speech
    speech = LiveSpeech(    
        verbose=False,
        sampling_rate=16000,
        buffer_size=2048,
        no_search=False,
        full_utt=False,
        hmm=os.path.join(model_path, 'en-us'),
        lm=os.path.join(model_path, 'en-us.lm.bin'),
        dic=os.path.join(model_path, 'cmudict-en-us.dict'))
    # If any answer is captured, return it to the main.
    for phrase in speech:
        if(len(str(phrase))>0):
            return str(phrase).split(" ")[0]    # We splitted the output, to only get the first answer and ignore the rest
                                                # In this way, if the user answers multiple times, it only gets the first one.