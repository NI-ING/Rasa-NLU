
# Load the Packages
from rasa_nlu.training_data  import load_data
from rasa_nlu.config import RasaNLUModelConfig
from rasa_nlu.model import Trainer
from rasa_nlu import config
import training  


MODEL_DIRECTORY = training.trainnn()


#import spacy
#nlp = spacy.load('en')

#docx = nlp(u"I am looking for an Italian Restaurant where I can eat")

#for word in docx.ents:
    #print("value",word.text,"entity",word.label_,"start",word.start_char,"end",word.end_char)

from rasa_nlu.model import Metadata, Interpreter

# where `model_directory points to the folder the model is persisted in
interpreter = Interpreter.load(MODEL_DIRECTORY)

#Prediction of Intent
#interpreter.parse(u"I am looking for an Italian Restaurant where I can eat")
print (interpreter.parse("have a good day and thank you "))
#interpreter.parse(u"Good morning World")





