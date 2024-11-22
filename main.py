# Programmer Name: Oreoluwa Adebusoye
# Course:  CS151, Dr. Zelalem Jembre Yalew
# Due Date: 11/21/2024
# Program Name:
# What program does (purpose):

import os

# Purpose: Read headlines from a file and store them in a list.
# Parameters: file_name (str) - The name of the file to read.
# Return: headlines (list of strings) - The list of headlines from the file.
def read_file():
    # Prompt user for the filename to read
    file_name = input("What file do you want to read? ").strip()

    # Check if the file exists, and if not, ask again until a valid file is entered
    while not os.path.isfile(file_name):
        print("That file does not exist. Please try again.")
        file_name = input("\nWhat file do you want to read? ")

    # Initialize an empty list to store the headlines table
    headlines = []

    try:
        # Open the file for reading
        with open(file_name, "r") as file:
            for line in file:
                # Append the headlines to the table
                headlines.append(line.strip())
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' could not be found.")

    return headlines

# Purpose: Count how many headlines contain a given word.
# Name: count_headlines_with_word
# Parameters: List of headlines, Word
# Return: count (int) – Number of matching headlines.
def count_headlines_with_word(headlines):
    count = 0
    word = input("Enter the word you want to count:")
    for headline in headlines:
        if word.lower() in headline.lower():  # Case-insensitive check
            count += 1
    print(f"The word '{word}' appears in {count} headlines.")
    return count

# Purpose: Write all headlines containing a specific word to a new file.
# Name: write_matching_headlines
# Parameters: headlines, word, output_file
# Return: None
def write_matching_headlines(headlines, output_file):
    matching_word = input("Enter the word you want to match: ").strip().lower()
    output_file = input("Enter the name of the file to write the headlines to: ").strip()
    with open(output_file, 'w') as file:  # Open the file for writing
        for headline in headlines:
            if matching_word.lower() in headline.lower():  # Case-insensitive check
                file.write(headline + '\n')  # Write matching headline to file
    print(f"Headlines containing '{matching_word}' have been written to '{output_file}'.")

# Purpose: Calculate the average number of characters in the headlines.
# Name: average_characters
# Parameters: headlines
# Return: average (float)
def average_characters(headlines):
    if headlines:  # Check if the list is not empty
        total_characters = 0
        for headline in headlines:
            total_characters += len(headline)  # Add the length of each headline to the total
        average = total_characters / len(headlines)  # Calculate the average
    else:
        average = 0  # If no headlines, set average to 0
    print(f"The average number of characters per headline is: {average_characters:.2f}\n")

# Purpose: Find and return the longest headlines by character count.
# Name: find_longest_headline
# Parameters: headlines
# Return: longest headline
# Find the longest headline
def find_longest_headline(headlines):
    shortest_headline = headlines[0]  # Start with the first headline
    for headline in headlines:
        if len(headline) > len(longest_headline):  # Compare lengths
            longest_headline = headline
    return shortest_headline

# Purpose: Find and return the shortest headlines by character count.
# Name: find_shortest_headline
# Parameters: headlines
# Return: shortest headline
def find_shortest_headline(headlines):
    shortest_headline = headlines[0]  # Start with the first headline
    for headline in headlines:
        if len(headline) < len(shortest_headline):  # Compare lengths
         shortest_headline = headline
    return shortest_headline

def load_new_file():
    # Prompt user for the filename to read
    file_name = input("Enter the name of the new file to load: ").strip()

    # Check if the file exists, and if not, ask again until a valid file is entered
    while not os.path.isfile(file_name):
        print("That file does not exist. Please try again.")
        file_name = input("\nWhat file do you want to read? ")

        # Initialize an empty list to store the headlines table
        headlines = []

        try:
            # Open the file for reading
            with open(file_name, "r") as file:
                for line in file:
                    line = line.strip()
                    # Append the headlines to the table
                    headlines.append(line)
        except FileNotFoundError:
            print(f"Error: The file '{file_name}' could not be found.")

        return headlines
# Purpose: Control the program flow.
# Name: main
# Parameters: None
# Return: None
def main():
    headlines = []
    # Main loop to allow user to choose again
    choose_again = 'y'
    while choose_again == 'y':
        # Display Menu
        print("\nMenu:")
        print("1. Count headlines containing a specific word")
        print("2. Write headlines containing a specific word to a new file")
        print("3. Calculate the average number of characters per headline")
        print("4. Output the longest and shortest headline")
        print("5. Load a new file to analyze")
        print("6. Quit")

        # Get user input and validate
        choice = input("Enter your choice (1-6): ").strip()
        options = [1, 2, 3, 4, 5, 6]

        # Loop until the user enters a valid choice
        while not choice.isdigit() or int(choice) not in options:
            print("Invalid choice. Please enter a number between 1 and 6.\n")
            choice = input("Please enter your choice (1-6): ").strip()

        # Convert the valid choice to an integer
        choice = int(choice)

        # Handle user choice
        if choice == 1:
            count_headlines_with_word(headlines)  # Function to count headlines with a specific word
        elif choice == 2:
            write_matching_headlines(headlines)  # Function to write matching headlines to a file
        elif choice == 3:
            average_characters(headlines)  # Function to calculate average number of characters in headlines
        elif choice == 4:
            # Find and display the shortest and longest headlines
            shortest = find_shortest_headline(headlines)
            longest = find_longest_headline(headlines)
            print(f"Shortest headline: {shortest}")
            print(f"Longest headline: {longest}")
        elif choice == 5:
            # Load a new file and overwrite the current headlines
            headlines = load_new_file()
        elif choice == 6:
            print("Thank you for using the Headline Analyzer! Goodbye!")
            break

        # Ask if the user wants to choose again
        choose_again = input("\nDo you want to choose again? (y/n): ").lower().strip()

        # Validate the user's decision to continue or exit
        while choose_again not in ['y', 'n']:
            print("Please enter 'y' for yes or 'n' for no.")
            choose_again = input("\nDo you want to choose again? (y/n): ").lower().strip()

    print("\nGoodbye! Thanks for using the program.")

# Run the main function
main()