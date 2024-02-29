import random
import shutil


def choose_word(field: str):
    word = random.choice(fields[field]).lower()
    chances = len(word)
    
    return [word, chances]


def show_menu():
    width, height = shutil.get_terminal_size()
    print("Welcome to the Hangman game".center(width))

    print('\n' + '-' * width)
    print('What field do you want the selected word to be in?\n')

    for i, field in fields_dic.items():
        print(f'{i}. {field}')
        

    print('\n' + '-' * width)


fields = {
    'Programming Languages': ['Python', 'Java', 'JavaScript', 'Ruby', 'Swift', 'Kotlin', 'TypeScript', 'Matlab', 'React', 'Assembly', 'Rust',
                              'HTML', 'CSS', 'SQL', 'Racket', 'php', 'go', 'scala'],
    
    'Countries': ['Afghanistan', 'Anguilla', 'Argentina', 'Australia', 'Azerbaijan', 'Brazil', 'Canada', 'Switzerland', 'China', 'Congo',
                  'Colombia', 'Cuba', 'Czechia', 'Germany', 'Denmark', 'Egypt', 'Spain', 'Finland', 'France', 'England', 'Greece', 'Greenland',
                  'HongKong', 'Honduras', 'Hungary', 'Indonesia', 'India', 'Ireland', 'Iran', 'Iraq', 'Iceland', 'Israel', 'Italy', 'Jordan',
                  'Japan', 'Kazakhstan', 'Kenya', 'South Korea', 'North Korea', 'Luxembourg', 'Latvia', 'Madagascar', 'Mexico', 'Mongolia',
                  'Netherlands', 'Norway', 'Nepal', 'Oman', 'Pakistan', 'Philippines', 'Poland', 'Portugal', 'Palestine', 'Qatar', 'Romania',
                  'Russia', 'Sudan', 'Senegal', 'Singapore', 'Serbia', 'Sweden', 'Thailand', 'Tajikistan', 'Turkey', 'Taiwan', 'Ukraine',
                  'America', 'Uzbekistan', 'Venezuela', 'Vietnam', 'Yemen'],
    
    'Animals': ["Ant", "Donkey", "Bat", "Bear", "Bee", "Buffalo", "Butterfly", "Camel", "Cat", "Cheetah", "Chicken", "Chimpanzee", "Cobra",
                "Crab", "Crocodile", "Dog", "Dolphin", "Duck", "Eagle", "Elephant", "Fish", "Flamingo", "Fly", "Fox", "Frog", "Giraffe",
                "Goat", "Gorilla", "Hamster", "Horse", "Jaguar", "Jellyfish", "Kangaroo", "Lion", "Llama", "Monkey", "Mosquito", "Mouse",
                "Octopus", "Ostrich", "Owl", "Panther", "Parrot", "Penguin", "Pig", "Pigeon", "Rabbit", "Raccoon", "Rat", "Seahorse", "Seal",
                "Shark", "Sheep", "Snail", "Snake", "Spider", "Tiger", "Turkey", "Turtle", "Whale", "Wolf", "Worm", "Zebra"],
}

fields_dic = {}
for i, field in enumerate(fields):
    fields_dic[i+1] = field

show_menu()

while True:
    choice = int(input('\n>> Choose one of the options above: '))

    try:
        chosen_word, attempts = choose_word(fields_dic[choice])
        break
    except KeyError:
        print('Invalid input!!!')

word_display = ['_' for char in chosen_word]
    
while attempts > 0 and '_' in word_display:
    print(f'You have {attempts} attempts left.')
    print('\n' + ' '.join(word_display))
        
    guess = input('\nGuess a letter: ').lower()
    if guess in chosen_word:
        for index, letter in enumerate(chosen_word):
            if letter == guess:
                word_display[index] = guess
    else:
        print(f"'{guess}' doesn't appear in the word!!!")
        attempts -= 1
        
if '_' not in word_display:
    print(f'\nCongratulations! You guessed the word: {chosen_word}')
    print('You win!')
else:
    print(f'\nYou ran out of attempts. the word was: {chosen_word}')
    print('You lost :(')