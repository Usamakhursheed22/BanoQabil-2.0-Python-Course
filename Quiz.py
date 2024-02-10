#Name: Usama khursheed
#Contact: 03493779335
#Email:usamakhursheed315@gmail.com
#Campus:Gulshan

#QUIZ GAME

print("Welcome to my computer quiz game! ")

playing = input("Do you want to play? ")

#Here is use != operator. If the user provides any answer other than "yes", the condition becomes true, and the quiz quits.

if playing.lower() != "yes":
    quit()

print("Great! Let's play ")
score = 0

#Question no:1

answer  = input("Who is the founder of Pakistan? ")

#I used ".lower()" so If the user types in uppercase, the program will automatically convert it to lowercase so it will still be recognized as correct.  

if answer.lower() == "muhammad ali jinnah":
    print('Correct!')

    # The score += 1 statement is used to increment the score by 1 every time the user provides a correct answer.
    
    score += 1
else:
    print("Incorrect")

#Question no: 2
    
answer  = input("Who saw the dream of Pakistan? ")
if answer.lower() == "allama iqbal":
    print('Correct!')
    score += 1
else:
    print("Incorrect")

#Question no: 3 

answer  = input("What does PPP stand for? ")
if answer.lower() == "pakistan peoples party":
    print('Correct!')
    score += 1
else:
    print("Incorrect")

#Question no: 4
    
answer  = input("What is the capital of pakistan? ")
if answer.lower() == "islamabad":
    print('Correct!')
    score += 1
else:
    print("Incorrect")

#Question no: 5
    
answer  = input("Which city called the city of lights? ")
if answer.lower() == "karachi":
    print('Correct!')
    score += 1
else:
    print("Incorrect")

print("Conguratulations you got " + str(score) + " questions correct! out of 5 ")

