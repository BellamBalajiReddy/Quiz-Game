print("Welcom to the game!")

playing =input("Do you want to play the game? ")
if playing.lower() !="yes":
    quit()

print("Lets play")
score=0
answer = input("what is the full form os CPU? ")
if answer.lower() == "control processing unit":
    print("correct")
    score +=1
else:
    print("Incorrect")

answer = input("what is the full form os GPU? ")
if answer.lower() == "graphical processing unit":
    print("correct")
    score +=1
else:
    print("Incorrect")       
  
answer = input("what is the full form os AI? ")
if answer.lower() == "Artificial intelligence":
    print("correct")
    score +=1
else:
    print("Incorrect")

answer = input("what is the full form os ML? ")
if answer.lower() == "Machine learning":
    print("correct")
    score +=1
else:
    print("Incorrect")  
      
print ("You have answerd  " + str(score)+ "  questions")      
print("you have got" +(str(score/4 )*100)+ "%.") 


