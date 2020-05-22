from pocketsphinx import AudioFile, get_model_path, get_data_path
from pocketsphinx import LiveSpeech
import os

def asr():
    model_path = get_model_path()
    
    speech = LiveSpeech(    
        verbose=False,
        sampling_rate=16000,
        buffer_size=2048,
        no_search=False,
        full_utt=False,
        hmm=os.path.join(model_path, 'en-us'),
        lm=os.path.join(model_path, 'en-us.lm.bin'),
        dic=os.path.join(model_path, 'cmudict-en-us.dict'))

    for phrase in speech:
        #print(phrase)
        if(len(str(phrase))>0):
            return str(phrase).split(" ")[0]
