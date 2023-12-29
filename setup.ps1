# Caminhos
$pythonInstaller = ".\python_installer.exe"
$desktopPath = [System.IO.Path]::Combine($env:USERPROFILE, 'Desktop', 'MeuApp.lnk')
$appDirectory = "C:\onrAudit"
$appScript = "$appDirectory\onrAdit\main.py"
$appExe = "$appDirectory\app.exe"

# Verifica se o Python está instalado
function IsPythonInstalled {
    $python = Get-Command python -ErrorAction SilentlyContinue
    return ($null -ne $python)
}

# Instalar o Python se não estiver instalado
if (-not (IsPythonInstalled)) {
    Start-Process -Wait -FilePath $pythonInstaller
}

# Criar diretório se não existir
if (-not (Test-Path $appDirectory)) {
    New-Item -Path $appDirectory -ItemType Directory -Force
}

# Copiar os arquivos necessários para o diretório
Copy-Item -Path ".\app.exe" -Destination $appDirectory
Copy-Item -Path ".\onrAdit" -Destination $appDirectory -Recurse

# Instalar dependências
python -m pip install -r .\requirements.txt

# Criar atalho no desktop, se não existir
if (-not (Test-Path $desktopPath)) {
    $WScriptShell = New-Object -ComObject WScript.Shell
    $Shortcut = $WScriptShell.CreateShortcut($desktopPath)
    $Shortcut.TargetPath = $appExe
    $Shortcut.Save()
}

# Executar a aplicação Flask
Start-Process -FilePath python -ArgumentList $appScript
