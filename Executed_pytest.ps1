$pythonroot = "C:\Python39"
$py = Join-Path -Path $pythonroot -ChildPath "python.exe"
$Project = "C:\p4\ApemMobile_UIautomation\DesktopApem\testcase"
$testcase = Join-Path -Path $Project -ChildPath "AllTest.py"
Set-Location -Path $Project
$process = Start-Process -FilePath $py -ArgumentList $testcase
while($process.Responding)
{
Start-Sleep -Seconds 10
}