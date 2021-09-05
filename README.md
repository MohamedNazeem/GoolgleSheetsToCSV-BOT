# GoolgleSheets to CSV-BOT
BOT to download google sheets and convert them to CSV files.
this BOT will help you to automate downloading of google sheets and convert them into CSV files.
for better design i have made a config file where you can control both the name of the spreadsheet and the name of the CSV file. 


# main.py
First of all download all the imported libraries in the start of the script.
For the python script all you need is to generate your own json file that will store the bot credentials from Google Workspace for Developers.
after the json file is downloaded import the file to the project environment and replace it with the YourOwnCreds.json
then open your json file and share the client_email attribute with your spreadsheet you want this BOT to auto download and convert.

# BOTconfig
this config file is a shell script i need to use in my business case but the configration can work on batch file for windows servers.
inside it import your script name then call the function and pass your paramters (Spreadsheet name, CSV file name)
Once you ran this shell script the process will be done. you can make a task scheduler to automate the process to fit your needs.
