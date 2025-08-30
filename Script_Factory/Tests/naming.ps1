for ($i = 2; $i -le 25; $i++) {
    $filename = "test_prompt${i}_qwen30b_default.py"
    
    # Check if file already exists to avoid overwriting
    if (-Not (Test-Path $filename)) {
        # Create empty Python file
        New-Item -ItemType File -Name $filename -Force | Out-Null
        Write-Host "Created: $filename"
    } else {
        Write-Host "Already exists: $filename (skipped)"
    }
}

Write-Host "Finished creating Python files for prompts 3-25"