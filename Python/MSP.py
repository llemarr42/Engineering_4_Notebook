
    
def everything(misses, guessed, PrettyDash, cguess):     #function for printing hangman
     if misses > 0:
        print("---┐ ")
     if misses > 1:
         print("   O" )
     if misses == 3:
         print("   | ")
     if misses == 4:
         print("  \| ")
     if misses > 4:
         print("  \|/ ")
     if misses > 5:
         print("   |")
     if misses == 7:
         print("   / " )
     if misses > 7:
         print("  / \ ")
     print("Guessed Words:\t" + str(guessed))    # Prints all the letters that were already guessed
     for place in range(len(word)):    # Repeates for every character in the word
         if word[place] in cguess:     # Checks where the correct guess is in word
            PrettyDash = PrettyDash[:place] + word[place] + PrettyDash[place+1:]     # Replaces "-" with correct letter
     PrettyDash = " ".join(PrettyDash) # Adds spaces between the dashes/letters
     print( PrettyDash+"\n")
misses=0
correct=0
txt=input("Player1, what's the word:")
while True:
    print("\n" * 50)
    if " " in txt:       #makes sure the player1's input is not multiple words
        print("please enter one word")
        txt=input("Player1, what's the word:")
    else:
        break
length = len(txt)
uni = len(set(txt))
word = [char for char in txt]
print("\n" * 50)
guessed = ""
cguess = ""
guess = ""
PrettyDash= ("_") * len(word) 
#PrettyDash=" ".join(dashes)
everything(misses, guessed, PrettyDash, cguess)    # Calls the function
while misses <=7:
   guess=input("Player2, guess a letter:")    # player2 gets to guess
   guessed = list(guessed)
   if guess in guessed:    # Checks to make sure they do not guess the same letter twice
        print("\n" * 50)
        print("you already guessed:" + guess)
        everything(misses, guessed, PrettyDash, cguess)
   elif guess in word:     # Checks to see if the guess is correct
        print("\n" * 50)
        guessed.append(guess) # Adds the guessed letter to the list guess
        correct = correct + 1
        cguess = cguess + guess
        everything(misses, guessed, PrettyDash, cguess)
   else:                    # Checks to see if guess is wrong
        print("\n" * 50)
        misses = misses + 1
        guessed.append(guess)
        everything(misses, guessed, PrettyDash, cguess)
   if  correct == uni:    # If Player2 had as many correct guesses as there are characters in the word they win
        print("Congratulations, Player2 wins!!!")
        print("The word was:\t" + str(word))
        break
if misses >7:    # If player2 got 8 guesses wrong they loose
    print("Game Over")
   

