<#-------------------This script is uesed to execute pytest and analysis test result---------------------------#>
<#---------------------------------Automation Engineer: Will.You-----------------------------------------------#>
<#--------------------------------------------Jul.21 2021------------------------------------------------------#>
$RootPath ="E:\Will\For Ziru"
$ResultFile = Join-Path -Path $RootPath -ChildPath "test.xml"
$starttime = Get-Date
$blueprint = "APEM"
function Convert-Timespan($timespan)
{
    $temp=$timespan.Split(":")
    if($temp.count -eq 2)
    {
        $mins=[int]$temp[0]+[int]$temp[1]/60
    }
    elseif($temp.Count -eq 3)
    {
        $mins=[int]$temp[0]*60+[int]$temp[1]+[int]$temp[2]/60
    }
    return $mins
}
Function Run-MSTestResultAnalysis($sResult,$node)
{
    function newResultObj($Id,$casename,$Result,$Detail)
    {
        $obj=New-Object PSObject
        $Obj|Add-Member -MemberType NoteProperty -Name "Id" -Value $Id
        $Obj|Add-Member -MemberType NoteProperty -Name "casename" -Value $casename
        $Obj|Add-Member -MemberType NoteProperty -Name "Result" -Value $Result
        $Obj|Add-Member -MemberType NoteProperty -Name "Detail" -Value $Detail
        
        return $Obj
    }
   $Id= $sResult.SelectNodes($node).VSTS_id
   $casename=$sResult.SelectNodes($node).case_name
   $result = $sResult.SelectNodes($node).result
   if($result -eq "passed")
    {
    $Detail = ""
    }
    else
    {
    $Detail = $sResult.SelectNodes($node).message
     }
 
    $obj=newResultObj -Id $Id -casename $casename -Result $result -Detail $Detail
    return $obj
 }

 Function generateHTMLfromCSV{
    Param(
      [string]$media = "Unspecified",
      [string]$clientConfig = "Unspecified",
      [DateTime]$startTime = [DateTime]"1/1/0001",
      [DateTime]$endTime = [DateTime]"1/1/0001",
        [Parameter(Mandatory=$false)][string]$resultsFile,
        [string]$clientName = "N/A",
        [int]$passed,
        [int]$failed
    )
 
    #read the .csv file
    if($resultsFile -ne "" -and $resultsFile -ne $null)
    {
        $lsRecord = Import-Csv -Path $resultsFile
        $passed=([array]($lsRecord|where{$_.result -match "passed"})).length
        $failed=([array]($lsRecord|where{$_.result -notmatch "passed"})).length
        $lsRecord|select id,headline,result |ConvertTo-Html -Fragment -As Table|Out-String|Out-File .\test.html

    }
    
    # ===---===---===---===--- ||||||||||||||||| ===---===---===---===---===

    $sTimeZone = [System.TimeZone]::CurrentTimeZone.DaylightName



    $tableColor1 = "#CCFFCC";
    $tableColor2 = "#CCFFCC";

    if($failed -gt 0){$errorColor = "#ff5959"; $headerColor = $errorColor; $sumColor = "rgb(217,217,217)"} else {$errorCOlor = "#CCFFCC"; $headerColor = "#e0fc85"; $sumColor = "rgb(0,0,0)"} 

    Write-host "$($startTime.ToString())"
    write-host "$($endTime.ToString())"

    $strStart = "$($startTime.ToString())"
    $strEnd = "$($endTime.ToString())"

    $htmlText ="    <!DOCTYPE html>
    <html>
    <head>
    <style>
 
    #resultsTable
    {
    font-family:`"Arial`";
    
    border-collapse:collapse;
 
    }
    #resultsTable td, #resultsTable th 
    {
    font-size:1em;
    border:1px solid #ffffff;
    background-color: $tableColor1;
    padding:3px 7px 2px 7px;
    }
    #resultsTable th 
    {
    font-size:1.5em;
    font-family:`"Arial`";
    text-align:center;
    padding-top:5px;
    padding-bottom:4px;
    background-color: $headerColor;
    color:$sumColor;
    }
    #resultsTable tr.alt td 
    {
    color: #000000;
    background-color: $tableColor2;
    }
    #resultsTable tr.error td 
    {
    background-color: $errorColor;
    color:$sumColor;
    font-weight:bold
    }
    </style>
    </head>
 
    <body>

 
    <table id=`"resultsTable`">
    <!--Specify Width of first column-->
    <col width=`"200`";>
 
    <tr>
      <th colspan=`"2`">SUMMARY</th>
    </tr>
    <tr>
    <td ><b>Media Number #</b></td>
    <td>$media</td>
 
    </tr>
    <tr class=`"alt`">
    <td><b>Client Configuration</b></td>
    <td>$clientConfig</td>
 
    </tr>
    <tr>
    <td><b>Test Date</b></td>
    <td>$($startTime.ToLongDateString())</td>
 
    </tr>
    <tr class=`"alt`">
    <td><b>Test Start Time</b></td>
    <td>$strStart ($sTimeZone)</td>
 
    </tr>
    <tr>
    <td><b>Test End Time</b></td>
    <td>$strEnd ($sTimeZone)</td>
 
    </tr>
    <tr class=`"alt`">
    <td><b>Test Duration</b></td>
    <td>$(($endTime - $startTime).ToString().SubString(0,8))</td>
 
    </tr>
    <tr>
    <td><b>Test Cases Passed</b></td>
    <td>$passed      ---   Percentage:&#160 $([math]::round((($passed * 1.0)/($passed + $failed) * 100.0), 1)) %</td>
 
    </tr>
    <tr class=`"error`">
    <td><b>Test Cases Failed</b></td>
    <td>$failed      ---   Percentage:&#160 $([math]::round((($failed * 1.0)/($passed + $failed) * 100.0), 1)) %</td>
 
    </tr>
    <tr>
    <td><b>Total Test Cases</b></td>
    <td>$($passed + $failed)</td>
 
    </tr>
	

 
    </table>

    <h1 style=`"font-family:verdana;font-size:16px;`">Operations Performed:</h1>
    <p>1. Installed the latest Media on clean state.<br>
       2. Executed Launch Test.<br>
       3. The details of the test and results are attached.<br>
    </p>
    <p> <br>
        
    </p>
    <p> Test machine name: $clientName<br>
    <p> Test machine User Account: $clientName\Admin or $clientName\Administrator<br>
    
        
    </p>
    <br>
    <p>Thank You for your Support,<br>
    <b>Smoke Test Automation Team<br></b>
    =====================================================================================================
    
    </p>
 
    
    </p>
	
	
	
	<style>
 
    #detailedSummaryTableDiv
    {
        width:1200px;
    }

    #detailedSummary
    {
    font-family:`"Arial`";
    border-collapse:collapse;
    width:100%;
    }
    #detailedSummary td, #detailedSummary th 
    {
    
    font-size:1em;
    border:1px solid #ffffff;
    background-color: #CCFFFF;
    padding:3px 7px 2px 7px;
    }
    #detailedSummary th 
    {
    font-size:1.5em;
    font-family:`"Arial`";
    text-align:center;
    padding-top:5px;
    padding-bottom:4px;
    background-color: #FFFFCC;
    color:#000000;
    }
    #detailedSummary tr.header td 
    {
    border:1px solid #000000;
    }
    #detailedSummary td 
    {
    border:1px solid #123455;
    
    }

    #detailedSummary td.left 
    {
    width:15%;
    word-wrap:break-word;
    
    }

    #detailedSummary td.right 
    {
    width:80%;
    }

    #detailedSummary td.pass 
    {
    width:5%;
    text-align: center
    }

    #detailedSummary td.NA
    {
    width:5%;
    text-align: center;
    background-color: Gray;
    color: #FFFFFF;
    }

    #detailedSummary td.fail 
    {
    width:5%;
    text-align: center;
    background-color: #FF5050;
    color: #FFFFFF;
    }

    }
    </style>

	<div id=`"detailedSummaryTableDiv`">
	<table id=`"detailedSummary`">
    <!--Specify Width of first column-->





 
    <tr>
      <th colspan=`"3`">Test Case Description</th>
    </tr>
    <tr class=`"header`">
    <td ><b>Test Case ID</b></td>
    <td><b>Case description</b></td>
    <td ><b>Pass/Fail</b></td>
    </tr>

    <!--marker.table_begin-->



    <!--marker.table_end-->
 
    </table>

    </div>
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
 
 
    </body>
    </html>"


    [string]$testCaseDesc=""
    
    $maxFileSizeForAttach = 20000000 #20MB
    $fileSize = (Get-Item $resultsFile).length
    if($lsRecord.Count -gt 1000)
    {
        if($fileSize -lt $maxFileSizeForAttach)
        {
            $htmlText = $htmlText.Insert($htmlText.IndexOf("<!--marker.table_end-->"),"<br><h3>Record Detail is hidden because the number of record is too much. For detail, please refer to attached Excel file</h3><br>")
        }
        else #filesize is greater than or equal to $maxFileSizeForAttach
        {
            $htmlText = $htmlText.Insert($htmlText.IndexOf("<!--marker.table_end-->"),"<br><h3>Record Detail is hidden because the number of record is too much. Excel file is too large to attach to email.  Please find Excel file $resultsFile on VM</h3><br>")
        }
    }

    [string]$testCaseDesc=$testCaseDesc+"<colgroup><col/><col/><col/></colgroup>"
    
    #$lsRecord
    if($lsRecord.Count -lt 1000)
    {
        if($lsRecord.Count -ne 0)
        {
            foreach ($rowEntry in $lsRecord){
                #write-host $rowEntry.id
                if($rowEntry.result.tolower() -match "passed"){                
                
                    $testCaseDesc = $testCaseDesc + "<tr><td class=`"left`">"+$rowEntry.id+"</td><td>"+$rowEntry.casename+"</td><td class=`"pass`">"+$rowEntry.result+"</td></tr>"
                
                } 
                elseif($rowEntry.result -eq "failed")
                {
                 $testCaseDesc = $testCaseDesc + "<tr><td class=`"left`" style=`"background-color: #FF5050; color: #FFFFFF`">"+$rowEntry.id+"</td><td style=`"background-color: #FF5050`; color: #FFFFFF`">"+$rowEntry.casename+"</td><td class=`"fail`">"+"Analysis required"+"</td></tr>"

                }
                else 
                {
               $testCaseDesc = $testCaseDesc + "<tr><td class=`"left`" style=`"background-color: Gray; color: #FFFFFF`">"+$rowEntry.id+"</td><td style=`"background-color: Gray`; color: #FFFFFF`">"+$rowEntry.casename+"</td><td class=`"NA`">"+"Not in Media Kit"+"</td></tr>"
                }
        

            }
            $htmlText = $htmlText.Insert($htmlText.IndexOf("<!--marker.table_end-->"),$testCaseDesc)
        }
    }
    $htmlText
    [double]$passRate = $([math]::round((($passed * 1.0)/($passed + $failed) * 100.0), 1))
    $passRate
    return;

}
Set-Location -Path $RootPath
$res = [xml](Get-Content -Path $ResultFile)
for($i = 1; $i -le $res.testsuites.testsuite.testresult.testcase.Count;$i++ )
{
$singlenode = "testsuites/testsuite/testresult/testcase[$i]"
$rex= Run-MSTestResultAnalysis -sResult $res -node $singlenode
$rex |Select-Object -Property Id, casename,result,Detail|Export-Csv -Delimiter ","  -Path (Join-Path -Path $RootPath -ChildPath "APEM.csv" ) -Append
}

#$rex =  $res.SelectNodes("testsuites/testsuite/testresult/testcase[1]").case_name
#$testcases = $res.testsuites.testsuite.testresult.testcase
$html=[string](generateHTMLfromCSV -media null -startTime $startTime -endTime (Get-Date)  -resultsFile (Join-Path -Path $RootPath -ChildPath "APEM.csv")-clientConfig $((Get-WmiObject -Class Win32_OperatingSystem).Name) -clientName $env:COMPUTERNAME)
 $attachmentPath=Join-Path -Path $RootPath -ChildPath "APEM.csv" 
 Send-MailMessage -Attachments @($attachmentPath) -From "MVT@aspentech.com" -To "will.you@aspentech.com" -Subject "Automated Testcase Execution Report for $blueprint" -Body $html -SmtpServer hqsmtp01.corp.aspentech.com -BodyAsHtml


