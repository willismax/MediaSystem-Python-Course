$ErrorActionPreference = 'Stop'
$courseRoot = Split-Path -Parent $PSScriptRoot
$slidesRoot = Join-Path $courseRoot 'slides'
$exportRoot = Join-Path $slidesRoot 'previews\exported'
New-Item -ItemType Directory -Force -Path $exportRoot | Out-Null

$powerPoint = New-Object -ComObject PowerPoint.Application
try {
    foreach ($deck in Get-ChildItem -LiteralPath $slidesRoot -Filter '*.pptx' | Sort-Object Name) {
        $target = Join-Path $exportRoot $deck.BaseName
        New-Item -ItemType Directory -Force -Path $target | Out-Null
        $presentation = $powerPoint.Presentations.Open($deck.FullName, $true, $true, $false)
        try {
            # 18 = ppSaveAsPNG
            $presentation.SaveAs($target, 18)
            Write-Output $deck.Name
        }
        finally {
            $presentation.Close()
        }
    }
}
finally {
    $powerPoint.Quit()
    [System.Runtime.InteropServices.Marshal]::FinalReleaseComObject($powerPoint) | Out-Null
}

