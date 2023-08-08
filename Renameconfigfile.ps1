$pythonroot = "C:\Python39"
$py = Join-Path -Path $pythonroot -ChildPath "python.exe"
$Project = "C:\p4\UIautomation"
$testcase = Join-Path -Path $Project -ChildPath "pendingFile.py"
$ResultFile = "C:\p4\UIautomation\log.xml"
Set-Location -Path $Project
 Start-Process -FilePath $py -ArgumentList $testcase
 $process = Get-Process -Name "python"
while($process.Responding)
{
Start-Sleep -Seconds 10
  if(Test-Path -Path $ResultFile)
  {
  Stop-Process -Name "python"
    break
  }
 }