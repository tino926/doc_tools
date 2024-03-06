import sys
import re
import os
import configparser


# Check if the ./pri/ subfolder exists
if os.path.exists('./pri/'):
    # Read the setting.ini file
    config = configparser.ConfigParser()
    config.read('./pri/setting.ini')
    input_file_path = config.get('Settings', 'input_file_path')
    output_file_path = config.get('Settings', 'output_file_path')
    easy_file_path = './pri/easy.txt'
else:
    # Default paths if the subfolder does not exist
    input_file_path = 'input.txt'
    output_file_path = 'output.txt'
    easy_file_path = 'easy.txt'


def remove_duplicates_from_file(input_file_path, output_file_path):
    # Step   1: Read the file
    with open(input_file_path, 'r') as file:
        text = file.read()

    # Step   2: Split the text into words
    words = text.split()

    with open(easy_file_path, 'r') as file:
        text = file.read()
        easy_words = text.split()
        easy_words = [re.sub(r"[^\w']+", '', word).lower()
                      for word in easy_words]

    # Step   3: Remove duplicates while preserving order
    seen_lower = {}
    for w in easy_words:
        seen_lower[w] = True

    unique_words = []
    for word in words:
        clean_word = re.sub(r"[^\w']+", '', word)
        if clean_word.lower() not in seen_lower:
            seen_lower[clean_word.lower()] = True
            unique_words.append(clean_word)

    # Step   4: Write the result back to a file
    with open(output_file_path, 'w') as file:
        for word in unique_words:
            file.write(word + '\n')


remove_duplicates_from_file(input_file_path, output_file_path)
