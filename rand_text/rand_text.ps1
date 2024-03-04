# usage example: .\rand_text.ps1 -InputFile "path\to\your\file.txt" -OutputFile "path\to\output\file.txt"
#
# Note: if you see this msg: rand_text.ps1 cannot be loaded because running scripts is disabled on this system.
#       you can change the execution policy as:
#     1. Open PowerShell as Administrator. 
#     2. Run the command: Run the following command
#        Set-ExecutionPolicy RemoteSigned

param(
    [Parameter(Mandatory=$true)]
    [string]$InputFile,

    [Parameter(Mandatory=$true)]
    [string]$OutputFile,

    [int]$Width=0
)

$text = Get-Content -Path $InputFile -Raw
$text = $text -replace '\s',''
$chars = $text.ToCharArray()
$random = New-Object System.Random
$chars = $chars | Sort-Object { $random.Next() }
$text = -join $chars

if ($Width -eq 0) {
    $Width = [Math]::Sqrt($text.Length)
    Write-Host "hihi here"
}

$lines = $text -split '(.{' + $Width + '})' | Where-Object { $_ }
$lines | Out-File -FilePath $OutputFile

# Print the width
# Write-Host "Width: $Width"
