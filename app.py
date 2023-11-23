from flask import Flask, render_template, request
import random
import logging

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)

def load_words(file_path):
    try:
        with open(file_path, "r") as file:
            lines = file.readlines()
            words = [line.strip() for line in lines]
            return words
    except FileNotFoundError:
        logging.error("File not found: %s", file_path)
        raise

def initialize_game(word):
    display = ["_" for _ in range(len(word))]
    return display

def play_game(word, guessed_letter, display, lives):
    for position in range(len(word)):
        letter = word[position]
        if letter == guessed_letter:
            display[position] = guessed_letter

    if guessed_letter not in word:
        lives -= 1
        if lives == 0:
            return True, "You Lose!! The word was: " + word, display, lives

    if "_" not in display:
        return True, "You Win!!", display, lives

    return False, "", display, lives

@app.route('/')
def index():
    file_path = "words_train.txt"
    words = load_words(file_path)
    selected_word = random.choice(words)
    max_lives = 6
    display = initialize_game(selected_word)

    return render_template('index.html', word=selected_word, display=display, lives=max_lives)

@app.route('/play', methods=['POST'])
def play():
    guessed_letter = request.form['guessed_letter'].lower()
    word = request.form['word']
    display = request.form['display'].split(',')
    lives = int(request.form['lives'])

    game_over, message, display, lives = play_game(word, guessed_letter, display, lives)

    return render_template('index.html', word=word, display=display, lives=lives, message=message, game_over=game_over)

if __name__ == "__main__":
    app.run(debug=True)
