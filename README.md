# Hangman game
This Python-powered Hangman game is here to challenge you and test your word-guessing skills
### Features:
- **Field Selection:** Choose from 3 different fields (categories) for the secret word, making the game more diverse and challenging.
- **150+ Words:** The game includes a rich vocabulary of over 150 words across the selected fields, ensuring variety and replayability.
- **Dynamic Attempts:** The number of attempts you have to guess the word dynamically adapts based on the length of the chosen word, providing a balanced difficulty level.
- **Visual Feedback:** Each wrong guess decrements your remaining attempts, offering visual feedback on your progress and increasing tension as the game progresses.
### Setting Up Your Journe
1. **Fuel Up (Prerequisites) ⛽:** Make sure you have Python 3 installed on your system. Download it from [Python website](https://www.python.org/downloads) if you haven't already.
2. **Download Ready? :**  Grab the project files by cloning or downloading them to your local machine.
3. **Launch Time! :** Open a terminal or command prompt, navigate to the project directory, and type python main.py to start the game.
### How to play
- **Field of Choice:** When the game begins, you'll be presented with 3 fields "Programming Languages", "Animals" and "Countries". Choose the one that sparks your guessing curiosity!
- **Word Wizardry ✨:** Based on your selection, a secret word will be chosen from that field.
- **Hidden Treasures:** You'll see an empty display representing the hidden word, with underscores indicating the number of letters (_ _ _ _ _).
- **Guessing Game:** Get ready to put your detective skills to the test! You'll have a certain number of attempts (based on the word length) to guess individual letters and uncover the hidden word.
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

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

>> Choose one of the options above: 3
You have 7 attempts left.

_ _ _ _ _ _ _

Guess a letter: a
'a' doesn't appear in the word!!!
You have 6 attempts left.

_ _ _ _ _ _ _

Guess a letter: c
You have 6 attempts left.

_ c _ _ _ _ _

... (Continue guessing letters)

Congratulations! You guessed the word: octopus
You win!
```
### Some Under Construction Features (Coming Soon!):
- **More Fields, More Fun! :** I'm constantly adding more unique fields and expanding the word database for an even wider range of gameplay experiences. Stay tuned!
- **Difficulty Levels Up! :** I'm committed to adding difficulty levels by adjusting the initial number of attempts or introducing time limits, catering to players of all skill levels. Coming soon!
- **Sounds and Ambience:** I'm exploring the possibility of adding sound effects (wrong guess sounds, victory music) or background music to create a more immersive and engaging atmosphere. Stay tuned!
- **Graphical Interface ✨:** A user-friendly graphical interface (GUI) using libraries like Tkinter or Pygame is on the roadmap to provide a visually appealing experience. Coming soon!

#### If you encounter any difficulties or have brilliant ideas for improvements, feel free to contribute or raise issues on the project's repository.
