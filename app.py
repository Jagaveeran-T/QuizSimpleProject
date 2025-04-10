# Simple Quiz
print("Welcome to computer quiz")

playing = input("Do you want to play (yes/no): ")
if playing.lower() != "yes":
    quit()
else:
    print("Ok, let's play!")

score = 0
answer = input("What does CPU stand for: ")
if answer.lower() == "central processing unit":
    print("You are correct!")
    score += 1
else:
    print("Incorrect")

answer = input("What does GPU stand for: ")
if answer.lower() == "graphics processing unit":
    print("You are correct!")
    score += 1
else:
    print("Incorrect")

answer = input("What does RAM stand for: ")
if answer.lower() == "random access memory":
    print("You are correct!")
    score += 1
else:
    print("Incorrect")

print(f"\nYour final score is: {score}/3")
print(score)
total = (score/4)*100
print(f"You are {score} question correct")
print(f"You got {total}%")
