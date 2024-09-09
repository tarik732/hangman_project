import random
from hangman_words import word_list
from hangman_art import stages,logo

print(logo)

#world_list = ["come", "go", "exit", "running", "sleeping", "eating"]
correct_letter=[]
chosen_word = random.choice(word_list)
print(chosen_word)

Game_over=False
live=6
placeholder = ""
for x in chosen_word:

        placeholder += "_"




print(f"Word to guess:",placeholder)
while not Game_over:
    guess = input("Guess a letter:").lower()
    display=""
    if guess in correct_letter:
        print(f"you have already guessd {guess}")
    for x in chosen_word:
        if x ==guess:
            display += x
            correct_letter.append(guess)
        elif x in correct_letter:
            display += x
        else:
            display += "_"

   # print(f"Word to guess:",display)

    if guess not in chosen_word:
        live -=1
        print(f"you guessed {guess},that's not in the word.you lose a life")
        if live==0:
            Game_over=True
            print(stages[live])
            print(f"*********oh! no .The word was {chosen_word}.you lose!**********")
            #print("you lose")
            break

    if "_" not in display:
        Game_over=True
        print(stages[live])
        print(f"*********Exactly!!! .The word is {chosen_word}.you Win!**********")
        #print("you win")
        break
    print(stages[live])
    print(f"***************<{live}>/6 LIVES LEFT*************")
    print(f"word to guess: {display}")