# rand text

This project reads a text file, randomly permutes the characters, and arranges 
them into lines of equal width.  
**Note:** This functionality may only be beneficial for Asian characters.  
**Note:** The code is only tested with Chinese characters.

[中文](#rand-text-隨機重排字元)

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



## rand text 隨機重排字元

這個項目讀取一個文字檔案，隨機重排字符，並將它們排列成等寬的行。
**注意：**這個程式可能只對亞洲字符有用。
**注意：**這個程式只對中文文件進行過測試。

## 特點

- **隨機化**：讀取一個輸入文件，移除所有空白字元，然後隨機重排字元。
- **輸出格式**：重排的文字依指定寬度分為數行（默認寬度是字數的平方根）。
- **靈活性**：您可以指定輸入和輸出文件，以及輸出行的寬度。

## 使用方法

1. 以管理員身份打開PowerShell。
2. 移至包含`rand_text.ps1`的目錄。
3. 使用所需的參數運行腳本：

```powershell 
.\rand_text.ps1 -InputFile "path\to\your\file.txt" -OutputFile "path\to\output\file.txt" -Width 7
```

- `-InputFile`：您想要隨機重排的文件的路徑。
- `-OutputFile`：重排後的文字將保存的路徑。
- `-Width`：（可選）重排時每行的寬度。默認是字數的平方根。

## 注意

如果您遇到關於在您的系統上禁用運行腳本的錯誤，您可以通過在
PowerShell中以**管理員**身份運行以下命令來更改執行策略：

```powershell
Set-ExecutionPolicy RemoteSigned
```
