import zipfile

zip_ref = zipfile.ZipFile(r'C:\Users\Adarsh\Downloads\14100287-eng.zip')

zip_ref.extractall(r'C:\Users\Adarsh\Downloads\14100287-eng')

zip_ref.close()

