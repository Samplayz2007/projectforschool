import os
import random
import time
import pickle

# Set up the lists of names, places, and animals to use in the game
names = ['Alice', 'Bob', 'Charlie', 'Dave', 'Emily', 'Frank']
places = ['Antarctica', 'Brazil', 'China', 'Denmark', 'Egypt', 'France']
animals = ['Aardvark', 'Bear', 'Cat', 'Dolphin', 'Elephant', 'Flamingo']

# Set the number of rounds to play and initialize the score and leaderboard
num_rounds = int(input('Enter the number of rounds:'))
score = 0
bonus_points = 0
leaderboard = []

# Load saved data if it exists
try:
    with open('save.dat', 'rb') as f:
        save_data = pickle.load(f)
        score = save_data['score']
        bonus_points = save_data['bonus_points']
        leaderboard = save_data['leaderboard']
        print('Save data loaded successfully!')
except FileNotFoundError:
    print('No save data found. Starting a new game...')

# Loop over the specified number of rounds
for i in range(num_rounds):
    # Generate a list of words with the same starting letter
    letter = random.choice('abcdef')
    word_list = [w for w in names + places + animals if w[0].lower() == letter]

    # If there are no words that start with the chosen letter, skip this round
    if not word_list:
        print(f'Sorry, there are no names, places, or animals that start with the generated letter: {letter} skipping this round. ')
        continue

    # Choose a random word from the list
    word = random.choice(word_list)

    # Shuffle the letters of the word (except the first and last letter)
    shuffled_word = word[0] + ''.join(random.sample(word[1:-1], len(word)-2)) + word[-1]

    # Print the shuffled word and ask the user to unscramble it
    print(f'Round {i+1}: Unscramble the word: {shuffled_word}')

    # Start the timer
    start_time = time.time()

    # Allow the player to guess and provide hints if needed
while True:
    guess = input('Your guess: ')

    if guess.lower() == word.lower():
        # Stop the timer and calculate the score for this round
        end_time = time.time()
        elapsed_time = end_time - start_time
        round_score = 10 - int(elapsed_time)
        if round_score < 1:
            round_score = 1

        # Apply the bonus points and add the score to the total
        round_score += bonus_points
        score += round_score

        # Print the score for this round
        print(f'Correct! You earned {round_score} points for this round.')

        # Add the score to the leaderboard
        leaderboard.append((score, round_score))
        leaderboard.sort(reverse=True)
        leaderboard = leaderboard[:5]

        # Reset the bonus points for the next round
        bonus_points = 0
        break
    elif len(guess) == 1 and guess.lower() == word[0].lower():
        # Give the player a hint if they guess the first letter
        print(f"The first letter of the word is '{word[0]}'.")
        
    elif len(guess) == len(word):
        # The player guessed the entire word
        if guess.lower() == word:
            # The guess is correct
            elapsed_time = time.time() - start_time
            round_score = max(0, 10 - int(elapsed_time))
            if bonus_points >= 5:
                round_score += 5
                bonus_points -= 5
                print('You used 5 bonus points for a hint.')
            score += round_score
            print(f'Correct! The word is {word}. You earned {round_score} points in this round.')
            break
        else:
            # The guess is incorrect
            print('Incorrect guess. Try again.')
            
# Give the player the option to use bonus points for a hint
if bonus_points >= 5:
    use_hint = input('Would you like to use 5 bonus points for a hint? (y/n)')
    if use_hint.lower() == 'y':
        bonus_points -= 5
        hint = word_list[random.randint(0, len(word_list)-1)]
        print(f'Here is your hint: {hint}')
    else:
        print('Hint not used.')

# Give the player the option to save their progress
save_progress = input('Would you like to save your progress? (y/n)')
if save_progress.lower() == 'y':
    save_data = {'score': score, 'bonus_points': bonus_points, 'leaderboard': leaderboard}
    with open('save.dat', 'wb') as f:
        pickle.dump(save_data, f)
    print('Progress saved successfully!')
# Print the final score and leaderboard
print(f'Your final score is {score}')
print('Leaderboard:')
for i, (score, round_score) in enumerate(leaderboard):
    print(f'{i+1}. Score: {score}, Round score: {round_score}')

# Save the score, bonus points, and leaderboard to a file
save_data = {'score': score, 'bonus_points': bonus_points, 'leaderboard': leaderboard}
with open('save.dat', 'wb') as f:
    pickle.dump(save_data, f)
    print('Game data saved!')