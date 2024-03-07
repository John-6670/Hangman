import random, shutil, math


# Function to choose a difficulty level
def choose_difficulty():
    """
    Prompts the user to choose a difficulty level and returns a multiplier
    to calculate the number of attempts allowed for the chosen difficulty.

    Returns:
        float: The multiplier for calculating the number of attempts.

    Raises:
        ValueError: If the user enters an invalid input.
    """
    print("\nChoose a difficulty level:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")

    while True:
        try:
            difficulty = int(input('\n>> Choose one of the options above: '))
            if difficulty == 1:
                return 2  # Return 2 as multiplier to calculate attempts for easy level
            elif difficulty == 2:
                return 1  # Return 1 as multiplier to calculate attempts for medium level
            elif difficulty == 3:
                return 0.5  # Return 0.5 as multiplier to calculate attempts for hard level
            else:
                print('Invalid input!!!')
        except ValueError:
            print('Invalid input!!!')
            
# Function to choose a word from a specific field
def choose_word(field: str) -> list:
    """
    Selects a random word from the given field and calculates the number of attempts.

    Args:
        field (str): The field from which to choose the word.

    Returns:
        list: A list containing the chosen word (str) and the number of attempts (int).
    """
    words = fields[field]
    easy_words = [word for word in words if len(word) <= 5]
    medium_words = [word for word in words if 6 <= len(word) <= 8]
    hard_words = [word for word in words if len(word) > 8]

    difficulty = choose_difficulty()
    if difficulty == 2:
        word = random.choice(easy_words)
    elif difficulty == 1:
        word = random.choice(medium_words if medium_words else easy_words)
    else:
        word = random.choice(hard_words if hard_words else (medium_words if medium_words else easy_words))

    return [word.lower(), math.ceil(len(word) * difficulty)]  # Return the chosen word and the number of attempts

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
    # List of programming languages
    'Programming Languages': ['Python', 'Java',  'JavaScript', 'Ruby', 'Swift', 'Kotlin', 'TypeScript', 'Matlab', 'React', 'Assembly',
                              'Rust', 'HTML', 'CSS', 'SQL', 'Racket', 'php', 'go', 'scala', 'perl', 'dart', 'lua', 'shell', 'typescript'],
    
    # List of countries
    'Countries': ['Afghanistan', 'Anguilla', 'Argentina', 'Australia', 'Azerbaijan', 'Brazil', 'Canada', 'Switzerland', 'China',
                  'Congo', 'Colombia', 'Cuba', 'Czechia', 'Germany', 'Denmark', 'Egypt', 'Spain', 'Finland', 'France', 'England',
                  'Greece', 'Greenland', 'HongKong', 'Honduras', 'Hungary', 'Indonesia', 'India', 'Ireland', 'Iran', 'Iraq', 'Iceland',
                  'Israel', 'Italy', 'Jordan', 'Japan', 'Kazakhstan', 'Kenya', 'South Korea', 'North Korea', 'Luxembourg', 'Latvia',
                  'Madagascar', 'Mexico', 'Mongolia', 'Netherlands', 'Norway', 'Nepal', 'Oman', 'Pakistan', 'Philippines', 'Poland',
                  'Portugal', 'Palestine', 'Qatar', 'Romania', 'Russia', 'Sudan', 'Senegal', 'Singapore', 'Serbia', 'Sweden',
                  'Thailand', 'Tajikistan', 'Turkey', 'Taiwan', 'Ukraine', 'America', 'Uzbekistan', 'Venezuela', 'Vietnam', 'Yemen'],  
    
    # List of animals
    'Animals': ["Ant", "Donkey", "Bat", "Bear", "Bee", "Buffalo", "Butterfly", "Camel", "Cat", "Cheetah", "Chicken", "Chimpanzee",
                "Cobra", "Crab", "Crocodile", "Dog", "Dolphin", "Duck", "Eagle", "Elephant", "Fish", "Flamingo", "Fly", "Fox", "Frog",
                "Giraffe", "Goat", "Gorilla", "Hamster", "Horse", "Jaguar", "Jellyfish", "Kangaroo", "Lion", "Llama", "Monkey",
                "Mosquito", "Mouse", "Octopus", "Ostrich", "Owl", "Panther", "Parrot", "Penguin", "Pig", "Pigeon", "Rabbit", "Raccoon",
                "Rat", "Seahorse", "Seal", "Shark", "Sheep", "Snail", "Snake", "Spider", "Tiger", "Turkey", "Turtle", "Whale", "Wolf",
                "Worm", "Zebra", "Starfish", "Toucan", "Panda", "Koala", "Gorilla", "Giraffe"], 
    
    # List of fruits
    'Fruits': ['Apple', 'Banana', 'Cherry', 'Date', 'Grape', 'Jackfruit', 'Kiwi', 'Lemon', 'Mango', 'Orange', 'Quince', 'Raspberry',
               'Strawberry', 'Tomato', 'Vanilla', 'Watermelon', 'Zucchini', 'Peach', 'Pineapple', 'Plum', 'Pear'],
    
    # List of planets
    'Planets': ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune'],
    
    # List of colors
    'Colors': ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet', 'Black', 'White', 'Gray', 'Pink', 'Brown', 'Cyan',
               'Magenta', 'Olive']
}

# Create a dictionary for easier menu option selection
fields_dic = {}
for i, field in enumerate(fields):
    fields_dic[i+1] = field

# Main game loop
while True:
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
        
    # After the game ends, ask the player if they want to continue
    play_again = input("\nDo you want to play again? (yes/no): ")

    # If the player doesn't want to continue, break the loop
    if play_again.lower() != "yes":
        break
