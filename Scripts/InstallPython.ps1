function PSScriptRoot { $MyInvocation.ScriptName | Split-Path }
try
{
    Push-Location $PSScriptRoot
	$Downloaddir=".\temp"
	IF (-not (Test-Path $Downloaddir)) {
        New-Item $Downloaddir -type directory
    }

	[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12

	Invoke-WebRequest -Uri "https://www.python.org/ftp/python/3.7.3/python-3.7.3-amd64.exe" -OutFile ".\temp\python-3.7.3-amd64.exe"

	.\temp\python-3.7.3-amd64.exe /quiet InstallAllUsers=0 PrependPath=1 Include_test=0
}
finally
{
    Pop-Location
}
