import random
import image
with open("words_train.txt", "r") as file:
    lines = file.readlines()

# Remove newline characters and create a list of words
words = [line.strip() for line in lines]

# Display the list of words
print(words)

word=random.choice(words)
print(word)
lives=6
display=[]
for i in range(len(word)):
    display+= "_"
print(display)
game_over=False
while not game_over:
    guesssed_letter=input("Guess a letter: ").lower()
    for position in range(len(word)):
        letter=word[position]
        if letter==guesssed_letter:
            display[position]=guesssed_letter
    print(display)
    if guesssed_letter not in word:
        lives-=1
        if lives==0:
            game_over=True
            print("You Lose!!")
            print("The word was :", word)
    
    if "_" not in display:
        game_over=True
        print("You Win!!")
    print(image.hangman[lives])

