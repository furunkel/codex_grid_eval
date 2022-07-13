
def joined_sequence(text):
    """
    Write a function to that returns True if the input string contains sequences of lowercase letters joined with a question mark and False otherwise.
    """
    
    sequence = False
    
    for letter in text:
        if letter.islower():
            sequence = True
            break
    
    return sequence
</cell>
<cell>
# Test your code
joined_sequence("AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz")
</cell>
<text>
Expected Output:



</text>
<text>
1.4. Write a function that takes as input a string and returns the number of lower case letters in that string.


</text>
<cell>
def count_letters(text):
    """
    Write a function that takes as input a string and returns the number of lower case letters in that string.
    
    Example string: count_letters("Hello World")
    
    Number of lower case letters: 5
    """
    
    count = 0
    
    for letter in text:
        if letter.islower():
            count += 1
            
    return count
</cell>
<cell>
# Test your code
count_letters("Hello World")
</cell>
<text>
Expected Output:



</text>
<text>
1.5. Write a function that takes as input a year and returns the number of days elapsed since that year (2020).


</text>
<cell>
def count_days(year):
    """
    Write a function that takes as input a year and returns the number of days elapsed since that year (2020).
    
    Number of days: 365
    """
    
    days = 0
    
    if year > 2020:
        days = 365
    else:
        days = 366
    
    return days
</cell>
<cell>
# Test your code
count_days(2020)
</cell>
<text>
Expected Output:



</text>
<text>
2. Write a Python program to read words from a text file and sort them in alphabetical order.

The program should continue reading words until it reaches the end of the file. After all the words have been read, your program should print the contents of the sorted word file.


</text>
<cell>
# Initialize dictionary
words = {}

# Open the text file and read it line by line
with open("words.txt") as file:
    for line in file:
        
        # Split the line into words
        words = line.split()
        
        # Add the words to the dictionary
        for word in words:
            words[word] = words.get(word, 0) + 1
            
# Sort the dictionary by value
sorted_words = sorted(words.items(), key=lambda x:x[1], reverse