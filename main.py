import random
lockedDifficulty = False
def getNumber(diff):
    currentNumber = 0
    numRange = (0,10)
    if diff == "easy":
        numRange = (0,10)
    elif diff == "normal":
        numRange = (10,100)
    elif diff == "hard":
        numRange = (0,100)   
    elif diff == "extreme":
        numRange = (0,1000)
    elif diff == "extreme+":
        numRange = (0,10000)         
    return random.randrange(*numRange)
    

print("""
        Difficulties
  ----------------------
   easy      ---> Numbers are between 0 and 10
   normal    ---> Numbers are between 10 and 100
   hard      ---> Numbers are between 0 and 100
   extreme   ---> Numbers are between 0 and 1000
   extreme+  ---> Numbers are between 0 and 10000
""")
print("\nLocking the difficulty will not ask for diffuculty level in each game...")
ldiff = input("Do you want to lock the difficulty level [Y/n]: ").strip().lower()
if ldiff == "y":
    lockedDifficulty = True
    difficulty = input("Difficulty Level: ").strip().lower()
else:
    lockedDifficulty = False
rounds = 5
currentRounds = 0
wonIn = 0
try:
    while True:
        if not lockedDifficulty:difficulty = input("Difficulty Level: ").strip().lower()
        num = int(input("Guess the Number: ").strip())
        
        randNum = int(getNumber(difficulty))
        if rounds>=2:
            if num==randNum:
                print("You Won!")
                print(f"\nRound: {currentRounds}\n")
                rounds = 5
                currentRounds+=1
                wonIn+=1
            else:
                print("Try again...")
        else:

            if num==randNum:
                print("You Won!")
                print(f"\nRound: {currentRounds}")
                rounds = 5
                currentRounds+=1
                wonIn+=1
            else:
                print(f"You Lose! The number was {randNum}")
                rounds = 5
                currentRounds+=1
                print(f"\nRound: {currentRounds}")
                
        rounds-=1
except KeyboardInterrupt:
    print(f"\nYou won in {wonIn} rounds!")