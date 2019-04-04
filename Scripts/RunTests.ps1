function PSScriptRoot { $MyInvocation.ScriptName | Split-Path }
try
{
    Push-Location $PSScriptRoot
	$RootDirectory="..\"

python -m unittest discover $RootDirectory "APIAssurity.py"
}
finally
{
    Pop-Location
}
