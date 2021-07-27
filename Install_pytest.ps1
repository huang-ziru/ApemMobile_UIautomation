$user = $env:USERNAME
$root = "C:\Users\$user\AppData\Local\Programs\Python\Python39"
$pip = Join-Path -Path $root -ChildPath "Scripts\pip.exe"
$Plugins = @("pytest","selenium")

Set-Location -Path $root
foreach($Plugin in $Plugins)
{
    $process = Start-Process -FilePath $pip -ArgumentList "install $Plugin" -PassThru
    while($process.Responding)
    {
        Start-Sleep -Seconds 1
    }
}

