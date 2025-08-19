# CONFIGURATION
$promptsFolder = "prompts"
$modelsFolder  = "models"
$outputBase    = "Script_Factory_Runs"

$prompts = Get-ChildItem $promptsFolder -Filter *.txt
$models  = Get-ChildItem $modelsFolder -Filter *.gguf

foreach ($prompt in $prompts) {
    foreach ($model in $models) {

        $promptID = [System.IO.Path]::GetFileNameWithoutExtension($prompt.Name)
        $modelID  = [System.IO.Path]::GetFileNameWithoutExtension($model.Name)
        $timestamp = (Get-Date).ToString("yyyy-MM-ddTHH-mm-ssZ")

        # Build run_id
        $runID = "${modelID}_${promptID}_${timestamp}"

        # OUTPUT FILES
        $outputFile   = "$outputBase/all_runs/${runID}.txt"
        $metadataFile = "$outputBase/all_runs/${runID}.json"

        # RUN THE MODEL (this assumes llama.cpp CLI — adjust for your backend)
        $startTime = Get-Date
        $output = & "./llama.cpp/main.exe" --model $model.FullName --prompt (Get-Content $prompt.FullName -Raw)
        $endTime = Get-Date

        $runtime = ($endTime - $startTime).TotalSeconds
        Set-Content -Path $outputFile -Value $output

        # Extract model details (fake data for prototype)
        $quant = ($modelID -split "-")[-1]  # last part of filename is quantization
        $meta = @{
            run_id           = $runID
            timestamp        = $timestamp
            model            = $modelID
            model_file       = $model.FullName
            quantization     = $quant
            context_size     = 4096
            prompt_id        = $promptID
            runtime_seconds  = [Math]::Round($runtime, 2)
            output_file      = $outputFile
        }
        $meta | ConvertTo-Json -Depth 5 | Set-Content $metadataFile

        # COPY TO OTHER FOLDERS
        Copy-Item $outputFile   "$outputBase/runs_by_prompt/$promptID/"
        Copy-Item $outputFile   "$outputBase/runs_by_model/$modelID/"
        Copy-Item $outputFile   "$outputBase/runs_by_quantization/$quant/"

        $runtimeFolder = "$outputBase/runs_by_runtime/lt_{0}s" -f [Math]::Ceiling($runtime)
        if (-not (Test-Path $runtimeFolder)) { New-Item -ItemType Directory -Path $runtimeFolder | Out-Null }
        Copy-Item $outputFile $runtimeFolder
    }
}
