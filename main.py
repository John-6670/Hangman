import random
import shutil

# Function to choose a word from a specific field
def choose_word(field: str) -> list:
    """
    Selects a random word from the given field and calculates the number of attempts.

    Args:
        field (str): The field from which to choose the word.

    Returns:
        list: A list containing the chosen word (str) and the number of attempts (int).
    """
    word = random.choice(fields[field]).lower()
    chances = len(word)
    return [word, chances]

# Function to display the game menu
def show_menu():
    """
    Displays a visually appealing menu with game options.
    """
    width, height = shutil.get_terminal_size()  # Get terminal dimensions for formatting
    print("Welcome to the Hangman game".center(width))  # Center the title

    print('\n' + '-' * width)
    print('What field do you want the selected word to be in?\n')

    for i, field in fields_dic.items():
        print(f'{i}. {field}')  # List each field with an index

    print('\n' + '-' * width)

# Define available fields and words
fields = {
    'Programming Languages': ['Python', 'Java',  'JavaScript', 'Ruby', 'Swift', 'Kotlin', 'TypeScript', 'Matlab', 'React', 'Assembly', 'Rust', 'HTML', 'CSS', 'SQL',
                              'Racket', 'php', 'go', 'scala'],  # List of programming languages
    
    'Countries': ['Afghanistan', 'Anguilla', 'Argentina', 'Australia', 'Azerbaijan', 'Brazil', 'Canada', 'Switzerland', 'China', 'Congo', 'Colombia', 'Cuba', 'Czechia',
                  'Germany', 'Denmark', 'Egypt', 'Spain', 'Finland', 'France', 'England', 'Greece', 'Greenland', 'HongKong', 'Honduras', 'Hungary', 'Indonesia', 'India',
                  'Ireland', 'Iran', 'Iraq', 'Iceland', 'Israel', 'Italy', 'Jordan', 'Japan', 'Kazakhstan', 'Kenya', 'South Korea', 'North Korea', 'Luxembourg', 'Latvia',
                  'Madagascar', 'Mexico', 'Mongolia', 'Netherlands', 'Norway', 'Nepal', 'Oman', 'Pakistan', 'Philippines', 'Poland', 'Portugal', 'Palestine', 'Qatar',
                  'Romania', 'Russia', 'Sudan', 'Senegal', 'Singapore', 'Serbia', 'Sweden', 'Thailand', 'Tajikistan', 'Turkey', 'Taiwan', 'Ukraine', 'America',
                  'Uzbekistan', 'Venezuela', 'Vietnam', 'Yemen'],  # List of countries
    
    'Animals': ["Ant", "Donkey", "Bat", "Bear", "Bee", "Buffalo", "Butterfly", "Camel", "Cat", "Cheetah", "Chicken", "Chimpanzee", "Cobra", "Crab", "Crocodile", "Dog",
                "Dolphin", "Duck", "Eagle", "Elephant", "Fish", "Flamingo", "Fly", "Fox", "Frog", "Giraffe", "Goat", "Gorilla", "Hamster", "Horse", "Jaguar", "Jellyfish",
                "Kangaroo", "Lion", "Llama", "Monkey", "Mosquito", "Mouse", "Octopus", "Ostrich", "Owl", "Panther", "Parrot", "Penguin", "Pig", "Pigeon", "Rabbit",
                "Raccoon", "Rat", "Seahorse", "Seal", "Shark", "Sheep", "Snail", "Snake", "Spider", "Tiger", "Turkey", "Turtle", "Whale", "Wolf", "Worm", "Zebra"],  # List of animals
}

# Create a dictionary for easier menu option selection
fields_dic = {}
for i, field in enumerate(fields):
    fields_dic[i+1] = field

# Main game loop
show_menu()  # Display the menu

while True:
    try:
        choice = int(input('\n>> Choose one of the options above: '))
        chosen_word, attempts = choose_word(fields_dic[choice])  # Get a word from the chosen field
        break  # Exit the loop if a valid choice is made
    except KeyError:
        print('Invalid input!!!')  # Handle invalid choices

# Initialize the word display with underscores
word_display = ['_' for char in chosen_word]

# Main game logic
while attempts > 0 and '_' in word_display:
    print(f'You have {attempts} attempts left.')
    print('\n' + ' '.join(word_display))  # Show the current progress

    guess = input('\nGuess a letter: ').lower()
    if guess in chosen_word:
        for index, letter in enumerate(chosen_word):
            if letter == guess:
                word_display[index] = guess  # Reveal the guessed letter
    else:
        attempts -= 1  # Decrease attempts for incorrect guesses
        print(f"'{guess}' doesn't appear in the word!!!")

# Game outcome
if '_' not in word_display:
    print(f'\nCongratulations! You guessed the word: {chosen_word}')
    print('You win!')
else:
    print(f'\nYou ran out of attempts. The word was: {chosen_word}')
    print('You lost :(')
