import random

def valid_input(): #function that verifies if the user's input is valid
   while True :
      input_user = input("Do you want to play a game? ฅ [y or n] ฅ ").lower() #asks for the user's input and lowers the input
      if input_user in ["y","n"] : #checks if the input is y or n
          return input_user
      else :
          print("Invalid input! >^•-•^<")

def cat_guessing_game():
   number = random.randint(1,15) #generates a random number out of the range established

   player = input("Hello there! What's your name? ")

   print(f"Hello {player}! ⋆˚🐾˖°")

   answer = valid_input() #checks if the user's input is valid (y or n)
   if answer == "n" :
      print("Come on! Let's have fun. ฅ(ᵔ꒳ ᵔマ.ᐟ")
      answer = input("Do you want to play a game? ฅ [y or n] ฅ ")
      if answer == "n" :
         print("I'm not jigsaw, I promise! =^-ㅅ-^=")
         answer = input("Do you want to play a game? ฅ [y or n] ฅ ")
         if answer == "n" :
           print("Okay, bye-bye /ᐠ ╥ ˕ ╥マ")
           return #exists function
   elif answer != "y" :
       print("Invalid input! >^•-•^<")


   print(f"Okay, {player}! Guess a number between 1 and 15: ᓚᘏᗢ ")

   number_of_guesses = 0 #initializes a variable outside of while loop

   while number_of_guesses < 5 :
       guess = input()
       if guess.isdigit():
           guess = int(guess)
           number_of_guesses += 1  # increments the number of guesses by one
           if guess < number:
               print("Too low!\n")
               print("     へ\n"
                     "  ૮  >  <)\n"
                     "  /  ⁻  ៸|\n"
                     "乀(ˍ, ل ل \n")
           elif guess > number:
               print("Too high!\n")
               print(" ╱|、\n"
                     "(˚ˎ 。7\n"
                     "|、˜〵\n"
                     "じしˍ,)ノ\n")
           elif guess == number:
               print(f"Congratulations, {player}! You guessed my number in " + str(
                   number_of_guesses) + " tries! Good job!\n")
               print("      へ   ♡    ╱|、\n"
                     "૮  >  <)      (˚ˎ 。7\n"
                     "/  ⁻  ៸|        |、˜〵\n"
                     "乀(ˍ, ل ل        じしˍ,)ノ\n")
               return  # exists function
           else:
               print(f"Sorry {player}, you did not guess my number. The number was " + str(number) + " /ᐠ - ˕ -マ Ⳋ")
               print("Goodbye!")
               return  # exists function
       else :
           print("Invalid input! >^•-•^<")


cat_guessing_game() #calls the function