# PowerShell script to batch process all test files in Tests folder
# Recursively looks up corresponding source files and applies import logic
# Usage: .\batch_import_tests.ps1

param(
    [Parameter(Mandatory=$false)]
    [string]$TestsFolder = "Tests",
    
    [Parameter(Mandatory=$false)]
    [string]$SourceFolder = "Script_Factory_Runs\all_runs"
)

# Function to extract function names from Python file
function Get-PythonFunctions {
    param([string]$FilePath)
    
    if (-Not (Test-Path $FilePath)) {
        Write-Warning "Source file not found: $FilePath"
        return @()
    }
    
    $content = Get-Content $FilePath -Raw
    
    # Regex pattern to match function definitions
    $pattern = '(?m)^[ \t]*def\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*\('
    
    $matches = [regex]::Matches($content, $pattern)
    
    $functions = @()
    foreach ($match in $matches) {
        $functionName = $match.Groups[1].Value
        # Skip private functions (starting with _) unless you want them
        if (-not $functionName.StartsWith('_')) {
            $functions += $functionName
        }
    }
    
    return $functions | Sort-Object -Unique
}

# Function to check if sys path setup exists in file
function Test-SysPathSetup {
    param([string]$FilePath)
    
    if (-not (Test-Path $FilePath)) {
        return $false
    }
    
    $content = Get-Content $FilePath -Raw
    return ($content -match 'sys\.path\.append\(os\.path\.abspath\(os\.path\.join\(os\.path\.dirname\(__file__\)')
}

# Function to check if sys, os imports exist
function Test-SysOsImports {
    param([string]$FilePath)
    
    if (-not (Test-Path $FilePath)) {
        return $false
    }
    
    $content = Get-Content $FilePath -Raw
    return ($content -match 'import sys,\s*os' -or ($content -match 'import sys' -and $content -match 'import os'))
}

# Function to find source file for a test file
function Find-SourceFile {
    param(
        [string]$TestFileName,
        [string]$TestsDir,
        [string]$SourceDir
    )
    
    # Remove test_ prefix and get base name
    $baseName = $TestFileName -replace '^test_', ''
    $baseNameWithoutExt = $baseName -replace '\.py$', ''
    
    # Possible source file locations (relative to Tests folder)
    $possibleSourcePaths = @(
        "..\$SourceDir\$baseName",
        "..\$SourceDir\$baseNameWithoutExt.py",
        "..\..\Script_Factory\$SourceDir\$baseName",
        "..\..\Script_Factory\$SourceDir\$baseNameWithoutExt.py"
    )
    
    foreach ($path in $possibleSourcePaths) {
        $fullPath = Join-Path $TestsDir $path
        $resolvedPath = Resolve-Path $fullPath -ErrorAction SilentlyContinue
        if ($resolvedPath -and (Test-Path $resolvedPath)) {
            return @{
                SourcePath = $resolvedPath
                BaseName = $baseNameWithoutExt
            }
        }
    }
    
    return $null
}

