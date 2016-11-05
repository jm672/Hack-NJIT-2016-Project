import random
wordBank = ['amalgamation','gathering','hilarious','particular','representations','sodiumcholrine','carbohydrate']
stat = true
strike = 0
score = 0
print("Type the word then press enter!")
while stat == true:
  wordQuiz = wordBank[random.randint(0,len(wordBank))]
  wordType = input(wordQuiz)
  if wordType == wordQuiz:
    score += 1
    continue
  else:
    strike += 1
  if strike == 3:
    print('Game Over!')
    break
  
  
