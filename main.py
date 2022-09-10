import random
#Simple chat program
#Responds randomly with one of four preprogrammed responses
def soda_response(soda):
  responses = [
    "Love that soda!",
    "Great choice!",
    "That soda tastes terrible!",
  ]
  return random.choice(responses)



def food_response(food):
  responses = [
    "I love that food!",
    "Great choice!",
    "I hope you enjoy that food. Personally, I don't!",
  ]
  return random.choice(responses)

def color_response(user_input):
  responses = [
    "Mine too!",
    "Not as great as my favorite color!",
    "Best color in the world!"
  ]
  return random.choice(responses)


def generate_response(user):
  responses = [
    "I wish you the best",
  ]
  return random.choice(responses)


def init_chat():

  user_input = input("Hello, how are you? (To quit enter q)\n")
  if user_input == "q":
    quit()

  user_input = print(generate_response(user_input) + "\n")

def color_function():
  user = input("What is your favorite color?\n")
  if user == "q":
    quit()
  user = print(color_response(user) + "\n")


def food_function():
  food = input("What is your favorite food?\n")
  food = print(food_response(food) + "\n")
  if food == "q":
    quit()

def soda_function():
  soda = input("What is your favorite soda?\n")
  soda = print(soda_response(soda) + "\n")
  if soda == "q":
    quit()


if __name__ == "__main__":
  init_chat()
  color_function()
  food_function()
  soda_function()


experience = input("How is your experience going? (great or not so good?) ")
if experience == "q":
    quit()
if experience == "great":
  print("\n" + "Im so happy let us continue")
else:
    print("\n" + "Aw sorry let's hope it gets better")


elective = input("\n" + "What is your favorite elective in school ")
if elective == "q":
    quit()
if elective == "Computer Science":
  print("\n" + "Computer Science rules!")
elif elective == "computer science":
  print("\n" + "Computer Science rules!")
elif elective == "cs":
  print("\n" + "Computer Science rules!")
elif elective == "CS":
  print("\n" + "Computer Science rules!")
elif elective == "Computer science":
  print("\n" + "Computer Science rules!")

else:
    print("\n" + "That sounds cool but computer science is better")

destination = input("\n" + "Where are you from ")
if destination == "q":
    quit()
if destination == "United States":
  print("\n" + "United States is awesome!")
elif destination == "US":
  print("\n" + "United States is awesome!")
elif destination == "United States of America":
  print("\n" + "United States is awesome!")
elif destination == "united states":
  print("\n" + "United States is awesome!")

else:
    print("\n" + "That sounds so cool. I want to go there!")

rating = int(input("\n" + "Final question. Rate your experience on a scale of 1-10 "))
if rating == "q":
    quit()
if rating<5:
  print("\n" + "Sorry you didn't like it!")
else:
    print("\n" + "Glad you enjoyed! See you next time")


