# python version, not test yet


import random
import os

# Define input and output file paths
input_file_path = r"path\to\your\file.txt"
output_file_path = r"path\to\output\file.txt"

# Read text from input file
with open(input_file_path, "r") as f:
    text = f.read()

# Remove whitespace and split text into characters
text = text.replace("\n", "")
characters = list(text)

# Randomly reorder characters
random.shuffle(characters)

# Join reordered characters into a string
reordered_text = "".join(characters)

# Write reordered text to output file
with open(output_file_path, "w") as f:
    f.write(reordered_text)

# Print the width
print("Width:", len(reordered_text.split("\n")))
