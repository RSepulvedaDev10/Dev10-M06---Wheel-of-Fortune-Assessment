#Game Setup

import random

playGame = True

playerName = [None, None, None]

playerBank = [0, 0, 0]

wheel = ['Bankrupt', 'Lose a Turn']
for x in range(2, 19):
    wheel.append(50 * x)
    
wordsAlpha = open('words_alpha.txt')
wordList = wordsAlpha.read().splitlines()

consonant = ['b', 'c', 'd', 'e', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']

vowel = ['a', 'e', 'i', 'o', 'u']

guessesMade = []

rounds = 1

playerTurn = 1

def displayWord(selectedWord):
    for letter in selectedWord:
        if letter in guessesMade:
            print(f"{letter}", end="")
        else:
            print(f"_", end="")
    return

def spinWheel():
    spin = random.randint(wheel)
    
    if spin == 'Bankrupt':
        return 0
    elif spin == 'Lose a Turn':
        return 1
    else:
        return spin
    

while playGame == True:
    
    #Starting the game and naming the contestants
    
    print(f"Welcome to the Wheel of Fortune")
    print(f"================================")
    
    playerName[0] = input("Please enter the name of the first contestant: ")
    playerName[1] = input("Please enter the name of the second contestant: ")
    playerName[2] = input("Please enter the name of the third contestant: ")

    #Round 1 and 2
    """
    while rounds != 3:
        
        roundBalance = [0,0,0]
        selectedWord = random.choice(wordList).lower()
        guessesMade = []
        displayWord(selectedWord)
        
        while playerTurn != 5:
            
            if playerTurn == 4:
                playerTurn = 1
                
            spinResult = spinWheel()
            
            if spinResult == 0:
                print(f"You landed on 'Bankrupt', and you lose your balance for the round.")
                roundBalance[playerTurn - 1] = 0
                playerTurn += 1
                
            elif spinResult == 1:
                print(f"You landed on 'Lose a Turn'. Your turn is over.")
                playerTurn += 1
                
            else:
                print(f"You landed on {str(spinResult)}.")
            
         
        print(f"Here are the results from the current round: {playerName[0]}:${roundBalance[0]}, {playerName[1]}:${roundBalance[1]}, {playerName[2]}:${roundBalance[2]}")
           
        playerBank[0] += roundBalance[0]
        playerBank[1] += roundBalance[1]
        playerBank[2] += roundBalance[2]
        
        print(f"Here are the current player balances: {playerName[0]}:${playerBank[0]}, {playerName[1]}:${playerBank[1]}, {playerName[2]}:${playerBank[2]}")
        print(f"Moving on to the next round!")
        
        rounds += 1
    """
    
    #Final Round
    
    print(f"Here are the results from the 2 rounds: {playerName[0]}:${playerBank[0]}, {playerName[1]}:${playerBank[1]}, {playerName[2]}:${playerBank[2]}")
    
    maxBank = max(playerBank)
    maxIndex = playerBank.index(maxBank)
    
    print(f"{playerName[maxIndex]} is the winner and is moving on to the final round")
    
    selectedWord = random.choice(wordList).lower()
    guessesMade = ['r', 's', 't', 'l', 'n', 'e']
    displayWord(selectedWord)
    
    consonant1 = input("Please enter your first consonant: ").lower()
    guessesMade.append(consonant1)
    consonant2 = input("Please enter your second consonant: ").lower()
    guessesMade.append(consonant2)
    consonant3 = input("Please enter your third consonant: ").lower()
    guessesMade.append(consonant3)
    vowel = input('Please enter your vowel: ').lower()
    guessesMade.append(vowel)
    
    displayWord(selectedWord)
    
    finalGuess = input('Please enter your final guess on the word ').lower()
    
    if finalGuess == selectedWord:
        print(f"You have correctly guessed the prize word: {selectedWord}. Congratulations!")
    else:
        print(f"You have not guessed the word correctly. The prize word was {selectedWord}.")
    
    