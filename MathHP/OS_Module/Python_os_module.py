import os

# Get current working directory

print("Current working directory:",os.getcwd())   #Current working directory: E:\PythonSeleniumTraining\GTM-PS-Batch02\MathHP\OS_Module
                                                 #import os

# Get environment value

print("path environment: ",os.getenv("path"))
#path environment:  C:\Python312\Scripts\;C:\Python312\;C:\Program Files\Common Files\Oracle\Java\javapath;C:\windows\system32;
# C:\windows;C:\windows\System32\Wbem;C:\windows\System32\WindowsPowerShell\v1.0\;C:\windows\System32\OpenSSH\;D:\Program Files\Git\cmd;
# C:\Program Files\Apache\apache-maven-3.9.6\bin;C:\Program Files\Apache\apache-maven-3.9.6\bin;;C:\Program Files\Docker\Docker\resources\bin;
# C:\Program Files\nodejs\;C:\Program Files\Microsoft SQL Server\Client SDK\ODBC\130\Tools\Binn\;
# C:\Program Files (x86)\Microsoft SQL Server\140\Tools\Binn\;C:\Program Files\Microsoft SQL Server\140\Tools\Binn\;
# C:\Program Files\Microsoft SQL Server\140\DTS\Binn\;C:\Program Files (x86)\Microsoft SQL Server\160\DTS\Binn\;
# C:\Program Files\Azure Data Studio\bin;C:\Users\madha\AppData\Local\Microsoft\WindowsApps;C:\Users\madha\AppData\Roaming\npm;
# C:\Program Files\JetBrains\PyCharm Community Edition 2023.3.2\bin;;C:\Program Files\Azure Data Studio\bin;
# C:\Program Files\Azure Data Studio\bin

print("Browser environment:" ,os.getenv("BROWSER"))        #Browser environment: None

print("Python version:",os.getenv("python_version"))      #Python version: None


