
# Load the Packages
from rasa_nlu.training_data  import load_data
from rasa_nlu.config import RasaNLUModelConfig
from rasa_nlu.model import Trainer
from rasa_nlu import config


def trainnn():

	# Load Data 
	#data/demo-rasa.json


	# Loading DataSet
	train_data = load_data('data/demo-rasa.json')


	# Config Backend using Sklearn and Spacy
	trainer = Trainer(config.load("config_spacy.yaml"))

	# Training Data
	trainer.train(train_data)

	# Returns the directory the model is stored in (Creat a folder to store model in)
	model_directory = trainer.persist('projects/')
	#print(model_directory)
	return (model_directory)
