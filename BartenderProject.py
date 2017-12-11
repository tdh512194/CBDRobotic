from random import randint

def Bartender():
  questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye likek a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?",
  }
  
  ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"],
  }
  for taste in questions:
    if input(questions[taste]) == "yes":
      print("I ve just got a drink for you here " + ingredients[taste][randint(0, len(ingredients[taste]) - 1)])
      break
  return