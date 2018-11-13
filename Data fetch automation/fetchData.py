import webbrowser
import requests
import time
import zipfile
import os.path
from os import path

cpi_url = 'https://www150.statcan.gc.ca/t1/wds/rest/getFullTableDownloadCSV/18100006/en'
cpi_zipFilePath = r'C:\Users\Adarsh\Downloads\18100006-eng.zip'
cpi_csvFilefolderPath = r'C:\Users\Adarsh\Downloads\18100006-eng'

url = 'https://www150.statcan.gc.ca/t1/wds/rest/getFullTableDownloadCSV/18100006/en'
zipFilePath = r'C:\Users\Adarsh\Downloads\18100006-eng.zip'
csvFilefolderPath = r'C:\Users\Adarsh\Downloads\18100006-eng'

36100127-eng

myResponse = requests.get(url)

if myResponse.ok:
    print("Response was ok from the URL...")
    myResponseText = myResponse.text
    myResponseObject = myResponse.json()['object']
    print(myResponseObject)
    webbrowser.open(myResponseObject)  # Go to example.com

    flag = 1
    while flag:
        if (path.exists(zipFilePath)):
            print("Zip File downloaded and exist!")
            flag = 0
            # Unzip CSV
            zip_ref = zipfile.ZipFile(zipFilePath)
            zip_ref.extractall(csvFilefolderPath)
            print("Unzipping...")
            zip_ref.close()
            print("File has been unziped!")

        else:
            time.sleep(10)
            continue

    os.remove(zipFilePath)
    print("The Zip file has been deleted!!")

else:
    print("Something wrong with the method at Statcan")

