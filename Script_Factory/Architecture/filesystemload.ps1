# Create main folders
$folders = @(
    "..\README.md",                      # placeholder readme
    "..\entropyprocessing.md",           # placeholder entropy file
    "..\agenticloadofscriptfactory.md",  # placeholder agent load notes
    "..\prompts",
    "..\raw_scripts\runs",
    "..\optimized_scripts",
    "..\gossip_cycles",
    "..\entropy_logs"
)

foreach ($folder in $folders) {
    $fullPath = Join-Path -Path (Get-Location) -ChildPath $folder
    if ($folder -match "\.md$") {
        if (-not (Test-Path $fullPath)) {
            New-Item -Path $fullPath -ItemType File -Force | Out-Null
            Write-Host "Created file: $fullPath"
        }
    } else {
        if (-not (Test-Path $fullPath)) {
            New-Item -Path $fullPath -ItemType Directory -Force | Out-Null
            Write-Host "Created folder: $fullPath"
        }
    }
}
