import pyjokes
import random
import time

# Fun welcome message
print("🎉 Welcome to the Joke Generator! 🎉")
print("Ready to hear some funny jokes?\n")

# Get a list of jokes (language is English, category is neutral or any valid category)
list_of_jokes = pyjokes.get_jokes(language="en", category="neutral")

# Shuffle the jokes to keep it fresh
random.shuffle(list_of_jokes)

# Ask how many jokes the user wants to hear
num_jokes = int(input("How many jokes would you like to hear? (Enter a number): "))

print("\nAlright, here we go!\n")

# Display jokes with a pause between each for dramatic effect
for i in range(min(num_jokes, len(list_of_jokes))):
    print(f"Joke {i + 1}:")
    print(list_of_jokes[i], "\n")
    
    # Add a little delay for suspense
    time.sleep(2)
    
    # Fun comment after each joke
    if i < num_jokes - 1:
        print("😆 That was funny! Ready for the next?\n")
    else:
        print("😅 That's all the jokes! Hope you had a good laugh!\n")

# Ending message
print("Thanks for playing! 🎉 Come back soon for more laughs!")
