print("=== Favour Ohejuwa Odeh's Word & Character Counter ===")

# Prompt the user for input text
text = input("Type something: ")

# Split the text by whitespace into a list of words
words = text.split()

# Display the results
print("Word count:", len(words))
print("Character count:", len(text))