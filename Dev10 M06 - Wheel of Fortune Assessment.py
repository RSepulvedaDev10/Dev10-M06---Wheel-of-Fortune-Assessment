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
    spin = random.randint(0, len(wheel) - 1)
    
    if spin == 'Bankrupt':
        return 0
    elif spin == 'Lose a Turn':
        return 1
    else:
        return spin * 50
    
while playGame == True:
    
    #Starting the game and naming the contestants
    
    print(f"Welcome to the Wheel of Fortune")
    print(f"================================")
    
    playerName[0] = input("Please enter the name of the first contestant: ")
    playerName[1] = input("Please enter the name of the second contestant: ")
    playerName[2] = input("Please enter the name of the third contestant: ")

    gameInitialize = input("The contestants are in. Press 'Enter' to begin the game.")
    
    #Round 1 and 2
    
    while rounds != 3:
        
        roundBalance = [0,0,0]
        selectedWord = random.choice(wordList).lower()
        guessesMade = []
        displayWord(selectedWord)
        solvedWord = False
        
        while solvedWord == False:
            
            while playerTurn != 5:
            
                if playerTurn == 4:
                    playerTurn = 1
            
                spinInitialize = input(f"\nIt is currently {playerName[playerTurn - 1]}'s turn. Press 'Enter' to spin the wheel.")
                spinResult = spinWheel()
            
                if spinResult == 0:
                    print(f"You landed on 'Bankrupt', and your balance has been reset to 0.\n")
                    roundBalance[playerTurn - 1] = 0
                    playerBank[playerTurn - 1] = 0
                    print(f"Moving on to the next player.\n")
                    playerTurn += 1
                    break
                
                elif spinResult == 50:
                    print(f"You landed on 'Lose a Turn'. Your turn is over.\n")
                    print(f"Moving on to the next player.\n")
                    playerTurn += 1
                    break
                
                else:
                    print(f"You landed on ${str(spinResult)}.\n")
                
                while (True):
                
                    displayWord(selectedWord)
                    
                    solvePrompt = input("\nWould you like to solve the puzzle (y/n)? ").lower()
                
                    if solvePrompt == 'y':
                        solveGuess = input("Please enter your guess to solve the puzzle: ")
                    
                        if len(solveGuess) != len(selectedWord):
                            print(f"Invalid guess.\n")
                            continue
                        
                        elif solveGuess == selectedWord:
                            print(f"{solveGuess} was the correct answer. Great job\n")
                            roundBalance[playerTurn - 1] += spinResult
                            print(f"{playerName[playerTurn - 1]} has earned ${roundBalance[playerTurn - 1]} from this round\n")
                            playerBank[playerTurn - 1] += roundBalance[playerTurn - 1]
                            solvedWord = True
                            break
                            
                        else:
                            print(f"Sorry. But {solveGuess} was not the correct answer.\n")
                            break  
                            
                    elif solvePrompt == 'n':
                        print(f"{playerName[playerTurn - 1]} has elected to not solve the puzzle.\n")

                    else:
                        print(f"Invalid input\n")
                        continue
                    
                    consonantGuess = input("Please enter your guess for the puzzle: ").lower()
            
                    if consonantGuess.isnumeric() or len(consonantGuess) > 1 or len(consonantGuess) <= 0 or consonantGuess in guessesMade or consonantGuess in vowel:
                        print(f"Invalid guess.\n")
                        continue
                    
                    elif consonantGuess in selectedWord:
                        guessesMade.append(consonantGuess)
                        print(f"Correct! '{consonantGuess}' is in the puzzle.\n")
                        roundBalance[playerTurn - 1] += spinResult
                        
                    else:
                        guessesMade.append(consonantGuess)
                        print(f"Sorry. '{consonantGuess}' is not in the puzzle\n")
                        break
                        
                    if roundBalance[playerTurn - 1] >= 250:
                        vowelPrompt = input("Would you like to buy a vowel (y/n)? ").lower()
                    
                        if vowelPrompt == 'y':
                            roundBalance[playerTurn - 1] -= 250
                            vowelGuess = input("Please enter your vowel guess for the puzzle: ").lower()
                       
                            if vowelGuess.isnumeric() or len(vowelGuess) > 1 or len (vowelGuess) <= 0 or vowelGuess in guessesMade:
                                print(f"Invalid guess.\n")
                                print(guessesMade)
                                continue
                            
                            elif vowelGuess in selectedWord:
                                guessesMade.append(vowelGuess)
                                print(f"Correct! '{vowelGuess}' is in the puzzle.\n")
                                
                            else:
                                guessesMade.append(vowelGuess)
                                print (f"Sorry. '{vowelGuess}' is not in the puzzle\n")
                                break 
                                  
                        elif vowelPrompt == 'n':
                            print(f"{playerName[playerTurn - 1]} has elected to not buy a vowel.\n")
                        
                        else:
                            print(f"Invalid input.\n")
                            continue
                        
                    endTurnPrompt = input("Would you like to end your turn (y/n)? ")
                    
                    if endTurnPrompt == 'y':
                        print(f"{playerName[playerTurn - 1]} has elected to end their turn.\n")
                        break
                                  
                    elif endTurnPrompt == 'n':
                        print(f"{playerName[playerTurn - 1]} has elected to continue their turn.\n")
                        
                    else:
                        print(f"Invalid input.\n")
                        continue
                    
                if solvedWord == True:
                    break
                                                        
                print(f"Here are the results from the current round: {playerName[0]}:${roundBalance[0]}, {playerName[1]}:${roundBalance[1]}, {playerName[2]}:${roundBalance[2]}\n")
                print(f"These are the guesses made currently in the round, {guessesMade}\n")
                print(f"Moving on to the next player.\n")
                playerTurn += 1
        
        print(f"Here are the current player balances: {playerName[0]}:${playerBank[0]}, {playerName[1]}:${playerBank[1]}, {playerName[2]}:${playerBank[2]}\n")
        print(f"Moving on to the next round!\n")
        
        rounds += 1
    
    
    #Final Round
    
    print(f"Here are the results from the 2 rounds: {playerName[0]}:${playerBank[0]}, {playerName[1]}:${playerBank[1]}, {playerName[2]}:${playerBank[2]}\n")
    
    maxBank = max(playerBank)
    maxIndex = playerBank.index(maxBank)
    finalPrize = 0
    
    print(f"{playerName[maxIndex]} is the winner and is moving on to the final round\n")
    
    finalInitialize = input(f"{playerName[maxIndex]}, press 'Enter' to spin for the final prize and start the final round")
    
    spinResult = spinWheel()
    
    if spinResult == 0:
        continue
    
    elif spinResult == 1:
        continue
    
    else:
        print(f"The final prize has been stored good luck.\n")
        finalPrize += (spinResult * 20)
    
    print(f"{playerName[maxIndex]}, here is your final word\n")
    
    selectedWord = random.choice(wordList).lower()
    guessesMade = ['r', 's', 't', 'l', 'n', 'e']
    
    print(f"We have entered these letters already: {guessesMade}, you need to enter 3 more consonants and a vowel.\n")
    
    displayWord(selectedWord)
    
    for x in range (0, 4):
        
        if x == 3:
            while(True):
                
                vowelGuess = input("\nPlease enter a vowel: ")
                if vowelGuess.isnumeric() or len(vowelGuess) > 1 or len(vowelGuess) <= 0 or vowelGuess in guessesMade:
                    print("Invalid input.\n")
                    continue
                
                else:
                    guessesMade.append(vowelGuess)
                    break
                
        else:
            while(True):
                
                consonantGuess = input("\nPlease enter a consonant: ")
                
                if consonantGuess.isnumeric() or len(consonantGuess) > 1 or len(consonantGuess) <= 0 or consonantGuess in guessesMade or consonantGuess in vowel:
                    print("Invalid input.\n")
                    continue
                else:
                    guessesMade.append(consonantGuess)
                    break
            
    displayWord(selectedWord)
    
    print(f"You have one guess to solve the puzzle. Good luck!\n")
    
    finalGuess = input('Please enter your final guess on the puzzle word: ').lower()
    
    if finalGuess == selectedWord:
        print(f"You have correctly guessed the prize word: {selectedWord}. Congratulations!\n")
        print(f"You final prize of ${finalPrize} will be added to your total.\n")
        maxBank += finalPrize
        
    else:
        print(f"You have not guessed the word correctly. The prize word was {selectedWord}.\n")
        print(f"You unfortunately have missed out on the final prize of ${finalPrize}\n")
    
    print(f"{playerName[maxIndex]} has won a total prize of ${maxBank}\n")
    print(f"Thank you for playing Wheel of Fortune!\n")
        
    quit()
    
    