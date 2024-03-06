# rand text

This project reads a text file, randomly permutes the characters, and arranges 
them into lines of equal width.  
**Note:** This functionality may only be beneficial for Asian characters.  
**Note:** The code is only tested with Chinese characters.

## Features

- **Randomization**: The script reads an input file, removes all whitespace, and 
  then randomly shuffles the characters.
- **Output Formatting**: The shuffled text is then formatted into lines of a 
  specified width (default is the square root of the text length).
- **Flexibility**: You can specify the input and output files, as well as the 
  width of the output lines.

## Usage

1. Open PowerShell as Administrator.
2. Navigate to the directory containing `rand_text.ps1`.
3. Run the script with the required parameters:

```powershell 
.\rand_text.ps1 -InputFile "path\to\your\file.txt" -OutputFile "path\to\output\file.txt" -Width 7
```

- `-InputFile`: The path to the text file you want to randomize.
- `-OutputFile`: The path where the randomized text will be saved.
- `-Width`: (Optional) The width of the output lines. Default is the square root 
  of the text length.

## Note

If you encounter an error about running scripts being disabled on your system, 
you can change the execution policy by running the following command in 
PowerShell as **Administrator**:

```powershell
Set-ExecutionPolicy RemoteSigned
```
