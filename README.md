# Hangman game
This Python-powered Hangman game is here to challenge you and test your word-guessing skills
### Features:
- **Field Selection:** Choose from 6 different fields (categories) for the secret word, making the game more diverse and challenging. The fields include "Programming Languages", "Animals", "Countries", "Planets", "Fruits", and "Sports".
- **200+ Words:** The game includes a rich vocabulary of over 200 words across the selected fields, ensuring variety and replayability.
- **Dynamic Attempts:** The number of attempts you have to guess the word dynamically adapts based on the length of the chosen word and the difficulty level, providing a balanced difficulty level.
- **Difficulty Levels:** Choose from 3 difficulty levels - Easy, Medium, and Hard. The difficulty level affects the length of the chosen word and the number of attempts.
- **Visual Feedback:** Each wrong guess decrements your remaining attempts, offering visual feedback on your progress and increasing tension as the game progresses.
### Setting Up Your Journey
1. **Fuel Up (Prerequisites) ⛽:** Make sure you have Python 3 installed on your system. Download it from [Python website](https://www.python.org/downloads) if you haven't already.
2. **Download Ready? :**  Grab the project files by cloning or downloading them to your local machine.
3. **Launch Time! :** Open a terminal or command prompt, navigate to the project directory, and type python main.py to start the game.
### How to play
- **Field of Choice:** When the game begins, you'll be presented with 6 fields. Choose the one that sparks your guessing curiosity!
- **Difficulty Selection:** After choosing the field, you'll be asked to select a difficulty level. Choose the one that suits your confidence level!
- **Word Wizardry ✨:** Based on your selection, a secret word will be chosen from that field.
- **Hidden Treasures:** You'll see an empty display representing the hidden word, with underscores indicating the number of letters (_ _ _ _ _).
- **Guessing Game:** Get ready to put your detective skills to the test! You'll have a certain number of attempts (based on the word length and difficulty level) to guess individual letters and uncover the hidden word.
- **Right on Track! :** For each correct guess, the letter will be revealed in its corresponding positions, bringing you closer to the word.
- **Oops, Wrong Turn! :** Guessing incorrectly has consequences! Each wrong guess deducts an attempt, building suspense as you try to avoid the dreaded ending.
- **Victory or Defeat? :** The game continues until you either:
   - Guess the entire word correctly, earning a triumphant victory and earning bragging rights!
   - Run out of attempts, resulting in the hidden word being revealed and the hangman meeting his unfortunate fate.
## Example Gameplay
```
                                     Welcome to the Hangman game

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
What field do you want the selected word to be in?

1. Programming Languages
2. Countries
3. Animals
4. Fruits
5. Planets
6. Colors

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

>> Choose one of the options above: 3

Choose a difficulty level:
1. Easy
2. Medium
3. Hard

>> Choose one of the options above: 2
You have 6 attempts left.

_ _ _ _ _ _

Guess a letter: a
'a' doesn't appear in the word!!!
You have 5 attempts left.

_ _ _ _ _ _

Guess a letter: u
You have 6 attempts left.

_ u _ _ _ _

... (Continue guessing letters)

Congratulations! You guessed the word: turtle
You win!

Do you want to play again? (yes/no): no
```

#### If you encounter any difficulties or have brilliant ideas for improvements, feel free to contribute or raise issues on the project's repository.
