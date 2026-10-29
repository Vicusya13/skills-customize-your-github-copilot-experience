
# 📘 Assignment: Hangman Game

## 🎯 Objective

Build a word-guessing game in Python to practice strings, loops, conditionals, user input, and random selection. The player will guess a hidden word before running out of attempts.

## 📝 Tasks

### 🛠️	Build the Hangman Game

#### Description
Create a Hangman game that randomly selects a word from a predefined list and lets the player guess it one letter at a time.

#### Requirements
Completed program should:

- Select a word at random from a list of at least five words.
- Show each unrevealed letter as an underscore and reveal correctly guessed letters.
- Track and display the number of incorrect guesses remaining.
- End when the player guesses the word or runs out of attempts.
- Display a clear win or loss message; on a loss, reveal the word.


### 🛠️	Add Input Checks and Replay

#### Description
Improve the game by handling invalid or repeated guesses and allowing the player to start another round after a game ends.

#### Requirements
Completed program should:

- Accept one letter per guess and reject empty input or input that is not a letter.
- Tell the player when they have already guessed a letter without using an attempt.
- Ask whether the player wants to play again after each round.
- Start a new round with a newly selected word when the player chooses to replay.
