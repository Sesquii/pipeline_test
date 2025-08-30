# PowerShell script to automatically generate import statements for all functions from a source script
# Usage: .\importscript.ps1 prompt2_qwen30b_default.py

param(
    [Parameter(Mandatory=$true, Position=0)]
    [string]$SourceScript
)

# Function to extract function names from Python file
function Get-PythonFunctions {
    param([string]$FilePath)
    
    if (-Not (Test-Path $FilePath)) {
        Write-Error "Source file not found: $FilePath"
        return @()
    }
    
    $content = Get-Content $FilePath -Raw
    
    # Regex pattern to match function definitions
    # Matches: def function_name( or def function_name():
    # Handles whitespace and various parameter patterns
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

# Get the source script name without .py extension
$sourceScriptName = $SourceScript -replace '\.py$', ''

# Auto-generate target file name with test_ prefix
$targetFileName = "test_$SourceScript"

# Get current directory and build proper paths
$currentDir = Get-Location
Write-Host "Current directory: $currentDir"

# Try to find the source file with correct relative paths
$possiblePaths = @(
    "..\Script_Factory_Runs\all_runs\$SourceScript",
    "..\Script_Factory_Runs\all_runs\$sourceScriptName.py",
    "..\..\Script_Factory\Script_Factory_Runs\all_runs\$SourceScript",
    "..\..\Script_Factory\Script_Factory_Runs\all_runs\$sourceScriptName.py",
    "$SourceScript",
    "$sourceScriptName.py"
)

$sourceFilePath = $null
foreach ($path in $possiblePaths) {
    $fullPath = Resolve-Path $path -ErrorAction SilentlyContinue
    if ($fullPath -and (Test-Path $fullPath)) {
        $sourceFilePath = $fullPath
        break
    }
}

if (-not $sourceFilePath) {
    Write-Error "Could not find source file. Tried paths: $($possiblePaths -join ', ')"
    Write-Host "Current working directory: $(Get-Location)"
    Write-Host "Looking for file: $SourceScript"
    exit 1
}

Write-Host "Found source file: $sourceFilePath"

# Extract function names
$functions = Get-PythonFunctions -FilePath $sourceFilePath

if ($functions.Count -eq 0) {
    Write-Warning "No functions found in $sourceFilePath"
    exit 0
}

Write-Host "Found $($functions.Count) functions: $($functions -join ', ')"

# Generate the import statement
$importStatement = "from Script_Factory.Script_Factory_Runs.all_runs.$sourceScriptName import ("
$importStatement += "`n    " + ($functions -join ",`n    ")
$importStatement += "`n)"

Write-Host "`nGenerated import statement:"
Write-Host $importStatement -ForegroundColor Green

# Create or update the target test file
$targetFilePath = Join-Path $currentDir $targetFileName

# Check if we need to add sys/os imports and path setup
$needsSysOsImports = -not (Test-SysOsImports -FilePath $targetFilePath)
$needsPathSetup = -not (Test-SysPathSetup -FilePath $targetFilePath)

if (Test-Path $targetFilePath) {
    $lines = Get-Content $targetFilePath
    $newLines = @()
    $importAdded = $false
    $pathSetupAdded = $false
    $sysOsImportsAdded = $false
    $inImportSection = $true
    $existingImportFound = $false
    
    # Check if our specific import already exists
    $existingContent = Get-Content $targetFilePath -Raw
    if ($existingContent -match [regex]::Escape("from Script_Factory.Script_Factory_Runs.all_runs.$sourceScriptName import")) {
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
    Set-Content -Path $targetFilePath -Value $newContent -Encoding UTF8
    
    if ($existingImportFound) {
        Write-Host "Import statement already exists in $targetFilePath" -ForegroundColor Yellow
    } else {
        Write-Host "Added import statement to $targetFilePath" -ForegroundColor Yellow
    }
    
    if ($needsSysOsImports -and $sysOsImportsAdded) {
        Write-Host "Added sys, os imports" -ForegroundColor Yellow
    }
    
    if ($needsPathSetup -and $pathSetupAdded) {
        Write-Host "Added sys.path.append setup" -ForegroundColor Yellow
    }
    
} else {
    # Create new file with basic test structure including sys path setup
    $testTemplate = @"
import pytest
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

$importStatement

# Add your test functions here
def test_example():
    '''Example test function - replace with actual tests'''
    assert True
"@
    
    Set-Content -Path $targetFilePath -Value $testTemplate -Encoding UTF8
    Write-Host "Created $targetFilePath with import statement and basic test structure" -ForegroundColor Yellow
}

Write-Host "`nTarget file: $targetFilePath" -ForegroundColor Cyan
Write-Host "Import statement added successfully!" -ForegroundColor Green