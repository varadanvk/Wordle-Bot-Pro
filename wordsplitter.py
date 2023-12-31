# Open the input text file
with open('answers.txt', 'r') as input_file:
    # Read lines from the input file
    lines = input_file.readlines()

# Create a list to store the extracted words
words = []

# Iterate through the lines and extract words
for line in lines:
    # Split each line into words using whitespace as a separator
    line_words = line.strip().split()
    
    # Add each word to the list
    words.extend(line_words)

# Create a text file to store the extracted words
with open('extracted_words.txt', 'w') as output_file:
    # Write each word to the output file
    for word in words:
        output_file.write(word + '\n')

# Open the input file for reading
with open('extracted_words.txt', 'r') as infile:
    # Read the lines from the input file
    lines = infile.readlines()

# Create a list to store the capitalized words
capitalized_words = []

# Iterate through the lines
for line in lines:
    # Split each line into words based on spaces
    words = line.strip().split()
    # Check if each word is capitalized and add it to the list
    for word in words:
        if word.isupper():
            capitalized_words.append(word)

# Create a new text file to store the capitalized words
with open('capitalized_words.txt', 'w') as outfile:
    # Write each capitalized word to the new file
    for word in capitalized_words:
        outfile.write(word + '\n')

