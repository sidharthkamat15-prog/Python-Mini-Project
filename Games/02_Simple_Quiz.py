# SIMPLE QUIZ PROGRAM

print("Welcome to the Simple Quiz!")
score = 0

answer1 = input("- What is the capital of Japan?\n")
if answer1.lower() == "tokyo":
    print("Correct!")
    score += 1
else:
    print("Wrong! The correct answer is Tokyo.")

answer2 = input("- Which planet is known as the Red Planet?\n")
if answer2.lower() == "mars":
    print("Correct!")
    score += 1
else:
    print("Wrong! The correct answer is Mars.")

answer3 = input("- Who painted the famous artwork Mona Lisa?\n")
if answer3.lower() == "leonardo da vinci":
    print("Correct!")
    score += 1
else:
    print("Wrong! The correct answer is Leonardo da Vinci.")

answer4 = input("- What is the largest mammal in the world?\n")
if answer4.lower() == "blue whale":
    print("Correct!")
    score += 1
else:
    print("Wrong! The correct answer is Blue Whale.")

answer5 = input("- Which sport is often called the beautiful game?\n")
if answer5.lower() == "football" or answer5.lower() == "soccer":
    print("Correct!")
    score += 1
else:
    print("Wrong! The correct answer is Football (Soccer).")

answer6 = input("- In which country would you find the Great Pyramid of Giza?\n")
if answer6.lower() == "egypt":
    print("Correct!")
    score += 1
else:
    print("Wrong! The correct answer is Egypt.")

answer7 = input("- What is the fastest land animal?\n")
if answer7.lower() == "cheetah":
    print("Correct!")
    score += 1
else:
    print("Wrong! The correct answer is Cheetah.")

answer8 = input("- Who wrote the play Romeo and Juliet?\n")
if answer8.lower() == "william shakespeare":
    print("Correct!")
    score += 1
else:
    print("Wrong! The correct answer is William Shakespeare.")

answer9 = input("- Which gas do humans need to breathe to survive?\n")
if answer9.lower() == "oxygen":
    print("Correct!")
    score += 1
else:
    print("Wrong! The correct answer is Oxygen.")

answer10 = input("- What is the tallest mountain in the world?\n")
if answer10.lower() == "mount everest":
    print("Correct!")
    score += 1
else:
    print("Wrong! The correct answer is Mount Everest.")

print(f"Your total score is {score} out of 10.")