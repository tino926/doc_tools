# need to install googletrans==4.0.0-rc1
from googletrans import Translator
import sys
import os

def translate_line(line, translator):
    translation = translator.translate(line, dest='zh-tw')
    return f"{line} ({translation.text})"

def translate_file(file_path):
    translator = Translator()
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # translated_lines = [translate_line(line.strip(), translator) for line in lines]
    translated_lines = []
    total_lines = len(lines)
    for i, line in enumerate(lines, start=1):
        translated_line = translate_line(line.strip(), translator)
        translated_lines.append(translated_line)
        print(f"Translated {i} out of {total_lines} lines.", end='\r')

    # Create the output filename by adding '_tr' to the original filename
    output_file_path = os.path.splitext(file_path)[0] + '_tr' + os.path.splitext(file_path)[1]

    with open(output_file_path, 'w', encoding='utf-8') as file:
        for line in translated_lines:
            file.write(line + '\n')

if __name__ == "__main__":
    if len(sys.argv) !=  2:
        print("Usage: python script.py <file_path>")
        if os.path.exists('./pri/'):
            file_path="./pri/output.txt"
        else:
            sys.exit(1)
    else:
        file_path = sys.argv[1]
    translate_file(file_path)
