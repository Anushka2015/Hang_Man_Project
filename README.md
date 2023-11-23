# Hang_Man_Project
1.Create a github repository named https://github.com/Anushka2015/Hang_Man_Project,Readme.md,.gitignore,and MIT License added.
2.Clone repository to my system.
3. Create New environment and activate it by using these commands
conda create -n hangman python==3.8 -y
conda activate hangman
4.import all the required libraries
pip install -r requirements.txt
5.setup.py install 
python setup.py install
6.setup.py created to import the packages 
8.code written in trial.py to check the hangman game
9.write that code in modular coding in hangman.py
10.Make the app for hangman game using flask in app.py followed by index.html in templates. 
STRATEGY TO PLAY THE GAME:
Hangman is a popular word guessing game where the player attempts to build a missing word by guessing one letter at a time. After a certain number of incorrect guesses, the game ends and the player loses. The game also ends if the player correctly identifies all the letters of the missing word.Here I use python to write a logic to play this game.The words which need to be gussed has taken from the dctionary of 25000 words randomly.Player can see the blank spaces according to the length of the word and start guessing the word.Play will get only 6 chance to guess the word no matter how long the word will be.If Player guess the right letter which is present in the word then that letter will dispay at perticular place if not then player will loose his one chance and hangman will start drawn,if this will continue till 6 changes the player will loose the game and complete hangman will be drawn and player can see that what was the correct word.If player will guess correct  letters present in word than he will won the game.I use flask to covert this Hang man game in to an app.