Write-Host "==> Running ruff..."
ruff check .
if ($LASTEXITCODE -ne 0) {
    Write-Host "Ruff check failed." -ForegroundColor Red
    exit 1
}

Write-Host "==> Running pyright..."
pyright
if ($LASTEXITCODE -ne 0) {
    Write-Host "Pyright failed." -ForegroundColor Red
    exit 1
}

Write-Host "==> Running pytest..."
python -m pytest
if ($LASTEXITCODE -ne 0) {
    Write-Host "Pytest failed." -ForegroundColor Red
    exit 1
}

Write-Host "All checks passed." -ForegroundColor Green