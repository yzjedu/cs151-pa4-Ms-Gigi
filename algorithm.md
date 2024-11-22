# Algorithm Document

Tasks:
1. Read File into a List
2. Count Headlines Containing a Specific Word
3. Write Matching Headlines to a File
4. Calculate Average Characters Per Headline
5. Find Longest Headlines
6. Find Shortest Headlines
7. Allow the user to load a new file, replacing the current one.
8. Main Function


1. Read File into a List
Purpose: Read headlines from a file and store them in a list.
Name: read_file
Parameters: file_name (str)
Return: headlines (list of strings)
Algorithm:
   1. Set table as an empty string
   2. Open the file specified by file_name for reading.
   3. Read each line of the file and strip any trailing whitespace.
   4. Append each line to a list called headlines.
   5. Error-check, output error if file is not found
   6. Return the headlines.

2. Count Headlines Containing a Specific Word
Purpose: Count how many headlines contain a given word.
Name: count_headlines_with_word
Parameters: List of headlines, Word
Return: count (int) – Number of matching headlines.
Algorithm:
   1. Initialize a count to 0. 
   2. Prompt user to enter the word they would like to search for
   3. For each headline in headlines:
      1. Check if the word exists in the headline. 
         1. If found, increment the counter.
   4. Return count and display

3. Write Matching Headlines to a File
Purpose: Write all headlines containing a specific word to a new file.
Name: write_matching_headlines
Parameters: headlines, word, output_file
Return: None
Algorithm:
   1. Prompt user to enter the word they would like to use 
   2. Open the output_file for writing.
   3. For each headline in headlines:
      1. If the word in the headline, write it to the file.
   
4. Calculate Average Characters Per Headline
Purpose: Calculate the average number of characters in the headlines.
Name: average_characters
Parameters: headlines 
Return: average (float) 
Algorithm:
   1. Initialize a variable total_characters to 0. 
   2. For each row in headlines:
      1. Add the length of the headline to total_characters. 
      2. Calculate the average as total_characters / number_of_headlines.
   3. Return the average.

5. Find Longest Headline
Purpose: Find and return the longest headlines by character count.
Name: find_longest_headline
Parameters: headlines 
Return: longest headline
Algorithm:
   1. Set longest to the first headline 
   2. For each headline in headlines:
      1. If the length of the headline is greater than longest, update longest.
   3. Return the longest
   
6. Find Shortest Headline
Purpose: Find and return the shortest headlines by character count.
Name: find_shortest_headline
Parameters: headlines 
Return: shortest headline
Algorithm:
   1. Set shortest to the first headline 
   2. For each headline in headlines:
      1. If the length of the headline is lesser than shortest, update shortest.
   3. Return the shortest

7. Allow the user to load a new file, replacing the current one.

7. Main Function
Purpose: Control the program flow.
Name: main
Parameters: None
Return: None
Algorithm:
   1. Display a welcome message and the program’s purpose. 
   2. Prompt the user for a file name and call read_file to load the headlines. 
   3. Display a menu with the following options:
      * Count headlines with a specific word.
      * Write matching headlines to a file.
      * Calculate the average number of characters.
      * Find and display the longest and shortest headlines.
      * Load a new file.
      * Quit the program.
   4. Based on the user’s choice, call the appropriate function.
   5. Error-check 
   6. Repeat the menu until the user chooses to quit.
