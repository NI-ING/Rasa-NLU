# Rasa-NLU

Rasa NLU is an open-source natural language processing tool for intent classification, 
response retrieval and entity extraction in chatbots.

 For example, taking a sentence like :  * "I am looking for a Mexican restaurant in the center of town" *
 
 and returning structured data (json)  like this :
 
 
 {
 
  "intent": "search_restaurant",
  
  "entities": {
 
    "cuisine" : "Mexican",
    
    "location" : "center"
    
  }
  
}

