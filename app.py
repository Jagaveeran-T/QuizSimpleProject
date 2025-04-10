# Simple Quiz

print("Welcome to computer quiz")
playing = input("Do you want to play(yes/no): ")
if playing.lower() != "yes":
  quit()
else:
  print("Ok lets play")
score = 0
answer = input("What does CPU stand for: ")
if answer.lower() == "Central Processing unit":
  print("You are correct")
  score +=1
else:
  print("Incorrect")
answer = input("What does GPU stand for: ")
if answer.lower() == "graphics processing unit":
  print("You are correct")
  score +=1
else:
  print("Incorrect")
answer = input("What does RAM stand for: ")
if answer.lower() == "random access memory":
  print("You are correct")
  score +=1
else:
  print("Incorrect")
answer = input("What does PSU stand for: ")
if answer.lower() == "power supply":
  print("You are correct")
  score +=1
else:
  print("Incorrect")
print(score)
total = (score/4)*100
print(f"You are {score} question correct")
print(f"You got {total}%")