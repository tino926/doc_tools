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

    translated_lines = [translate_line(line.strip(), translator) for line in lines]

    # Create the output filename by adding '_tr' to the original filename
    output_file_path = os.path.splitext(file_path)[0] + '_tr' + os.path.splitext(file_path)[1]

    with open(output_file_path, 'w', encoding='utf-8') as file:
        for line in translated_lines:
            file.write(line + '\n')

if __name__ == "__main__":
    if len(sys.argv) !=  2:
        print("Usage: python script.py <file_path>")
        file_path="output.txt"
        # sys.exit(1)
    else:
        file_path = sys.argv[1]
    translate_file(file_path)