# Function to process a single test file
function Process-TestFile {
    param(
        [string]$TestFilePath,
        [string]$TestsDir,
        [string]$SourceDir
    )
    
    $testFileName = Split-Path $TestFilePath -Leaf
    Write-Host "`nProcessing: $testFileName" -ForegroundColor Cyan
    
    # Skip if not a test file
    if (-not $testFileName.StartsWith('test_')) {
        Write-Host "  Skipping (not a test file): $testFileName" -ForegroundColor Yellow
        return
    }
    
    # Find corresponding source file
    $sourceInfo = Find-SourceFile -TestFileName $testFileName -TestsDir $TestsDir -SourceDir $SourceDir
    
    if (-not $sourceInfo) {
        Write-Host "  No corresponding source file found for: $testFileName" -ForegroundColor Red
        return
    }
    
    Write-Host "  Found source: $($sourceInfo.SourcePath)" -ForegroundColor Green
    
    # Extract functions from source file
    $functions = Get-PythonFunctions -FilePath $sourceInfo.SourcePath
    
    if ($functions.Count -eq 0) {
        Write-Host "  No functions found in source file" -ForegroundColor Yellow
        return
    }
    
    Write-Host "  Found $($functions.Count) functions: $($functions -join ', ')"
    
    # Generate import statement
    $importStatement = "from Script_Factory.Script_Factory_Runs.all_runs.$($sourceInfo.BaseName) import ("
    $importStatement += "`n    " + ($functions -join ",`n    ")
    $importStatement += "`n)"
    
    # Check what needs to be added
    $needsSysOsImports = -not (Test-SysOsImports -FilePath $TestFilePath)
    $needsPathSetup = -not (Test-SysPathSetup -FilePath $TestFilePath)
    
    # Process the test file
    if (Test-Path $TestFilePath) {
        $lines = Get-Content $TestFilePath
        $newLines = @()
        $importAdded = $false
        $pathSetupAdded = $false
        $sysOsImportsAdded = $false
        $inImportSection = $true
        $existingImportFound = $false
        
        # Check if our specific import already exists
        $existingContent = Get-Content $TestFilePath -Raw
        if ($existingContent -match [regex]::Escape("from Script_Factory.Script_Factory_Runs.all_runs.$($sourceInfo.BaseName) import")) {
            $existingImportFound = $true
        }
        
        foreach ($line in $lines) {
            # Add sys, os imports after pytest if needed
            if ($needsSysOsImports -and $line -match '^import pytest' -and -not $sysOsImportsAdded) {
                $newLines += $line
                $newLines += "import sys, os"
                $sysOsImportsAdded = $true
                continue
            }
            
            # Add path setup after sys, os imports if needed
            if ($needsPathSetup -and ($line -match '^import sys,\s*os' -or ($sysOsImportsAdded -and $line.Trim() -eq "")) -and -not $pathSetupAdded) {
                $newLines += $line
                if ($line.Trim() -ne "") {
                    $newLines += 'sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))'
                    $newLines += ""
                }
                $pathSetupAdded = $true
                continue
            }
            
            # Handle import section logic
            if (($line -match '^(from |import |#|$)' -or $line.Trim() -eq '') -and $inImportSection) {
                $newLines += $line
            } else {
                # We've hit the first non-import line
                if ($inImportSection -and -not $existingImportFound -and -not $importAdded) {
                    $newLines += ""
                    $newLines += $importStatement
                    $newLines += ""
                    $importAdded = $true
                    $inImportSection = $false
                } elseif ($inImportSection) {
                    $inImportSection = $false
                }
                $newLines += $line
            }
        }
        
        # If we never found non-import lines and need to add import
        if ($inImportSection -and -not $existingImportFound -and -not $importAdded) {
            $newLines += ""
            $newLines += $importStatement
        }
        
        $newContent = $newLines -join "`n"
        Set-Content -Path $TestFilePath -Value $newContent -Encoding UTF8
        
        # Report what was done
        $changes = @()
        if (-not $existingImportFound) { $changes += "import statement" }
        if ($needsSysOsImports -and $sysOsImportsAdded) { $changes += "sys/os imports" }
        if ($needsPathSetup -and $pathSetupAdded) { $changes += "path setup" }
        
        if ($changes.Count -gt 0) {
            Write-Host "  Added: $($changes -join ', ')" -ForegroundColor Green
        } elseif ($existingImportFound) {
            Write-Host "  Already up to date" -ForegroundColor Yellow
        }
    }
}

# Main execution
Write-Host "Batch Import Script for Tests" -ForegroundColor Magenta
Write-Host "=============================" -ForegroundColor Magenta

# Check if Tests folder exists
if (-not (Test-Path $TestsFolder)) {
    Write-Error "Tests folder not found: $TestsFolder"
    exit 1
}

$testsDir = Resolve-Path $TestsFolder
Write-Host "Processing tests in: $testsDir"
Write-Host "Looking for source files in: $SourceFolder"

# Get all Python files in Tests folder
$testFiles = Get-ChildItem -Path $testsDir -Filter "*.py" -File

if ($testFiles.Count -eq 0) {
    Write-Host "No Python files found in Tests folder" -ForegroundColor Yellow
    exit 0
}

Write-Host "Found $($testFiles.Count) Python files to process"

$processed = 0
$updated = 0

foreach ($testFile in $testFiles) {
    try {
        $beforeContent = Get-Content $testFile.FullName -Raw -ErrorAction SilentlyContinue
        Process-TestFile -TestFilePath $testFile.FullName -TestsDir $testsDir -SourceDir $SourceFolder
        $afterContent = Get-Content $testFile.FullName -Raw -ErrorAction SilentlyContinue
        
        $processed++
        if ($beforeContent -ne $afterContent) {
            $updated++
        }
    }
    catch {
        Write-Host "  Error processing $($testFile.Name): $($_.Exception.Message)" -ForegroundColor Red
    }
}

Write-Host "`n=============================" -ForegroundColor Magenta
Write-Host "Batch processing complete!" -ForegroundColor Green
Write-Host "Files processed: $processed"
Write-Host "Files updated: $updated"
Write-Host "Files unchanged: $($processed - $updated)"